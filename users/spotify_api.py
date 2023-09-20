import os
from dotenv import load_dotenv
import base64
from requests import post, get
import json


load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")


# CREDIT - This video got me started with Spotify APIs:
# https://www.youtube.com/watch?v=WAmEZBEeNmg
def get_access_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    access_token = json_result["access_token"]
    return access_token


def get_auth_header(access_token):
    return {"Authorization": "Bearer " + access_token}


def search_for_item(access_token, item):
    headers = get_auth_header(access_token)

    url = f"https://api.spotify.com/v1/search"
    query = f"?q={item}&type=track&limit=5"
    query_url = url + query

    results = get(query_url, headers=headers)

    if results.status_code == 200:
        json_data = json.loads(results.content)
        json_tracks = json_data["tracks"]["items"]

        track_names = [track["name"] for track in json_tracks]
        return track_names

    elif results.status_code == 401:
        access_token = get_access_token()
        return search_for_item(access_token, item)

    elif results.status_code == 429:
        error_message = "Spotify API limit is reached, please try again later!"
        return error_message

    else:
        error_message = f"Error: {results.status_code}"
        return error_message


access_token = get_access_token()
results = search_for_item(access_token, "we are")
