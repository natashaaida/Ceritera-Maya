################################################################################
## Pengawalan
################################################################################

## Kenyataan init offset dalam fail ini menyebabkan kenyataan dalam fail ini
## dijalankan sebelum sebarang kenyataan init dalam fail lain.
init offset = -2

## Memanggil gui.init menetapkan semula gaya ke nilai lalai yang wajar, dan
## menetapkan lebar dan tinggi permainan.
init python:
    gui.init(1920, 1080)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## Pemboleh Ubah Tatarajah GUI
################################################################################


## Warna #######################################################################
##
## Warna tulisan dalam antara muka.

## Warna aksen yang digunakan di seluruh antara muka untuk melabel dan menanda
## tulisan.
define gui.accent_color = '#0099cc'

## Warna yang digunakan untuk butang tulisan apabila ia tidak dipilih mahupun
## dilalukan tetikus.
define gui.idle_color = '#888888'

## Warna kecil itu digunakan untuk tulisan kecil, ia mestilah lebih terang/
## gelap untuk mencapai kesan yang sama.
define gui.idle_small_color = '#aaaaaa'

## Warna yang digunakan untuk butang dan bar yang dilalukan tetikus.
define gui.hover_color = '#66c1e0'

## Warna yang digunakan untuk butang tulisan apabila ianya dipilih tetapi tidak
## difokuskan. Butang dipilih sekiranya ia skrin semasa atau nilai diutamakan.
define gui.selected_color = '#ffffff'

## Warna yang digunakan untuk butang tulisan apabila ia tidak boleh dipilih.
define gui.insensitive_color = '#8888887f'

## Warna digunakan untuk bahagian bar yang belum diisi. Warna ini tidak
## digunakan secara terus, tetapi digunakan ketika menjana semula fail imej bar.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## Warna yang digunakan untuk tulisan dialog dan pilihan menu.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fon dan Saiz Fon ############################################################

## Fon yang digunakan untuk tulisan di dalam permainan.
define gui.text_font = "DejaVuSans.ttf"

## Fon yang digunakan untuk nama-nama watak.
define gui.name_text_font = "DejaVuSans.ttf"

## Fon yang digunakan untuk tulisan di luar permainan.
define gui.interface_text_font = "DejaVuSans.ttf"

## Saiz untuk tulisan dialog biasa.
define gui.text_size = 33

## Saiz untuk nama-nama watak.
define gui.name_text_size = 45

## Saiz tulisan dalam antara muka pengguna permainan.
define gui.interface_text_size = 33

## Saiz label dalam antara muka pengguna permainan.
define gui.label_text_size = 36

## Saiz tulisan pada skrin pemberitahuan.
define gui.notify_text_size = 24

## Saiz tulisan tajuk permainan.
define gui.title_text_size = 75


## Menu Utama dan Permainan ####################################################

## Imej yang digunakan untuk menu utama dan permainan.
define gui.main_menu_background = "gui/menu_bg.jpg"
define gui.game_menu_background = "gui/menu_bg.jpg"


## Dialog ######################################################################
##
## Pemboleh ubah ini mengawal bagaimana dialog dipaparkan di atas skrin sebaris
## pada sesuatu masa.

## Tinggi kotak tulisan yang mengandungi dialog.
define gui.textbox_height = 278

## Peletakan menegak kotak tulisan di atas skrin. 0.0 di atas, 0.5 di tengah,
## dan 1.0 di bawah.
define gui.textbox_yalign = 1.0


## Peletakan nama watak yang sedang bercakap, relatif kepada kotak tulisan.
## Nilai boleh jadi nombor bulat piksel dari kiri atau atas, atau 0.5 untuk di
## tengah.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Penjajaran melintang nama watak. Ini boleh jadi 0.0 untuk penjajaran kiri,
## 0.5 untuk penjajaran tengah, dan 1.0 untuk penjajaran kanan.
define gui.name_xalign = 0.0

## Lebar, tinggi, dan sempadan kotak yang mengandungi nama watak, atau None
## untuk menentukan saiz secara automatik.
define gui.namebox_width = None
define gui.namebox_height = None

