"""
3D Pixar Character Lip-Sync & Video Engine
Orchestrates AI lip sync and cinematic animation for 3D Pixar Islamic Reels:
1. Generates 1080x1920 cute 3D Pixar character portrait (little Muslim girl in pastel hijab)
2. Tries deep-learning AI lip sync (SadTalker) to synchronize lips and head movements to speech
3. Falls back seamlessly to 4-shot cinematic sequence (crossfades + camera pan/zoom) if cloud spaces are queued
"""

import os
import random
import subprocess
import urllib.parse
import requests
from pixar_visual_engine import generate_pixar_story_video, generate_with_google_imagen


def download_character_portrait(prompt, output_image_path="char_base.jpg"):
    # Tier 1: Google Imagen 3
    img = generate_with_google_imagen(prompt, output_image_path)
    if img and os.path.exists(output_image_path) and os.path.getsize(output_image_path) > 5000:
        return output_image_path

    # Tier 2: Pollinations AI
    print(f"[*] Generating 3D Pixar Character portrait via Pollinations: '{prompt[:65]}...'")
    short_prompt = prompt[:280]
    encoded = urllib.parse.quote(short_prompt)
    seed = random.randint(1000, 999999)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1080&height=1920&model=turbo&seed={seed}&nologo=true"

    try:
        res = requests.get(url, timeout=50)
        if res.status_code == 200 and len(res.content) > 5000:
            with open(output_image_path, "wb") as f:
                f.write(res.content)
            print(f"[+] Downloaded 3D character portrait to {output_image_path}")
            return output_image_path
    except Exception as e:
        print(f"[Warning] Online character fetch notice: {e}")

    cmd = [
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=0x2b1055:s=1080x1920:d=1",
        "-vframes", "1", output_image_path,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_image_path


def try_ai_lipsync(image_path, audio_path, output_video_path="pixar_background.mp4"):
    """
    Attempts to generate neural AI lip sync using SadTalker.
    """
    spaces = [
        "kevinwang676/SadTalker",
        "vinthony/SadTalker",
    ]
    hf_token = os.getenv("HF_TOKEN", None)

    for space_name in spaces:
        try:
            print(f"[*] Connecting to AI lip-sync space: {space_name}...")
            from gradio_client import Client, handle_file

            client = Client(space_name, token=hf_token)
            result = client.predict(
                source_image=handle_file(image_path),
                driven_audio=handle_file(audio_path),
                preprocess="full",
                still_mode=True,
                enhancer=None,
                api_name="/generate",
            )
            if result and os.path.exists(result):
                print(f"[+] Neural Lip-Sync generated successfully: {result}")
                cmd = [
                    "ffmpeg", "-y", "-i", result,
                    "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
                    "-c:v", "libx264", "-preset", "fast", "-crf", "20",
                    "-an",
                    output_video_path,
                ]
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return output_video_path
        except Exception as e:
            print(f"[Notice] AI lip-sync on {space_name} note: {e}")

    return None


def generate_character_video(script_data, audio_path, output_video_path="pixar_background.mp4", target_duration=25):
    """
    Main animation dispatcher:
    1. Attempts AI Lip-Sync on the 3D character portrait.
    2. If cloud AI lip-sync is busy/queued, renders the 4-shot cinematic sequence with crossfades.
    """
    char_theme = script_data.get("character_theme", "ultra-cute 3D Pixar little Muslim girl wearing pastel pink hijab")
    portrait_prompt = (
        f"Disney Pixar 3D animation style render, ultra-cute adorable 3D little Muslim toddler girl with big sparkling brown eyes, "
        f"chubby pink cheeks, sweet angelic smile, wearing a beautiful pastel hijab, facing front towards camera, close-up portrait, "
        f"warm cinematic lighting, magical Islamic home interior background, octane render 8k, vertical 9:16 aspect ratio"
    )
    portrait_file = "char_portrait.jpg"
    download_character_portrait(portrait_prompt, portrait_file)

    # Attempt 1: AI Lip-Sync
    lipsync_res = try_ai_lipsync(portrait_file, audio_path, output_video_path=output_video_path)
    if lipsync_res and os.path.exists(output_video_path):
        return output_video_path

    # Attempt 2: 4-Shot Cinematic Visuals (Islamishortsai style)
    print("[*] AI Lip-sync unavailable; deploying 4-shot cinematic 3D visual progression with crossfades...")
    return generate_pixar_story_video(
        script_data["shots_prompts"],
        output_video_path=output_video_path,
        target_duration=target_duration,
    )
