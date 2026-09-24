# ═══════════════════════════════════════════════════════════════
#  CHAPTER 1 — অধ্যায় ১
# ═══════════════════════════════════════════════════════════════
#  LABEL NAMING RULE
#      ch{chapter}_s{scene}_{location}
#      e.g. ch1_s1_rooftop, ch1_s2_hotel, ch1_s3_cafe
#
#  FILE RULES
#    • শুধু Chapter 1-এর label এই ফাইলে।
#    • প্রথম label:  ch1_s1_<location>
#    • শেষ label:    jump ch2_s1_<location>
#    • Label নাম globally unique হবে।
#    • "#" কমেন্টের ভেতরে কখনো "label" লিখবেন না।
#
#  DIALOGUE STYLE
#    • Spoken dialogue নেই — সব চরিত্রের মনের কথা।
#    • character variable (a, t, ...) নিজেই thought → italic দেখাবে।
#    • দৃশ্যের বর্ণনা narrator (নাম ছাড়া "..." ) দিয়ে।
#
#  SPRITE TIPS
#    • Position একবার দিলে পরের show-এ reset হয় না।
#      → শুধু expression বদলাতে: show arman smiling
#      → position বদলাতে হলে আবার at pos_right লিখুন
#    • hide + show একসাথে না করে শুধু show করলেই swap হয়।
# ═══════════════════════════════════════════════════════════════


# ── SCENE 1: ROOFTOP SUNSET ────────────────────────────────────
# আরমান ছাদে দাঁড়িয়ে কফি হাতে সূর্যাস্ত দেখছে।
label ch1_s1_rooftop:
    scene bg rooftop sunset with fade
    # play music "audio/music/mus_ch1_rooftop.ogg" fadein 2.0

    show arman neutral at pos_right with dissolve

    # ── চরিত্রের মনের কথা ───────────────────────────────────────
    a "চা-কফি হাতে নিয়ে এই ভিউটা দেখলে সময় থেমে যায়।"
    a "মনে হয় শহরটা নিজেই একটা গল্প বলছে।"

    # ── দৃশ্যের বর্ণনা (narrator) ───────────────────────────────
    "শহরের বাতিগুলো একে একে জ্বলে উঠছে।"
    "দূরে একটা বিমান আকাশে মিলিয়ে যাচ্ছে।"

    # ── হাসিমুখ (position আগের মতোই থাকবে) ─────────────────────
    show arman smiling with dissolve

    a "কফি খেতে খেতে সূর্যাস্ত দেখা — মজাটাই আলাদা।"
    a "একা হলে তেমন লাগত না, কিন্তু আজ ভালো লাগছে।"

    # ── আবার নিরপেক্ষ ───────────────────────────────────────────
    show arman neutral with dissolve

    a "কাল আবার অফিস।"
    a "কিন্তু এখন সেই কথা ভাববো না।"

    "সূর্য পুরোপুরি ডুবে গেছে।"
    "আকাশটা এখন গাঢ় নীল।"

    hide arman with dissolve

    jump ch1_s2_bedroom

label ch1_s2_bedroom:
    scene bg bedroom night with fade

    a "Thrisa তুমি কি ঘুমিয়ে পড়েছ?"

    hide arman with dissolve
    jump ch1_s3_rooftop

label ch1_s3_rooftop:
    scene bg bedroom night with fade

    a "Thrisa ঘুমিয়ে পড়েছ?"