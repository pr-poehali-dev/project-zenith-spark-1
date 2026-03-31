import json
import os
import psycopg2

def handler(event: dict, context) -> dict:
    """Старт боя между двумя игроками и завершение боя с записью победителя."""
    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400'}, 'body': ''}

    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    schema = 't_p1624076_project_zenith_spark'
    method = event.get('httpMethod')

    if method == 'POST':
        body = json.loads(event.get('body') or '{}')
        player1_id = body.get('player1_id')
        player2_id = body.get('player2_id')
        if not player1_id or not player2_id:
            return {'statusCode': 400, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': json.dumps({'error': 'player1_id и player2_id обязательны'})}

        cur.execute(f"INSERT INTO {schema}.battles (player1_ref, player2_ref, status) VALUES ({player1_id}, {player2_id}, 'active') RETURNING id, status, started_at")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': {'battle_id': row[0], 'status': row[1], 'started_at': str(row[2])}}

    if method == 'PUT':
        body = json.loads(event.get('body') or '{}')
        battle_id = body.get('battle_id')
        winner_id = body.get('winner_id')
        player1_score = body.get('player1_score', 0)
        player2_score = body.get('player2_score', 0)
        if not battle_id or not winner_id:
            return {'statusCode': 400, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': {'error': 'battle_id и winner_id обязательны'}}

        cur.execute(f"UPDATE {schema}.battles SET winner_ref={winner_id}, player1_score={player1_score}, player2_score={player2_score}, status='finished', finished_at=NOW() WHERE id={battle_id} RETURNING id, status")
        row = cur.fetchone()
        cur.execute(f"UPDATE {schema}.players SET wins=wins+1, rating=rating+25 WHERE id={winner_id}")
        loser_col = f"SELECT CASE WHEN player1_ref={winner_id} THEN player2_ref ELSE player1_ref END FROM {schema}.battles WHERE id={battle_id}"
        cur.execute(f"UPDATE {schema}.players SET losses=losses+1, rating=GREATEST(rating-15, 0) WHERE id=({loser_col})")
        conn.commit()
        cur.close()
        conn.close()
        return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': {'battle_id': row[0], 'status': row[1]}}

    cur.execute(f"SELECT b.id, p1.username, p2.username, pw.username, b.player1_score, b.player2_score, b.status, b.started_at FROM {schema}.battles b JOIN {schema}.players p1 ON b.player1_ref=p1.id JOIN {schema}.players p2 ON b.player2_ref=p2.id LEFT JOIN {schema}.players pw ON b.winner_ref=pw.id ORDER BY b.started_at DESC LIMIT 50")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    battles = [{'id': r[0], 'player1': r[1], 'player2': r[2], 'winner': r[3], 'score': f"{r[4]}:{r[5]}", 'status': r[6], 'started_at': str(r[7])} for r in rows]
    return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': {'battles': battles}}