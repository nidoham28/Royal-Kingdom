# ═══════════════════════════════════════════════════════════════
#  DEFINITIONS.RPY — চরিত্র, ইমেজ (Global constants)
# ═══════════════════════════════════════════════════════════════
#  PURPOSE
#    • Characters, images — যেগুলো কখনো বদলায় না।
#    • এখানে define করা সব কিছু সব .rpy ফাইলে ব্যবহারযোগ্য।
#
#  STYLE
#    • Monochrome — কোনো রং নেই, শুধু ধূসর ও সাদা।
#    • সব ডায়ালগ = চরিত্রের মনের কথা (thoughts), spoken নয়।
#    • Name tag দেখাবে — কার ভাবনা স্পষ্ট।
#
#  RULES
#    • শুধু `define` — পরিবর্তনযোগ্য ভেরিয়েবল variables.rpy-তে।
#    • `narrator` কখনো redefine করবে না।
#    • Character variable ছোট (a, t, tn)।
#    • এক variable একবারই define — duplicate করলে error।
#
#  SPRITE WIDTH (গুরুত্বপূর্ণ)
#    • সব sprite-এর source file একই canvas-এ বানানো উচিত।
#      উদাহরণ: 800 × 1200 px, চরিত্র নিচের-মাঝখানে।
#    • তাহলে height=1000 দিলে width স্বয়ংক্রিয়ভাবে মিলবে।
#    • যদি ভিন্ন মাপে বানানো হয় → দুই expression swap করলে
#      width বদলে যাবে (ভাসমান/চিকন দেখাবে)।
# ═══════════════════════════════════════════════════════════════


# ── HELPERS ────────────────────────────────────────────────────
init python:

    # Background-কে স্ক্রিন cover করায় — ছোট/বড় যেকোনো ছবি।
    def bg(path):
        return Transform(path, fit="cover")

    # Sprite-কে নির্দিষ্ট tinggi-তে scale করে।
    # 1920×1080 গেমে height=1000 ideal।
    #
    # ⚠️ সব sprite source একই canvas-এ বানানো থাকলে
    #    width স্বয়ংক্রিয়ভাবে consistent থাকবে।
    def sprite(path, height=1000):
        return Transform(path, ysize=height)


# ── POSITIONS ──────────────────────────────────────────────────
transform pos_left:
    xalign 0.15
    yalign 1.0          # নিচে দাঁড়িয়ে

transform pos_center:
    xalign 0.5
    yalign 1.0

transform pos_right:
    xalign 0.90
    yalign 1.0

# ═══════════════════════════════════════════════════════════════
#  CHARACTERS — THOUGHT ONLY (Monochrome, italic, name visible)
# ═══════════════════════════════════════════════════════════════
# Chapter files-এ শুধু লিখবেন:
#     a "কফি খেতে খেতে সূর্যাস্ত দেখা — মজাটাই আলাদা।"
#
# → স্বয়ংক্রিয়ভাবে italic-এ, monochrome-এ দেখাবে।
# ═══════════════════════════════════════════════════════════════

