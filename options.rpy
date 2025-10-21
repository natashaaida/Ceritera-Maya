## Fail ini mengandungi pilihan yang boleh ditukar untuk mengubahsuai permainan
## anda.
##
## Baris bermula dengan dua tanda '#' ialah komen, dan anda tidak patut
## menyahkomen mereka. Baris bermula dengan satu tanda '#' ialah kod yang
## dikomenkan, dan anda mungkin ingin menyahkomen mereka apabila perlu.


## Asas ########################################################################

## Nama permainan yang boleh dibaca manusia. Ini digunakan untuk menetapkan
## tajuk tetingkap lalai, dan ditunjukkan dalam antara muka dan laporan ralat.
##
## Tanda _() di sekeliling rentetan menandakan ia layak untuk diterjemah.

define config.name = _("Ceritera Maya")


## Menentukan sama ada tajuk yang diberikan di atas ditunjukkan pada skrin menu
## utama. Tetapkan kepada False untuk menyembunyikan tajuk.

define gui.show_name = True


## Versi permainan ini.

define config.version = "1.0"


## Tulisan yang diletakkan pada skrin perihalan permainan. Letakkan tulisan di
## antara tanda petikan ganda tiga, dan biarkan baris kosong di antara perenggan.

define gui.about = _p("""
""")


## Nama pendek untuk permainan yang digunakan untuk boleh laku dan direktori
## dalam pengedaran yang dibina. Ini mestilah aksara ASCII sahaja, dan tidak
## boleh ada selang, titik bertindih, atau koma bertindih.

define build.name = "CeriteraMaya"


## Bunyi dan muzik #############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Untuk membolehkan pengguna memainkan bunyi percubaan untuk saluran bunyi
## atau suara, nyahkomen satu baris di bawah dan gunakannya untuk menetapkan
## bunyi sampel untuk dimainkan.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Nyahkomen baris di bawah untuk menetapkan fail audio yang akan dimainkan
## ketika pemain berada di menu utama. Fail ini akan terus dimainkan selepas
## permainan bermula, sehingga ia dihentikan atau fail lain dimainkan.

# define config.main_menu_music = "main-menu-theme.ogg"


## Peralihan ###################################################################
##
## Pemboleh ubah ini menetapkan peralihan yang akan digunakan apabila
## berlakunya acara tertentu. Setiap pemboleh ubah patut ditetapkan kepada
## sejenis peralihan, atau kepada None untuk menunjukkan tiada peralihan patut
## digunakan.

## Masuk atau keluar menu permainan.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Di antara skrin berbeza di menu permainan.

define config.intra_transition = dissolve


## Peralihan yang digunakan selepas permainan dimuatkan.

define config.after_load_transition = None


## Digunakan ketika memasuki menu utama selepas permainan tamat.

define config.end_game_transition = None


## Pemboleh ubah untuk menetapkan peralihan yang digunakan apabila permainan
## yang dimulakan tidak wujud. Sebaliknya, gunakan dengan kenyataan selepas
## menunjukkan adegan awal.


## Pengurusan tetingkap ########################################################
##
## Ini mengawal apabila tetingkap dialog dipaparkan. Jika ditetapkan kepada
## "show", ia akan sentiasa dipaparkan. Jika "hide", ia hanya dipaparkan apabila
## ada dialog. Jika "auto", tetingkap disembunyikan sebelum kenyataan adegan dan
## ditunjukkan semula selepas dialog dipaparkan.
##
## Selepas permainan dimulakan, ini boleh ditukar dengan kenyataan "window
## show", "window hide", dan "window auto".

define config.window = "auto"


## Peralihan yang digunakan untuk menunjukkan dan menyembunyikan tetingkap
## dialog

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Lalai keutamaan #############################################################

## Mengawal kelajuan lalai tulisan. Nilai lalai, 0, ialah tiada had (keluar
## semua serentak), manakala nombor lain ialah jumlah aksara per saat untuk
## ditulis.

default preferences.text_cps = 0


## Lengah masa bergerak-sendiri yang lalai. Nombor lebih besar menyebabkan
## lengah lebih lama, dengan julat yang sah dari 0 hingga 30.

default preferences.afm_time = 15


## Direktori simpan ############################################################
##
## Mengawal tempat khusus-platform yang Ren'Py akan letakkan fail simpan untuk
## permainan ini. Fail simpan akan diletakkan di:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Secara umumnya, ini tidak patut ditukar, namun jika perlu ditukar, ia
## mestilah rentetan literal dan bukannya ungkapan.

define config.save_directory = "CeriteraMaya-1759825781"


## Ikon ########################################################################
##
## Ikon dipaparkan di bar tugas atau dok.

define config.window_icon = "gui/window_icon.png"


## Tatarajah pembinaan #########################################################
##
## Bahagian ini mengawal bagaimana Ren'Py menukarkan projek anda menjadi fail
## pengedaran.

init python:

    ## Fungsi di bawah mengambil corak fail. Corak fail tidak sensitif huruf,
    ## dan dipadankan dengan haluan relatif kepada direktori asas, dengan dan
    ## tanpa tanda pendahuluan /. Jika pelbagai corak terpadan, padanan pertama
    ## digunakan.
    ##
    ## Dalam padanan:
    ##
    ## / ialah pemisah direktori.
    ##
    ## * padan semua aksara, kecuali pemisah direktori.
    ##
    ## ** padan semua aksara, termasuk pemisah direktori.
    ##
    ## Contohnya, "*.txt" padan dengan fail txt dalam direktori asas, "game/
    ## **.ogg" padan dengan fail ogg dalam direktori game atau mana-mana
    ## subdirektorinya, dan "**.psd" padan dengan fail psd di mana-mana dalam
    ## projek.

    ## Klasifikasikan fail sebagai None untuk mengecualikan mereka daripada
    ## pengedaran yang dibina.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Untuk mengarkib fail, klasifikasikan mereka sebagai 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Fail yang padan dengan corak pendokumenan akan dipenduakan dalam binaan
    ## aplikasi Mac, jadi mereka muncul dalam kedua-dua aplikasi dan fail zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."

init python:
    # Tetapan asas binaan web
    build.name = "Ceritera_Maya"
    build.version = "1.0"
    build.include_web = True
    build.directory_name = "CeriteraMayaWeb"
    build.executable_name = "ceritera_maya"
    build.itch_project = "natashaaida/ceritera-maya"    

