# ==========================================
# ARC 6: THE FIRST TEST
# Quiz 1 — Geografi
# ==========================================

# --- SCENE 1: PENGUMUMAN KUIS ---
label arc6_scene1:
    scene bg_classroom_morning with fade
    show mc neutral at center
    show pg neutral at center with fade

    pg "Baik, anak-anak. Sebelum kita lanjutkan materi, hari ini ada kuis singkat tentang Geografi."
    pg "Persiapkan diri kalian. Kuis dimulai sekarang!"

    hide pg with dissolve

    jump arc6_scene2


# --- SCENE 2: KUIS GEOGRAFI ---
label arc6_scene2:
    hide mc

    "Kertas soal mulai beredar. [nama_mc] menatap lembar pertanyaan itu dengan pandangan kosong."
    mc "(Dalam hati) Oke... geografi. Aku bisa ini."

    call quiz1_start

    # Setelah kuis selesai
    scene bg_classroom_morning with fade
    show mc neutral at center

    if quiz_passed:
        show pg neutral at center with dissolve
        pg "Waktunya habis. Kumpulkan lembar jawaban kalian."
        hide pg with dissolve
        mc "(Dalam hati) Semoga nilainya cukup. Aku sudah berusaha."
    else:
        show mc sad
        mc "(Dalam hati) Gagal... aku masih tidak bisa fokus di sini."

    jump arc7_scene1
