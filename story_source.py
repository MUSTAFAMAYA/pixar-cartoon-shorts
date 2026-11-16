"""
3D Pixar Islamic Sunnah Habits & Manners (Cute Little Muslim Girl Character)
Features:
- Ultra-cute adorable 3D Pixar little Muslim girl with big sparkling eyes, chubby rosy cheeks, and pastel hijab
- Authentic daily Islamic Sunnah habits (Drinking water, Sleeping, Salam & Smiling, Eating, Entering home, Kindness to Parents)
- 4 Progressive 3D visual scene prompts per habit with cinematic camera motion & crossfades
- Sweet, heartwarming narration in Hindi/Urdu with Roman English/Urdu subtitles
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
        "id": "habit_water_sunnah_girl",
        "title_hindi": "पानी पीने की 4 सुन्नतें",
        "title_roman": "4 Sunnah Habits of Drinking Water",
        "moral_hindi": "बैठकर, सीधे हाथ से, 3 सांसों में 'बिस्मिल्लाह' कहकर पानी पीना सुन्नत है।",
        "moral_roman": "Baith kar, seedhe haath se, 3 saanson mein 'Bismillah' keh kar paani peena Sunnah hai.",
        "character_theme": "ultra-cute 3D Pixar little Muslim girl wearing pastel pink hijab and modest dress",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, ultra-cute adorable 3D little Muslim toddler girl with big expressive sparkling brown eyes "
                "and chubby rosy cheeks, wearing a soft pastel pink floral hijab neatly framing her face and a cute modest cream dress, "
                "sitting down politely on a clean wooden chair, holding a clear glass of water with her right hand, looking up with a sweet cheerful smile, "
                "bright warm morning sunlight, cozy Islamic home interior with soft lantern light, octane render 8k, Disney Unreal Engine 5 style, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the cute little Muslim girl saying 'Bismillah' with a joyful glowing face, "
                "gently drinking water from the glass in her right hand with small peaceful sips, soft golden sparkle particles around the glass, "
                "warm cinematic lighting, ultra-detailed 8k, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the little toddler girl pausing to take a breath away from the glass with a happy sigh, "
                "her tiny fingers holding the glass firmly with her right hand, big glittering eyes full of innocence and gratitude, "
                "storybook Disney aesthetic, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the sweet little girl finishing the water, placing the glass down, and raising both tiny hands "
                "in sweet dua saying 'Alhamdulillah', glowing heavenly warm light framing her face, pure heartwarming Disney-Pixar magic, vertical 9:16"
            ),
        ],
        "spoken_text": "پیارے بچوں اور دوستو! کیا آپ جانتے ہیں پانی پینے کی پیاری سنتیں کیا ہیں؟ نمبر ایک: ہمیشہ بیٹھ کر پانی پیجیے۔ نمبر دو: سیدھے ہاتھ سے گلاس پکڑیے۔ نمبر تین: پینے سے پہلے 'بسم اللہ' کہیے۔ اور نمبر چار: تین سانسوں میں گھونٹ گھونٹ کر کے پیجیے اور آخر میں 'الحمد للہ' کہیے۔ سنت پر عمل کرنے میں ہی برکت اور شفا ہے۔",
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
        "id": "habit_sleeping_sunnah_girl",
        "title_hindi": "सोने की प्यारी सुन्नत",
        "title_roman": "Sunnah Way of Sleeping (Sone Ki Sunnah)",
        "moral_hindi": "दाहिनी करवट पर गाल के नीचे हाथ रखकर दुआ पढ़कर सोना सुन्नत है।",
        "moral_roman": "Daayein karwat par gaal ke neeche haath rakh kar dua padh kar sona Sunnah hai.",
        "character_theme": "cute 3D Pixar little Muslim girl in soft lavender hijab and cozy pajamas",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, cute chubby 3D little Muslim toddler girl wearing a soft lavender sleep hijab and soft cream pajamas, "
                "gently dusting her cozy bed with a clean cloth before sleeping, cute focused expression, warm glowing crescent moon lamp on bedside table, "
                "peaceful twilight bedroom, octane render 8k, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the adorable little girl lying down on her right side, resting her soft chubby cheek on her right palm, "
                "facing towards Qiblah with a peaceful serene smile, cozy soft pink quilt covering her, warm ethereal fairy-tale glow, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the little girl with eyes gently closing, whispering the bedtime sleeping dua with soft golden "
                "sparkles drifting around her like blessings, heavenly peaceful atmosphere, Disney Pixar masterpiece, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the sweet toddler girl sleeping peacefully under a vast magical night sky with glowing stars and crescent moon "
                "visible through the arched Islamic window, calm angels and serene light protecting her, vertical 9:16"
            ),
        ],
        "spoken_text": "رات کو سونے سے پہلے، ہمارے پیارے نبی، حضرت محمد مصطفیٰ، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، کی پیاری سنتیں اپنائیے۔ سب سے پہلے اپنا بستر تین بار جھاڑ لیجیے۔ پھر دائیں کروٹ پر لیٹ کر اپنا سیدھا ہاتھ گال کے نیچے رکھیے۔ اور سونے کی دعا 'اللہم باسمک اموت واحیا' پڑھ کر سو جائیے۔ اللہ کی رحمت پوری رات آپ کی حفاظت کرے گی۔",
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
        "id": "habit_salam_smile_girl",
        "title_hindi": "सलाम और मुस्कुराहट की सुन्नत",
        "title_roman": "Salam & Smiling Sunnah (Muskurana Sunnah Hai)",
        "moral_hindi": "मुस्कुराकर सलाम करने से दिलों की नफरत खत्म होती है और मोहब्बत बढ़ती है।",
        "moral_roman": "Muskura kar Salam karne se dilon ki nafrat khatam hoti hai aur mohobbat badhti hai.",
        "character_theme": "cute 3D Pixar little Muslim girl at Masjid an-Nabawi in Madinah",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, ultra-cute adorable 3D little Muslim toddler girl with big sparkling brown eyes and rosy cheeks, "
                "wearing a lovely white and gold floral hijab and pristine modest frock, standing cheerfully in the grand marble courtyard of Masjid an-Nabawi in Madinah, "
                "the iconic Green Dome and tall minarets in background, gentle white pigeons walking around, golden hour sunbeams, 8k vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the cute little girl raising her right hand gently to wave with a radiant sweet smile, "
                "placing her other hand on her heart saying 'Assalamu Alaikum' with pure joy, bright welcoming eyes, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the little girl pointing her tiny index finger up towards the heavens with a proud pious smile (Tawheed), "
                "flocks of white doves gracefully taking flight in the golden sky above the Green Dome, awe-inspiring cinematic beauty, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the happy Muslim girl clapping her hands in joy, surrounded by fluttering white pigeons, "
                "warm golden glow and sparkling blessing particles, heartwarming Disney Pixar aesthetic, vertical 9:16"
            ),
        ],
        "spoken_text": "اللہ کے پیارے رسول، حضرت محمد، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: تم میں سے کوئی اس وقت تک سچا مومن نہیں ہو سکتا جب تک آپس میں محبت نہ کرے۔ اور محبت بڑھانے کا سب سے پیارا طریقہ ہے: آپس میں سلام کو عام کرو! جب بھی کسی سے ملیں تو مسکرا کر 'السلام علیکم' کہیے، کیونکہ مسکرانا بھی صدقہ ہے اور سلام دلوں کو جوڑتا ہے۔",
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
        "id": "habit_eating_sunnah_girl",
        "title_hindi": "खाना खाने की 4 सुन्नतें",
        "title_roman": "4 Sunnah Manners of Eating",
        "moral_hindi": "हाथ धोकर, सीधे हाथ से, अपने सामने से खाना खाना सुन्नत है।",
        "moral_roman": "Haath dho kar, seedhe haath se, apne samne se khana khana Sunnah hai.",
        "character_theme": "cute 3D Pixar little Muslim girl sitting on floor dastarkhwan",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, cute chubby 3D little Muslim girl with soft pink hijab sitting cross-legged politely on a colorful "
                "traditional woven floor mat (dastarkhwan), washing her hands clean with water, beaming with happy excitement, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the little girl raising her right hand gently to take a sweet date from a silver plate, "
                "saying 'Bismillah wa ala barakatillah' with glowing gratitude, warm golden dining lighting, octane render 8k, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the toddler girl eating carefully with her right hand from the side directly in front of her, "
                "respectful and neat table manners, chewing with mouth closed, big sparkling innocent eyes, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the happy girl finishing her food without wasting a single grain, raising her tiny hands in heartfelt dua "
                "saying 'Alhamdulillah', glowing heavenly warm light around her, pure heartwarming Pixar family joy, vertical 9:16"
            ),
        ],
        "spoken_text": "کھانا کھانے کے پیارے اسلامی آداب سیکھیے۔ نمبر ایک: کھانے سے پہلے دونوں ہاتھ اچھی طرح دھوئیں اور کلی کریں۔ نمبر دو: زمین پر بیٹھ کر 'بسم اللہ' پڑھ کر شروع کریں۔ نمبر تین: ہمیشہ سیدھے ہاتھ سے اور اپنے سامنے سے کھائیں۔ اور نمبر چار: کھانے میں کبھی عیب نہ نکالیں اور آخر میں اللہ کا شکر ادا کریں۔",
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
        "id": "habit_parents_kindness_girl",
        "title_hindi": "वालिदैन की खिदमत और दुआ",
        "title_roman": "Kindness & Dua for Parents (Walidain Ki Khidmat)",
        "moral_hindi": "मां-बाپ की खिदमत करना और उनके लिए दुआ करना जन्नत का रास्ता है।",
        "moral_roman": "Maa-Baap ki khidmat karna aur unke liye dua karna Jannat ka rasta hai.",
        "character_theme": "cute 3D Pixar little Muslim girl with her loving mother",
        "shots_prompts": [
            (
                "Disney Pixar 3D animation style render, cute adorable 3D little Muslim girl with pink hijab smiling lovingly as she brings "
                "a warm cup of tea on a tray to her mother, showing great respect and tenderness, cozy warm home, 8k vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, close-up of the little girl gently hugging her mother's hand and kissing it with pure love, "
                "warm golden glow and soft sparkle particles of angelic blessings, Disney Pixar heartwarming moment, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the little girl raising her tiny hands high in heartfelt Dua, tears of joy in her big glittering eyes, "
                "reciting 'Rabbirhamhuma kama rabbayani sagheera', heavenly light streaming down, vertical 9:16"
            ),
            (
                "Disney Pixar 3D animation style, the happy mother and daughter smiling together, wrapped in divine peace and barakah, "
                "warm family harmony, storybook 3D animation aesthetic, vertical 9:16"
            ),
        ],
        "spoken_text": "اللہ کے پیارے رسول، حضرت محمد، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: والدین کی رضا میں ہی اللہ کی رضا ہے۔ اپنے ماں باپ کا ہمیشہ ادب کیجیے، ان سے کبھی اونچی آواز میں بات نہ کیجیے، اور ہر نماز کے بعد ان کے لیے یہ پیاری دعا مانگیے: رب ارحمہما کما ربیانی صغیرا۔",
        "subtitles_hindi": [
            "वालिदैन की खिदमत और प्यार!",
            "1. मां-बाप का हमेशा अदब कीजिए।",
            "2. कभी उनसे ऊंची आवाज़ में न बोलें।",
            "3. उनकी खुशी में अल्लाह की खुशी है।",
            "4. हर रोज़ उनके लिए दुआ मांगिए:",
            "'रब्बिर हमहुमा कमा रब्बयानी सगीरा'!",
        ],
        "subtitles_roman": [
            "Walidain ki Khidmat aur Pyar!",
            "1. Maa-Baap ka hamesha adab kijiye.",
            "2. Kabhi unse oonchi aawaz mein na bolein.",
            "3. Unki khushi mein Allah ki khushi hai.",
            "4. Har roz unke liye dua maangiye:",
            "'Rabbir hamhuma kama rabbayani sagheera'!",
        ],
    },
    {
        "id": "bukhari_6011_good_character",
        "title_hindi": "सब से बेहतरीन इंसान कौन?",
        "title_roman": "Best Person (Achhe Akhlaaq - Bukhari 6011)",
        "moral_hindi": "इंसान की असली खूबसूरती उसकी दौलत में नहीं, बल्कि उसके अच्छे अख़लाक़ में है।",
        "moral_roman": "Insaan ki asal khoobsurti uski daulat mein nahi, balke uske achhe akhlaaq mein hai.",
        "character_theme": "cute 3D Pixar little Muslim girl helping an elder smile",
        "shots_prompts": [],
        "spoken_text": "ہمارے پیارے نبی، حضرت محمد مصطفیٰ، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: تم میں سے سب سے بہترین انسان وہ ہے جس کے اخلاق اور کردار سب سے اچھے ہوں۔ انسان کی اصل خوبصورتی اچھے اخلاق اور زبان کی مٹھاس میں ہے۔",
        "subtitles_hindi": [
            "सब से बेहतरीन इंसान कौन?",
            "हज़रत मुहम्मद ﷺ ने फरमाया:",
            "'तुम में सब से बेहतरीन वो है,",
            "जिसका अख़लाक़ सब से अच्छा हो!'",
            "(सहीह बुखारी 6011)",
        ],
        "subtitles_roman": [
            "Sab Se Behtareen Insaan Kaun?",
            "Hazrat Muhammad ﷺ ne farmaya:",
            "'Tum mein sab se behtareen wo hai,",
            "Jiska akhlaaq sab se achha ho!'",
            "(Sahih Bukhari 6011)",
        ],
    },
    {
        "id": "bukhari_13_true_believer",
        "title_hindi": "सच्चे मोमिन की पहचान",
        "title_roman": "True Believer & Love (Bukhari 13)",
        "moral_hindi": "दूसरों के लिए वही पसंद करें जो अपने लिए पसंद करते हैं।",
        "moral_roman": "Doosron ke liye wahi pasand karein jo apne liye pasand karte hain.",
        "character_theme": "cute 3D Pixar little Muslim girl sharing toys happily",
        "shots_prompts": [],
        "spoken_text": "ہمارے پیارے نبی، حضرت محمد مصطفیٰ، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: تم میں سے کوئی اس وقت تک کامل مومن نہیں ہو سکتا، جب تک اپنے بھائی کے لیے وہی پسند نہ کرے، جو اپنے لیے پسند کرتا ہے۔ دوسروں کی خوشی میں خوش ہونا ہی ایمان ہے۔",
        "subtitles_hindi": [
            "सच्चे मोमिन की प्यारी पहचान!",
            "हज़रत मुहम्मद ﷺ ने फरमाया:",
            "दूसरों के लिए वही पसंद करो,",
            "जो अपने लिए पसंद करते हो!",
            "(सहीह बुखारी 13)",
        ],
        "subtitles_roman": [
            "Sacche Momin Ki Pehchan!",
            "Hazrat Muhammad ﷺ ne farmaya:",
            "Doosron ke liye wahi pasand karo,",
            "Jo apne liye pasand karte ho!",
            "(Sahih Bukhari 13)",
        ],
    },
    {
        "id": "muslim_2588_gentleness_sabr",
        "title_hindi": "नरमी और सब्र की ताक़त",
        "title_roman": "Power of Gentleness (Narmi Aur Sabr - Muslim 2588)",
        "moral_hindi": "नरमी हर चीज़ को खूबसूरत बना देती है और ग़ुस्सा बिगाड़ देता है।",
        "moral_roman": "Narmi har cheez ko khoobsurat bana deti hai aur gussa bigaad deta hai.",
        "character_theme": "cute 3D Pixar little Muslim girl speaking politely with flowers",
        "shots_prompts": [],
        "spoken_text": "اللہ کے پیارے رسول، حضرت محمد، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: نرمی جس چیز میں بھی ہو، اسے خوبصورت بنا دیتی ہے، اور جس چیز سے نکال دی جائے، اسے عیب دار بنا دیتی ہے۔ ہمیشہ غصے کا جواب نرمی اور مسکراہٹ سے دیجیے۔",
        "subtitles_hindi": [
            "नरमी और सब्र की ताक़त!",
            "हज़रत मुहम्मद ﷺ ने फरमाया:",
            "नरमी हर चीज़ को खूबसूरत बना देती है,",
            "और ग़ुस्सा उसे बिगाड़ देता है!",
            "(सहीह मुस्लिम 2588)",
        ],
        "subtitles_roman": [
            "Narmi Aur Sabr Ki Taaqat!",
            "Hazrat Muhammad ﷺ ne farmaya:",
            "Narmi har cheez ko khoobsurat bana deti hai,",
            "Aur gussa use bigaad deta hai!",
            "(Sahih Muslim 2588)",
        ],
    },
    {
        "id": "tirmidhi_1956_smile_charity",
        "title_hindi": "मुस्कुराना भी सदक़ा है",
        "title_roman": "A Smile is Charity (Muskurana Sadqah Hai - Tirmidhi 1956)",
        "moral_hindi": "किसी को देखकर प्यार से मुस्कुराना भी अल्लाह के नज़दीक सदक़ा है।",
        "moral_roman": "Kisi ko dekh kar pyar se muskurana bhi Allah ke nazdeeq sadqah hai.",
        "character_theme": "cute 3D Pixar little Muslim girl smiling with radiant light",
        "shots_prompts": [],
        "spoken_text": "ہمارے پیارے نبی، حضرت محمد مصطفیٰ، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: اپنے بھائی کے چہرے کو دیکھ کر مسکرانا بھی تمہارے لیے صدقہ ہے۔ کسی اداس دل میں مسکراہٹ لانا اللہ تعالیٰ کو بے حد پسند ہے۔",
        "subtitles_hindi": [
            "मुस्कुराना भी सदक़ा है!",
            "हज़रत मुहम्मद ﷺ ने फरमाया:",
            "अपने भाई को देखकर मुस्कुराना भी,",
            "तुम्हारे लिए एक सदक़ा है!",
            "(जामे तिर्मिज़ी 1956)",
        ],
        "subtitles_roman": [
            "Muskurana Bhi Sadqah Hai!",
            "Hazrat Muhammad ﷺ ne farmaya:",
            "Apne bhai ko dekh kar muskurana bhi,",
            "Tumhare liye ek sadqah hai!",
            "(Jami At-Tirmidhi 1956)",
        ],
    },
    {
        "id": "bukhari_6018_good_words",
        "title_hindi": "अच्छी बात बोलो या ख़ामोश रहो",
        "title_roman": "Speak Good or Remain Silent (Bukhari 6018)",
        "moral_hindi": "ज़ुबान से हमेशा मीठी और सच्ची बात कहनी चाहिए।",
        "moral_roman": "Zuban se hamesha meethi aur sacchi baat kehni chahiye.",
        "character_theme": "cute 3D Pixar little Muslim girl thinking wisely",
        "shots_prompts": [],
        "spoken_text": "ہمارے پیارے نبی، حضرت محمد مصطفیٰ، صَلَّی اللہُ عَلَیْہِ وَسَلَّم، نے فرمایا: جو شخص اللہ اور آخرت کے دن پر ایمان رکھتا ہے، اسے چاہیے کہ اچھی بات کہے یا پھر خاموش رہے۔ میٹھے بول صدقہ ہیں اور دلوں کو جیت لیتے ہیں۔",
        "subtitles_hindi": [
            "अच्छी बात कहो या ख़ामोश रहो!",
            "हज़रत मुहम्मद ﷺ ने फरमाया:",
            "जो अल्लाह पर ईमान रखता है,",
            "वो अच्छी बात कहे या ख़ामोश रहे!",
            "(सहीह बुखारी 6018)",
        ],
        "subtitles_roman": [
            "Achhi Baat Kaho Ya Khamosh Raho!",
            "Hazrat Muhammad ﷺ ne farmaya:",
            "Jo Allah par imaan rakhta hai,",
            "Wo achhi baat kahe ya khamosh rahe!",
            "(Sahih Bukhari 6018)",
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
        "character_theme": story.get("character_theme", "ultra-cute 3D Pixar little Muslim girl with pink hijab"),
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
    print("Character:", data["character_theme"])
    print("Prompts count:", len(data["shots_prompts"]))
