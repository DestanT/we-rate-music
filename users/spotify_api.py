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

    query_url = f"https://api.spotify.com/v1/search?q={item}&type=track&limit=5"

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


def get_user_playlists(access_token, user_id):
    headers = get_auth_header(access_token)

    query_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

    results = get(query_url, headers=headers)

    if results.status_code == 200:
        json_data = json.loads(results.content)
        json_playlists = json_data["items"]

        all_playlists = []

        for playlist in json_playlists:
            playlist_id = playlist["id"]
            playlist_name = playlist["name"]
            playlist_image = playlist["images"][0]["url"]

            # Get Playlist Items
            query_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            results = get(query_url, headers=headers)

            if results.status_code == 200:
                json_data = json.loads(results.content)
                json_tracks = json_data["items"]

                track_details = []

                for track in json_tracks:
                    track_name = track["track"]["name"]
                    genres = "genres"
                    track_details.append({"track_name": track_name, "genres": genres})

                tracks = [track["track"]["name"] for track in json_tracks]
                # genres = json_tracks["track"]["artists"]

                all_playlists.append(
                    {
                        "playlist_name": playlist_name,
                        "playlist_image": playlist_image,
                        "track_details": track_details,
                    }
                )

        return all_playlists

    elif results.status_code == 401:
        access_token = get_access_token()
        return get_user_playlists(access_token, user_id)

    elif results.status_code == 429:
        error_message = "Spotify API limit is reached, please try again later!"
        return error_message

    else:
        error_message = f"Error: {results.status_code}"
        return error_message


access_token = get_access_token()
results = get_user_playlists(access_token, "11120434932")
print(results[0])
