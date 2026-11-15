"""
Facebook Reels Auto-Uploader via Official Meta Graph API
Uploads vertical 1080x1920 3D cartoon videos directly to your Facebook Page as Reels.
Never blocks from cloud servers (GitHub Actions) because it uses official Meta Graph API.
"""

import os
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GRAPH_API_VERSION = "v19.0"


def upload_facebook_reel(video_path, caption):
    page_id = os.getenv("FB_PAGE_ID")
    access_token = os.getenv("FB_PAGE_ACCESS_TOKEN")

    if not page_id or not access_token:
        print("[Notice] Facebook upload skipped: FB_PAGE_ID or FB_PAGE_ACCESS_TOKEN not set in Secrets.")
        return None

    video_file = Path(video_path).resolve()
    if not video_file.exists():
        print(f"[Error] Video file not found: {video_file}")
        return None

    print(f"[*] Initializing Facebook Reel upload for Page ID: {page_id}...")
    try:
        # Step 1: Initialize the Video Reel Upload Session
        init_url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/video_reels"
        init_payload = {
            "upload_phase": "start",
            "access_token": access_token,
        }
        res = requests.post(init_url, data=init_payload, timeout=30)
        data = res.json()

        if "video_id" not in data or "upload_url" not in data:
            print(f"[Error] Failed to initialize Facebook Reel session: {data}")
            return None

        video_id = data["video_id"]
        upload_url = data["upload_url"]
        print(f"[+] Facebook Reel session created. Video ID: {video_id}")

        # Step 2: Stream the Video Binary Data
        file_size = video_file.stat().st_size
        print(f"[*] Uploading video binary ({file_size} bytes)...")
        headers = {
            "Authorization": f"OAuth {access_token}",
            "offset": "0",
            "file_size": str(file_size),
        }

        with open(video_file, "rb") as f:
            up_res = requests.post(upload_url, headers=headers, data=f, timeout=180)

        # Step 3: Finish and Publish as Reel
        print("[*] Publishing Facebook Reel...")
        time.sleep(3)
        finish_url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/video_reels"
        finish_payload = {
            "access_token": access_token,
            "video_id": video_id,
            "upload_phase": "finish",
            "video_state": "PUBLISHED",
            "description": caption,
        }

        fin_res = requests.post(finish_url, data=finish_payload, timeout=30)
        fin_data = fin_res.json()

        if fin_data.get("success"):
            print(f"[SUCCESS] Facebook Reel published successfully! Video ID: {video_id}")
            return video_id
        else:
            print(f"[Notice] Facebook Reel response: {fin_data}")
            return video_id
    except Exception as e:
        print(f"[Error] Facebook Reel exception: {e}")
        return None
