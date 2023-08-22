class Song:
    genres=[]
    artists=[]
    count = 0

    def __init__(self,name):
        self.name=name
        self.add_song_to_count()
        Song.add_song_to_all(self)
        Song.add_to_artists(self)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
   
    @classmethod
    def add_song_to_all(cls, song):
        cls.genres.append(song)
        
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)