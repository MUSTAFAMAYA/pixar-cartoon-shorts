"""
Expressive Storytelling Voice Engine
Synthesizes warm, engaging Hindi & Urdu narration using Microsoft Edge Neural TTS.
Primary Voice: 'hi-IN-MadhurNeural' (Warm, friendly Disney-style storyteller)
Fallback Voice: 'ur-PK-AsadNeural'
Captures real-time word boundary events (WordBoundary) so typography can animate
in exact sync with the narration voice!
"""

import asyncio
import os
import re
import edge_tts

VOICE_NAME = os.getenv("STORY_VOICE", "hi-IN-MadhurNeural")


def clean_text(text):
    text = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", text)
    return text.strip()


async def synthesize_story_voice(text, output_path="story_audio.mp3"):
    cleaned_text = clean_text(text)
    print(f"[*] Synthesizing expressive Pixar story narration with {VOICE_NAME}...")

    word_timings = []
    try:
        communicate = edge_tts.Communicate(cleaned_text, VOICE_NAME)
        with open(output_path, "wb") as f:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    start_sec = chunk["offset"] / 10_000_000.0
                    dur_sec = chunk["duration"] / 10_000_000.0
                    word_timings.append({
                        "word": chunk["text"],
                        "start": start_sec,
                        "end": start_sec + dur_sec,
                    })
    except Exception as e:
        print(f"[Warning] Primary voice ({VOICE_NAME}) stream notice: {e}. Trying fallback voice...")
        fallback_voice = "ur-PK-AsadNeural"
        try:
            fallback = edge_tts.Communicate(cleaned_text, fallback_voice)
            with open(output_path, "wb") as f:
                async for chunk in fallback.stream():
                    if chunk["type"] == "audio":
                        f.write(chunk["data"])
                    elif chunk["type"] == "WordBoundary":
                        start_sec = chunk["offset"] / 10_000_000.0
                        dur_sec = chunk["duration"] / 10_000_000.0
                        word_timings.append({
                            "word": chunk["text"],
                            "start": start_sec,
                            "end": start_sec + dur_sec,
                        })
        except Exception as e2:
            print(f"[Warning] Fallback stream notice: {e2}. Saving standard...")
            comm = edge_tts.Communicate(cleaned_text, fallback_voice)
            await comm.save(output_path)

    print(f"[+] Story narration audio saved to {output_path} ({len(word_timings)} words tracked)")
    return output_path, word_timings


def generate_story_audio(text, output_path="story_audio.mp3"):
    return asyncio.run(synthesize_story_voice(text, output_path))


if __name__ == "__main__":
    audio_path, timings = generate_story_audio("एक नन्ही चींटी की प्यारी कहानी।")
    print("Words captured:", len(timings))
