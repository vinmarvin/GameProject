# ==========================================
# ARC 10: THE CROSSROADS OF PRESSURE (UTS)
# ==========================================

# --- SCENE 0: UTS BERLANGSUNG ---
label arc10_scene0:
    scene bg_classroom_morning with fade
    show mc neutral at center
    show pg neutral at center with fade

    pg "Ujian Tengah Semester dimulai sekarang. Tidak ada suara, tidak ada kecurangan."
    pg "Waktu kalian terbatas. Gunakan sebaik mungkin!"

    hide pg with dissolve
    hide mc

    call quiz2_start

    jump arc10_scene1


# --- SCENE 1: THE SILENT PRESSURE ---
label arc10_scene1:
    scene bg_classroom_morning with dissolve
    show mc anxious at center

    "Ruang kelas yang biasanya bising kini terasa mencekam. Bau kertas ujian yang baru dicetak memenuhi udara. Hanya ada suara detak jam dinding yang seolah berdetak di dalam kepala [nama_mc]."
    mc "(Menatap lembar soal yang masih terbalik) Ayo... konsentrasi. Ini cuma ujian. Jangan biarkan tanganmu gemetar."
    "(Narasi Internal) Aku bisa merasakan mata pengawas ujian yang berkeliling. Kenapa setiap pasang mata di sini seolah sedang menungguku untuk melakukan kesalahan?"

    jump arc10_scene2



# --- SCENE 2: PATH DIVERGENCE (VISUALS) ---
label arc10_scene2:
    if stevia_route_lock or trust_stevia or emotional_bond:
        # BRANCH A — Jalur Stevia
        show stevia calm at right
        "(Stevia menoleh sekilas ke arah [nama_mc] sebelum ujian dimulai)"
        s "(Tanpa suara, hanya mengangguk kecil memberikan semangat)"
        show mc neutral
        "(Mengambil napas panjang, pandangan mata menjadi lebih fokus)"
        "(Narasi Internal) Mengingat catatan Stevia semalam membantuku. Tulisannya rapi, seolah dia sedang membimbingku langsung dari setiap baris jawaban ini."
        hide stevia
    else:
        # BRANCH B — Jalur Rangga
        show rangga smirk at right
        "(Rangga duduk tepat di belakang [nama_mc])"
        r "(Menendang pelan kaki kursi [nama_mc])"
        show mc anxious
        "(Memijat pelipis, pandangan tidak stabil)"
        "(Narasi Internal) Kepalaku berdenyut. Suara tawa di markas semalam masih terngiang. Barisan huruf di lembar soal ini seolah mencair dan lari dari mataku. Aku tidak bisa fokus."
        hide rangga

    jump arc10_scene3


# --- SCENE 3: THE CRITICAL CHOICE (THE CHEAT NOTE) ---
label arc10_scene3:
    show mc anxious at center

    "Jam menunjukkan sepuluh menit terakhir. Separuh lembar jawabanmu masih kosong. Rangga baru saja menjatuhkan 'bantuan' tepat di bawah mejamu."

    menu:
        "Ambil Contekan (Accept Help)":
            $ sanity -= 10
            $ cheated = True
            $ took_cheat = True

            show mc neutral
            "(Mengambil kertas dengan gerakan cepat dan menyembunyikannya di bawah telapak tangan)"
            "(Narasi Internal) Persetan dengan integritas. Aku hanya ingin ini semua berakhir. Aku tidak mau terlihat bodoh lagi."
            "Layar sesekali berkedip merah—simbol rasa bersalah dan paranoia."

        "Berusaha Sendiri (Honest Struggle)":
            $ sanity += 3
            $ honest_effort = True

            show mc anxious
            "(Menyingkirkan kertas itu dengan ujung kaki dan kembali menatap soal)"
            "(Narasi Internal) Tidak. Sekali aku memulai ini, aku tidak akan pernah bisa berhenti. Aku harus melakukannya dengan caraku sendiri."
            show mc sad

        "Menyerah (Give Up)":
            $ sanity -= 8

            show mc sad
            "(Meletakkan pulpen dan menutup lembar jawaban dengan pasrah)"
            "(Narasi Internal) Mungkin aku memang tidak pernah berubah. Aku masih anak malang yang tidak tahu apa-apa."
            "[nama_mc] hanya menatap jendela sampai bel berbunyi."

    jump arc10_scene4


# --- SCENE 4: AFTERMATH ---
label arc10_scene4:
    scene bg_school_hallway_noon with fade
    show mc neutral at center

    if cheated:
        show rangga smirk at left
        r "(Melewati [nama_mc] dan menepuk bahunya dengan penuh kemenangan)"
        hide rangga with moveoutleft
    elif honest_effort:
        show stevia calm at right
        s "(Menunggu di depan kelas dengan raut wajah penuh harap)"

    show mc sad
    mc "(Berjalan menjauh dari kerumunan)"
    "Ujian berakhir, tapi beban di dada [nama_mc] justru terasa semakin berat. Nilai di atas kertas mungkin bisa diperbaiki, tapi garis moral yang baru saja ia sentuh... tidak akan pernah sama lagi."

    hide stevia
    hide rangga

    jump arc11_scene1
