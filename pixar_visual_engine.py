"""
Disney-Pixar 3D Multi-Shot Cinematic Visual Engine
Takes 4 Pixar-style story prompts, downloads 1080x1920 vertical 3D renders from Pollinations FLUX,
applies dynamic 3D camera motions (zoom, pan, tilt), and crossfades them into a cohesive story sequence!
"""

import os
import random
import urllib.parse
import subprocess
import requests


def download_pixar_image(prompt, output_image_path):
    print(f"[*] Generating Pixar 3D visual: '{prompt[:65]}...'")
    encoded = urllib.parse.quote(prompt)
    seed = random.randint(1000, 999999)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1080&height=1920&model=flux&seed={seed}&nologo=true"

    try:
        res = requests.get(url, timeout=35)
        if res.status_code == 200:
            with open(output_image_path, "wb") as f:
                f.write(res.content)
            print(f"[+] Downloaded 3D visual to {output_image_path}")
            return output_image_path
    except Exception as e:
        print(f"[Warning] Image download notice: {e}. Using procedural colorful fallback.")

    # Procedural cartoon fallback if network fails
    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "lavfi",
        "-i",
        "color=c=0x1a2b4c:s=1080x1920:d=1",
        "-vframes",
        "1",
        output_image_path,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_image_path


def create_motion_clip(image_path, output_clip_path, motion_type="zoom_in", duration=7):
    """
    Applies dynamic 3D camera pan/zoom motion to a static image.
    """
    total_frames = duration * 30

    if motion_type == "zoom_in":
        vf = f"scale=1080:1920,zoompan=z='min(zoom+0.0015,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30"
    elif motion_type == "pan_right":
        vf = f"scale=1280:1920,zoompan=z='1.15':x='if(lte(on,1),(iw-iw/zoom)/2,x+1.2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30"
    elif motion_type == "zoom_out":
        vf = f"scale=1080:1920,zoompan=z='if(lte(on,1),1.25,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30"
    else:
        vf = f"scale=1080:1920,zoompan=z='min(zoom+0.001,1.18)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.5*on':d={total_frames}:s=1080x1920:fps=30"

    cmd = [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-i",
        image_path,
        "-vf",
        f"{vf},format=yuv420p",
        "-t",
        str(duration),
        "-c:v",
        "libx264",
        "-preset",
        "fast",
        output_clip_path,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_clip_path


def generate_pixar_story_video(shots_prompts, output_video_path="pixar_background.mp4", target_duration=25):
    """
    Creates a 4-shot animated sequence stitched together with cinematic crossfade transitions.
    """
    motions = ["zoom_in", "pan_right", "zoom_out", "tilt_up"]
    clip_files = []
    shot_dur = max(6, int((target_duration + 3) / max(len(shots_prompts), 1)))

    for i, prompt in enumerate(shots_prompts):
        img_file = f"shot_{i+1}.jpg"
        clip_file = f"clip_{i+1}.mp4"
        download_pixar_image(prompt, img_file)
        create_motion_clip(img_file, clip_file, motion_type=motions[i % len(motions)], duration=shot_dur)
        clip_files.append(clip_file)

    print("[*] Stitching 4 shots together with crossfade transitions...")
    # FFmpeg xfade filter complex for 4 clips
    n = len(clip_files)
    if n == 4:
        # Crossfade duration = 1s
        d = 1.0
        # Calculate transition offset points
        t1 = shot_dur - d
        t2 = t1 + shot_dur - d
        t3 = t2 + shot_dur - d

        filter_graph = (
            f"[0:v][1:v]xfade=transition=fade:duration={d}:offset={t1}[v01];"
            f"[v01][2:v]xfade=transition=fade:duration={d}:offset={t2}[v02];"
            f"[v02][3:v]xfade=transition=fade:duration={d}:offset={t3}[vfinal]"
        )

        cmd = [
            "ffmpeg",
            "-y",
            "-i", clip_files[0],
            "-i", clip_files[1],
            "-i", clip_files[2],
            "-i", clip_files[3],
            "-filter_complex", filter_graph,
            "-map", "[vfinal]",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "20",
            "-pix_fmt", "yuv420p",
            output_video_path,
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        # Simple concat fallback
        concat_txt = "concat_list.txt"
        with open(concat_txt, "w") as f:
            for c in clip_files:
                f.write(f"file '{c}'\n")
        cmd = [
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_txt,
            "-c", "copy",
            output_video_path,
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[+] Multi-shot Pixar background video created at {output_video_path}")
    return output_video_path
