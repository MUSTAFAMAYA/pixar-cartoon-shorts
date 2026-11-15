"""
3D Pixar Islamic Sunnah Habits & Manners (Inspired by Islamishortsai)
Features:
- Ultra-cute 3D Pixar Muslim baby character (Zayd & Ayesha)
- Authentic daily Islamic Sunnah habits (Drinking water, Sleeping, Salam, Eating, Dua, Kindness)
- 4 Progressive 3D visual scene prompts per habit with cinematic motion
- Sweet, heartwarming narration in Hindi/Urdu with Roman English
- Tracks used habits in used_stories.json so every video is 100% unique!
"""

import json
import os
import random
from dotenv import load_dotenv

load_dotenv()

HISTORY_FILE = "used_stories.json"

ISLAMIC_HABITS = [
    {
        "id": "habit_water_sunnah",
        "title_hindi": "पानी पीने की 4 सुन्नतें",
        "title_roman": "4 Sunnah Habits of Drinking Water",
        "moral_hindi": "बैठकर, सीधे हाथ से, 3 सांसों में 'बिस्मिल्लाह' कहकर पानी पीना सुन्नत है।",
        "moral_roman": "Baith kar, seedhe haath se, 3 saanson mein 'Bismillah' keh kar paani peena Sunnah hai.",
        "character_theme": "ultra-cute 3D Pixar baby boy wearing white prayer cap topi and white kurta",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, ultra-cute adorable 3D Muslim baby boy with big expressive sparkling brown eyes "
                "and chubby rosy cheeks, wearing a pristine white crochet prayer cap topi and white silk kurta, sitting down politely on a clean wooden chair, "
                "holding a clear glass of water with his right hand, looking up with a sweet cheerful smile, bright warm morning sunlight, "
                "cozy Islamic home interior with soft lantern light, octane render 8k, Disney Unreal Engine 5 style, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the cute baby boy saying 'Bismillah' with a joyful glowing face, "
                "gently drinking water from the glass in his right hand with gentle sips, soft golden sparkle particles around the glass, "
                "warm cinematic lighting, ultra-detailed 8k, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the little Muslim toddler pausing to take a breath away from the glass with a happy sigh, "
                "his tiny fingers holding the glass firmly with his right hand, big glittering eyes full of innocence and gratitude, "
                "storybook aesthetic, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the cute baby boy finishing the water, placing the glass down, and raising both tiny hands "
                "in sweet dua saying 'Alhamdulillah', glowing heavenly warm light framing his face, pure heartwarming Disney-Pixar magic, vertical 9:16"
            ),
        ],
        "spoken_text": "प्यारे बच्चों और दोस्तों! क्या आप जानते हैं पानी पीने की प्यारी सुन्नतें क्या हैं? नंबर एक: हमेशा बैठ कर पानी पीजिए। नंबर दो: सीधे हाथ से गिलास पकड़िए। नंबर तीन: पीने से पहले 'बिस्मिल्लाह' कहिए। और नंबर चार: तीन सांसों में घूंट-घूंट करके पीजिए और आखिर में 'अल्हम्दुलिल्लाह' कहिए। सुन्नत पर अमल करने में ही बरकत और शिफा है।",
        "subtitles_hindi": [
            "पानी पीने की 4 प्यारी सुन्नतें!",
            "1. हमेशा बैठ कर पानी पीजिए।",
            "2. सीधे हाथ से गिलास पकड़िए।",
            "3. शुरू में 'बिस्मिल्लाह' कहिए।",
            "4. तीन सांसों में घूंट-घूंट पीजिए।",
            "और आखिर में 'अल्हम्दुलिल्लाह' कहिए!",
        ],
        "subtitles_roman": [
            "Paani peene ki 4 pyari Sunnatein!",
            "1. Hamesha baith kar paani pijiye.",
            "2. Seedhe haath se glass pakdiye.",
            "3. Shuru mein 'Bismillah' kahiye.",
            "4. Teen saanson mein ghoont-ghoont pijiye.",
            "Aur aakhir mein 'Alhamdulillah' kahiye!",
        ],
    },
    {
        "id": "habit_sleeping_sunnah",
        "title_hindi": "सोने की प्यारी सुन्नत",
        "title_roman": "Sunnah Way of Sleeping (Sone Ki Sunnah)",
        "moral_hindi": "दाहिनी करवट पर गाल के नीचे हाथ रखकर दुआ पढ़कर सोना सुन्नत है।",
        "moral_roman": "Daayein karwat par gaal ke neeche haath rakh kar dua padh kar sona Sunnah hai.",
        "character_theme": "cute 3D Pixar baby boy in cozy white pajamas and topi",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, cute chubby 3D Muslim baby boy wearing a white topi and soft cream pajamas, "
                "gently dusting his cozy bed with a clean cloth before sleeping, cute focused expression, warm glowing crescent moon lamp on bedside table, "
                "peaceful twilight bedroom, octane render 8k, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the adorable toddler lying down on his right side, resting his soft chubby cheek on his right palm, "
                "facing towards Qiblah with a peaceful serene smile, cozy soft blue quilt covering him, warm ethereal fairy-tale glow, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the baby boy with eyes gently closing, whispering the bedtime sleeping dua with soft golden "
                "sparkles drifting around him like blessings, heavenly peaceful atmosphere, Disney Pixar masterpiece, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the sweet baby boy sleeping peacefully under a vast magical night sky with glowing stars and crescent moon "
                "visible through the arched window, calm angels and serene light protecting him, vertical 9:16"
            ),
        ],
        "spoken_text": "रात को सोने से पहले प्यारे नबी सल्लल्लाहु अलैहि वसल्लम की प्यारी सुन्नतें अपनाइए। सबसे पहले अपना बिस्तर तीन बार झाड़ लीजिए। फिर दाहिनी करवट लेटकर अपना सीधा हाथ गाल के नीचे रखिए। और 'अल्लाहुम्मा बिस्मिका अमूतू व अहया' पढ़कर सो जाइए। अल्लाह की रहमत पूरी रात आपकी हिफाज़त करेगी।",
        "subtitles_hindi": [
            "सोने से पहले की प्यारी सुन्नतें!",
            "1. बिस्तर को तीन बार झाड़ लीजिए।",
            "2. दाहिनी करवट पर लेटिए।",
            "3. सीधा हाथ गाल के नीचे रखिए।",
            "4. सोने की प्यारी दुआ पढ़िए।",
            "अल्लाह की रहमत पूरी रात हिफाज़त करेगी!",
        ],
        "subtitles_roman": [
            "Sone se pehle ki pyari Sunnatein!",
            "1. Bistar ko teen baar jhaad lijiye.",
            "2. Daahini karwat par letiye.",
            "3. Seedha haath gaal ke neeche rakhiye.",
            "4. Sone ki pyari dua padhiye.",
            "Allah ki rehmat poori raat hifazat karegi!",
        ],
    },
    {
        "id": "habit_salam_smile",
        "title_hindi": "सलाम और मुस्कुराहट की सुन्नत",
        "title_roman": "Salam & Smiling Sunnah (Muskurana Sunnah Hai)",
        "moral_hindi": "मुस्कुराकर सलाम करने से दिलों की नफरत खत्म होती है और मोहब्बत बढ़ती है।",
        "moral_roman": "Muskura kar Salam karne se dilon ki nafrat khatam hoti hai aur mohobbat badhti hai.",
        "character_theme": "cute 3D Pixar baby boy at Masjid an-Nabawi in Madinah",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, ultra-cute adorable 3D Muslim baby boy with big sparkling brown eyes and rosy cheeks, "
                "wearing a white crochet topi and clean white kurta, standing cheerfully in the grand marble courtyard of Masjid an-Nabawi in Madinah, "
                "the iconic Green Dome and tall minarets in background, gentle white pigeons walking around, golden hour sunbeams, 8k vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the cute toddler raising his right hand gently to wave with a radiant sweet smile, "
                "placing his other hand on his heart saying 'Assalamu Alaikum' with pure joy, bright welcoming eyes, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the little boy pointing his tiny index finger up towards the heavens with a proud pious smile (Tawheed), "
                "flocks of white doves gracefully taking flight in the golden sky above the Green Dome, awe-inspiring cinematic beauty, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the happy Muslim boy clapping his hands in joy, surrounded by fluttering white pigeons, "
                "warm golden glow and sparkling blessing particles, heartwarming Disney Pixar aesthetic, vertical 9:16"
            ),
        ],
        "spoken_text": "रसूलुल्लाह सल्लल्लाहु अलैहि वसल्लम ने फरमाया: तुम में से कोई उस वक़्त तक मोमिन नहीं हो सकता जब तक आपस में मोहब्बत न करे। और मोहब्बत बढ़ाने का सबसे प्यारा तरीका है: आपस में सलाम को आम करो! जब भी किसी से मिलें तो मुस्कुराकर सलाम कीजिए, क्योंकि मुस्कुराना भी सदक़ा है और सलाम दिलों को जोड़ता है।",
        "subtitles_hindi": [
            "सलाम और मुस्कुराहट की बरकत!",
            "1. जब भी किसी से मिलें, पहले सलाम करें।",
            "2. 'अस्सलाम वालेकुम' पूरा बोलें।",
            "3. चेहरे पर प्यारी सी मुस्कान रखें।",
            "क्योंकि मुस्कुराना भी सदक़ा है!",
            "सलाम से दिलों में मोहब्बत बढ़ती है!",
        ],
        "subtitles_roman": [
            "Salam aur Muskurahat ki Barkat!",
            "1. Jab bhi kisi se milein, pehle Salam karein.",
            "2. 'Assalamu Alaikum' poora bolein.",
            "3. Chehre par pyari si muskaan rakhein.",
            "Kyunke muskurana bhi Sadqah hai!",
            "Salam se dilon mein mohobbat badhti hai!",
        ],
    },
    {
        "id": "habit_eating_sunnah",
        "title_hindi": "खाना खाने की 4 सुन्नतें",
        "title_roman": "4 Sunnah Manners of Eating",
        "moral_hindi": "हाथ धोकर, सीधे हाथ से, अपने सामने से खाना खाना सुन्नत है।",
        "moral_roman": "Haath dho kar, seedhe haath se, apne samne se khana khana Sunnah hai.",
        "character_theme": "cute 3D Pixar baby boy sitting on floor dastarkhwan",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, cute chubby 3D Muslim baby boy with white topi sitting cross-legged politely on a colorful "
                "traditional woven floor mat (dastarkhwan), washing his hands clean with water, beaming with happy excitement, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the little boy raising his right hand gently to take a small bite from a plate of dates and fresh fruits, "
                "saying 'Bismillah wa ala barakatillah' with glowing gratitude, warm golden dining lighting, octane render 8k, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the toddler eating carefully with his right hand from the side directly in front of him, "
                "respectful and neat table manners, chewing with mouth closed, big sparkling innocent eyes, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the happy boy finishing his food without wasting a single grain, raising his tiny hands in heartfelt dua "
                "saying 'Alhamdulillah', glowing heavenly warm light around him, pure heartwarming Pixar family joy, vertical 9:16"
            ),
        ],
        "spoken_text": "खाना खाने के प्यारे इस्लामी आदाब सीखिए। नंबर एक: खाने से पहले दोनों हाथ अच्छी तरह धोएं। नंबर दो: ज़मीन पर बैठकर 'बिस्मिल्लाह' पढ़कर शुरू करें। नंबर तीन: हमेशा सीधे हाथ से खाएं और अपने सामने से खाएं। और नंबर चार: खाने में कभी ऐब न निकालें और आखिर में अल्लाह का शुक्र अदा करें।",
        "subtitles_hindi": [
            "खाना खाने के प्यारे आदाब!",
            "1. खाने से पहले दोनों हाथ धोएं।",
            "2. 'बिस्मिल्लाह' कहकर शुरू करें।",
            "3. हमेशा सीधे हाथ से खाएं।",
            "4. अपने सामने से छोटा लुकमा लें।",
            "और आखिर में 'अल्हम्दुलिल्लाह' कहें!",
        ],
        "subtitles_roman": [
            "Khana khaane ke pyare aadab!",
            "1. Khaane se pehle dono haath dhoyen.",
            "2. 'Bismillah' keh kar shuru karein.",
            "3. Hamesha seedhe haath se khaayein.",
            "4. Apne samne se chhota luqma lein.",
            "Aur aakhir mein 'Alhamdulillah' kahein!",
        ],
    },
    {
        "id": "habit_entering_home",
        "title_hindi": "घर में दाखिल होने की सुन्नत",
        "title_roman": "Sunnah of Entering Home",
        "moral_hindi": "सीधा पैर आगे रखकर सलाम और दुआ के साथ घर में दाखिल होना बरकत लाता है।",
        "moral_roman": "Seedha pair aage rakh kar Salam aur dua ke saath ghar mein dakhil hona barkat laata hai.",
        "character_theme": "cute 3D Pixar baby boy stepping through front door",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, cute little Muslim baby boy with white topi and colorful backpack standing at the wooden door of his home, "
                "stepping forward with his right foot first, looking inside with big sparkling excited eyes, warm welcoming entryway light, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the toddler calling out 'Assalamu Alaikum' with a huge cheerful smile and waving hands, "
                "the cozy living room warmly lit with Islamic calligraphy art on walls, joyful family atmosphere, 8k vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the baby boy removing his tiny shoes neatly and placing them side by side, "
                "disciplined sweet manners, soft golden ambient light, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the happy boy hugging his loving family, golden blessing particles filling the home with peace and barakah, "
                "storybook Disney Pixar warmth, vertical 9:16"
            ),
        ],
        "spoken_text": "जब भी आप अपने घर में दाखिल हों तो सुन्नत का ख्याल रखिए। हमेशा सीधा पैर पहले अंदर रखिए, मुस्कुराकर बुलंद आवाज़ में 'अस्सलाम वालेकुम' कहिए, और घर में दाखिल होने की दुआ पढ़िए। ऐसा करने से शैतान घर से भाग जाता है और घर में बरकत और रहमत नाज़िल होती है।",
        "subtitles_hindi": [
            "घर में दाखिल होने की सुन्नत!",
            "1. सीधा पैर पहले अंदर रखें।",
            "2. घर वालों को मुस्कुराकर सलाम करें।",
            "3. घर में दाखिल होने की दुआ पढ़ें।",
            "अपने जूते करीने से रखें।",
            "इससे घर में बरकत और सुकून आता है!",
        ],
        "subtitles_roman": [
            "Ghar mein dakhil hone ki Sunnah!",
            "1. Seedha pair pehle andar rakhein.",
            "2. Ghar walon ko muskura kar Salam karein.",
            "3. Ghar mein dakhil hone ki dua padhein.",
            "Apne joote qareene se rakhein.",
            "Isse ghar mein barkat aur sukoon aata hai!",
        ],
    },
]


