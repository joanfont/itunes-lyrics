from appscript import *
from providers.lyrics import Lyrics
from pprint import pprint

def get_itunes_track():
	itunes = app('iTunes')
	
	artist = itunes.current_track.artist()
	title = itunes.current_track.name()

	return { 'title' : title, 'artist' : artist }


def search_lyrics(song_info):
	provider = Lyrics(song_info)
	return provider.fetch()

def show_header(song_info):
	header = song_info["title"] + " - " + song_info["artist"]
	l_header = len(header)
	print("-"*l_header)
	print(header)
	print("-"*l_header)
	print()

def main():

	song_info = get_itunes_track()
	song_lyrics = search_lyrics(song_info)

	show_header(song_info)
	print(song_lyrics)
	print()


if __name__ == "__main__":

	main()