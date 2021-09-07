import os
from LyricFetcher import LyricFetcher
import time
from SwSpotify import spotify

def main():
    try:
        with open("./apikey.txt", "r") as file:
            line = file.readline()
            if line == "":
                print("API Key not set, add Genius API Key to apikey.txt")
                input()
                exit()
            else:
                GeniusAPIKey = line

    except FileNotFoundError:
        with open("./apikey.txt", "w") as mkfile:
            mkfile.close()

        print("Created apikey.txt file. Add your Genius API Key here and restart")
        input()
        exit()

    
    lf = LyricFetcher(GeniusAPIKey)

    while 1:
        try:
            song = lf.GetSong()
            lyrics = lf.GetLyrics(song)
            time.sleep(0.1)
        except spotify.SpotifyClosed:
            print("Spotify must be running, press Enter to try again.")
            input()

if __name__ == '__main__':
    main()
