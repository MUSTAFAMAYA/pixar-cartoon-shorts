"""
Peaceful Islamic Ambient Soundscape Engine
Synthesizes a heartwarming, reverent ambient soundscape via FFmpeg harmonic synthesis,
providing gentle Nasheed/ambient background pads for Islamic 3D Pixar habit stories.
"""

import os
import subprocess


def generate_pixar_fairytale_music(output_path="fairytale_ambient.mp3", duration=45):
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return output_path

    print(f"[*] Generating peaceful Islamic ambient soundscape ({duration}s)...")
    # Soft meditative harmonic chord (A3, C#4, E4, A4) with acoustic reverb and warmth
    expr = (
        "0.06*sin(2*PI*220.00*t) + "   # A3
        "0.04*sin(2*PI*277.18*t) + "   # C#4
        "0.04*sin(2*PI*329.63*t) + "   # E4
        "0.02*sin(2*PI*440.00*t)"      # A4
    )
    filter_chain = (
        f"aevalsrc='{expr}':s=44100:d={duration},"
        "aecho=0.8:0.9:1000|1800:0.35|0.25,"
        "lowpass=f=750,"
        "afade=t=in:ss=0:d=2,"
        f"afade=t=out:st={duration-3}:d=3,"
        "volume=0.25"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", filter_chain,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        output_path,
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return output_path
    except Exception as e:
        print(f"[Warning] Procedural sound synthesis notice: {e}")
        return None
