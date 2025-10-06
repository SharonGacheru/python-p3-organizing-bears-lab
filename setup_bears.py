import sqlite3

conn = sqlite3.connect('bears.db')
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS bears;

CREATE TABLE bears (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    sex TEXT,
    color TEXT,
    temperament TEXT,
    alive INTEGER
);

INSERT INTO bears (name, age, sex, color, temperament, alive) VALUES
    ('Mr. Chocolate', 8, 'M', 'Brown', 'Calm', 1),
    ('Rowdy', 10, 'M', 'Black', 'Aggressive', 1),
    ('Tabitha', 6, 'F', 'Honey', 'Friendly', 1),
    ('Sergeant Brown', 19, 'M', 'Brown', 'Aggressive', 0),
    ('Melissa', 7, 'F', 'White', 'Calm', 1),
    ('Grinch', 2, 'M', 'Black', 'Aggressive', 1),
    ('Wendy', 17, 'F', 'Brown', 'Calm', 0),
    ('Maddie', 7, 'F', 'Brown', 'Calm', 1);
""")

conn.commit()
conn.close()
