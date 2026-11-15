"""
Whimsical Story Soundtrack Engine
Synthesizes a heartwarming fairytale orchestral/acoustic soundscape via FFmpeg harmonic synthesis,
providing gentle Disney-Pixar style background music for stories.
"""

import os
import subprocess


def generate_pixar_fairytale_music(output_path="fairytale_ambient.mp3", duration=45):
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return output_path

    print(f"[*] Generating whimsical fairytale soundtrack ({duration}s)...")
    # Soft whimsical harmonic progression (C Major / G Major playful fairytale chord)
    expr = (
        "0.05*sin(2*PI*261.63*t) + "   # C4
        "0.04*sin(2*PI*329.63*t) + "   # E4
        "0.04*sin(2*PI*392.00*t) + "   # G4
        "0.03*sin(2*PI*523.25*t) + "   # C5
        "0.02*sin(2*PI*659.25*t)"      # E5
    )
    filter_chain = (
        f"aevalsrc='{expr}':s=44100:d={duration},"
        "aecho=0.8:0.9:800|1400:0.3|0.2,"
        "lowpass=f=950,"
        "afade=t=in:ss=0:d=1.5,"
        f"afade=t=out:st={duration-2.5}:d=2.5,"
        "volume=0.3"
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
        print(f"[Warning] Procedural fairytale sound notice: {e}")
        return None
