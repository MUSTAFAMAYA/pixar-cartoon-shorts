"""
Instagram Reels Auto-Uploader for Pixar Cartoon Shorts
"""

import os
import json
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SESSION_FILE = "ig_session.json"


def get_instagram_client():
    from instagrapi import Client

    # Bypass deprecated Instagram qe/expose 404 error during media upload
    if not hasattr(Client, "_qe_patched"):
        _orig_request = Client.private_request

        def _patched_request(self, endpoint, *args, **kwargs):
            try:
                return _orig_request(self, endpoint, *args, **kwargs)
            except Exception as e:
                if "qe/expose" in str(endpoint) or "qe/expose" in str(e):
                    return {}
                raise e

        Client.private_request = _patched_request
        Client._qe_patched = True

    cl = Client()
    cl.delay_range = [2, 5]

    # Check any session secret: INSTAGRAM_SESSION_ID or IG_SESSION_JSON
    session_val = (os.getenv("INSTAGRAM_SESSION_ID") or os.getenv("IG_SESSION_JSON") or "").strip()
    if session_val:
        if session_val.startswith("{") and session_val.endswith("}"):
            try:
                print("[*] Loading Instagram session from JSON secret...")
                session_data = json.loads(session_val)
                cl.set_settings(session_data)
                return cl
            except Exception as e:
                print(f"[Warning] Failed to load JSON session settings: {e}")
        else:
            try:
                print("[*] Authenticating with Instagram via session ID cookie...")
                cl.login_by_sessionid(session_val)
                return cl
            except Exception as e:
                print(f"[Warning] Failed login_by_sessionid: {e}")

    # Check local session file
    if os.path.exists(SESSION_FILE):
        try:
            print(f"[*] Loading Instagram session from {SESSION_FILE}...")
            cl.load_settings(SESSION_FILE)
            return cl
        except Exception as e:
            print(f"[Warning] Failed to load {SESSION_FILE}: {e}")

    # Fallback to username & password
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    if not username or not password:
        raise ValueError("Neither INSTAGRAM_SESSION_ID nor username/password provided.")

    print(f"[*] Authenticating with Instagram as @{username}...")
    cl.login(username, password)
    try:
        cl.dump_settings(SESSION_FILE)
    except Exception:
        pass
    return cl


def upload_instagram_reel(video_path, caption):
    print("[*] Uploading Reel to Instagram...")
    cl = None
    try:
        cl = get_instagram_client()

        video_file = Path(video_path).resolve()
        thumb_file = Path("thumb_cover.jpg").resolve()

        # Generate explicit JPEG thumbnail cover via FFmpeg
        cmd = [
            "ffmpeg",
            "-y",
            "-i", str(video_file),
            "-ss", "00:00:01",
            "-vframes", "1",
            str(thumb_file),
        ]
        subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        thumbnail_to_use = thumb_file if thumb_file.exists() else None

        # Upload as Reel clip with Facebook auto-share enabled
        try:
            media = cl.clip_upload(
                video_file,
                caption=caption,
                thumbnail=thumbnail_to_use,
                share_to_facebook=True,
            )
        except Exception as fb_err:
            print(f"[*] Standard Reel upload notice: {fb_err}. Uploading standard clip...")
            media = cl.clip_upload(
                video_file,
                caption=caption,
                thumbnail=thumbnail_to_use,
            )

        media_id = getattr(media, "id", None) or getattr(media, "pk", str(media))
        print(f"[SUCCESS] Instagram Reel posted successfully! ID: {media_id}")
        return media_id
    except Exception as e:
        print(f"[Notice] Instagram clip_upload notice: {e}")
        if cl:
            try:
                print("[*] Attempting fallback video_upload...")
                media = cl.video_upload(
                    Path(video_path).resolve(),
                    caption=caption,
                    thumbnail=Path("thumb_cover.jpg").resolve()
                    if Path("thumb_cover.jpg").exists()
                    else None,
                )
                print(f"[SUCCESS] Fallback Reel posted! ID: {getattr(media, 'id', media)}")
                return getattr(media, "id", str(media))
            except Exception as e2:
                print(f"[Notice] Fallback upload notice: {e2}")
        return None
