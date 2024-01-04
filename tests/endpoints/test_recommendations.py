import json

import pytest
from src import SpotifyApi
from src.endpoints.recommendations import RecommendationsRequestRequiredArguments
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()


@pytest.fixture
def api():
    return SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))


@pytest.fixture
def get_genre_data():
    with open("tests/data/valid_genres.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_genres(api, get_genre_data):
    result = api.recommendations.genre_seeds()

    assert result == get_genre_data

@pytest.mark.asyncio
async def test_get_genres_async(api, get_genre_data):
    result = await api.recommendations.genre_seeds()

    assert result == get_genre_data


def test_get_recommendations(api):
    result = api.recommendations.get(RecommendationsRequestRequiredArguments(["0oSGxfWSnnOXhD2fKuz2Gy"], ["rock"], ["0c6xIDDpzE81m2q797ordA"]))

    assert len(result["tracks"]) > 0

@pytest.mark.asyncio
async def test_get_recommendations_async(api):
    result = await api.recommendations.get(RecommendationsRequestRequiredArguments(["0oSGxfWSnnOXhD2fKuz2Gy"], ["rock"], ["0c6xIDDpzE81m2q797ordA"]))

    assert len(result["tracks"]) > 0

