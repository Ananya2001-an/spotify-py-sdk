import json

import pytest
from src import SpotifyApi
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()


@pytest.fixture
def api():
    return SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))


@pytest.fixture
def get_album_data():
    with open("tests/data/valid_album_result.json", "r") as f:
        item = f.read()
    return json.loads(item)


@pytest.fixture
def get_album_tracks_data():
    with open("tests/data/valid_album_tracks_result.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_album_single_item(api, get_album_data):
    result = api.albums.get(get_album_data["id"])

    assert result["name"] == get_album_data["name"]


@pytest.mark.asyncio
async def test_get_album_single_item_async(api, get_album_data):
    result = await api.albums.get(get_album_data["id"])

    assert result["name"] == get_album_data["name"]


def test_get_album_multiple_items(api, get_album_data):
    result = api.albums.get([get_album_data["id"], get_album_data["id"]])

    assert len(result) == 2
    assert result[0]["id"] == get_album_data["id"]
    assert result[1]["id"] == get_album_data["id"]


@pytest.mark.asyncio
async def test_get_album_multiple_items_async(api, get_album_data):
    result = await api.albums.get([get_album_data["id"], get_album_data["id"]])

    assert len(result) == 2
    assert result[0]["id"] == get_album_data["id"]
    assert result[1]["id"] == get_album_data["id"]


def test_get_album_tracks(api, get_album_data, get_album_tracks_data):
    result = api.albums.tracks(get_album_data["id"])

    assert len(result["items"]) == len(get_album_tracks_data["items"])


@pytest.mark.asyncio
async def test_get_album_tracks_async(api, get_album_data, get_album_tracks_data):
    result = await api.albums.tracks(get_album_data["id"])

    assert len(result["items"]) == len(get_album_tracks_data["items"])
