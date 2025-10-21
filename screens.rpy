﻿################################################################################
## Pengawalan
################################################################################

init offset = -1


################################################################################
## Gaya
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Skrin dalam permainan
################################################################################


## Skrin sebutan ###############################################################
##
## Skrin sebutan digunakan untuk memaparkan dialog kepada pemain. Ia mengambil
## dua parameter, who ialah nama watak yang bercakap, dan what ialah tulisan
## untuk dipaparkan. (Parameter who boleh ditetapkan kepada None jika tiada nama
## diberikan.)
##
## Skrin ini mesti mencipta tulisan yang boleh dipaparkan dengan id "what",
## kerana Ren'Py menggunakan ini untuk mengurus paparan tulisan. Ia juga boleh
## mencipta paparan dengan id "who" dan id "window" untuk menggunakan sifat gaya.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Jika ada imej sampingan, paparkan ia di atas tulisan. Jangan paparkan ia
    ## pada varian telefon - ia tidak cukup ruang.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Buatkan kotak nama boleh digayakan melalui objek watak (Character).
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Skrin input #################################################################
##
## Skrin ini digunakan untuk memaparkan renpy.input. Parameter prompt digunakan
## untuk memberikan prom tulisan.
##
## Skrin ini mesti mencipta input yang boleh dipaparkan dengan id "input" untuk
## menerima pelbagai parameter input.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Skrin pilihan ###############################################################
##
## Skrin ini digunakan untuk memaparkan pilihan dalam permainan yang
## dipersembahkan melalui kenyataan menu. Satu-satunya parameter, items, ialah
## senarai objek, setiap satunya dengan medan keterangan dan medan perbuatan.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Skrin Menu Cepat ############################################################
##
## Menu cepat dipaparkan dalam permainan untuk menyediakan capaian mudah ke
## menu luar permainan.

screen quick_menu():

    ## Pastikan ini muncuk di atas skrin-skrin lain.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Kembali") action Rollback()
            textbutton _("Sejarah") action ShowMenu('history')
            textbutton _("Langkau") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Simpan") action ShowMenu('save')
            textbutton _("C.Simpan") action QuickSave()
            textbutton _("C.Muat") action QuickLoad()
            textbutton _("Keutamaan") action ShowMenu('preferences')


## Kod ini memastikan skrin quick_menu dipaparkan dalam permainan, apabila
## pemain tidak menyembunyikan antara muka secara khusus.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Skrin Menu Utama dan Permainan
################################################################################

## Skrin Navigasi ##############################################################
##
## Skrin ini disertakan dalam menu utama dan permainan, dan menyediakan
## navigasi ke menu lain, dan untuk memulakan permainan.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Mula") action Start()

        else:

            textbutton _("Sejarah") action ShowMenu("history")

            textbutton _("Simpan") action ShowMenu("save")

        textbutton _("Muat") action ShowMenu("load")

        textbutton _("Keutamaan") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Tamatkan Ulang Tayang") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu Utama") action MainMenu()

        textbutton _("Perihal") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Bantuan tidak diperlukan atau sesuai untuk peranti mudah alih.
            textbutton _("Bantuan") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Keluar") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Skrin Menu Utama ############################################################
##
## Digunakan untuk memaparkan menu utama apabila Ren'Py dimulakan.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Ini memastikan sebarang skrin menu lain digantikan.
    tag menu

    add gui.main_menu_background

    ## Bingkai kosong ini menggelapkan menu utama.
    frame:
        style "main_menu_frame"

    ## Kenyataan use memasukkan skrin lain ke dalam skrin ini. Kandungan
    ## sebenar menu utama ada dalam skrin navigasi.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Skrin Menu Permainan ########################################################
