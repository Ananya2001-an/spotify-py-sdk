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
def get_show_data():
    with open("tests/data/valid_show.json", "r", encoding="utf-8") as f:
        item = f.read()
    return json.loads(item)


# TODO: data doesn't exist anymore; need to update json file to run tests


# def test_get_show_single_item(api, get_show_data):
#     result = api.shows.get(get_show_data["id"], "GB")
#
#     assert result["id"] == get_show_data["id"]


# def test_get_show_multiple_items(api, get_show_data):
#     result = api.shows.get([get_show_data["id"], get_show_data["id"]], "GB")
#
#     assert len(result) == 2
#     assert result[0]["id"] == get_show_data["id"]
#     assert result[1]["id"] == get_show_data["id"]
#
#
# def test_get_show_episodes(api, get_show_data):
#     result = api.shows.episodes(get_show_data["id"], "GB")
#
#     assert len(result["items"]) > 0

