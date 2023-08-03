import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests
import pandas as pd

class MusixMatchAPIConnection(ExperimentalBaseConnection[requests.Session]):
    """Basic st.experimental_connection implementation for MusixMatch API"""

    def _connect(self, **kwargs) -> requests.Session:
        session = requests.Session()
        session.headers.update({"user-agent": "Streamlit App"})
        return session

    def get_top_tracks(self, api_key, country_code="XW"):
        base_url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get"
        params = {
            "chart_name": "top",
            "page": 1,
            "page_size": 5,
            "country": country_code,
            "f_has_lyrics": 1,
            "apikey": api_key
        }
        response = self._instance.get(base_url, params=params)
        data = response.json()

        if "track_list" in data["message"]["body"]:
            track_list = data["message"]["body"]["track_list"]
            track_names = [track["track"]["track_name"] for track in track_list]
            return track_names
        else:
            return []

# Initialize MusixMatchAPIConnection
musix_conn = MusixMatchAPIConnection(ConnectionError)

def main():
    st.title('MusixMatch: Generating Top-5 songs of a Country')

    # Search track
    api_key = st.text_input("Enter Musixmatch API key:")
    country_name = st.text_input('Enter country name (2-letter code):', 'XW')
    
    if st.button('Get Top Songs'):
        tracks = musix_conn.get_top_tracks(api_key, country_name)
        if tracks:
            st.write(f"Top Songs in {country_name}:")
            for idx, track in enumerate(tracks, start=1):
                st.write(f"{idx}. {track}")
        else:
            st.warning("No tracks found for the given country code.")

if __name__ == '__main__':
    main()
