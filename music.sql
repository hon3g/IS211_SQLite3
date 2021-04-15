DROP TABLE IF EXISTS artist;
CREATE TABLE artist(
	artist_id SERIAL PRIMARY KEY,
	artist_name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS album;
CREATE TABLE album(
	album_id SERIAL PRIMARY KEY,
	artist_id INTEGER REFERENCES artist(artist_id),
	album_name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS song;
CREATE TABLE song(
	song_id SERIAL PRIMARY KEY,
	album_id INTEGER REFERENCES album(album_id),
	song_name VARCHAR(250) NOT NULL,
	track_num SMALLINT,
	song_len INT NOT NULL
);
