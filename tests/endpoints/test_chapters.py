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
def get_chapter_data():
    with open("tests/data/valid_chapter_api_response.json", "r", encoding="utf-8") as f:
        item = f.read()
    return json.loads(item)


def test_get_chapter_single_item(api, get_chapter_data):
    result = api.chapters.get(get_chapter_data["id"], "GB")

    assert result["id"] == get_chapter_data["id"]

@pytest.mark.asyncio
async def test_get_chapter_single_item_async(api, get_chapter_data):
    result = await api.chapters.get(get_chapter_data["id"], "GB")

    assert result["id"] == get_chapter_data["id"]


def test_get_chapter_multiple_items(api, get_chapter_data):
    result = api.chapters.get([get_chapter_data["id"], get_chapter_data["id"]], "GB")

    assert len(result) == 2
    assert result[0]["id"] == get_chapter_data["id"]
    assert result[1]["id"] == get_chapter_data["id"]

@pytest.mark.asyncio
async def test_get_chapter_multiple_items(api, get_chapter_data):
    result = await api.chapters.get([get_chapter_data["id"], get_chapter_data["id"]], "GB")

    assert len(result) == 2
    assert result[0]["id"] == get_chapter_data["id"]
    assert result[1]["id"] == get_chapter_data["id"]