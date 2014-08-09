from slugify import slugify
import mechanicalsoup
import re

class Lyrics():

	# url pattern: one-after-909-lyrics-the-beatles.html
	BASE_URL = "http://www.lyrics.com/"

	def __init__(self, song_info):
		self.song_info = song_info
		

	def generate_url(self):
		query_string = self.song_info["title"].lower() + " lyrics "+self.song_info["artist"].lower()
		return slugify(query_string)+".html"

	@staticmethod
	def clean_lyrics(lyrics):
		cleaned_lyrics = lyrics.strip()
		cleaned_lyrics = cleaned_lyrics.partition("---");
		return cleaned_lyrics[0]

	def fetch(self):
		browser = mechanicalsoup.Browser()

		generated_url = self.generate_url()
		lyrics_url = Lyrics.BASE_URL + generated_url

		lyrics_page = browser.get(Lyrics.BASE_URL+generated_url)

		lyrics = lyrics_page.soup.select("#lyric_space")[0].get_text()

		return Lyrics.clean_lyrics(lyrics)
