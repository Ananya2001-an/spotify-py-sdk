## Python SDK for Spotify (Unofficial)

This is a Python library for the [Spotify Web API](https://developer.spotify.com/web-api/). This SDK is very simple to use if you are already familiar with the [typescript SDK](https://github.com/spotify/spotify-web-api-ts-sdk) provided by Spotify. It takes a lot of help from there. 


### Requirements

- python 3.8 or higher

### Using this in your project

```commandline
pip install spotify-py-sdk 
```

or if using poetry

```commandline
poetry add spotify-py-sdk 
```

### Running the example provided

First install the dependencies (make sure you have **poetry** installed):

```commandline
poetry install
```

Create a .env file in the root directory with your client_id and client_secret. Refer the `.env.example` file for reference.

```text
CLIENT_ID=
CLIENT_SECRET=
```

Now run the file to get results back from the web api:
```commandline
python example.py
```

### Create a client instance

Currently, we only have client credentials flow for authentication. If you're building a server side application, you should use Client Credentials Flow, and is the correct choice when you have both your Client ID and Client Secret available.

```python
from spotify-py-sdk import SpotifyApi, SdkConfig
from dotenv import load_dotenv
load_dotenv()

config = SdkConfig() # optional; can create custom methods
api: SpotifyApi = SpotifyApi(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), config)
```

Once you have an authenticated instance of the SDK, you can make requests to the Spotify Web API by using the methods exposed on the client instance of the API.

```python
api.search.execute("purpose", ["album"])
api.browse.get_categories()
```

### Running the tests

To run the tests, you need to have a Spotify account.

You will need to create a new app in the Spotify Developer portal, and add a redirect URI of http://localhost:3000.

You will need to add the following environment variables:
- `CLIENT_ID`
- `CLIENT_SECRET`

You can run the tests using `pytest`. We support `python-dotenv`, so you can add these to a `.env` file in the root of the repository.

To run all tests:
```python
pytest
```
To run a specific test.
```python
pytest tests/endpoints/test_albums.py
```

        
