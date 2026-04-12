# ==========================================
# ARC 15: BREAKING POINT (KEPUTUSAN AKHIR)
# Cek Flag: took_package / cheated / emotional_bond
# Pilihan ini MENGUNCI ENDING secara permanen di ARC 16
# ==========================================

# --- SCENE 1: THE ROOFTOP CONFRONTATION ---
label arc15_scene1:
    scene bg_school_rooftop_storm with fade
    show rangga serious at left
    show stevia worried at right
    show mc sad at center

    "Suara guntur terdengar di kejauhan. Atap sekolah yang biasanya sepi kini terasa seperti medan perang yang menyesakkan. [nama_mc] berdiri di antara dua kutub yang selama ini menarik hidupnya."
    r "Gue denger guru-guru mulai nanya soal paket itu. Tapi lo nggak usah takut. Selama lo tetep sama gue, lo aman. Lo udah jadi bagian dari kita, [nama_mc]."
    s "[nama_mc], jangan dengerin dia! Aku tahu kamu tertekan, tapi ini bukan kamu yang sebenarnya. Aku... aku nggak kenal siapa kamu yang sekarang."

    jump arc15_scene2


# --- SCENE 2: GEMA MASA LALU (THE INTERNAL CALLBACK) ---
label arc15_scene2:
    "(Narasi Internal) Suara mereka terdengar seperti gema dari sekolah lamaku. Dulu, aku sendirian saat mereka menginjak-injak harga diriku. Sekarang... apa aku benar-benar ingin menjadi orang yang menginjak harga diri orang lain demi rasa aman?"
    show mc sad
    mc "(Melihat telapak tangannya sendiri) Aku hanya ingin... berhenti merasa takut."
    r "Kalau lo mau berhenti takut, lo harus jadi orang yang ditakuti. Sesimpel itu."
    show stevia worried
    s "Bukan dengan cara itu, [nama_mc]! Itu cuma bakal bikin kamu jadi monster yang dulu kamu benci!"

    jump arc15_scene3


# --- SCENE 3: THE BIG CHOICE (FINAL DECISION) ---
label arc15_scene3:
    "Ini adalah keputusan terakhirmu."

    menu:
        "Tetap Lanjut (Stay with Rangga)":
            $ final_path = "rangga"
            $ sanity -= 30

            show mc neutral
            mc "Aku sudah sejauh ini... tidak ada gunanya kembali sekarang. Aku tetap sama lo, Ngga."
            show rangga serious
            r "(Hanya mengangguk kecil) Pilihan cerdas. Jangan pernah nengok ke belakang lagi."
            show stevia disappointed
            "(Perlahan mundur dan pergi meninggalkan atap tanpa kata-kata)"
            hide stevia with moveoutright

        "Berhenti Sekarang (Choose Stevia)":
            $ final_path = "stevia"
            $ sanity += 20

            show mc sad
            mc "Aku nggak mau jadi seperti dulu... tapi aku juga nggak mau jadi monster. Gue berhenti, Ngga. Gue bakal tanggung jawab atas semuanya."
            show stevia worried
            s "(Mendekat dengan ragu tapi penuh harapan) Aku akan menemanimu, [nama_mc]. Kita hadapi ini bersama."
            show rangga annoyed
            r "Yaudah. Selamat jadi orang suci yang hancur sendirian. Jangan cari gue kalau lo butuh perlindungan nanti."
            hide rangga with moveoutleft

        "Diam (Passive/Normal Ending)":
            $ final_path = "isolation"
            $ sanity -= 10

            show mc neutral
            mc "(Hanya diam membisu, menatap lantai atap) Aku... aku tidak tahu. Tinggalkan aku sendiri."
            "Kamu membiarkan kesempatan ini berlalu. Rangga pergi dengan kesal, dan Stevia pergi dengan air mata."
            hide rangga with moveoutleft
            hide stevia with moveoutright

    jump arc15_scene4


# --- SCENE 4: THE BREAKING POINT ---
label arc15_scene4:
    hide rangga
    hide stevia
    scene bg_school_rooftop_storm with dissolve
    show mc neutral at center

    "Hujan akhirnya turun, membasahi seragam dan wajahmu. Kamu berdiri di sana, di antara kepingan hidupmu yang lama dan yang baru."
    mc "Inilah aku. Dengan segala retakan dan pilihanku."
    "(Narasi Internal) Apapun yang terjadi besok di ujian terakhir... semuanya sudah diputuskan hari ini."

    jump arc16_scene1
