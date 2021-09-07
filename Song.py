class Song:
    Title = ""
    Artist = ""
    
    def __init__(self, spSong):
        self.Title = spSong[0]
        self.Artist = spSong[1]

    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__