# ==========================================
# ARC 5: THE FIRST TEMPTATION
# Cek Flag: join_rangga / trust_stevia / uncertain
# Menentukan: took_smoke / refused_init / emotional_bond
# ==========================================

# --- BRANCH: Tentukan alur arc5 berdasarkan pilihan arc3/4 ---
label arc5_branch:
    if join_rangga:
        jump arc5_rangga_path
    elif trust_stevia:
        jump arc5_stevia_path
    else:
        jump arc5_alone_path


# ==========================================
# PATH A — Ikut Rangga (Penawaran di Warung)
# ==========================================

label arc5_rangga_path:
    scene bg_warung_jago_night with fade
    show rangga smirk at left
    show ucup neutral at right
    show mc neutral at center

    "Malam itu, [nama_mc] duduk di warung kaki lima bersama Rangga dan Ucup. Lampu jalan yang redup membuat suasana terasa lebih privat dari biasanya."
    r "Lo udah resmi bagian dari kita sekarang, [nama_mc]. Tapi ada satu hal yang harus lo lakuin dulu."
    u "(Mengeluarkan sebatang rokok dari saku jaket) Ini semacam... ritual penyambutan. Santai aja."

    jump arc5_scene_choice


# ==========================================
# PATH B — Bersama Stevia (Belajar di Rumah)
# ==========================================

label arc5_stevia_path:
    scene bg_classroom_morning with fade
    show stevia calm at right
    show mc neutral at left

    "Esok harinya, Stevia mendatangi [nama_mc] di kelas sebelum pelajaran dimulai."
    s "Aku tahu kemarin kamu pasti melihat Rangga dan Ucup di warung itu. Aku... khawatir."
    show mc anxious
    mc "Kamu tahu soal itu?"
    s "Satu sekolah ini tahu kebiasaan mereka. [nama_mc], aku mau tanya sesuatu yang mungkin terdengar aneh..."
    s "Kalau mereka pernah menawarkan sesuatu yang tidak baik... kamu akan menolak, kan?"

    show mc neutral
    "(Narasi Internal) Ada sesuatu di matanya. Bukan sekadar pertanyaan biasa. Mungkin dia pernah melihat hal ini terjadi pada orang lain sebelumnya."
    $ emotional_bond = True

    jump arc5_scene_choice_stevia


# ==========================================
# PATH C — Sendirian (Kebingungan)
# ==========================================

label arc5_alone_path:
    scene bg_street_night with fade
    show mc sad at center

    "Malam itu [nama_mc] berjalan pulang sendirian melewati gang yang sama setiap hari."
    "(Narasi Internal) Tidak bersama Rangga. Tidak bersama Stevia. Aku tidak punya siapa-siapa."
    "Di tikungan gang, [nama_mc] melihat sesosok bayangan melambai."
    show ucup neutral at right
    u "Eh, [nama_mc]! Sendirian? Mampir dulu, ada yang mau kita obrolin."

    show mc anxious
    mc "(Menatap Ucup dengan curiga) Obrolin apa?"
    u "(Mengeluarkan sebatang rokok, melemparkan satu ke arah [nama_mc]) Santai. Ini cuma tawaran."

    jump arc5_scene_choice


# ==========================================
# SCENE PILIHAN — Tawaran Rokok (Path A & C)
# ==========================================

label arc5_scene_choice:
    menu:
        "Terima (Took the Cigarette)":
            $ took_smoke = True
            $ sanity -= 8
            $ friendship_rangga += 5

            show mc neutral
            mc "(Mengambil rokok itu dengan tangan gemetar) Oke. Satu kali tidak akan bikin mati."
            show rangga smirk
            r "Nah! Gitu dong. Sekarang lo baru bisa dibilang orang kita."
            "(Narasi Internal) Rasanya pahit, tapi senyum mereka... membuat aku untuk sesaat merasa diterima."

        "Tolak (Refused)":
            $ refused_init = True
            $ sanity += 5
            $ friendship_rangga -= 5

            show mc anxious
            mc "Maaf... aku tidak mau. Ini bukan sesuatu yang aku mau coba."
            show rangga annoyed
            r "Hayah. Lo pikir lo lebih baik dari kita? Kalau begitu, jangan harap kita jaga punggung lo."
            hide rangga with moveoutleft
            hide ucup with moveoutright
            show mc sad
            "(Narasi Internal) Aku menolak. Tapi sekarang... aku sendirian lagi."

    jump arc5_ending


# ==========================================
# SCENE PILIHAN — Bersama Stevia (Path B)
# ==========================================

label arc5_scene_choice_stevia:
    menu:
        "Ya, aku pasti menolak (Reassure Stevia)":
            $ refused_init = True
            $ friendship_stevia += 8
            $ quiz_bonus = True

            show mc neutral
            mc "Tenang, Stev. Aku tidak akan melakukan hal seperti itu."
            show stevia calm
            s "(Tersenyum lega) Bagus. Kalau begitu... mau belajar bareng lagi malam ini? Kuis geografi besok penting."
            mc "Tentu. Aku butuh semua bantuan yang bisa kudapat."
            "(Narasi Internal) Malam itu kami belajar bersama sampai larut. Materi geografi terasa jauh lebih mudah dengan catatan Stevia di sampingku."

        "Aku tidak tahu... (Uncertain)":
            $ sanity -= 3

            show mc anxious
            mc "Jujur... aku tidak tahu. Situasinya tidak sesederhana yang kamu bayangkan, Stev."
            show stevia worried
            s "Aku mengerti. Tapi [nama_mc]... hati-hati saja. Aku tidak mau kehilangan teman baik."
            "(Narasi Internal) 'Teman baik.' Kata-kata itu terngiang di kepalaku sepanjang hari."

    jump arc5_ending


# ==========================================
# AKHIR ARC 5 — Menuju Quiz Geografi (Arc 6)
# ==========================================

label arc5_ending:
    hide stevia
    hide rangga
    hide ucup
    scene black with fade

    if took_smoke:
        "(Narasi Internal) Pagi ini aku bangun dengan rasa pahit yang masih ada di lidah. Bukan hanya rokok itu... tapi pilihan yang kuambil semalam."
    elif refused_init:
        "(Narasi Internal) Aku menolak. Dan entah kenapa, tidurku malam itu justru lebih nyenyak dari biasanya."
    else:
        "(Narasi Internal) Besok ada kuis geografi. Aku bahkan belum membuka buku."

    if quiz_bonus:
        "(Narasi Internal) Catatan Stevia memenuhi mejaku. Aku siap."

    jump arc6_scene1
