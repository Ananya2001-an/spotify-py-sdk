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
def get_episode_data():
    with open("tests/data/valid_episode.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_episode_single_item(api, get_episode_data):
    result = api.episodes.get(get_episode_data["id"], "GB")

    assert result == get_episode_data


def test_get_episode_multiple_items(api, get_episode_data):
    result = api.episodes.get([get_episode_data["id"], get_episode_data["id"]], "GB")

    assert len(result) == 2
    assert result[0]["id"] == get_episode_data["id"]
    assert result[1]["id"] == get_episode_data["id"]


