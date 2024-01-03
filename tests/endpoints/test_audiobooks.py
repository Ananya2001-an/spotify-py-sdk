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
def get_audiobook_data():
    with open("tests/data/valid_audiobook.json", "r", encoding="utf-8") as f:
        item = f.read()
    return json.loads(item)


# TODO: data doesnt exist anymore; need to update json file to run tests


# def test_get_audiobook_single_item(api, get_audiobook_data):
#     result = api.audiobooks.get(get_audiobook_data["id"])
#
#     assert result["id"] == get_audiobook_data["id"]
#
#
# def test_get_audiobook_multiple_items(api, get_audiobook_data):
#     result = api.audiobooks.get([get_audiobook_data["id"], get_audiobook_data["id"]])
#
#     assert len(result) == 2
#     assert result[0]["id"] == get_audiobook_data["id"]
#     assert result[1]["id"] == get_audiobook_data["id"]
#
#
# def test_get_audiobook_chapters(api, get_audiobook_data):
#     result = api.audiobooks.get_audiobook_chapters(get_audiobook_data["id"])
#
#     assert len(result["items"]) > 0

