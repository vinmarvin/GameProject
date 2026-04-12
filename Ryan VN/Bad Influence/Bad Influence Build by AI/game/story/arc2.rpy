# ==========================================
# ARC 2: MEET THE NEW GUY
# Cek Flag: defend_stevia / passive_start
# ==========================================

# --- SCENE 1: THE INTRODUCTION ---
label arc2_scene1:
    scene bg_classroom_morning with fade

    # Guru tampil duluan, perkenalan kelas
    show pg neutral at center with fade
    pg "Anak-anak, harap tenang sebentar. Hari ini kita kedatangan kawan baru. Silakan, perkenalkan dirimu."

    # Guru disembunyikan, MC maju memperkenalkan diri
    hide pg with dissolve
    show mc anxious at center with dissolve
    mc "(Menelan ludah, menatap seisi kelas) Ha.. lo semuanya. Nama aku [nama_mc]. Aku pindahan dari SMA Juara Jaya."
    "(Narasi Internal) Sial, suaraku gemetar. Aku bisa melihat beberapa murid mulai berbisik. Apa mereka tahu alasan asliku pindah?"

    # Rangga komentar dari belakang
    show rangga smirk at right
    r "(Dari barisan belakang) Juara Jaya? Sekolah elit itu? Kenapa pindah ke sini? Diusir ya?"
    show stevia worried at left
    s "Rangga! Jaga bicaramu. Dia murid baru."
    hide stevia
    hide rangga

    # Guru muncul lagi untuk menutup perkenalan
    hide mc with dissolve
    show pg neutral at center with dissolve
    if defend_stevia:
        pg "Sudah, sudah. [nama_mc], silakan duduk di bangku kosong di depan Rangga."
    else:
        pg "Rangga, mohon tenang. [nama_mc], silakan duduk."

    hide pg with dissolve

    jump arc2_scene2


# --- SCENE 2: THE MATH SESSION ---
label arc2_scene2:
    scene bg_classroom_morning with dissolve
    show mc neutral at center

    "(Narasi Internal) Jam pelajaran matematika dimulai. Rumus-rumus di papan tulis terasa membosankan, tapi atmosfer di belakangku jauh lebih mengganggu. Aku bisa merasakan tatapan Rangga tepat di tengkukku."
    "Kelas menjadi hening saat Pak Guru mulai menulis soal di papan tulis. Namun, keheningan itu dipecah oleh suara dengkuran halus dari arah belakang [nama_mc]."

    jump arc2_scene3


# --- SCENE 3: THE SLEEPING GIANT ---
label arc2_scene3:
    show stevia worried at right

    s "(Berbisik pelan) [nama_mc]... bangunin Rangga. Pak Guru sudah mulai melirik ke belakang. Kalau dia ketahuan tidur lagi, dia bisa kena detensi berat hari ini."
    show mc anxious
    mc "Kenapa harus aku? Dia pasti marah kalau dibangunkan."
    s "Tolonglah. Aku ketua kelas, kalau aku yang bangunin, dia pasti makin nyolot. Kamu kan orang baru, mungkin dia lebih segan."
    "(Narasi Internal) Inilah dia. Dilema pertama. Jika aku membangunkannya, aku membantu Stevia tapi berisiko dimusuhi Rangga. Jika aku diam, aku membiarkan masalah terjadi."

    jump arc2_scene4


# --- SCENE 4: THE BIG CHOICE #1 (CLASSROOM DYNAMICS) ---
label arc2_scene4:
    show mc anxious at left
    show rangga neutral at right

    menu:
        "Bangunkan Rangga (Disturb Rangga)":
            $ friendship_rangga -= 7
            $ sanity += 1
            $ disturb_rangga = True

            mc "(Menyenggol bahu Rangga pelan) Ngga... bangun. Ada Pak Guru."
            show rangga annoyed with vpunch
            r "(Terbangun kaget) Agh! Apaan sih lo?! Berisik banget!"
            hide rangga
            hide mc
            show pg neutral at center with dissolve
            pg "Rangga! Tidur lagi kamu? Keluar sekarang, cuci muka!"
            hide pg with dissolve
            show mc anxious at left with dissolve
            show rangga serious at right
            r "(Menatap tajam [nama_mc] sebelum keluar) Awas lo nanti."
            hide rangga with moveoutright
            show stevia calm at right
            s "Makasih, [nama_mc]. Setidaknya dia nggak langsung dikirim ke ruang BK."

        "Diam Saja (Avoid Conflict)":
            $ friendship_rangga += 2
            $ sanity -= 3
            $ avoid_conflict = True

            show mc neutral
            "(Kembali menatap papan tulis, pura-pura tidak dengar)"
            "Beberapa menit kemudian, Pak Guru melempar spidol tepat ke meja Rangga."
            hide mc
            hide rangga
            show pg neutral at center with dissolve
            pg "RANGGA! Keluar sekarang! Jangan bawa kebiasaan burukmu ke jam saya!"
            hide pg with dissolve
            show mc neutral at left with dissolve
            show rangga annoyed at right
            r "(Berjalan keluar dengan malas, tidak peduli siapapun)"
            hide rangga with moveoutright
            show stevia disappointed at right
            s "Padahal aku sudah minta tolong..."

    jump arc2_scene5


# --- SCENE 5: CLOSING ARC 2 ---
label arc2_scene5:
    hide stevia
    scene bg_classroom_morning with dissolve
    show mc sad at center

    "(Narasi Internal) Bel istirahat berbunyi. Aku merasa lelah, padahal hari belum setengah jalan. Setiap pilihanku seolah-olah sedang menanam benih badai yang akan datang."
    mc "Apa aku benar-benar bisa jadi 'normal' di sini?"

    jump arc3_scene1
