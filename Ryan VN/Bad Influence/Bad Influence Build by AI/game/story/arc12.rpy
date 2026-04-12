# ==========================================
# ARC 12: PRESSURE BUILDS
# ==========================================

# --- SCENE 1: THE OVERWHELMING CLASSROOM ---
label arc12_scene1:
    scene bg_classroom_morning with fade
    show mc anxious at center

    "Jam pelajaran berjalan dua kali lebih cepat dari biasanya. Suara kapur yang beradu dengan papan tulis terdengar seperti detak bom waktu."
    mc "(Menatap papan tulis dengan pandangan kosong)"
    "(Narasi Internal) Kenapa... kenapa aku tidak bisa menangkap satu kalimat pun? Suara Guru terdengar sangat jauh, seperti tersaring air. Tanganku kaku. Aku tertinggal lagi."

    jump arc12_scene2


# --- SCENE 2: PATH DIVERGENCE (CONSEQUENCE) ---
label arc12_scene2:

    if recovery_path:
        # BRANCH A — Jalur Stevia (Library)
        scene bg_library_afternoon with dissolve
        show stevia calm at right
        show mc anxious at left

        s "[nama_mc], coba lihat bagian ini. Kalau kamu pakai rumus yang tadi, hasilnya pasti ketemu."
        mc "Maaf, Stev... kepalaku rasanya penuh sekali hari ini."
        show stevia disappointed
        s "(Menutup buku dengan pelan) Kamu harus lebih serius, [nama_mc]. Kita sudah di jalur yang benar, jangan biarkan fokusmu hilang sekarang. Aku nggak bisa terus-terusan narik kamu kalau kamu nggak mau melangkah."
        "(Narasi Internal) Tekanannya berbeda. Stevia tidak membully-ku, tapi harapannya terasa seperti beban berat yang harus kupanggul agar dia tidak kecewa."

    elif denial_path:
        # BRANCH B — Jalur Rangga
        scene bg_school_gate_afternoon with dissolve
        show rangga smirk at left
        show ucup neutral at center
        show mc neutral at right

        r "Woi, muka lo udah kayak kertas kusut gitu. Mending ikut kita, ada tempat baru yang asik buat 'napas' bentar."
        mc "Gue... gue ada tugas yang belum selesai sebenarnya."
        show rangga annoyed
        r "Tugas lagi? Lo mau jadi budak sistem kayak si Pincang itu? Udah, ikut aja. Dunia nggak bakal kiamat cuma gara-gara lo bolos ngerjain satu tugas."
        "(Narasi Internal) Ajakan Rangga terdengar seperti pelarian yang manis. Tapi aku tahu, setiap kali aku ikut, aku hanya sedang menunda kehancuran yang lebih besar."

    else:
        # BRANCH C — Jalur Isolasi
        scene bg_mc_room_night with dissolve
        show mc anxious at center

        mc "(Menatap buku di meja yang gelap) Kenapa... kenapa sulit sekali?"
        "(Narasi Internal) Aku sendirian. Tidak ada Stevia yang menuntut, tidak ada Rangga yang menggoda. Tapi di dalam sini, suaraku sendiri adalah musuh yang paling kejam."

    jump arc12_scene3


# --- SCENE 3: QUIZ 3 (THE CHECKPOINT) ---
label arc12_scene3:
    hide stevia
    hide rangga
    hide ucup
    scene bg_classroom_day with fade
    show mc anxious at center

    "Kuis dadakan dimulai. Ujian untuk melihat seberapa kuat fondasimu sekarang."

    if recovery_path:
        "(Teks soal tampil stabil. Catatan Stevia membantu.)"
    elif denial_path:
        "(Teks soal sesekali blur dan goyang. Kepalamu berdenyut.)"
    else:
        "(Timer bergerak tidak menentu. Konsentrasi tercerai-berai.)"

    mc "(Memegang pulpen dengan sangat erat)"

    jump arc12_scene4


# --- SCENE 4: END OF DAY REFLECTION ---
label arc12_scene4:
    scene bg_school_hallway_sunset with fade
    show mc sad at center

    "Hari berakhir dengan rasa lelah yang luar biasa."
    mc "(Berhenti sebentar, melihat bayangannya di kaca jendela) Apa ini harga yang harus kubayar untuk sebuah 'perubahan'?"
    "(Narasi Internal) Keputusanku kemarin mulai memakan diriku sendiri. Dan aku merasa... sesuatu yang lebih besar sedang menungguku di tikungan berikutnya."

    jump arc13_scene0
