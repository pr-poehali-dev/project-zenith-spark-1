CREATE TABLE t_p1624076_project_zenith_spark.battles (
    id SERIAL PRIMARY KEY,
    player1_id VARCHAR(100) NOT NULL,
    player2_id VARCHAR(100) NOT NULL,
    winner_id VARCHAR(100),
    player1_score INT DEFAULT 0,
    player2_score INT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'active', 'finished')),
    started_at TIMESTAMP DEFAULT NOW(),
    finished_at TIMESTAMP
);