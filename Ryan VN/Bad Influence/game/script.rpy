# Declare characters used by this game.
define mc = Character("[mc_name]")
define unk = Character("?????")
define stevia = Character("Stevia")
define rangga = Character("Rangga")
define ucup = Character("Ucup") # Menambahkan char Ucup yang disebut

# Custom Transforms
transform custom_bg:
    # Scale background to exact screen size (misal 1920x1080 atau default Ren'Py 1280x720)
    size (1920, 1080) # Pastikan mengisi seluruh layar 
    alpha 0.75  # 75% opacity

transform custom_char_center:
    zoom 1.5    
    yalign 1.0  
    xalign 0.5  # Tengah

transform custom_char_left:
    zoom 1.5    
    yalign 1.0  
    xalign 0.15 # Kiri

transform custom_char_right:
    zoom 1.5    
    yalign 1.0  
    xalign 0.85 # Kanan

# Animasi menggeser
transform move_to_left:
    linear 0.5 xalign 0.15

transform move_to_center:
    linear 0.5 xalign 0.5

# The game starts here.
label start:
    $ mc_name = "MC" 
    
    # Arc 1: Orientation (Gerbang Sekolah - Pagi Hari)
    scene placeholder at custom_bg

    "Hari ini adalah hari pertama sekolah, semua siswa telah menyelesaikan liburan dan siap untuk kembali ke sekolah."
    "Namun berbeda dengan [mc_name], ia adalah murid pindahan."
    "Di masa lalunya, [mc_name] selalu menjadi target bullying, dan akhirnya ia memutuskan untuk pindah sekolah untuk memulai lembaran baru."

    # Latar 1: Gerbang Sekolah Pagi Hari
    scene gerbangpagihari at custom_bg
    show charmc at custom_char_center

    mc "Sekolah baru, identitas baru. Semoga kali ini aku bisa bertahan tanpa jadi sasaran empuk seperti di sekolah lama."

    # Latar 2: Area Lorong Kelas - Pagi Hari
    scene lorongpagihari at custom_bg
    show charmc at custom_char_center

    mc "(Tampak Kebingungan) Kira-kira kelas baruku yang mana ya?"
    mc "Coba aku cari di papan pengumuman."

    # Scene 1: Papan Pengumuman
    scene placeholder at custom_bg
    show charmc at custom_char_center

    mc "Mana ya namaku?"

    # Scene 2: Siswa Menepuk Pundak
    scene lorongpagihari at custom_bg
    
    # MC sedang sendiri di tengah
    show charmc at custom_char_center
    
    "Seseorang mendekat dan menepuk pundak [mc_name]."

    # Stevia (unk) muncul, kita akan geser MC ke kiri, dan Stevia muncul di kanan
    show charmc at move_to_left
    show charstevia at custom_char_right
    
    unk "Hei! Kamu murid pindahan baru di sini, ya?"

    mc "(Kaget)..."
    mc "(Agak gugup) I..iyaa..."

    stevia "Gausah gugup gitulah, kenalin aku Stevia, Kalau kamu?"

    mc "(Agak gugup) A..aaku [mc_name]."

    stevia "Ohh, [mc_name], namamu keren juga."

    mc "(Agak gugup) Ma..ma..kasih."

    stevia "Hmmm, ngomong-ngomong kamu di kelas berapa?"

    mc "(Agak gugup) Aku di kelas 10."

    stevia "Wah, berarti kita sekelas dong, salam kenal ya."

    mc "(Agak gugup) I..iiya, salam kenal juga."

    # Scene 3: Papan pengumuman, sambil menunjuk di nama (mencari nama)
    scene placeholder at custom_bg
    # Asumsikan masih format yang sama: MC kiri, Stevia Kanan
    show charmc at custom_char_left
    show charstevia at custom_char_right
    
    "Stevia menunjuk ke arah papan pengumuman untuk mencari nama."

    stevia "Wihh, kebetulan banget nih, aku liat nama kamu di kelas 10A, berarti kita sekelas dong nanti."

    stevia "Nanti kalau ada masalah jangan sungkan ke aku ya, soalnya aku ketua kelas."

    mc "I..iya, maa…kasih ya."

    # Scene 4: Murid Bersenggolan
    scene lorongpagihari at custom_bg
    show charmc at custom_char_left
    show charstevia at custom_char_right

    "Tiba-tiba ada murid yang bersenggolan dengan mereka."

    # Rangga muncul di kanan, Stevia kita geser ke tengah.
    show charstevia at move_to_center
    show charrangga at custom_char_right

    rangga "Minggir lu dari jalan gw."

    stevia "Apa sih, orang jalan luas gini, lu aja kali yang minggir."

    rangga "Ngelawan gw lu."

    "Rangga melirik ke arah [mc_name]."

    rangga "Wihh, siapa nih, anak baru ya, nama lu siapa?"

    mc "A..aa..aaku [mc_name]."

    rangga "[mc_name]? Nama lu lucu banget, pantes aura culunnya kecium."

    stevia "Apa sih lu, mending lu minggir deh dari sini, ga sopan banget lu sama anak baru."

    rangga "Berani ya lu lawan gw, gw hantam lu."

    # Scene 4 (Lanjutan): Kepalan tangan yang mau menonjok murid
    scene placeholder at custom_bg
    # Fokus adegan ke Rangga, MC dan Stevia disembunyikan / tidak jadi fokus utama
    show charrangga at custom_char_center

    "Rangga mengepalkan tangannya dan bersiap untuk menonjok."

    return
