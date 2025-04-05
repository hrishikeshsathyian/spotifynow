import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv, time
import os


def main():
    
    dotenv.load_dotenv()
    print("Loading environment variables from .env file")
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    scope = "user-library-read user-read-playback-state"

    cache_path = ".cache"
    if os.path.exists(cache_path):
        os.remove(cache_path)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        scope=scope, 
        redirect_uri="http://127.0.0.1:8888/callback"))

    while True: 
        current = sp.current_playback()
        if not current: 
            break
        current = current['item']
        current_album_image = current['album']['images'][0]['url']
        print("Current album image: ", current_album_image)
        print("Current track: ", current['name'])
        time.sleep(3)

if __name__ == "__main__":
    main()