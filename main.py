"""
====================================================================
PIXAR 3D CARTOON MORAL STORIES AUTO-GENERATOR & PUBLISHER
====================================================================
1. Pulls unique moral / wisdom story from story_source.py
2. Generates warm, expressive neural storytelling voiceover (Edge-TTS)
3. Tracks real-time word boundaries for voice-synchronized text animation
4. Renders 4 multi-shot Pixar 3D visual scenes with 3D camera pan/zoom & crossfades
5. Blends whimsical fairytale orchestral background soundtrack
6. Composites elastic cartoon typography & outputs final 1080x1920 MP4
7. Publishes to Instagram Reels & YouTube Shorts
====================================================================
"""

import argparse
import os
from dotenv import load_dotenv

from story_source import get_next_story, build_story_script
from voice_engine import generate_story_audio
from typography_engine import generate_pixar_typography, get_audio_duration
from pixar_visual_engine import generate_pixar_story_video
from video_engine import render_pixar_video
from uploader_youtube import upload_youtube_short
from uploader_facebook import upload_facebook_reel
from uploader_instagram import upload_instagram_reel

load_dotenv()


def run_pixar_pipeline(preview_only=False, platforms=("instagram", "facebook", "youtube")):
    print("\n========================================================")
    print("🎨 STARTING DISNEY-PIXAR 3D CARTOON STORY AUTOMATION")
    print("========================================================\n")

    # Step 1: Pick an unused Pixar moral story
    print("[Step 1] Sourcing Pixar 3D story...")
    raw_story = get_next_story()
    script_data = build_story_script(raw_story)
    print(f"  -> Title: {script_data['title_hindi']} ({script_data['title_roman']})")
    print(f"  -> Moral: {script_data['moral_hindi']}")

    # Step 2: Voiceover Narration with Word Sync
    print("\n[Step 2] Synthesizing expressive storytelling voiceover...")
    audio_file = "story_audio.mp3"
    audio_file, word_timings = generate_story_audio(script_data["spoken_text"], audio_file)
    audio_dur = int(get_audio_duration(audio_file)) + 2

    # Step 3: Cartoon Typography & Animated Subtitles
    print("\n[Step 3] Generating voice-synchronized Pixar cartoon typography...")
    subtitles_file = "story_subtitles.ass"
    generate_pixar_typography(script_data, audio_file, subtitles_file, word_timings=word_timings)

    # Step 4: 3D Pixar Multi-Shot Cinematic Visuals (Islamishortsai style)
    print("\n[Step 4] Generating 4-shot 3D Pixar cinematic visual sequence with crossfades...")
    bg_video = "pixar_background.mp4"
    generate_pixar_story_video(script_data["shots_prompts"], output_video_path=bg_video, target_duration=audio_dur)

    # Step 5: Render Video with Fairytale Soundtrack
    print("\n[Step 5] Rendering final Pixar Cartoon Short...")
    final_video = "final_pixar_short.mp4"
    render_pixar_video(bg_video, audio_file, subtitles_file, final_video)

    if not os.path.exists(final_video):
        print("[Fatal Error] Video rendering failed.")
        return

    print(f"\n[+] Pixar 3D Video ready at: {os.path.abspath(final_video)}")

    # Step 6: Social Media Publishing
    if preview_only:
        print("\n[!] --preview-only set. Skipping uploads.")
        return

    print("\n[Step 6] Publishing to Social Media...")
    if "facebook" in platforms:
        try:
            upload_facebook_reel(final_video, caption=script_data["caption"])
        except Exception as e:
            print(f"[!] Facebook notice: {e}")

    if "youtube" in platforms:
        try:
            upload_youtube_short(
                final_video,
                title=script_data["title"],
                description=script_data["caption"],
            )
        except Exception as e:
            print(f"[!] YouTube notice: {e}")

    if "instagram" in platforms:
        try:
            upload_instagram_reel(final_video, caption=script_data["caption"])
        except Exception as e:
            print(f"[!] Instagram notice: {e}")

    print("\n========================================================")
    print("✅ DISNEY-PIXAR 3D STORY AUTOMATION COMPLETED!")
    print("========================================================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pixar 3D Cartoon Story Automation")
    parser.add_argument("--preview-only", action="store_true", help="Generate video without uploading")
    args = parser.parse_args()

    run_pixar_pipeline(preview_only=args.preview_only)
