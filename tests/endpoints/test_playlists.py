import json

import pytest
from spotify_py_sdk import SpotifyApi
import os
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def api():
    return SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))


@pytest.fixture
def get_playlist_data():
    with open("tests/data/valid_playlist.json", "r") as f:
        item = f.read()
    return json.loads(item)


@pytest.fixture
def get_user_data():
    with open("tests/data/valid_user.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_playlist(api, get_playlist_data):
    result = api.playlists.get_playlist(get_playlist_data["id"])

    assert len(result["tracks"]["items"]) > 0


def test_get_playlist_with_additional_types(api, get_playlist_data):
    result = api.playlists.get_playlist(playlist_id=get_playlist_data["id"], additional_types=["episode"])

    assert len(result["tracks"]["items"]) > 0


def test_get_playlist_items(api, get_playlist_data):
    result = api.playlists.get_playlist_items(get_playlist_data["id"])

    assert len(result["items"]) > 0


def test_get_playlist_items_with_additional_types(api, get_playlist_data):
    result = api.playlists.get_playlist_items(playlist_id=get_playlist_data["id"], limit=1, offset=0, additional_types=["episode"])

    assert len(result["items"]) > 0


def test_get_user_playlists(api, get_user_data):
    result = api.playlists.get_users_playlists(get_user_data["id"])

    assert len(result["items"]) > 0


def test_get_playlist_cover_image(api):
    playlist_id = "37i9dQZF1DWXIcbzpLauPS"
    result = api.playlists.get_playlist_cover_image(playlist_id)

    assert len(result[0]["url"]) > 0