## Sempadan kotak yang mengandungi nama watak, mengikut susunan kiri, atas,
## kanan, bawah.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Jika ditetapkan kepada True, latar belakang kotak nama akan dijubinkan, jika
## False, latar belakang kotak nama akan dissesuaikan saiznya.
define gui.namebox_tile = False


## Peletakan dialog relatif kepada kotak tulisan. Nilai boleh jadi nombor bulat
## piksel dari kiri atau atas dari kotak tulisan, atau 0.5 untuk di tengah.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 20

## Lebar maksimum tulisan dialog, dalam piksel.
define gui.dialogue_width = 1116

## Penjajaran melintang tulisan dialog. Ini boleh jadi 0.0 untuk penjajaran
## kiri, 0.5 untuk penjajaran tengah, dan 1.0 untuk penjajaran kanan.
define gui.dialogue_text_xalign = 0.0


## Butang ######################################################################
##
## Pemboleh ubah ini, beserta fail imej dalam gui/button, mengawal aspek mana
## butang akan dipaparkan.

## Lebar dan tinggi butang, dalam piksel. Jika ditetapkan kepada None, Ren'Py
## akan mengira saiz sendiri.
define gui.button_width = None
define gui.button_height = None

## Sempadan di setiap sisi butang, dalam susunan kiri, atas, kanan, bawah.
define gui.button_borders = Borders(6, 6, 6, 6)

## Jika ditetapkan kepada True, latar belakang imej akan dijubinkan. Jika
## False, latar belakang imej akan disesuaikan saiznya secara linear.
define gui.button_tile = False

## Fon yang digunakan pada butang.
define gui.button_text_font = gui.interface_text_font

## Saiz untuk tulisan yang digunakan pada butang.
define gui.button_text_size = gui.interface_text_size

## Warna tulisan butang dalam pelbagai keadaan.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Penjajaran melintang tulisan butang. (0.0 untuk kiri, 0.5 untuk tengah, 1.0
## untuk kanan).
define gui.button_text_xalign = 0.0


## Pemboleh ubah ini mengatasi tetapan untuk pelbagai jenis butang. Sila lihat
## pendokumenan gui untuk pelbagai jenis butang yang ada, dan apa fungsi setiap
## satunya.
##
## Pengubahsuaian ini digunakan di antara muka lalai:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Anda juga boleh menambah ubah suai anda sendiri, dengan menambah pemboleh
## ubah yang dinamakan dengan betul. Contohnya, anda boleh nyahkomen baris di
## bawah untuk menetapkan lebar butang navigasi.

# define gui.navigation_button_width = 250


## Butang Pilihan ##############################################################
##
## Butang pilihan digunakan pada menu dalam permainan.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Butang Slot Fail ############################################################
##
## Butang slot fail ialah butang jenis istimewa. Ia mengandungi imej kecil,
## dan tulisan yang menerangkan kandungan slot simpanan. Sebuah slot simpanan
## menggunakan fail imej dalam gui/button, seperti butang-butang jenis lain.

## Butang slot simpan.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Lebar dan tinggi imej kecil yang digunakan di slot simpan.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Jumlah lajur dan baris dalam grid slot simpan.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Peletakan dan Penjarakan ####################################################
##
## Pemboleh ubah ini mengawal peletakan dan penjarakan pelbagai unsur antara
## muka pengguna.

## Kedudukan sisi kiri butang navigasi, relatif kepada sisi kiri skrin.
define gui.navigation_xpos = 60

## Kedudukan menegak penunjuk langkau.
define gui.skip_ypos = 15

## Kedudukan menegak skrin pemberitahuan.
define gui.notify_ypos = 68

## Penjarakan di antara pelbagai pilihan menu.
define gui.choice_spacing = 33

## Butang dalam bahagian navigasi di menu utama dan permainan.
define gui.navigation_spacing = 6

## Mengawal jumlah jarak di antara keutamaan.
define gui.pref_spacing = 15

