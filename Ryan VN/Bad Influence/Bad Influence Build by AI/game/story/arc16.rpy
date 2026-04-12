# ==========================================
# ARC 16: UAS + ENDING (RESOLUSI)
# Cek Flag: final_path (stevia / rangga / isolation)
# ==========================================

# --- SCENE 1: THE FINAL EXAM (UAS) ---
label arc16_scene1:
    if final_path == "stevia":
        scene bg_classroom_morning with fade
    else:
        scene bg_classroom_morning with fade

    show mc neutral at center
    show pg neutral at center with fade

    pg "Ini adalah Ujian Akhir Semester. Gunakan semua yang telah kalian pelajari."
    pg "Waktu dimulai sekarang!"

    hide pg with dissolve

    "Hari terakhir ujian. Ruang kelas terasa begitu tenang, seolah memberikan ruang bagi [nama_mc] untuk menyelesaikan apa yang telah ia mulai."
    mc "(Menarik napas panjang, lalu mulai menulis)"
    "(Narasi Internal) Inilah akhirnya. Semua pilihan, semua pertengkaran, dan semua ketakutan membawaku ke titik ini."

    hide mc

    call quiz5_start

    scene bg_classroom_morning with dissolve
    show mc neutral at center

    if quiz5_score >= 80:
        mc "(Menarik napas lega) Aku berhasil menyelesaikannya."
    elif quiz5_score >= 50:
        mc "(Menatap kertas jawaban) Lumayan... setidaknya aku mencoba."
    else:
        show mc sad
        mc "(Meletakkan pulpen) Sudahlah..."

    hide mc
    scene black with fade

    if final_path == "stevia":
        jump arc16_good_ending
    elif final_path == "rangga":
        jump arc16_bad_ending
    else:
        jump arc16_normal_ending



# ==========================================
# GOOD ENDING — JALUR PEMULIHAN
# Kondisi: final_path == "stevia"
# ==========================================

label arc16_good_ending:
    scene bg_school_gate_afternoon with fade
    show stevia calm at right
    show mc neutral at left

    s "Nilai UAS sudah keluar. Kamu berhasil, [nama_mc]. Kamu benar-benar melampaui ekspektasiku."
    mc "(Tersenyum tipis) Terima kasih, Stev. Kalau bukan karena kamu yang terus menarikku, mungkin aku sudah hilang arah."
    s "Kita semua punya retakan, [nama_mc]. Tapi retakan itulah yang membiarkan cahaya masuk. Ayo, Nenekmu pasti sudah menunggu di rumah."
    hide stevia
    "(Narasi Internal) Aku berjalan keluar gerbang sekolah dengan kepala tegak. Aku bukan lagi 'si korban' yang melarikan diri. Aku adalah [nama_mc], yang akhirnya berani menghadapi dunianya sendiri."

    jump arc16_credits


# ==========================================
# BAD ENDING — JALUR KEHANCURAN
# Kondisi: final_path == "rangga"
# ==========================================

label arc16_bad_ending:
    scene bg_warung_jago_night with fade
    show rangga smirk at center
    show mc neutral at left

    r "Gue dengar nilai lo berantakan. Tapi tenang saja, di sini lo nggak butuh angka merah itu buat dihormati."
    mc "(Menatap jalanan dengan pandangan kosong) Ya. Sekolah itu cuma tempat buat orang-orang yang nggak punya nyali."
    r "Nah, gitu dong. Besok ada paket lagi yang harus jalan. Inget, lo sekarang tangan kanan gue."
    "[nama_mc] tertawa kecil, tapi suaranya terdengar hampa. Ia merasa berkuasa, namun jauh di dalam dadanya, ia tahu ia telah menjadi monster yang dulu paling ia takuti. Tidak ada jalan pulang."

    jump arc16_credits


# ==========================================
# NORMAL ENDING — JALUR KESEPIAN
# Kondisi: final_path == "isolation"
# ==========================================

label arc16_normal_ending:
    scene bg_bus_stop_sunset with fade
    show mc neutral at center

    "Semua orang sudah pulang. Stevia lewat tanpa bicara, dan Rangga melaju dengan motornya tanpa menoleh."
    mc "(Melihat teman-teman lain tertawa di seberang jalan)"
    "(Narasi Internal) Aku selamat. Aku tidak dikeluarkan, aku tidak dipenjara. Tapi duniaku tetap berwarna abu-abu. Aku pindah untuk mencari teman, tapi aku berakhir di halte ini... sendirian lagi."
    "Bus datang, dan [nama_mc] naik ke dalamnya, menghilang di tengah keramaian kota yang tidak pernah benar-benar mengenalnya."

    jump arc16_credits


# ==========================================
# CREDIT TITLE
# ==========================================

label arc16_credits:
    hide mc
    scene bg_black with fade
    pause 1.5
    "Setiap pilihan memiliki harga."
    pause 0.5
    "Dan kamu telah membayarnya."
    pause 1.5

    return
