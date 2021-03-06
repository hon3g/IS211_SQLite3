import sqlite3

con = sqlite3.connect('pets.db')
cur = con.cursor()

cur.executescript('''

DROP TABLE IF EXISTS person;
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER);

DROP TABLE IF EXISTS pet;
CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER);

DROP TABLE IF EXISTS person_pet;
CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER);

''')

many_person = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
]
many_pet = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1),
]
many_person_pet = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6),
]
cur.executemany('INSERT INTO person VALUES(?,?,?,?)', many_person)
cur.executemany('INSERT INTO pet VALUES(?,?,?,?,?)', many_pet)
cur.executemany('INSERT INTO person_pet VALUES(?,?)', many_person_pet)

con.commit()
con.close()
