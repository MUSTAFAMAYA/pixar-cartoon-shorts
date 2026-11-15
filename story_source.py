"""
Pixar-Style Heartwarming Moral & Life Wisdom Stories in Hindi & Roman Hindi/Urdu
Curated 3D animated storylines with character visual prompts, narration scripts, and moral lessons.
Tracks used IDs in used_stories.json to ensure every video features a brand new unique story!
"""

import json
import os
import random
from dotenv import load_dotenv

load_dotenv()

HISTORY_FILE = "used_stories.json"

PIXAR_STORIES = [
    {
        "id": "pixar_courage_ant",
        "title_hindi": "नन्ही चींटी और उड़ता पत्ता",
        "title_roman": "The Brave Little Ant (Nanhi Cheenti)",
        "moral_hindi": "मदद करने के लिए बड़ा होना ज़रूरी नहीं, सिर्फ बड़ा दिल होना चाहिए।",
        "moral_roman": "Madad karne ke liye bada hona zaroori nahi, sirf bada dil hona chahiye.",
        "character_theme": "cute tiny 3D Pixar animated worker ant with giant expressive brown eyes and blue scarf",
        "shots_prompts": [
            "Disney Pixar 3D animation style render, cute tiny worker ant with giant expressive sparkling brown eyes wearing a tiny red acorn cap, standing on a giant vibrant green leaf in an enchanted glowing forest, dew drops, morning golden sunlight, octane render 8k, whimsical storybook aesthetic, vertical 9:16",
            "Disney Pixar 3D animation style, the tiny ant braving a giant rushing raindrop puddle, holding onto a golden autumn leaf like a boat, determined heroic expression, dynamic motion, soft cinematic lighting, vertical 9:16",
            "Disney Pixar 3D animation style, the little ant pulling a cute colorful baby ladybug out of the water onto the dry leaf, heartwarming rescue, expressive joyful faces, magical sunbeams, 8k vertical 9:16",
            "Disney Pixar 3D animation style, the tiny ant and little ladybug hugging and smiling under a giant mushroom shelter with glowing fireflies around them, cozy warm fairy-tale atmosphere, vertical 9:16",
        ],
        "spoken_text": "एक जंगल में चीकू नाम की नन्ही चींटी रहती थी। सब उसे बहुत छोटा समझते थे। एक दिन तेज़ बारिश में एक नन्हीं तितली का बच्चा पानी में फंस गया। बड़े-बड़े कीड़े डर कर भाग गए, लेकिन चीकू ने एक सूखे पत्ते को नाव बनाया और अपनी जान जोखिम में डालकर उसे बचा लिया। सच है, किसी की मदद करने के लिए ताक़त नहीं, बड़ा दिल चाहिए।",
        "subtitles_hindi": [
            "एक जंगल में चीकू नाम की नन्ही चींटी रहती थी।",
            "सब उसे कमज़ोर और छोटा समझते थे।",
            "एक दिन तेज़ बारिश में नन्ही तितली पानी में बहने लगी।",
            "चीकू ने हिम्मत नहीं हारी, पत्ते को नाव बनाया।",
            "और अपनी जान पर खेलकर उसे बचा लिया।",
            "मदद करने के लिए ताक़त नहीं, बड़ा दिल चाहिए!",
        ],
        "subtitles_roman": [
            "Ek jungle mein Cheeku naam ki nanhi cheenti rehti thi.",
            "Sab use kamzor aur chhota samajhte the.",
            "Ek din tez baarish mein nanhi titli paani mein behne lagi.",
            "Cheeku ne himmat nahi haari, patte ko naav banaya.",
            "Aur apni jaan par khelkar use bacha liya.",
            "Madad karne ke liye taaqat nahi, bada dil chahiye!",
        ],
    },
    {
        "id": "pixar_magic_stone",
        "title_hindi": "जादुई चमकता पत्थर",
        "title_roman": "The Glowing Pebble (Jaadui Patthar)",
        "moral_hindi": "सच्ची खुशी दूसरों की ज़िंदगी में रोशनी भरने से मिलती है।",
        "moral_roman": "Sacchi khushi doosron ki zindagi mein roshni bharne se milti hai.",
        "character_theme": "cute fluffy 3D Pixar rabbit with big curious ears and oversized blue sweater",
        "shots_prompts": [
            "Disney Pixar 3D animation style render, adorable fluffy baby rabbit with huge curious ears wearing an oversized knitted blue sweater, walking through a twilight mossy forest, holding a mysterious softly glowing magical golden stone, 8k octane render, vertical 9:16",
            "Disney Pixar 3D animation style, the little bunny looking at the warm golden light of the stone, mesmerized and smiling with wonder, sparkling fireflies and mystical flowers in the background, cinematic soft glow, vertical 9:16",
            "Disney Pixar 3D animation style, the bunny seeing a sad shivering little hedgehog family in the dark hollow tree, feeling deep empathy, expressive emotional face, 8k vertical 9:16",
            "Disney Pixar 3D animation style, the bunny placing the glowing stone in the hedgehogs' home, everyone smiling warmly in the golden embrace of light, pure heartwarming Pixar happiness, vertical 9:16",
        ],
        "spoken_text": "टोनी खरगोश को जंगल में एक चमकता हुआ जादुई पत्थर मिला, जो बहुत सुकून और रोशनी देता था। टोनी पहले उसे अपनी जेब में छुपा कर खुश होता रहा। लेकिन रास्ते में जब उसने एक अंधेरे पेड़ में ठिठुरते हुए नन्हे साही के बच्चों को देखा, तो उसने वो पत्थर उनके घर में रख दिया। टोनी समझ गया कि रोशनी छुपाने से नहीं, बांटने से बढ़ती है।",
        "subtitles_hindi": [
            "टोनी खरगोश को एक चमकता जादुई पत्थर मिला।",
            "वो पहले उसे अपनी जेब में छुपाकर खुश था।",
            "मगर रास्ते में उसने अंधेरे में ठिठुरते नन्हे बच्चों को देखा।",
            "टोनी ने वो जादुई पत्थर उनके आशियाने में रख दिया।",
            "पूरा घर गर्म सुनहरी रोशनी से जगमगा उठा!",
            "रोशनी छुपाने से नहीं, बांटने से बढ़ती है।",
        ],
        "subtitles_roman": [
            "Tony khargosh ko ek chamakta jaadui patthar mila.",
            "Wo pehle use apni jeb mein chhupa kar khush tha.",
            "Magar raaste mein usne andhere mein thithurte nanhe bachon ko dekha.",
            "Tony ne wo jaadui patthar unke aashiyane mein rakh diya.",
            "Poora ghar garm sunhari roshni se jagmaga utha!",
            "Roshni chhupaane se nahi, baantne se badhti hai.",
        ],
    },
    {
        "id": "pixar_fear_flying",
        "title_hindi": "उड़ान से डरने वाली नन्ही चिड़िया",
        "title_roman": "The Bird Who Learned to Fly (Nanhi Chidiya)",
        "moral_hindi": "डर सिर्फ एक वहम है, पंख खोलते ही आसमान आपका होता है।",
        "moral_roman": "Darr sirf ek waham hai, pankh kholte hi aasmaan aapka hota hai.",
        "character_theme": "chubby cute 3D Pixar baby robin bird with fluffy feathers and tiny goggles",
        "shots_prompts": [
            "Disney Pixar 3D animation style render, cute chubby baby robin bird with fluffy blue and orange feathers wearing tiny aviator goggles on its head, peeking nervously over the edge of a high wooden birdhouse, expressive cartoon fear, 8k vertical 9:16",
            "Disney Pixar 3D animation style, the little baby bird looking at other birds soaring freely among golden sunset clouds, longing and doubt in its big glittering eyes, breathtaking scenic sky, vertical 9:16",
            "Disney Pixar 3D animation style, the baby bird taking a brave leap of faith, spreading its fluffy colorful wings, glowing wind swirls around it, euphoric expression of freedom, octane render 8k, vertical 9:16",
            "Disney Pixar 3D animation style, the happy bird soaring high into the vibrant golden pastel sunset sky above green rolling hills, joyful triumphant smile, cinematic masterpiece, vertical 9:16",
        ],
        "spoken_text": "पीको चिड़िया को ऊंचाई से बहुत डर लगता था। उसके सारे दोस्त आसमान में उड़ते थे, लेकिन पीको घोंसले में ही बैठी रहती थी। एक दिन उसकी माँ ने मुस्कुराकर कहा: 'अगर तुम कभी छलांग नहीं लगाओगी, तो कभी नहीं जान पाओगी कि तुम्हारे पंख कितने मज़बूत हैं।' पीको ने आंखें बंद की, छलांग लगाई, और उसके पंखों ने उसे आसमान का राजा बना दिया। डर के आगे ही जीत है।",
        "subtitles_hindi": [
            "पीको चिड़िया को उड़ने से बहुत डर लगता था।",
            "उसके सारे साथी खुले आसमान में सैर करते थे।",
            "माँ ने कहा: 'डर के आगे ही असली उड़ान है!'",
            "पीको ने हिम्मत की, आंखें बंद कर छलांग लगाई।",
            "और उसके पंखों ने उसे बादलों की सैर करा दी!",
            "डर सिर्फ वहम है, हिम्मत कीजिए, आसमान आपका है।",
        ],
        "subtitles_roman": [
            "Peeko chidiya ko udne se bohot darr lagta tha.",
            "Uske saare saathi khule aasmaan mein sair karte the.",
            "Maa ne kaha: 'Darr ke aage hi asli udaan hai!'",
            "Peeko ne himmat ki, aankhein band kar chhalaang lagai.",
            "Aur uske pankhon ne use baadlon ki sair kara di!",
            "Darr sirf waham hai, himmat kijiye, aasmaan aapka hai.",
        ],
    },
    {
        "id": "pixar_patient_turtle",
        "title_hindi": "कछुए का सच्चा हौसला",
        "title_roman": "The Patient Turtle (Sabr Ka Phal)",
        "moral_hindi": "रफ़्तार से ज़्यादा मंज़िल की तरफ लगातार चलना मायने रखता है।",
        "moral_roman": "Raftaar se zyada manzil ki taraf lagataar chalna maayne rakhta hai.",
        "character_theme": "cute 3D Pixar baby turtle with backpack and compass",
        "shots_prompts": [
            "Disney Pixar 3D animation style render, adorable baby turtle wearing a tiny leather explorer backpack and hiking boots, holding a miniature golden compass, standing at the foot of a winding rainbow mountain trail, vibrant 8k octane render, vertical 9:16",
            "Disney Pixar 3D animation style, a flashy cocky rabbit in sports sneakers speeding past laughing at the slow turtle, dynamic motion blur, expressive cartoon comedy, vertical 9:16",
            "Disney Pixar 3D animation style, the rabbit sleeping under a shaded apple tree while the little turtle steadily climbs the steep rocky path with sweat on its brow and determination in its eyes, vertical 9:16",
            "Disney Pixar 3D animation style, the smiling baby turtle standing proudly at the summit of the mountain bathed in glorious golden dawn sunlight with a trophy flag, breathtaking view, vertical 9:16",
        ],
        "spoken_text": "सैम कछुआ हमेशा धीरे-धीरे चलता था। बाकी जानवर उसकी धीमी चाल का मज़ाक उड़ाते थे। एक दिन पहाड़ की चोटी पर पहुंचने की दौड़ हुई। तेज़ भागने वाले रास्ते में ही थक कर सो गए, लेकिन सैम बिना रुके, एक-एक कदम आगे बढ़ाता रहा और सबसे पहले चोटी पर पहुंचकर इतिहास रच दिया। याद रखिए, लगातार चलना, रुक जाने से हमेशा बेहतर है।",
        "subtitles_hindi": [
            "सैम कछुआ हमेशा धीमी चाल से चलता था।",
            "बाकी सब उसका मज़ाक बनाते थे।",
            "एक दिन पहाड़ की चोटी तक रेस लगी।",
            "तेज़ भागने वाले घमंड में सो गए।",
            "मगर सैम बिना रुके मंज़िल तक पहुंच गया!",
            "सफलता रफ़्तार में नहीं, लगातार कोशिश में है।",
        ],
        "subtitles_roman": [
            "Sam kachhua hamesha dheemi chaal se chalta tha.",
            "Baaki sab uska mazaaq banate the.",
            "Ek din pahaad ki choti tak race lagi.",
            "Tez bhaagne wale ghamand mein so gaye.",
            "Magar Sam bina ruke manzil tak pahunch gaya!",
            "Safalta raftaar mein nahi, lagataar koshish mein hai.",
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


def save_used_id(story_id):
    used = load_used_ids()
    used.add(story_id)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(list(used)), f, indent=2)


def get_next_story():
    used_ids = load_used_ids()
    available = [s for s in PIXAR_STORIES if s["id"] not in used_ids]

    if not available:
        print("[*] All stories have cycled. Resetting history...")
        available = PIXAR_STORIES
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    chosen = random.choice(available)
    save_used_id(chosen["id"])
    return chosen


def build_story_script(story):
    title = f"✦ {story['title_hindi']} ✦ | {story['title_roman']} #pixar #3danimation #shorts"
    caption = (
        f"🎬 Disney Pixar 3D Moral Story\n"
        f"✨ {story['title_hindi']} ({story['title_roman']})\n\n"
        f"💡 Moral / सीख:\n"
        f"🇮🇳 {story['moral_hindi']}\n"
        f"🔤 {story['moral_roman']}\n\n"
        f"Follow @ for daily inspiring 3D Pixar stories & wisdom! ❤️\n\n"
        f"#pixaranimation #disneypixar #3dcartoon #moralstories #hindistories #lifelessons #reelsindia #shorts #viralshorts"
    )

    return {
        "id": story["id"],
        "title_hindi": story["title_hindi"],
        "title_roman": story["title_roman"],
        "moral_hindi": story["moral_hindi"],
        "moral_roman": story["moral_roman"],
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
    print("Story:", data["title_hindi"])
    print("Prompts count:", len(data["shots_prompts"]))
