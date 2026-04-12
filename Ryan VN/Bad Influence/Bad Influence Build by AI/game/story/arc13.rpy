# ==========================================
# ARC 13: THE LINE CROSSED
# ==========================================

# --- SCENE 0: KUIS PKN (Sebelum Malam Hari) ---
label arc13_scene0:
    scene bg_classroom_morning with fade
    show mc neutral at center
    show pg neutral at center with fade

    pg "Sebelum kalian pulang hari ini, ada kuis PKN singkat."
    pg "Ingat, nilai kuis ini masuk rapor. Harap dikerjakan dengan serius!"

    hide pg with dissolve
    hide mc

    call quiz3_start

    # Lanjut ke malam hari — kejadian paket
    jump arc13_scene1


# --- SCENE 1: THE PACKAGE ---
label arc13_scene1:
    scene bg_back_alley_night with fade
    show ucup neutral at center
    show rangga smirk at left
    show mc anxious at right

    "Matahari sudah lama tenggelam. Suara kendaraan di kejauhan terdengar samar, tenggelam oleh kesunyian di gang sepi ini. Ucup merogoh tasnya dan mengeluarkan sebuah paket kecil yang terbungkus plastik hitam."
    u "Cuma titip barang doang. Gampang. Lo tinggal bawa ini, nanti ada yang ambil di depan gang sebelah sana."
    mc "(Menatap paket itu dengan tangan gemetar) Ini... isinya apa, Cup?"
    r "Nggak usah banyak tanya, Bro. Anggap aja ini ujian buat jadi 'keluarga' kita yang sebenernya."

    jump arc13_scene2


# --- SCENE 2: THE MORAL BOUNDARY ---
label arc13_scene2:
    show rangga serious

    r "Gue nggak butuh orang yang cuma bisa nongkrong doang. Gue butuh orang yang punya nyali. Lo bilang lo nggak mau di-bully lagi, kan?"
    r "Orang yang punya kuasa itu orang yang berani ambil risiko. Lo mau tetep jadi pecundang, atau mau maju bareng kita?"
    "(Narasi Internal) Jantungku berpacu sangat cepat. Aku tahu paket ini bukan barang biasa. Tapi kalau aku menolak... apa aku akan kembali ke lubang gelap sendirian? Tanpa pelindung?"

    jump arc13_scene3


# --- SCENE 3: THE BIG CHOICE (THE LINE) ---
label arc13_scene3:
    menu:
        "Terima (Cross the Line)":
            $ friendship_rangga += 20
            $ sanity -= 25
            $ took_package = True

            show mc neutral
            mc "(Mengambil paket itu perlahan) Oke. Gue bawa. Cuma nganterin, kan?"
            show rangga smirk
            r "Nah! Gitu dong. Itu baru namanya nyali."

        "Tolak (Stand Your Ground)":
            $ friendship_rangga -= 20
            $ sanity += 10
            $ refused_package = True

            show mc sad
            mc "Maaf... gue nggak bisa. Ini udah kelewatan, Ngga."
            show rangga annoyed
            r "Gue kira lo beda. Ternyata lo cuma pengecut yang kebetulan pindah sekolah."
            show rangga serious
            r "Jangan cari gue kalau besok-besok ada yang nyari masalah sama lo."

        "Ragu (Uncertainty)":
            $ friendship_rangga -= 5
            $ sanity -= 5

            show mc anxious
            mc "Bisa kasih gue waktu? Gue... gue nggak tahu harus gimana."
            show rangga annoyed
            r "Lama lo. Buang-buang waktu gue aja."
            "Situasi menjadi sangat menegangkan dan awkward."

    jump arc13_scene4


# --- SCENE 4: PARANOIA ---
label arc13_scene4:
    hide rangga
    hide ucup
    scene bg_street_night with fade
    show mc anxious at center

    "Langkah kakiku terasa sangat berat. Setiap lampu jalan yang berkedip membuatku tersentak."
    mc "(Menoleh ke belakang berkali-kali)"
    "(Narasi Internal) Apa ada yang mengikutiku? Apa polisi sudah tahu? Kenapa duniaku yang baru saja mulai membaik, tiba-tiba terasa lebih gelap dari sebelumnya?"

    jump arc14_scene1
