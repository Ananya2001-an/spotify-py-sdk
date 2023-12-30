import pytest
from src import SpotifyApi
import os
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def api():
    return SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))


def test_search_track(api):
    q = "Katatonia"
    result = api.search.execute(q, ["artist"])
    all_mentioned_artists: list[str] = [artist["name"] for artist in result["artists"]["items"]]

    assert "Katatonia" in all_mentioned_artists

