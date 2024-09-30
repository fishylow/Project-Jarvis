import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'
scope = "user-read-playback-state user-modify-playback-state" #for spotipy playback

#Authenticate with spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

#play song on spotify
def play_song(song_name, artist_name=None):
    # Refine search query with additional details like artist or album
    query = song_name
    if artist_name:
        query += f' artist:{artist_name}'
    
    # Search for the song with refined query
    results = sp.search(q=query, type='track', limit=1)
    
    if results['tracks']['items']:
        # Get the track ID
        track_id = results['tracks']['items'][0]['id']
        track_info = results['tracks']['items'][0]
        print(f"Playing: {track_info['name']} by {track_info['artists'][0]['name']} from the album '{track_info['album']['name']}'")
            
        # Start playback on the active device
        sp.start_playback(uris=[f"spotify:track:{track_id}"])
    else:
        print(f"Song '{song_name}' not found.")

def add_song_to_queue(song_name, artist_name=False):
    try:
        # Search for the song by name and artist
        results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track', limit=1)
        
        # Check if we got a result
        if results['tracks']['items']:
            track_id = results['tracks']['items'][0]['id']
            
            # Add the track to the queue
            sp.add_to_queue(track_id)
            return None
        else:
            return None
    
    except Exception as e:
        return None


#stops spotify music
def stop_music_playback():
    try:
        sp.pause_playback()  # Pause playback on the active device
        print("Playback stopped.")
    except Exception as e:
        print(f"Error stopping playback: {e}")

#skips song
def skip_song():
    try:
        sp.next_track()  # Skip to the next track
        print("Skipped to the next song.")
    except Exception as e:
        print(f"Error skipping song: {e}")

#goes back to the previous song.
def previous_song():
    try:
        sp.previous_track()  # Go back to the previous track
        print("Returned to the previous song.")
    except Exception as e:
        print(f"Error going back to previous song: {e}")

def start_song_from_beginning():
    try:
        sp.seek_track(0)  # Seek to the beginning of the current track
        print("Started the current song from the beginning.")
    except Exception as e:
        print(f"Error starting song from the beginning: {e}")