import json
import os
import psycopg2

def handler(event: dict, context) -> dict:
    """Регистрация нового игрока и получение списка игроков."""
    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400'}, 'body': ''}

    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    schema = 't_p1624076_project_zenith_spark'

    method = event.get('httpMethod')

    if method == 'POST':
        body = json.loads(event.get('body') or '{}')
        username = body.get('username', '').strip()
        if not username:
            return {'statusCode': 400, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': json.dumps({'error': 'username обязателен'})}

        cur.execute(f"INSERT INTO {schema}.players (username) VALUES ('{username}') ON CONFLICT (username) DO UPDATE SET username=EXCLUDED.username RETURNING id, username, rating, wins, losses")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': {'id': row[0], 'username': row[1], 'rating': row[2], 'wins': row[3], 'losses': row[4]}}

    cur.execute(f"SELECT id, username, rating, wins, losses FROM {schema}.players ORDER BY rating DESC LIMIT 100")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    players = [{'id': r[0], 'username': r[1], 'rating': r[2], 'wins': r[3], 'losses': r[4]} for r in rows]
    return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*'}, 'body': {'players': players}}