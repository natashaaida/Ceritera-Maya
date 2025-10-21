# ===========================================
# K-POP DEMON HUNTER: Rumi & Jinu — FINAL v9
# Serasi Ren’Py 8.4.x+
# ===========================================

define config.developer = False

# -------- CHARACTERS --------
define r = Character("Rumi", who_color="#E4C6FF", what_color="#FFFFFF")
define j = Character("Jinu", who_color="#C6E4FF", what_color="#FFFFFF")
define n = Character(None)

# -------- IMAGES --------
image bg classroom = "bg_classroom.jpg"
image bg school    = "bg_school.jpg"
image bg victory   = "bg_victory.jpg"
image bg enemy     = "bg_enemy.jpg"

image rumi normal  = "rumi_normal.png"
image rumi happy   = "rumi_happy.png"
image jinu normal  = "jinu_normal.png"
image jinu happy   = "jinu_happy.png"
image jinu angry   = "jinu_angry.png"

# -------- SAY SCREEN (DIALOG BOX) --------
screen say(who, what):
    frame:
        at breathe_glow
        background Solid("#3a1066D0")
        xalign 0.5
        yalign 0.78          # kedudukan kotak (tidak ganggu kuiz)
        xsize 0.92
        ypadding 42
        xpadding 48
        yminimum 270
        xfill True

        vbox:
            spacing 8         # jarak kecil supaya teks naik sedikit
            if who is not None:
                frame:
                    at breathe_glow_fast
                    background Solid("#6b1fd6EE")
                    xfill True
                    yminimum 50
                    xpadding 18
                    ypadding 6
                    text who style "say_label_text" xalign 0.0
            text what id "what" style "say_dialogue_text" xalign 0.0

style say_label_text is default:
    color "#FFFFFF"
    size 30
    bold True

# TEKS DIALOG: buang layout "subtitle" & gunakan yoffset untuk naikkan teks
style say_dialogue_text is default:
    color "#FFFFFF"
    size 26
    line_spacing 5
    yoffset -16
    outlines [(1, "#00000090", 0, 0)]

# -------- QUIZ BUTTON STYLES --------
style quiz_button is default:
    background Solid("#2a0b4fE6")
    padding (10, 12)
    xfill True
    yminimum 68
    outlines [ (3, "#7c3aed66", 0, 0) ]
    hover_outlines [ (5, "#c084fcAA", 0, 0) ]
    top_margin 5
    bottom_margin 5

style quiz_button_text is default:
    color "#FFFFFF"
    size 25
    xalign 0.0

# -------- TRANSFORMS (ANIMATION) --------
transform breathe_glow:
    linear 1.4 alpha 1.0
    linear 1.4 alpha 0.92
    repeat

transform breathe_glow_fast:
    linear 0.9 alpha 1.0
    linear 0.9 alpha 0.85
    repeat

transform char_breathe:
    linear 1.5 zoom 1.02 alpha 0.98
    linear 1.5 zoom 1.00 alpha 1.0
    repeat

transform char_breathe_fast:
    linear 0.8 zoom 1.03 alpha 0.95
    linear 0.8 zoom 1.00 alpha 1.0
    repeat

transform pulse:
    linear 0.8 alpha 0.9
    linear 0.8 alpha 1.0
    repeat

transform place_left:
    xalign 0.3
    yalign 1.0

transform place_right:
    xalign 0.7
    yalign 1.0

# -------- HUD --------
default friendship = 0
default lives = 5

image star_full  = "star_full.png"
image star_empty = "star_empty.png"

screen hud():
    # Bintang Poin
    frame:
        background None
        xalign 0.02
        yalign 0.02
        hbox:
            spacing 6
            for i in range(10):
                if i < friendship:
                    add "star_full" at breathe_glow_fast zoom 1.2
                else:
                    add "star_empty" zoom 1.2
    # Nyawa & Poin (BOLD)
    frame:
        background None
        xalign 0.98
        yalign 0.02
        vbox:
            spacing 2
            text "{b}Nyawa:{/b} [lives]/5" size 24 color "#FFFFFF"
            text "{b}Poin:{/b} [friendship]/10" size 22 color "#E4C6FF"