##
## Ini meletakkan struktur biasa asas untuk skrin menu permainan. Ia dipanggil
## dengan tajuk skrin, dan memaparkan latar belakang, tajuk, dan navigasi.
##
## Parameter tatal boleh jadi None, atau salah satu dari "viewport" atau
## "vpgrid". Skrin ini bertujuan untuk digunakan dengan satu atau lebih anak,
## yang mana mereka ditransklusikan (diletakkan) ke dalamnya.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Menyimpan ruang untuk bahagian navigasi.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Kembali"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Skrin perihal ###############################################################
##
## Skrin ini memberi penghargaan dan maklumat hak cipta berkaitan permainan dan
## Ren'Py.
##
## Tiada apa istimewa dengan skrin ini, dan sebab itu ia dikekalkan sebagai
## contoh cara membuat skrin sendiri.

screen about():

    tag menu

    ## Kenyataan use ini memasukkan skrin game_menu ke dalam skrin ini. Anak
    ## vbox kemudiannya dimasukkan ke dalam port pandang dalam skrin game_menu.
    use game_menu(_("Perihal"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versi [config.version!t]\n")

            ## gui.about selalunya ditetapkan di options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Dibuat menggunakan {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Muat dan Simpan skrin #######################################################
##
## Skrin-skrin ini bertanggungjawab untuk membolehkan pemain menyimpan dan
## memuatkan permainan. Memandangkan mereka berkongsi hampir semua benda, kedua-
## duanya dilaksanakan dengan cara skrin ketiga, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Simpan"))


screen load():

    tag menu

    use file_slots(_("Muat"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Simpan automatik"), quick=_("Simpan cepat"))

    use game_menu(title):

        fixed:

            ## Ini memastikan input mendapat acara masuk sebelum sebarang
            ## butang lain.
            order_reverse True

            ## Nama halaman, yang boleh disunting dengan menekan butang.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Grid slot fail.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("slot kosong")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Butang untuk mencapai halaman lain.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) memberikan nombor dari 1 hingga 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Skrin keutamaan #############################################################
##
## Skrin keutamaan membolehkan pemain untuk menatarajah permainan agar lebih
## selesa dengan diri mereka.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Keutamaan"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Paparan")
                        textbutton _("Tetingkap") action Preference("display", "window")
                        textbutton _("Skrin Penuh") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Langkau")
                    textbutton _("Teks Belum Lihat") action Preference("skip", "toggle")
                    textbutton _("Lepas Pilihan") action Preference("after choices", "toggle")
                    textbutton _("Lepas Peralihan") action InvertSelected(Preference("transitions", "toggle"))

                ## Vbox tambahan jenis "radio_pref" atau "check_pref" boleh
                ## ditambah di sini, untuk menambah keutamaan ditakrifkan oleh
                ## pencipta permainan.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Kelajuan Tulisan")

                    bar value Preference("text speed")

                    label _("Masa untuk Gerak Sendiri")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Kekuatan Muzik")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Kekuatan Bunyi")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Cuba") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Kekuatan Suara")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Cuba") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Bisukan SEMUA"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Skrin Sejarah ###############################################################
##
## Ini skrin yang memaparkan sejarah dialog kepada pemain. Walaupun tiada apa
## yang istimewa dengan skrin ini, ia mempunyai capaian ke sejarah dialog dalam
## _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Mengelakkan ramalan skrin ini, kerana ia boleh jadi sangat besar.
    predict False

    use game_menu(_("Sejarah"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Ini meletakkan semua benda dengan elok jika history_height
                ## ditetapkan ke None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Mengambil warna tulisan 'who' dari objek watak
                        ## (Character), jika ia ditetapkan.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Sejarah dialog kosong.")


## Ini menentukan tag apa yang dibenarkan untuk dipaparkan di skrin sejarah.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Skrin Bantuan ###############################################################
##
## Skrin yang memberikan maklumat berkaitan pengikatan kekunci dan tetikus. Ia
## menggunakan skrin lain (keyboard_help, mouse_help, dan gamepad_help) untuk
## memaparkan bantuan sebenar.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Bantuan"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Papan Kekunci") action SetScreenVariable("device", "keyboard")
                textbutton _("Tetikus") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Pad Permainan") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Menggerakkan dialog dan mengaktifkan antara muka.")

    hbox:
        label _("Space")
        text _("Menggerakkan dialog tanpa memilih pilihan.")

    hbox:
        label _("Kekunci Anak Panah")
        text _("Melayar antara muka.")

    hbox:
        label _("Escape")
        text _("Mencapai menu permainan.")

    hbox:
        label _("Ctrl")
        text _("Langkau dialog apabila ditekan.")

    hbox:
        label _("Tab")
        text _("Menogol langkauan dialog.")

    hbox:
        label _("Page Up")
        text _("Bergerak ke dialog sebelumnya.")

    hbox:
        label _("Page Down")
        text _("Bergerak ke dialog seterusnya.")

    hbox:
        label "H"
        text _("Menyembunyikan antara muka pengguna.")

    hbox:
        label "S"
        text _("Mengambil tangkap skrin.")

    hbox:
        label "V"
        text _("Menogol {a=https://www.renpy.org/l/voicing}penyuaraan sendiri{/a} yang membantu.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Klik Kiri")
        text _("Menggerakkan dialog dan mengaktifkan antara muka.")

    hbox:
        label _("Klik Tengah")
        text _("Menyembunyikan antara muka pengguna.")

    hbox:
        label _("Klik Kanan")
        text _("Mencapai menu permainan.")

    hbox:
        label _("Tatal Ke Atas")
        text _("Bergerak ke dialog sebelumnya.")

    hbox:
        label _("Tatal Ke Bawah")
        text _("Bergerak ke dialog seterusnya.")


screen gamepad_help():

    hbox:
        label _("Picu Kanan\nA/Butang Bawah")
        text _("Menggerakkan dialog dan mengaktifkan antara muka.")

    hbox:
        label _("Picu Kiri\nBahu Kiri (L1)")
        text _("Bergerak ke dialog sebelumnya.")

    hbox:
        label _("Bahu Kanan (R1)")
        text _("Bergerak ke dialog seterusnya.")

    hbox:
        label _("D-Pad (Butang Arah), Kayu Bedik")
        text _("Melayar antara muka.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Mencapai menu permainan.")

    hbox:
        label _("Y/Butang Atas")
        text _("Menyembunyikan antara muka pengguna.")

    textbutton _("Tentuukur") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Skrin tambahan
################################################################################


## Skrin pengesahan ############################################################
##
## Skrin pengesahan dipanggil apabila Ren'Py ingin bertanya pemain soalan ya
## atau tidak.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Memastikan skrin-skrin lain tidak mendapat input apabila skrin ini
    ## dipaparkan.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Ya") action yes_action
                textbutton _("Tidak") action no_action

    ## Klik-kanan dan keluar menjawab "tidak".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skrin Penunjuk Langkau ######################################################
##
## Skrin skip_indicator dipaparkan untuk menandakan pelangkauan sedang
## dilakukan.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Melangkau")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Peralihan ini digunakan untuk mengerdipkan anak panah satu selepas satu.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Kami perlu menggunakan fon yang mempunyai glif bernama BLACK RIGHT-
    ## POINTING SMALL TRIANGLE (segi tiga kecil hitam menunjuk ke kanan) di
    ## dalamnya.
    font "DejaVuSans.ttf"


## Skrin Pemberitahuan #########################################################
##
## Skrin pemberitahuan digunakan untuk menunjukkan mesej kepada pemain.
## (Contohnya, apabila permainan disimpan cepat atau tangkap skrin telah
## diambil.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Skrin NVL ###################################################################
##
## Skrin ini digunakan untuk dialog dan menu mod NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Memaparkan dialog sama ada dalam vpgrid atau vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly
        ## if config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ini mengawal jumlah maksimum entri mod NVL yang boleh dipaparkan dalam
## sesuatu masa.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using
## speech bubbles. The bubble screen takes the same parameters as the say
## screen, must create a displayable with the id of "what", and can create
## displayables with the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Varian Mudah Alih
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Memandangkan tetikus tidak semestinya ada, kami menggantikan menu cepat
## dengan versi yang menggunakan sedikit butang dan butang lebih besar agar
## lebih mudah disentuh.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Kembali") action Rollback()
            textbutton _("Langkau") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
