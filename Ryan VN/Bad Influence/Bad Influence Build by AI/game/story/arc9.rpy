# ==========================================
# ARC 9: THE DIVERGING PATHS (GOOD VS BAD ROUTE)
# ==========================================

# Router — pilih jalur
label arc9_branch:
    if bad_route_lock or rely_on_rangga:
        jump arc9b_scene1
    else:
        jump arc9a_scene1


# ==========================================
# JALUR A: THE SHARED SCAR (GOOD PATH)
# ==========================================

label arc9a_scene1:
    # SCENE 1: KEHENINGAN YANG MENYESAKKAN
    scene bg_stevia_living_room_evening with fade
    show stevia worried at right
    show mc neutral at left

    s "(Menatap buku Matematika dengan kosong) Persamaan logaritma ini... kalau basisnya sudah salah dari awal, hasilnya nggak akan pernah bisa presisi, kan?"
    mc "Hah? Oh, iya. Kayaknya aku salah masukin variabel di baris ketiga."
    "Cahaya sore yang hangat menyapu ruangan, tapi udara di sekeliling terasa membeku. Stevia tiba-tiba berhenti menulis dan mencengkeram lutut kirinya."

    jump arc9a_scene2


label arc9a_scene2:
    # SCENE 2: BREAKING POINT (ANALOGI RETAK)
    show stevia disappointed

    s "(Menatap kakinya dengan pandangan dingin) Tadi siang Rangga bilang langkahku berisik. Dia benar. Aku itu... barang gagal yang dipaksa tetap jalan."
    show mc sad
    mc "Stev..."
    s "Dulu di tangga SMP, aku yang ceroboh. Aku biarkan mereka punya kesempatan buat ngerusak hidupku. Dan sekarang... aku punya jeda yang nggak bisa hilang."
    "Dia bicara seolah-olah dia adalah mesin yang malfungsi, bukan manusia yang sengaja dihancurkan oleh orang lain."

    jump arc9a_scene3


label arc9a_scene3:
    # SCENE 3: CHOICE #4A (KONEKSI EMOSIONAL)
    menu:
        "Terbuka (Shared Trauma)":
            $ friendship_stevia += 20
            $ sanity += 10
            $ emotional_bond = True

            show mc sad
            mc "Aku punya cermin tua yang retak di rumah. Kelihatannya utuh dari jauh, tapi kalau kamu mendekat, pantulannya nggak akan pernah lurus lagi. Aku pindah ke sini... karena aku juga 'retak', Stev."
            show stevia calm
            s "(Menoleh perlahan dengan mata lelah) [nama_mc]... jadi kamu juga?"
            "Suasana menjadi sangat melankolis dan intim."

        "Menghindar (Self-Protection)":
            $ sanity -= 3

            show mc anxious
            mc "(Menutup buku dengan keras) Anu... Stev, kayaknya kita harus fokus ke tugas ini sekarang. Waktunya nggak banyak."
            show stevia disappointed
            s "Oh. Iya. Kamu benar. Kita di sini buat belajar, bukan bahas hal nggak logis."
            "Tembok pertahanan Stevia kembali naik dengan cepat."

    jump arc10_scene0


# ==========================================
# JALUR B: THE POISONED TRUST (BAD PATH)
# ==========================================

label arc9b_scene1:
    # SCENE 1: VALIDASI SANG PEMIMPIN
    scene bg_warung_jago_night with fade
    show rangga smirk at center
    show ucup neutral at right
    show mc neutral at left

    r "Gue nggak nyangka lo bakal berani ngomong gitu ke Stevia tadi siang. Padahal gue udah siap-siap mau 'nyikat' lo kalau lo ikutan sok suci."
    mc "Gue cuma nggak suka cara dia ngatur-ngatur."
    r "(Merangkul [nama_mc]) Lo tahu kenapa gue suka lo? Karena lo nggak munafik. Lo tahu dunia ini nggak adil, dan lo nggak berusaha jadi pahlawan kesiangan. Kita itu sama, [nama_mc]."

    jump arc9b_scene2


label arc9b_scene2:
    # SCENE 2: TAWARAN BERBAHAYA
    u "(Menaruh amplop cokelat tebal di meja) Nih, Ngga. Titipan dari 'Abang' buat dikirim besok. Tapi jalur biasa lagi dijaga ketat."
    show rangga serious
    r "(Menatap [nama_mc] dengan tajam) Gue butuh seseorang yang mukanya nggak dicurigai. Seseorang yang kelihatan 'alim' tapi punya nyali. Kira-kira... lo orangnya bukan, [nama_mc]?"
    show mc anxious
    mc "(Menatap amplop itu dengan ragu)"

    jump arc9b_scene3


label arc9b_scene3:
    # SCENE 3: CHOICE #4B (LOUTH VS DOUBT)
    menu:
        "Terima (Accept The Package)":
            $ friendship_rangga += 10
            $ sanity -= 10
            $ took_package = True

            show mc neutral
            mc "Gue ambil. Gue bakal buktiin kalau gue bisa diandelin."
            show rangga smirk
            r "(Tertawa lebar) Mantap! Itu baru temen gue. Besok kita bakal seneng-seneng!"
            "[nama_mc] merasa 'diterima', meski ada rasa takut yang dalam."

        "Ragu (Start To Doubt)":
            $ friendship_rangga -= 5
            $ sanity -= 3
            $ refused_package = True

            show mc anxious
            mc "Gue pengen bantu, tapi kalau ini soal barang ilegal... gue takut malah ngerusak posisi lo juga."
            show rangga annoyed
            r "(Melepaskan rangkulan) Gue nggak punya banyak waktu, [nama_mc]. Gue kira lo beda. Ternyata lo cuma mau perlindungan gue tanpa mau repot."
            "Suasana di markas seketika menjadi dingin dan mencekam."

    jump arc9b_scene4


label arc9b_scene4:
    # SCENE AKHIR: REFLEKSI MALAM
    hide rangga
    hide ucup
    scene bg_mc_room_night with fade
    show mc sad at center

    "Malam itu, [nama_mc] menatap bayangannya di kegelapan. Ada sesuatu yang hilang, entah itu ketenangannya atau sebagian dari jiwanya yang ia tinggalkan di sekolah."
    mc "Besok ujian dimulai... tapi kenapa rasanya aku sudah gagal bahkan sebelum mengerjakannya?"

    jump arc10_scene0
