from src import SpotifyApi, SdkConfig

CLIENT_ID = "Enter your Client ID"
CLIENT_SECRET = "Enter your Client Secret"


def main():
    config = SdkConfig()
    config.before_request = lambda x, y: print("Before request!")
    # TODO async/await request
    # config.after_request = lambda x, y, z: print("After request!")

    api: SpotifyApi = SpotifyApi(CLIENT_ID, CLIENT_SECRET, config)
    print(api.albums.get("4EcfbzCtbJDk2wMwhT4D1h"))


if __name__ == "__main__":
    main()
