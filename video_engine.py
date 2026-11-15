"""
Pixar Cartoon Video Compositor
Combines:
- 1080x1920 Multi-shot 3D Pixar animated video sequence
- Warm storytelling voice narration (volume 1.0)
- Whimsical fairytale soundtrack (volume 0.18)
- Elastic cartoon animated typography (.ass)
Outputs broadcast-ready 1080x1920 MP4 for Instagram Reels & YouTube Shorts.
"""

import os
import subprocess
from sound_engine import generate_pixar_fairytale_music


def render_pixar_video(
    background_video_path,
    audio_path,
    subtitles_path,
    output_path="final_pixar_short.mp4",
):
    print("[*] Compositing final Pixar Cartoon Reel via FFmpeg...")

    clean_sub = subtitles_path.replace("\\", "/").replace(":", "\\:")
    soundtrack = generate_pixar_fairytale_music("fairytale_ambient.mp3", duration=40)

    if soundtrack and os.path.exists(soundtrack):
        print(f"[*] Blending narration voiceover with fairytale soundtrack...")
        filter_complex = (
            f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,ass={clean_sub}[v];"
            f"[1:a]volume=1.0[voice];"
            f"[2:a]volume=0.18,aloop=loop=-1:size=2e+09[bgm];"
            f"[voice][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]"
        )
        cmd = [
            "ffmpeg",
            "-y",
            "-stream_loop", "-1",
            "-i", background_video_path,
            "-i", audio_path,
            "-i", soundtrack,
            "-filter_complex", filter_complex,
            "-map", "[v]",
            "-map", "[aout]",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "21",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            output_path,
        ]
    else:
        filter_complex = f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,ass={clean_sub}[v]"
        cmd = [
            "ffmpeg",
            "-y",
            "-stream_loop", "-1",
            "-i", background_video_path,
            "-i", audio_path,
            "-filter_complex", filter_complex,
            "-map", "[v]",
            "-map", "1:a",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "21",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            output_path,
        ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"[Warning] Libass notice: {proc.stderr[-250:]}. Running simple fallback...")
            fallback_cmd = [
                "ffmpeg",
                "-y",
                "-stream_loop", "-1",
                "-i", background_video_path,
                "-i", audio_path,
                "-c:v", "libx264",
                "-preset", "fast",
                "-c:a", "aac",
                "-shortest",
                output_path,
            ]
            subprocess.run(fallback_cmd, check=True)

        print(f"[SUCCESS] Final Pixar 3D Video rendered: {output_path}")
        return output_path
    except Exception as e:
        print(f"[!] Rendering exception: {e}")
        return None