# -------- QUICK MENU (BOLD) --------
style quick_button_text is default:
    color "#FFFFFF"
    bold True
    size 22

# -------- HELPER (hanya watak bercakap muncul) --------
init python:
    def show_rumi(expr="normal"):
        renpy.hide("jinu")
        renpy.show("rumi " + expr, at_list=[char_breathe, place_left], zorder=10)
    def show_jinu(expr="normal"):
        renpy.hide("rumi")
        renpy.show("jinu " + expr, at_list=[char_breathe, place_right], zorder=10)

# -------- SOALAN (10 soalan) --------
init python:
    import random
    noun_questions = [
        {"q": "Simpulan bahasa ialah:", "choices": ["Cerita rakyat", "Peribahasa ringkas", "Kata kiasan", "Ungkapan nasihat"], "ans": 1, "type": "noun"},
        {"q": "Apakah contoh simpulan bahasa?", "choices": ["Hiruk-pikuk", "Ringan tulang", "Sebilah", "Matahari"], "ans": 1, "type": "noun"},
        {"q": "Apakah simpulan bahasa bagi seseorang yang tidak pandai bermain bola?", "choices": ["Berat mulut", "Panjang tangan", "Kaki bangku", "Buruk siku"], "ans": 2, "type": "noun"},
        {"q": "Apakah yang dimaksudkan dengan kuat semangat?", "choices": ["Tetap berusaha", "Suka bergantung", "Takut mencuba", "Refleksi diri"], "ans": 0, "type": "noun"},
        {"q": "Apakah simpulan bahasa bagi seseorang yang tidak menjaga perasaan orang lain?", "choices": ["Mulut celupar", "Pandang rendah", "Bocor rahsia", "Banyak cakap"], "ans": 0, "type": "noun"},
    ]
    verb_questions = [
        {"q": "Apakah yang dimaksudkan dengan tajam akal?", "choices": ["Cepat faham", "Susah faham", "Lambat faham", "Cepat lupa"], "ans": 0, "type": "verb"},
        {"q": "Otak udang bermaksud...", "choices": ["Cepat lupa", "Tidak bijak", "Cepat faham", "Rajin"], "ans": 1, "type": "verb"},
        {"q": "Apakah simpulan bahasa untuk orang yang tidak suka bergaul?", "choices": ["Kera sumbang", "Kaki bangku", "Mulut murai", "Berat tulang"], "ans": 0, "type": "verb"},
        {"q": "Simpulan bahasa apa yang paling sesuai untuk sikap Rumi dalam cerita ini?", "choices": ["Ringan tulang", "Kera sumbang", "Lepas tangan", "Panjang akal"], "ans": 0, "type": "verb"},
        {"q": "Apakah simpulan bahasa yang boleh digunakan untuk menggambarkan sikap negatif seseorang?", "choices": ["Baik hati", "Jatuh hati", "Sampai hati", "Busuk hati"], "ans": 3, "type": "verb"},
    ]
    def build_quiz():
        qs = noun_questions + verb_questions
        random.shuffle(qs)
        return qs[:10]
    quiz_list = []

# -------- SCREEN QUIZ (4 pilihan sentiasa muat) --------
screen quiz(qdata):
    modal True
    default shuffled = list(enumerate(qdata["choices"]))
    $ renpy.random.shuffle(shuffled)

    frame:
        at breathe_glow
        background Solid("#1c0833CC")
        xalign 0.5
        yalign 0.37          # cukup tinggi jauh dari quick menu
        xsize 0.92
        yminimum 520
        ypadding 20
        top_margin 8
        bottom_margin 220

        vbox:
            spacing 12
            xfill True
            text qdata["q"] size 30 color "#FFFFFF"
            for idx, choice in shuffled:
                button:
                    at pulse
                    style "quiz_button"
                    action Return(idx)
                    has hbox
                    xfill True
                    text choice style "quiz_button_text"