def load_used_ids():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()


def save_used_id(habit_id):
    used = load_used_ids()
    used.add(habit_id)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(list(used)), f, indent=2)


def get_next_story():
    used_ids = load_used_ids()
    available = [h for h in ISLAMIC_HABITS if h["id"] not in used_ids]

    if not available:
        print("[*] All Islamic habits have cycled. Resetting history...")
        available = ISLAMIC_HABITS
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    chosen = random.choice(available)
    save_used_id(chosen["id"])
    return chosen


def build_story_script(story):
    title = f"✦ {story['title_hindi']} ✦ | {story['title_roman']} #islamic #shorts #sunnah"
    caption = (
        f"🕌 3D Animated Islamic Habits & Sunnah\n"
        f"✨ {story['title_hindi']} ({story['title_roman']})\n\n"
        f"💡 सीख / Sunnah Rule:\n"
        f"🇮🇳 {story['moral_hindi']}\n"
        f"🔤 {story['moral_roman']}\n\n"
        f"Share this with your kids & family to revive the Sunnah! ❤️✨\n\n"
        f"#islamicreels #sunnahhabits #islamickids #3danimation #bukhari #muslim #prophetmuhammad #hadith #shorts #reels"
    )

    return {
        "id": story["id"],
        "title_hindi": story["title_hindi"],
        "title_roman": story["title_roman"],
        "moral_hindi": story["moral_hindi"],
        "moral_roman": story["moral_roman"],
        "character_theme": story.get("character_theme", "ultra-cute 3D Pixar Muslim baby boy with white topi"),
        "shots_prompts": story["shots_prompts"],
        "spoken_text": story["spoken_text"],
        "subtitles_hindi": story["subtitles_hindi"],
        "subtitles_roman": story["subtitles_roman"],
        "title": title,
        "caption": caption,
    }


if __name__ == "__main__":
    s = get_next_story()
    data = build_story_script(s)
    print("Habit:", data["title_hindi"])
    print("Prompts count:", len(data["shots_prompts"]))
