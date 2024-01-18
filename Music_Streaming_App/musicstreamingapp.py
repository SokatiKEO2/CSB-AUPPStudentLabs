class Song:
    #Use class object to create song
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length
        
    #This will display when you print an object
    def __repr__(self):
        return f"{self.title} by {self.artist} ({self.album}, {self.genre}, {self.length} mins)"


class MusicLibrary:
    #Use dictionary to store songs and ensure efficiency when restrieving song data
    #Use set to preventing duplicate, before adding to self.songs(), it checks if it already exists in self.song_set
    def __init__(self):
        self.songs = {}
        self.song_set = set()

    def add_song(self, song):
        if song.title not in self.song_set:
            self.songs[song.title] = song
            self.song_set.add(song.title)
        else:
            print("Song already exists in the library.")

    def get_songs_by_artist(self, artist):
        print(f"Songs by {artist}:")
        return [song for song in self.songs.values() if song.artist == artist]

    def get_songs_by_album(self, album):
        print(f"Song in \"{album}\":")
        return [song for song in self.songs.values() if song.album == album]

    def get_songs_by_genre(self, genre):
        print(f"{genre} songs:")
        return [song for song in self.songs.values() if song.genre == genre]

    def get_songs_by_title(self, title):
        print(f"Song with the title of: {title}")
        return self.songs.get(title, None)


class Playlist:
    #Use list in self.songs to maintain the song data and for indexing in display_playlist()
    #Use set in self.song_set to stores the unique titles of songs 
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.song_set = set()

    def add_song(self, song):
        if song.title not in self.song_set:
            self.songs.append(song)
            self.song_set.add(song.title)
        else:
            print("Song already exists in the playlist.")

    def remove_song(self, song):
        if song.title in self.song_set:
            self.songs.remove(song)
            self.song_set.remove(song.title)
        else:
            print("Song not found in the playlist.")

    def reorder_songs(self, new_order):
        if set(new_order) == self.song_set:
            self.songs = [song for title, song in sorted(zip(new_order, self.songs), key=lambda x: new_order.index(x[0]))]
        else:
            print("Invalid new order. Playlist remains unchanged.")

    def display_playlist(self):
        print(f"{self.name}'s playlist:")
        for index, song in enumerate(self.songs, start=1):
            print(f"{index}. {song}")

