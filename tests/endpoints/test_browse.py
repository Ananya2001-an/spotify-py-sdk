import json

import pytest
from src import SpotifyApi
import os
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def api():
    return SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))


@pytest.fixture
def get_category_data():
    with open("tests/data/valid_category.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_categories(api):
    result = api.browse.get_categories()

    assert len(result["categories"]["items"]) > 0


def test_get_category(api, get_category_data):
    result = api.browse.get_category(get_category_data["id"])

    assert result == get_category_data


def test_get_category_playlists(api, get_category_data):
    result = api.browse.get_playlists_for_category(get_category_data["id"])

    assert len(result["playlists"]["items"]) > 0


def test_get_new_releases(api):
    result = api.browse.get_new_releases()

    assert len(result["albums"]["items"]) > 0

