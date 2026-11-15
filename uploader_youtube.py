"""
YouTube Shorts Auto-Uploader
Uploads generated Pixar 3D video to YouTube Shorts using OAuth2 client secrets / token.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def get_authenticated_service():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    token_str = os.getenv("YOUTUBE_TOKEN_JSON")
    if token_str:
        token_info = json.loads(token_str)
        creds = Credentials.from_authorized_user_info(token_info)
        return build("youtube", "v3", credentials=creds)

    token_file = Path("token.json")
    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file))
        return build("youtube", "v3", credentials=creds)

    raise FileNotFoundError("Missing YOUTUBE_TOKEN_JSON or token.json for YouTube upload.")


def upload_youtube_short(video_path, title, description, tags=None):
    from googleapiclient.http import MediaFileUpload

    print(f"[*] Uploading Pixar 3D Short to YouTube: '{title[:50]}...'")
    try:
        youtube = get_authenticated_service()
        if tags is None:
            tags = ["pixar", "3danimation", "disney", "moralstories", "shorts"]

        body = {
            "snippet": {
                "title": title[:100],
                "description": description,
                "tags": tags,
                "categoryId": "24",  # Entertainment
            },
            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False,
            },
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/mp4")
        request = youtube.videos().insert(part=",".join(body.keys()), body=body, media_body=media)
        response = request.execute()

        video_id = response.get("id")
        print(f"[SUCCESS] YouTube Short uploaded successfully! ID: {video_id}")
        return video_id
    except Exception as e:
        print(f"[Notice] YouTube upload skipped/notice: {e}")
        return None
