# PYTHON GENIUS SCRAPER

import lyricsgenius as genius
import requests
from bs4 import BeautifulSoup
import os

GENIUS_API_KEY = ''
api = genius.Genius(GENIUS_API_KEY)
base_url = 'http://api.genius.com'
headers = {
        'Authorization': 'Bearer ' + GENIUS_API_KEY
        }

# list of artists to scrape from
artists = [
        ]

def get_lyrics(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)
    json = response.json()
    path = json['response']['song']['path']
    #print 'path %s' % path
    page_url = 'http://genius.com' + path
    page = requests.get(page_url)

    print ('Page %s' % page)

    html = BeautifulSoup(page.text, 'html.parser')

    print ('HTML %s' % html)

    [h.extract() for h in html('script')]
    lyrics = html.find('div', { 'class': 'lyrics'}).get_text()

    # print out the lyrics
    print ('Lyrics %s' % lyrics)
    with open('lyrics/input.txt', 'a') as f:
        f.write(lyrics.encode('utf-8'))
        f.close()

if __name__ == "__main__":
    for artist_name in artists:

        artist = api.search_artist(artist_name, max_songs=200)

        for song in artist._songs:
            artist.add_song(song)
            print(song)

        with open ('data/lyrics/input.txt', 'a') as file:
            file.write(artist.save_lyrics('txt'))
            file.close()
