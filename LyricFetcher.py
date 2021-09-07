import os
from Song import Song
import lyricsgenius
from SwSpotify import spotify

class LyricFetcher:
    def __init__(self, apikey):
        self.APIKey = apikey
        self.Genuis = lyricsgenius.Genius(self.APIKey)
        self.CurSong = Song

    def GetSong(self):
        song = Song(spotify.current())
        return song

    def GetLyrics(self, song):
        if (song != self.CurSong):
            result = self.Genuis.search_song(song.Title + " - " + song.Artist)
            self.CurSong = song
            os.system("cls")
            try:
                print(result.lyrics)
            except:
                print("No Lyrics")