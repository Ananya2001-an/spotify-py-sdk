import asyncio
import os

from src import SpotifyApi, SdkConfig
from dotenv import load_dotenv
load_dotenv()

config = SdkConfig()
config.before_request = lambda x, y: print("⁠✯🧸🎧☕⁠✯")
api: SpotifyApi = SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), config)
def main_sync():

    # TODO async/await request
    # config.after_request = lambda x, y, z: print("After request!")


    # print(api.albums.get(["4EcfbzCtbJDk2wMwhT4D1h", "4EcfbzCtbJDk2wMwhT4D1h"]))
    # print(api.current_user.followed_artists()) # insufficient client scope;
    # print(api.search.execute("purpose", ["album"]))
    resp = api.browse.get_categories()
    print(resp)

async  def main_async():
    async_response = await api.browse.get_categories()
    print(async_response)

if __name__ == "__main__":
    # main_sync()
    asyncio.run(main_async())