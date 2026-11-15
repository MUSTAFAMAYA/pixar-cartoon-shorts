"""
3D Pixar Islamic Habits Animated Typography Engine
Renders vibrant, modern dual subtitles formatted for 9:16 Islamic Reels:
- Header: '✦ रोज़मर्रा की सुन्नतें ✦' in royal gold
- Topic Pill: '[ Title in Hindi | Title in Roman English ]'
- Dual Synchronized Subtitles:
    - Line 1: Bold Hindi text with dark outline & soft shadow
    - Line 2: Vibrant golden-yellow Roman English transliteration
    - Animated elastic bounce pop (\fscx108\fscy108 -> 100%) in exact real-time sync with speech!
- Sunnah Rule / सीख at the bottom!
"""

import subprocess

ASS_HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: PixarHeader,Nirmala UI,64,&H0042D4F5,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,6,3,2,60,60,1540,1
Style: PixarTopic,Nirmala UI,50,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,5,2,2,60,60,1440,1
Style: CartoonHindi,Nirmala UI,72,&H00FFFFFF,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,7,4,2,70,70,880,1
Style: CartoonRoman,Arial,52,&H0042D4F5,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,6,3,2,70,70,680,1
Style: PixarMoral,Nirmala UI,48,&H0000FFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,5,3,2,80,80,360,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def format_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int(round((seconds - int(seconds)) * 100))
    if centis >= 100:
        centis = 99
    return f"{hours:01d}:{minutes:02d}:{secs:02d}.{centis:02d}"


def get_audio_duration(audio_path):
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        audio_path,
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        return float(res.stdout.strip())
    except Exception:
        return 25.0


def generate_pixar_typography(
    story_info, audio_path, output_ass_path="story_subtitles.ass", word_timings=None
):
    duration = get_audio_duration(audio_path)
    total_time_str = format_ass_time(duration)

    lines = []
    # 1. Top Header with playful pop
    header_anim = r"{\fad(400,0)\t(0,250,\fscx106\fscy106)\t(250,500,\fscx100\fscy100)}"
    lines.append(
        f"Dialogue: 0,0:00:00.00,{total_time_str},PixarHeader,,0,0,0,,{header_anim}✦ रोज़मर्रा की सुन्नतें ✦"
    )

    # 2. Topic Pill
    topic_anim = r"{\fad(500,0)}"
    topic_str = f"[ {story_info['title_hindi']}  |  {story_info['title_roman']} ]"
    lines.append(
        f"Dialogue: 0,0:00:00.00,{total_time_str},PixarTopic,,0,0,0,,{topic_anim}{topic_str}"
    )

    # 3. Bottom Moral Highlight
    moral_anim = r"{\fad(500,0)}"
    moral_str = f"💡 सुन्नत: {story_info['moral_hindi']}"
    lines.append(
        f"Dialogue: 0,0:00:00.00,{total_time_str},PixarMoral,,0,0,0,,{moral_anim}{moral_str}"
    )

    # 4. Synchronized Story Subtitles
    hindi_lines = story_info.get("subtitles_hindi", [])
    roman_lines = story_info.get("subtitles_roman", [])
    num_subs = max(len(hindi_lines), len(roman_lines), 1)

    # Calculate timing slices
    if word_timings and len(word_timings) >= num_subs:
        words_per_sub = len(word_timings) / num_subs
        timing_slices = []
        for idx in range(num_subs):
            w_start_idx = int(idx * words_per_sub)
            w_end_idx = min(int((idx + 1) * words_per_sub), len(word_timings) - 1)
            t_start = max(0.0, word_timings[w_start_idx]["start"] - 0.05)
            t_end = min(duration, word_timings[w_end_idx]["end"] + 0.25)
            timing_slices.append((t_start, t_end))
    else:
        time_per_sub = duration / num_subs
        timing_slices = [
            (idx * time_per_sub, min((idx + 1) * time_per_chunk if 'time_per_chunk' in locals() else (idx + 1) * time_per_sub, duration))
            for idx in range(num_subs)
        ]

    for idx, (t_start, t_end) in enumerate(timing_slices):
        start_t = format_ass_time(t_start)
        end_t = format_ass_time(t_end)

        h_text = hindi_lines[idx] if idx < len(hindi_lines) else ""
        r_text = roman_lines[idx] if idx < len(roman_lines) else ""

        # Elastic cartoon pop animation
        anim_pop = r"{\fad(100,100)\t(0,120,\fscx108\fscy108)\t(120,240,\fscx100\fscy100)}"

        if h_text:
            lines.append(f"Dialogue: 1,{start_t},{end_t},CartoonHindi,,0,0,0,,{anim_pop}{h_text}")
        if r_text:
            lines.append(f"Dialogue: 1,{start_t},{end_t},CartoonRoman,,0,0,0,,{anim_pop}{r_text}")

    with open(output_ass_path, "w", encoding="utf-8") as f:
        f.write(ASS_HEADER + "\n".join(lines))

    print(f"[+] Islamic habits animated subtitles generated at {output_ass_path}")
    return output_ass_path
