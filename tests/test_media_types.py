from unittest import TestCase

from api_deezer import API
from api_deezer.utils import magic_link
from api_deezer.exceptions.data import Error_Data_404


class Test_Types_Serialization(TestCase):
	__API = API()


	def test_album(self):
		"""

		Test that json from album is serialized correctly

		"""

		album_links = (
			'https://api.deezer.com/album/103248', 'https://www.deezer.com/us/album/61014232',
			'https://www.deezer.com/us/album/48667542', 'https://www.deezer.com/us/album/48667541'
		)

		for album_link in album_links:
			type_media, album_link = magic_link(album_link)

			try:
				self.__API.get_album(album_link)
			except Error_Data_404:
				pass


	def test_track(self):
		"""

		Test that json from track is serialized correctly

		"""

		track_links = (
			'https://api.deezer.com/track/916409', 'https://deezer.page.link/JvPGmTbTvAvQrzAq6', 'https://api.deezer.com/track/367620991'
		)
		
		for track_link in track_links:
			type_media, track_link = magic_link(track_link)

			track = self.__API.get_track(track_link)
			print(track.explicit_content_lyrics)
			print(track.explicit_content_cover)


	def test_track_by_isrc(self):
		assert self.__API.get_track_by_isrc('USUM71703861').isrc == 'USUM71703861'


	def test_album_by_upc(self):
		assert self.__API.get_album_by_upc('602557656527').upc == '602557656527'


	def test_artist(self):
		"""
		Test that json from artist is serialized correctly
		"""

		artist_links = (
			'https://deezer.page.link/WaEsJEunPW7zYgSf8', 'https://api.deezer.com/artist/13',
			'https://deezer.page.link/dUjJTkNsBXphpNWb9'
		)

		for artist_link in artist_links:
			type_media, artist_link = magic_link(artist_link)

			self.__API.get_artist(artist_link)


	def test_playlist(self):
		"""
		Test that json from playlist is serialized correctly
		"""

		playlist_links = (
			'https://api.deezer.com/playlist/10759081022', 'https://www.deezer.com/us/playlist/7326402184'
		)

		for playlist_link in playlist_links:
			type_media, playlist_link = magic_link(playlist_link)

			playlist = self.__API.get_playlist(playlist_link)
			print(playlist.tracks[0].explicit_content_lyrics)


	def test_chart(self):
		"""
		Test that json from chart is serialized correctly
		"""

		self.__API.get_chart()


	def test_search(self):
		"""
		Test that json from search is serialized correctly
		"""

		self.__API.search('eminem')
		#pp(res)
