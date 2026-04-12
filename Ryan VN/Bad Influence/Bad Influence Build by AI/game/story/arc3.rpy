# ==========================================
# ARC 3: LUNCH BREAK
# 3 Pilihan → menentukan Route Lock
# ==========================================

# --- SCENE 1: THE OVERWHELMING NOISE ---
label arc3_scene1:
    scene bg_school_canteen_noon with fade
    show mc anxious at center

    "Kantin sangat ramai. Bau uap nasi bercampur keringat dan suara teriakan murid-murid membuat kepalaku berdenyut."
    mc "(Menelan ludah) Ramai banget... Rasanya semua mata tertuju padaku. Apa mereka tahu aku 'orang asing' di sini?"
    "(Narasi Internal) Aku hanya ingin makan dengan tenang tanpa ada yang menyadari keberadaanku. Tapi di sekolah ini, ketenangan adalah kemewahan."

    jump arc3_scene2


# --- SCENE 2: STEVIA'S SAFETY NET ---
label arc3_scene2:
    show stevia calm at right

    s "[nama_mc]! Akhirnya ketemu. Wah, untung kita masih kebagian nasi goreng. Biasanya jam segini sudah ludes."
    show mc neutral
    mc "Iya... ternyata di sini jauh lebih ramai dari sekolah lamaku."
    s "Tunggu di sini sebentar, ya. Aku mau cari minum di sebelah sana. Nanti kita duduk di meja pojok yang sepi itu."
    hide stevia
    "[nama_mc] berdiri sendiri di tengah kerumunan, memegang piringnya dengan kaku."

    jump arc3_scene3


# --- SCENE 3: THE BAD INFLUENCE ---
label arc3_scene3:
    show rangga smirk at left
    show ucup neutral at right

    u "Woi! Murid baru! Sini gabung sama kita!"
    r "(Menyenggol [nama_mc]) Ngapain lo berdiri kayak patung di tengah jalan? Sini duduk sama kita. Daripada lo makan sama si Ketua Kelas yang kaku itu."
    show mc anxious
    mc "Eh, tapi Stevia tadi sudah..."
    show rangga serious
    r "(Menatap tajam) Lo lebih milih dengerin ceramah Stevia daripada asik-asikan sama kita? Gini deh, lo mau dikenal sebagai 'anak emas guru' atau mau jadi bagian dari yang 'punya kuasa' di sini?"

    jump arc3_scene4


# --- SCENE 4: THE BIG CHOICE #2 (SOCIAL POSITIONING) ---
label arc3_scene4:
    show stevia worried at right
    show rangga smirk at left
    show mc anxious at center

    s "[nama_mc], ayo. Meja yang tadi sudah kosong."
    r "Jangan kaku lah, Stev. Dia mau gabung sama kita kok. Ya kan, [nama_mc]? Nanti sore kita mau nongkrong, lo bisa ikut kalau mau 'bernafas' dikit."

    menu:
        "Ikut Rangga (The Risk Path)":
            $ friendship_stevia -= 5
            $ friendship_rangga += 15
            $ sanity -= 10
            $ join_rangga      = True
            $ bad_route_lock   = True

            show mc neutral
            mc "Kayaknya seru... aku ikut kalian saja."
            show rangga smirk
            r "Nah! Gitu dong. Gue tunggu lo di parkiran pas pulang."
            show stevia disappointed
            s "Terserah kamu saja, [nama_mc]. Aku harap kamu bisa jaga diri."
            hide stevia with moveoutright

        "Ragu-ragu (Uncertain)":
            $ friendship_rangga += 3
            $ sanity -= 2
            $ uncertain = True

            show mc anxious
            mc "Aku... aku lihat nanti ya. Belum tahu bisa atau nggak."
            show rangga annoyed
            r "Halah, kelamaan mikir lo. Kesempatan buat gabung sama kita nggak dateng dua kali."
            show stevia worried
            s "[nama_mc], mending kamu langsung pulang saja nanti."

        "Ikut Stevia (The Safe Path)":
            $ friendship_stevia   += 10
            $ friendship_rangga   -= 5
            $ sanity              += 5
            $ trust_stevia        = True
            $ stevia_route_lock   = True

            show mc neutral
            mc "Maaf, Rangga. Aku sudah janji mau diskusi tugas sama Stevia."
            show stevia calm
            s "Ayo, [nama_mc]. Makanannya keburu dingin."
            show rangga annoyed
            r "Cih. Dasar murid teladan. Jangan nyesel ya kalau nanti lo dikucilkan."
            hide rangga with moveoutleft

    jump arc3_scene5


# --- SCENE 5: CLOSING ARC 3 ---
label arc3_scene5:
    hide rangga
    hide stevia
    hide ucup
    scene bg_school_canteen_noon with dissolve
    show mc sad at center

    "Suara bel masuk berbunyi. Pertemuan singkat di kantin ini baru saja membelah masa depanku menjadi dua."
    mc "(Melihat ke arah gerbang sekolah) Langkah pertamaku... ke mana ini akan membawaku?"

    jump arc4_scene1
