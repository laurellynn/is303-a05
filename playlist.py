'''
Laurel Lynn
IS 303 - A05

Playlist
This program contains a playlist of songs. 
Users can add songs, remove songs, and find songs over five minutes. 

Inputs: 
- Song title, artist, duration

Processes: 
Songs: song title, artist, duration, displays info. Checks if longer than 5 min
Playlists: stores all songs as a list. Adds songs, finds playlist length. Displays all books

Outputs:
- Each book's info, total songs, total duration
'''

class Song: 
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def is_long(self): 
        "Return True if song is over 5 minutes"
        return self.duration > 5
    
    def __str__(self):
        length = "long song" if self.is_long() else "average length"
        return f"'{self.title}' by {self.artist} ({self.duration} minutes, {length})"
    

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        "Add a song to the playlist"
        self.songs.append(song)

    def get_longest(self):
        "Return longest song"
        if len(self.songs) == 0:
            return None
        longest = self.songs[0]
        for s in self.songs:
            if s.duration > longest.duration: 
                longest = s
        return longest
    
    def __str__(self):
        header = f"Playlist: {self.name} ({len(self.songs)} songs)"
        song_list = ""
        for s in self.songs: 
            song_list = song_list + f"\n = {s}"
        return header + song_list
    

 #--- Main Flow ---

shelf = Playlist("My Favorite Songs")

shelf.add_song(Song("Don't Stop Me Now", "Queen", 3.32) )
shelf.add_song(Song("Fishin' In The Dark", "Nitty Gritty Dirt Band", 3.23) )
shelf.add_song(Song("Hotel California", "The Eagles", 6.30) )

print(shelf)

longest = shelf.get_longest()
print(f"Longest song: {longest.title} ({longest.duration} minutes)")

