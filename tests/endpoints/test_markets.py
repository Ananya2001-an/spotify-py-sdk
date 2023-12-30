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
def get_market_data():
    with open("tests/data/valid_markets.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_markets(api, get_market_data):
    result = api.markets.get_available_markets()

    assert result == get_market_data


