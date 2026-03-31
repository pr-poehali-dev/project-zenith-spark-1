CREATE TABLE t_p1624076_project_zenith_spark.players (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    rating INT DEFAULT 1000,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

ALTER TABLE t_p1624076_project_zenith_spark.battles
    ADD COLUMN player1_ref INT REFERENCES t_p1624076_project_zenith_spark.players(id),
    ADD COLUMN player2_ref INT REFERENCES t_p1624076_project_zenith_spark.players(id),
    ADD COLUMN winner_ref INT REFERENCES t_p1624076_project_zenith_spark.players(id);