## Mengawal jumlah jarak di antara butang keutamaan.
define gui.pref_button_spacing = 0

## Jarak di antara butang halaman fail.
define gui.page_spacing = 0

## Jarak di antara slot fail.
define gui.slot_spacing = 15

## Kedudukan tulisan menu utama.
define gui.main_menu_text_xalign = 1.0


## Bingkai #####################################################################
##
## Pemboleh ubah ini mengawal rupa bingkai yang boleh mengandungi komponen
## antara muka apabila tindihan atas atau tetingkap tidak wujud.

## Bingkai umum.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Bingkai yang digunakan sebagai sebahagian skrin pengesahan.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Bingkai yang digunakan sebagai sebahagian skrin langkau.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Bingkai yang digunakan sebagai sebahagian skrin pemberitahuan.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Adakah latar belakang bingkai patut dijubinkan?
define gui.frame_tile = False


## Bar, Bar Tatal, dan Lungsur #################################################
##
## Ini mengawal rupa dan saiz bar, bar tatal, dan lungsur.
##
## GUI lalai hanya menggunakan lungsur dan bar tatal menegak. Semua bar lain
## hanya digunakan dalam skrin ditulis oleh para pencipta.

## Tinggi bar melintang, bar tatal, dan lungsur. Lebar bar menegak, bar tatal,
## dan lungsur.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## Tetapkan True jika imej bar patut dijubinkan. Tetapkan False jika mereka
## patut disesuaikan saiz secara linear.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Sempadan melintang.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Sempadan menegak.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## Sejarah #####################################################################
##
## Skrin sejarah memaparkan dialog yang pemain telah tolak tepi.

## Jumlah blok sejarah dialog yang Ren'Py akan simpan.
define config.history_length = 250

## Tinggi untuk entri skrin sejarah, atau tetapkan kepada None untuk membiarkan
## tinggi dikira sendiri dengan mengorbankan prestasi.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## Kedudukan, lebar, dan penjajaran label yang memberikan nama kepada watak
## yang sedang bercakap.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Kedudukan, lebar, dan penjajaran tulisan dialog.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Mod NVL #####################################################################
##
## Skrin mod NVL menunjukkan dialog yang dicakapkan oleh watak mod NVL.

## Sempadan latar belakang tetingkap latar mod NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Jumlah entri mod NVL maksimum yang Ren'Py akan paparkan. Apabila lebih
## banyak entri akan ditunjukkan, entri paling lama akan dibuang.
define gui.nvl_list_length = 6

## Tinggi entri mod NVL. Tetapkan ini kepada None untuk membuatkan entri
## melaraskan tinggi secara dinamik.
define gui.nvl_height = 173

## Jarak di antara entri mod NVL apabila gui.nvl_height ditetapkan kepada None,
## dan di antara entri mod NVL dan menu mod NVL.
define gui.nvl_spacing = 15

## Kedudukan, lebar, dan penjajaran label yang memberikan nama kepada watak
## yang sedang bercakap.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Kedudukan, lebar, dan penjajaran tulisan dialog.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Kedudukan, lebar, dan penjajaran tulisan nvl_thought (tulisan yang
## dicakapkan oleh watak nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Kedudukan menu_buttons nvl.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Terjemahan ##################################################################

## Ini mengawal di mana baris pemisah dibenarkan. Lalainya ia sesuai untuk
## semua bahasa. Senarai nilai yang ada boleh dijumpai di https://www.renpy.org/
## doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Peranti mudah alih
################################################################################

init python:

    ## Ini menambah saiz butang cepat untuk membuatkan mereka lebih mudah
    ## disentuh pada tablet dan telefon.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Ini menukar saiz dan penjarakan pelbagai unsur GUI untuk memastikan
    ## mereka lebih mudah dilihat pada telefon.
    @gui.variant
    def small():

        ## Saiz fon.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Laras kedudukan kotak tulisan.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Tukar saiz dan penjarakan pelbagai benda.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Tataletak butang fail.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Mod NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30