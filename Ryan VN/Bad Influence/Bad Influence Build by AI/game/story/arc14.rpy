# ==========================================
# ARC 14: CRACKING MIND (THE MENTAL BREAKDOWN)
# Cek Flag: took_package / refused_package
# Cek Sanity: jika < 30, distorsi lebih parah
# ==========================================

# --- SCENE 1: THE DISTORTED REALITY ---
label arc14_scene1:
    scene bg_classroom_blurry with fade
    show mc anxious at center

    "Ruang kelas ini terasa asing. Suara pengawas ujian terdengar sangat jauh, seperti tersaring air. Detak jam dinding berubah menjadi dentuman yang memekakkan telinga."
    mc "(Memegang kepalanya, napas pendek-pendek)"
    "(Narasi Internal) Kenapa... kenapa semua orang menatapku? Apa mereka bisa melihat apa yang ada di pikiranku? Apa mereka tahu apa yang kulakukan semalam?"

    if sanity < 30:
        "Dunia di sekitarnya terasa semakin kabur. Wajah orang-orang di sekelilingnya melebur menjadi bayangan tanpa rupa."

    jump arc14_scene2


# --- SCENE 2: GEMA MASA LALU (THE CALLBACK) ---
label arc14_scene2:
    "Layar sesekali memberikan kilatan visual warna hitam putih."

    if took_package:
        "(Narasi Internal) Aku bukan lagi korban bullying. Aku sekarang... pelakunya. Kalau polisi datang ke sini, apa Nenek akan sanggup melihatku diborgol? Aku... aku kotor."
    elif refused_package:
        "(Narasi Internal) Rangga menatapku seolah aku adalah target berikutnya. Aku sendirian lagi. Tidak ada pelindung. Stevia... dia tidak akan bisa menghentikan Rangga kalau dia benar-benar marah. Aku akan hancur lagi."
    else:
        "(Narasi Internal) Pilihanku yang ragu-ragu... tidak membantuku. Aku tidak tahu ke mana seharusnya aku berpijak."

    show mc sad
    mc "Aku ingin pulang... aku ingin semua ini berhenti."

    jump arc14_scene3


# --- SCENE 3: QUIZ 4 (THE BREAKING POINT) ---
label arc14_scene3:
    hide mc
    "Kuis dimulai, tapi huruf-huruf di kertas ini seolah mencair dan merayap keluar dari lembaran."

    if sanity < 30:
        "Tombol pilihan jawaban sesekali menghilang atau berpindah posisi."
        "Teks soal bergetar hebat."
        mc "(Mencengkeram pulpen) Ayo... konsentrasi. Pilih saja satu. Apapun itu."
    else:
        "Kamu memaksakan dirimu untuk fokus, meski kepalamu terasa berat seperti batu."

    call quiz4_start

    jump arc14_scene4



# --- SCENE 4: THE SILENT COLLAPSE ---
label arc14_scene4:
    "Bel berakhirnya kuis berbunyi, tapi kamu tetap duduk di sana. Semua orang mulai keluar, tapi bagimu, waktu telah berhenti."
    show mc sad
    mc "(Menatap telapak tangan yang gemetar)"
    "(Narasi Internal) Aku sudah retak sejak lama. Dan sekarang... aku merasa kepingan-kepingan itu mulai jatuh satu per satu. Tidak ada lagi yang bisa menyelamatkanku, kecuali keputusanku sendiri."

    jump arc15_scene1
