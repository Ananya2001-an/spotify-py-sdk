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
def get_artist_data():
    with open("tests/data/valid_artist.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_artist_single_item(api, get_artist_data):
    result = api.artists.get(get_artist_data["id"])

    assert result["name"] == get_artist_data["name"]


def test_get_artist_multiple_items(api, get_artist_data):
    result = api.artists.get([get_artist_data["id"], get_artist_data["id"]])

    assert len(result) == 2
    assert result[0]["id"] == get_artist_data["id"]
    assert result[1]["id"] == get_artist_data["id"]


def test_get_artist_albums(api, get_artist_data):
    result = api.artists.albums(get_artist_data["id"])

    assert len(result["items"]) > 0


def test_get_artist_top_tracks(api, get_artist_data):
    result = api.artists.top_tracks(get_artist_data["id"], "GB")

    assert len(result["tracks"]) > 0


def test_get_artist_related_artists(api, get_artist_data):
    result = api.artists.related_artists(get_artist_data["id"])

    assert len(result["artists"]) > 0
