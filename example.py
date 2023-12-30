import os

from src import SpotifyApi, SdkConfig
from dotenv import load_dotenv
load_dotenv()


def main():
    config = SdkConfig()
    config.before_request = lambda x, y: print("⁠✯🧸🎧☕⁠✯")
    # TODO async/await request
    # config.after_request = lambda x, y, z: print("After request!")

    api: SpotifyApi = SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), config)
    # print(api.albums.get(["4EcfbzCtbJDk2wMwhT4D1h", "4EcfbzCtbJDk2wMwhT4D1h"]))
    # print(api.current_user.followed_artists()) # insufficient client scope;
    # print(api.search.execute("purpose", ["album"]))
    # print(api.browse.get_categories())


if __name__ == "__main__":
    main()
