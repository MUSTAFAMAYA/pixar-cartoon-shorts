"""
Royalty-Free Licensed Islamic & Nature Visuals Engine
Features:
1. Real 1080x1920 9:16 vertical Islamic & Natural moving video clips from assets/videos/
2. Curated high-definition 1080x1920 9:16 vertical Islamic & Natural theme backgrounds from assets/backgrounds/
3. Applies smooth 3D Ken Burns cinematic motion (slow zoom & pan) on static backgrounds
4. Seamless concatenation across multi-shot sequences
5. Guaranteed 100% offline availability with ZERO API failures, timeouts, or rate limits!
"""

import os
import random
import shutil
import subprocess

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets", "backgrounds")
VIDEOS_DIR = os.path.join(os.path.dirname(__file__), "assets", "videos")


def prepare_video_clip(src_video, output_clip_path, duration=8):
    """Trims, loops, and formats a source video to strict 1080x1920 vertical 30fps MP4."""
    cmd = [
        "ffmpeg", "-y", "-stream_loop", "-1", "-i", src_video,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p",
        "-t", str(duration),
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-an",
        output_clip_path,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_clip_path


def get_random_islamic_background(output_image_path="bg_frame.jpg"):
    """Picks a curated royalty-free Islamic architectural or natural background image."""
    if os.path.exists(ASSETS_DIR):
        files = [os.path.join(ASSETS_DIR, f) for f in os.listdir(ASSETS_DIR) if f.endswith(".jpg")]
        if files:
            chosen = random.choice(files)
            print(f"[+] Loaded royalty-free background: {os.path.basename(chosen)}")
            shutil.copyfile(chosen, output_image_path)
            return output_image_path

    cmd = [
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=0x182638:s=1080x1920:d=1",
        "-vframes", "1", output_image_path,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_image_path


def create_motion_clip(image_path, output_clip_path, motion_type="zoom_in", duration=7):
    """Applies dynamic 3D camera pan/zoom motion to a static 1080x1920 background image."""
    total_frames = duration * 30

    if motion_type == "zoom_in":
        vf = f"scale=1080:1920,zoompan=z='min(zoom+0.0008,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30"
    elif motion_type == "pan_right":
        vf = f"scale=1280:1920,zoompan=z='1.10':x='if(lte(on,1),(iw-iw/zoom)/2,x+0.8)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30"
    elif motion_type == "zoom_out":
        vf = f"scale=1080:1920,zoompan=z='if(lte(on,1),1.15,max(1.0,zoom-0.0008))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30"
    else:
        vf = f"scale=1080:1920,zoompan=z='min(zoom+0.0006,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.3*on':d={total_frames}:s=1080x1920:fps=30"

    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image_path,
        "-vf", f"{vf},fps=30,format=yuv420p",
        "-t", str(duration),
        "-c:v", "libx264",
        "-preset", "fast",
        output_clip_path,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_clip_path


def generate_pixar_story_video(shots_prompts=None, output_video_path="pixar_background.mp4", target_duration=25):
    """
    Creates a multi-shot cinematic video using REAL moving video loops from assets/videos/
    with seamless fallback to high-definition 9:16 motion backgrounds.
    """
    motions = ["zoom_in", "pan_right", "zoom_out", "tilt_up"]
    clip_files = []

    # Check for real moving video clips first (User 5 videos + Fresh clips)
    local_videos = []
    if os.path.exists(VIDEOS_DIR):
        local_videos = [os.path.join(VIDEOS_DIR, f) for f in os.listdir(VIDEOS_DIR) if f.endswith(".mp4")]
        # Randomize selection so every video has fresh diverse background motion
        random.shuffle(local_videos)

    # Check for static high-definition backgrounds
    bg_files = []
    if os.path.exists(ASSETS_DIR):
        bg_files = [os.path.join(ASSETS_DIR, f) for f in os.listdir(ASSETS_DIR) if f.endswith(".jpg")]

    num_shots = 3
    shot_dur = max(7, int((target_duration + 3) / num_shots))

    for i in range(num_shots):
        clip_file = f"clip_{i+1}.mp4"

        # Tier 1: Real moving video loop from assets/videos/
        if local_videos:
            src_video = local_videos[i % len(local_videos)]
            print(f"[*] Preparing real moving video scene {i+1}: {os.path.basename(src_video)} ({shot_dur}s)...")
            try:
                prepare_video_clip(src_video, clip_file, duration=shot_dur)
                if os.path.exists(clip_file) and os.path.getsize(clip_file) > 10000:
                    clip_files.append(clip_file)
                    continue
            except Exception as e:
                print(f"[Warning] Failed to prepare video clip {src_video}: {e}")

        # Tier 2: Curated high-definition 9:16 background with 3D camera pan/zoom
        if bg_files:
            src_img = bg_files[i % len(bg_files)]
            print(f"[*] Animating 9:16 background scene {i+1}: {os.path.basename(src_img)} ({shot_dur}s)...")
            create_motion_clip(src_img, clip_file, motion_type=motions[i % len(motions)], duration=shot_dur)
            clip_files.append(clip_file)

    print(f"[*] Concatenating {len(clip_files)} video scenes...")
    concat_txt = "concat_list.txt"
    with open(concat_txt, "w") as f:
        for c in clip_files:
            f.write(f"file '{c}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-pix_fmt", "yuv420p",
        output_video_path,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_video_path