# -------- CERITA --------
label start:
    $ friendship = 0
    $ lives = 5
    $ quiz_list = build_quiz()
    show screen hud
    play music "bgm.ogg" fadein 1.0 loop
    scene bg classroom

    $ show_rumi("normal")
    r "Hari yang biasa di sekolah... Tiba-tiba, Rumi yang sedang membaca buku di dalam kelas terkejut apabila suasana kelas bertukar menjadi {i}suram dan menakutkan!{/i} "

    $ show_jinu("normal")
    j "Hai... awak Rumi, kan? Nama saya Jinu. Saya memerlukan pertolongan awak untuk kalahkan {b}raksasa tatabahasa{/b}."
    $ show_rumi("normal")
    r "Raksasa tatabahasa? Bunyinya menakutkan..."

    n "Bantu Jinu?"

    menu:
        "Baiklah, mari saya bantu!":
            $ friendship += 1
            $ show_jinu("happy")
            j "Terima kasih! Mari kita kalahkan raksasa tatabahasa bersama-sama."
        "Maafkan saya, saya tidak boleh bantu.":
            $ friendship = max(0, friendship - 1)
            $ show_jinu("angry")
            with hpunch
            play sound "wrong_sfx.ogg"
            j "Oh... begitu rupanya. Betul awak tidak mahu membantu saya?"
            $ show_rumi("normal")
            r "Maafkan saya, mari saya bantu awak."

    scene bg school with fade
    n "Untuk menang, kumpulkan {b}10 poin persahabatan{/b}. Hati-hati — {b}5 kesilapan{/b} akan mengakibatkan kekalahan!"

    call play_quiz from _call_play_quiz

    if friendship >= 10:
        jump victory_end
    else:
        jump bad_end

# -------- LOGIK QUIZ --------
label play_quiz:
    python:
        for q in quiz_list:
            show_jinu("normal")
            renpy.say(j, "Mari teruskan! ({})".format("Kalahkan Raksasa Tatabahasa!" if q["type"]=="noun" else "Raksasa Tatabahasa mengganggu Simpulan Bahasa!"))
            choice_index = renpy.call_screen("quiz", q)

            if choice_index == q["ans"]:
                friendship += 1
                renpy.play("correct_sfx.ogg")
                show_jinu("happy")
                renpy.say(j, "Betul! Poin persahabatan telah bertambah.")
            else:
                lives -= 1
                renpy.play("wrong_sfx.ogg")
                show_jinu("angry")
                renpy.with_statement(hpunch)
                renpy.say(j, "Salah! Nyawa awak semakin berkurang.")
                if lives <= 0:
                    break

            show_rumi("happy" if choice_index == q["ans"] else "normal")
            if choice_index == q["ans"]:
                renpy.say(r, "Bagus! Teruskan usaha awak.")
            else:
                renpy.say(r, "Tidak mengapa, awak boleh cuba lagi!")
    return

# -------- ENDINGS --------
label victory_end:
    stop music fadeout 1.0
    scene bg victory with dissolve
    play music "victory.ogg"
    show rumi happy at place_left, char_breathe
    show jinu happy at place_right, char_breathe
    r "Kita Menang! Raksasa tatabahasa telah berjaya ditewaskan!"
    j "Rumi, awak sangat hebat! Awak dan saya kini sahabat karib~!"
    n "Tahniah! Anda telah mengumpul kesemua poin persahabatan dan menewaskan raksasa tatabahasa. Sila tekan skrin untuk bermain lagi."
    hide screen hud
    return

label bad_end:
    stop music fadeout 0.8
    scene bg enemy with fade
    play music "enemy.ogg" loop
    show rumi normal at place_left, char_breathe_fast
    show jinu angry  at place_right, char_breathe_fast
    with hpunch
    j "Kita gagal... Raksasa tatabahasa masih bebas!"
    r "Tidak mengapa, kita akan cuba lagi untuk menang."
    n "Anda telah gagal membantu Jinu dan raksasa tatabahasa masih mengganggu Simpulan bahasa. Sila tekan skrin untuk cuba lagi menewaskan raksasa tatabahasa!"
    hide screen hud
    return
