# ==========================================
# ARC 4: AFTER SCHOOL
# Cek Flag: join_rangga / trust_stevia / uncertain
# Menentukan: bad_route_lock / stevia_route_lock
# ==========================================

# --- SCENE 1: END OF CLASS ---
label arc4_scene1:
    scene bg_classroom_sunset with fade
    show mc neutral at center

    "Bel pulang berbunyi. Cahaya matahari sore masuk melalui celah jendela, memberikan bayangan panjang di lantai kelas."
    show mc sad
    mc "Selesai. Hari pertamaku hampir berakhir, tapi perasaanku justru makin tidak karuan."
    "(Narasi Internal) Aku melihat ke arah gerbang. Keputusanku di kantin tadi masih membayangi. Apakah aku benar-benar siap untuk langkah selanjutnya?"

    jump arc4_scene2


# --- SCENE 2: THE FINAL CALL ---
label arc4_scene2:
    scene bg_school_gate_sunset with dissolve

    if join_rangga:
        # BRANCH A — Bergabung dengan Rangga
        show ucup neutral at right
        show rangga smirk at left
        show mc anxious at center

        u "Lama amat lo. Gue kira lo diculik Stevia ke ruang guru."
        r "Siap buat bersenang-senang, [nama_mc]? Lupain tugas-tugas itu. Dunia di luar sini jauh lebih nyata."
        "(MC menoleh sekilas ke arah Stevia yang berjalan menjauh sendirian)"
        $ friendship_rangga += 12
        $ sanity -= 10

    elif trust_stevia:
        # BRANCH B — Bersama Stevia
        show stevia calm at right
        show mc neutral at left

        s "[nama_mc]! Jadi kan? Rumahku tidak jauh dari sini, kita bisa naik angkutan umum atau jalan kaki sebentar."
        mc "Iya, Stev. Aku juga bingung kalau mengerjakan tugas sejarah itu sendirian."
        s "Baguslah. Aku senang kamu memilih jalan yang benar. Daripada... yah, kamu tahu sendiri geng Rangga."
        $ friendship_stevia += 12
        $ sanity += 8

    else:
        # BRANCH C — Ragu / Sendiri
        show mc sad at center

        mc "Akhirnya... semua sudah pulang. Aku tidak memilih siapapun."
        "(Narasi Internal) Rangga mengajakku nongkrong, Stevia mengajakku belajar. Tapi aku... aku malah tidak mengambil keduanya. Mungkin pulang dan bertemu Nenek adalah pilihan terbaik."
        $ sanity -= 10

    jump arc4_scene3


# --- SCENE 3: REFLECTION ---
label arc4_scene3:
    hide stevia
    hide rangga
    hide ucup
    scene black with fade

    "Langkah kaki [nama_mc] sore ini menentukan ke mana arah hidupnya di sekolah baru ini. Akankah ia menjadi bagian dari mereka yang berkuasa, atau mereka yang bertahan dalam prinsip?"
    show mc neutral at center
    mc "Semua... baru saja dimulai."

    jump arc5_branch
