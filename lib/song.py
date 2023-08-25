class Song:
    count = 0
    genres = list()
    artists = list()
    genre_count = dict()
    artist_count = dict()

    def __init__(self, name, artist, genre) -> (None):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if (genre.lower() not in cls.genres):
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if (artist.lower() not in cls.artists):
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # ipdb.set_trace()
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