# ── MAIN CAST ──────────────────────────────────────────────────
define a  = Character("আরমান",   what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define t  = Character("তৃষা",    what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define tn = Character("তানিশা",  what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define sd = Character("সাদিয়া",  what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define rf = Character("রাফি",    what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])


# ── EXTENDED CAST ──────────────────────────────────────────────
define rn = Character("রনো",     what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define nm = Character("নায়েম",   what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define mh = Character("মাহিরা",  what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define tv = Character("তানভীর",  what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define mk = Character("মেহক",    what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define jy = Character("জয়",     what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define ry = Character("রিয়া",    what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define kb = Character("কাবির",   what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define ns = Character("নুসরাত",  what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])


# ── SUB CAST ───────────────────────────────────────────────────
define mo = Character("মা",       what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define fa = Character("বাবা",     what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define dc = Character("ডাক্তার",  what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])
define dr = Character("ড্রাইভার", what_italic=True, what_color="#e8e8e8", who_color="#9a9a9a", who_outlines=[(1, "#00000080", 0, 0)])


# ═══════════════════════════════════════════════════════════════
#  NARRATION
# ═══════════════════════════════════════════════════════════════
# ⚠️ `narrator` Ren'Py-র বিল্ট-ইন — redefine করো না।
#    দৃশ্যের বর্ণনা narrator দিয়ে:
#        "শহরের বাতিগুলো একে একে জ্বলে উঠছে।"
#
#    ইটালিক narration চাইলে inline tag:
#        "{i}এটা ইটালিক narration।{/i}"


# ═══════════════════════════════════════════════════════════════
#  BACKGROUNDS
# ═══════════════════════════════════════════════════════════════
# সব background `bg()` helper দিয়ে — auto fit="cover"।
#
# ব্যবহার:
#     scene bg rooftop sunset with fade
# ═══════════════════════════════════════════════════════════════

# ── Chapter 1 ──────────────────────────────────────────────────
# image bg airport       = bg("images/backgrounds/ch1/bg_airport_day.png")
# image bg home_living   = bg("images/backgrounds/ch1/bg_home_living_day.png")
# image bg cafe          = bg("images/backgrounds/ch1/bg_cafe_day.png")
# image bg rooftop_party = bg("images/backgrounds/ch1/bg_rooftop_party_night.png")
# image bg bedroom_night = bg("images/backgrounds/ch1/bg_bedroom_night.png")

# ── Chapter 1 — Rooftop Sunset (আছে) ───────────────────────────
image bg rooftop sunset = bg("images/backgrounds/ch1/bg_rooftop_sunset.png")
image bg bedroom night = bg("images/backgrounds/ch1/bg_bedroom_night.jpg")

# ── Common (সব চ্যাপ্টারে) ──────────────────────────────────────
# image bg street_night  = bg("images/backgrounds/common/bg_street_night.png")
image bg black         = Solid("#000000")
image bg white         = Solid("#ffffff")


# ═══════════════════════════════════════════════════════════════
#  CHARACTER SPRITES
# ═══════════════════════════════════════════════════════════════
# নাম convention: <character> <expression>
#
# ⚠️ সব sprite source একই canvas-এ বানান — যেমন 800 × 1200 px,
#    চরিত্র নিচের-মাঝখানে। না হলে swap-এ width বদলে যাবে।
#
# ব্যবহার:
#     show arman neutral at pos_right with dissolve
#     show arman smiling      # ← width একই থাকবে
# ═══════════════════════════════════════════════════════════════

# ── আরমান ──────────────────────────────────────────────────────
image arman neutral = sprite("images/characters/arman/arman_neutral.png", 1000)
image arman smiling = sprite("images/characters/arman/arman_smiling.png", 1000)
# image arman surprised = sprite("images/characters/arman/arman_surprised.png", 1000)
# image arman angry     = sprite("images/characters/arman/arman_angry.png", 1000)
# image arman sad       = sprite("images/characters/arman/arman_sad.png", 1000)
# image arman thinking  = sprite("images/characters/arman/arman_thinking.png", 1000)

# ── তৃষা ───────────────────────────────────────────────────────
# image trisha neutral  = sprite("images/characters/trisha/trisha_neutral.png", 1000)
# image trisha smiling  = sprite("images/characters/trisha/trisha_smiling.png", 1000)
# image trisha crying   = sprite("images/characters/trisha/trisha_crying.png", 1000)
# image trisha shy      = sprite("images/characters/trisha/trisha_shy.png", 1000)
# image trisha serious  = sprite("images/characters/trisha/trisha_serious.png", 1000)
# image trisha sad      = sprite("images/characters/trisha/trisha_sad.png", 1000)

# ── রিয়া ──────────────────────────────────────────────────────
# image riya happy      = sprite("images/characters/riya/riya_happy.png", 1000)
# image riya excited    = sprite("images/characters/riya/riya_excited.png", 1000)

# ── রনো ────────────────────────────────────────────────────────
# image rono neutral    = sprite("images/characters/rono/rono_neutral.png", 1000)
# image rono smirk      = sprite("images/characters/rono/rono_smirk.png", 1000)
# image rono angry      = sprite("images/characters/rono/rono_angry.png", 1000)

# ── জয় ────────────────────────────────────────────────────────
# image joy laughing    = sprite("images/characters/joy/joy_laughing.png", 1000)


# ⚠️ বাকি চরিত্রের ছবি বানানোর পর এই ফরম্যাটে যোগ করো:
#     image [নাম] [expression] = sprite("images/characters/[নাম]/[file].png", 1000)