import spotipy
import os 
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import json 


#loading environment variables
load_dotenv()

#Authenticate Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET")))

def get_song_data_from_spotify(song):
    res = sp.search(q=song, type="track", limit=1)

    if res and res['tracks']['items'][0]:
        track = res['tracks']['items'][0]
        return{
            "title": track["name"],
            "artist": track["artists"][0]["name"],
            "id": track["id"],
            "preview_url": track["preview_url"],
            "spotify_url": track["external_urls"]["spotify"]
        }
    else:
        return {"error": "track not found"}
    
def get_audio_data(track_id):
    audio_data = sp.audio_features(track_id)
    if audio_data:
        return audio_data[0]
    else:
        return {"error": "audio data not found"}
    

#Save metadata to json so its more easily readable(for personal use)
def save_response_to_json(data, filename="spotify_response.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)  # Pretty print with indentation
    print(f"Response saved to {filename}")

if __name__ == "__main__":
   song = get_song_data_from_spotify("Shape of you")
   save_response_to_json(song)
   id = song["id"]
   print(sp.audio_features(["7qiZfU4dY1lWllzX7mPBI3"]))
   '''if "id" in song:
       audio_data = get_audio_data(song["id"])
       save_response_to_json(audio_data)'''

 


