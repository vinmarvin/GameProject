# ==========================================
# ARC 8: THE CROSSROADS (KONFRONTASI)
# ==========================================

# --- SCENE 1: THE TENSE STANDOFF ---
label arc8_scene1:
    scene bg_back_corridor_noon with fade
    show stevia worried at right
    show rangga smirk at left
    show ucup neutral at center
    show mc anxious at center

    s "Rangga, aku sudah bilang berkali-kali. Ini area sekolah. Berhenti memakai vape di sini atau aku laporin ke guru piket sekarang juga."
    r "Stev, lo itu nggak ada bosennya ya? Tiap istirahat kerjaan lo cuma nyari kesalahan gue. Lo itu mau jadi murid atau mau jadi CCTV sekolah?"
    u "Hahaha... mungkin dia kesepian, Ngga. Makanya hobi nyari perhatian kita."

    jump arc8_scene2


# --- SCENE 2: THE LOW BLOW ---
label arc8_scene2:
    show rangga serious

    r "Lo tahu kenapa nggak ada yang mau deket sama lo selain 'Anak Baru' ini? Karena lo itu lemah, Stev. Tapi lo akting sok paling bener buat nutupin cacat lo."
    show stevia disappointed
    s "(Suara bergetar) Rangga... cukup. Jangan bawa-bawa hal itu."
    r "(Menoleh tajam ke arah [nama_mc]) Oi, [nama_mc]! Lo kan sering bareng kita. Lo sadar nggak sih? Kalau si Ketua Kelas ini jalan... bunyinya aneh. Kayak ada yang nyangkut. Lo nggak keganggu apa?"
    "Keheningan yang menyakitkan menyelimuti lorong. [nama_mc] teringat kembali pada bayangan dirinya sendiri di sekolah lama—saat ia hanya bisa diam ketika dihina."

    jump arc8_scene3


# --- SCENE 3: THE BIG CHOICE (MORAL BOUNDARY) ---
label arc8_scene3:
    show mc anxious at center

    menu:
        "Bela Stevia (Stand for Integrity)":
            $ friendship_stevia += 15
            $ friendship_rangga -= 20
            $ sanity += 8

            mc "Cukup, Ngga! Masalah aturan itu satu hal, tapi nyerang fisik dia itu rendah banget. Berhenti jadi pengecut."
            show rangga annoyed
            r "Wah, jadi lo pilih jadi pahlawan buat si pengkor ini? Oke. Inget ini, [nama_mc]. Jangan nyesel ya kalo nanti lo nggak punya tempat lagi di sini."
            hide rangga with moveoutleft
            hide ucup
            show stevia calm
            s "(Menyeka matanya) Makasih, [nama_mc]... kamu nggak perlu sejauh itu."

        "Pilih Rangga (Side with Power)":
            $ friendship_stevia -= 20
            $ friendship_rangga += 15
            $ sanity -= 10

            show mc neutral
            mc "Stev... mungkin Rangga ada benernya. Lo emang terlalu maksa orang. Nggak semua orang nyaman diatur terus pake jabatan lo."
            show stevia disappointed
            "(Hanya diam, namun air matanya jatuh satu tetes sebelum ia berbalik pergi dengan langkah yang berat)"
            hide stevia with moveoutright
            show rangga smirk
            r "Nah! Itu baru temen gue. Emang si Pincang ini perlu dikasih pelajaran biar nggak sok suci."

    jump arc8_scene4


# --- SCENE 4: AFTERMATH & REFLECTION ---
label arc8_scene4:
    hide rangga
    hide stevia
    hide ucup
    scene bg_classroom_sunset with fade
    show mc sad at center

    "Pelajaran terakhir berakhir. Kelas sudah sepi. Namun, gema dari kata-kata yang terucap di koridor tadi masih menghantui setiap sudut ruangan."
    mc "(Menatap telapak tangannya sendiri) Apa aku baru saja melakukan hal yang benar? Atau aku baru saja menjadi monster yang dulu paling aku takuti?"
    "(Narasi Internal) Tempat ini bukan cuma soal jadi diterima atau tidak... tapi soal siapa yang harus aku sakiti supaya aku bisa bertahan."

    jump arc9_branch
