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
def get_user_data():
    with open("tests/data/valid_user.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_user_profile(api, get_user_data):
    result = api.users.profile(get_user_data["id"])

    assert result["id"] == get_user_data["id"]
    assert result["display_name"] == get_user_data["display_name"]


