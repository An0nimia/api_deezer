from enum import StrEnum

from urllib.parse import urlparse
from requests import get as req_get

from .exceptions.links import (
	Invalid_Link, Error_Making_Link
)

VALID_DOMAINS = (
	'deezer.page.link', 'deezer.com', 'api.deezer.com',
	'www.deezer.com',
)

NOT_VERIFY = VALID_DOMAINS[1:]


class Type_Media(StrEnum):
	TRACK = 'track'
	ALBUM = 'album'
	PLAYLIST = 'playlist'
	ARTIST = 'artist'


types_media = {
	type_media.value: type_media
	for type_media in Type_Media
}


def magic_link(link: str) -> tuple[Type_Media, str]:
	url_parsed = urlparse(link)

	if 'deezer.page.link' == url_parsed.netloc:
		url = req_get(link).url
		url_parsed_new = urlparse(url)
		path = url_parsed_new.path
	elif url_parsed.netloc in NOT_VERIFY:
		path = url_parsed.path
	else:
		raise Invalid_Link(link)

	s_path = path.split('/')
	id_media = s_path[-1]
	type_media = s_path[-2]

	if not id_media.isdigit():
		raise Error_Making_Link(link)

	return types_media[type_media], id_media