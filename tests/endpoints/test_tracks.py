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
def get_track_data():
    with open("tests/data/valid_track.json", "r") as f:
        item = f.read()
    return json.loads(item)


def test_get_tracks_single_item(api, get_track_data):
    result = api.tracks.get(get_track_data["id"])

    assert result["id"] == get_track_data["id"]


def test_get_tracks_multiple_items(api, get_track_data):
    result = api.tracks.get([get_track_data["id"], get_track_data["id"]])

    assert len(result) == 2
    assert result[0]["id"] == get_track_data["id"]
    assert result[1]["id"] == get_track_data["id"]


def test_get_tracks_audio_features(api, get_track_data):
    result = api.tracks.audio_features(get_track_data["id"])

    assert result["id"] == get_track_data["id"]


def test_get_tracks_audio_features_multiple_items(api, get_track_data):
    result = api.tracks.audio_features([get_track_data["id"], get_track_data["id"]])

    assert len(result) == 2
    assert result[0]["id"] == get_track_data["id"]
    assert result[1]["id"] == get_track_data["id"]


def test_get_tracks_audio_analysis(api, get_track_data):
    result = api.tracks.audio_analysis(get_track_data["id"])

    assert result["track"]["tempo"] > 0

