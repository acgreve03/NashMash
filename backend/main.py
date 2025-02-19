import spotipy
import os 
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_songs(song1, song2):

    """Fetch song data"""
    song1_data = get_song_data_from_spotify(song1)
    song2_data = get_song_data_from_spotify(song2)


    """Get recommendation response"""
    openai_response = query_openai(song1_data, song2_data)