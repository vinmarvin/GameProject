# ==========================================
# QUIZ 3 — PKN (Pendidikan Kewarganegaraan)
# Dipanggil dari: arc13 (sebelum scene paket malam)
# Mudah/Sedang: 5 soal, 60 detik
# Susah       : 7 soal, 30 detik
# ==========================================

init python:

    # ---- SOAL MUDAH — PKN ----
    _q3_easy = [
        {
            "q": "Lambang negara Indonesia adalah...",
            "c": [
                "A. Bendera Merah Putih",
                "B. Bhinneka Tunggal Ika",
                "C. Garuda Pancasila",
                "D. Burung Merpati"
            ],
            "a": 2
        },
        {
            "q": "Sila ke-3 Pancasila berbunyi...",
            "c": [
                "A. Kemanusiaan yang adil dan beradab",
                "B. Ketuhanan Yang Maha Esa",
                "C. Keadilan sosial bagi seluruh rakyat Indonesia",
                "D. Persatuan Indonesia"
            ],
            "a": 3
        },
        {
            "q": "UUD 1945 pertama kali disahkan pada tanggal...",
            "c": [
                "A. 17 Agustus 1945",
                "B. 22 Juni 1945",
                "C. 1 Juni 1945",
                "D. 18 Agustus 1945"
            ],
            "a": 3
        },
        {
            "q": "Hak warga negara yang tertuang dalam UUD 1945 pasal 28 adalah...",
            "c": [
                "A. Kewajiban membayar pajak",
                "B. Hak kebebasan berserikat, berkumpul, dan berpendapat",
                "C. Kewajiban membela negara",
                "D. Hak memperoleh pekerjaan layak"
            ],
            "a": 1
        },
        {
            "q": "Lembaga negara yang berwenang membuat undang-undang adalah...",
            "c": ["A. Presiden", "B. Mahkamah Agung", "C. MPR", "D. DPR"],
            "a": 3
        },
    ]

    _q3_easy_narr = [
        "Pak Guru PKN: 'Soal pertama sangat mendasar. Lambang negara kita yang gagah itu...'",
        "(Dalam hati) Maju mundur cantik... sila ke-3... ah, Persatuan Indonesia!",
        "(Dalam hati) UUD 1945 disahkan sehari setelah proklamasi, 18 Agustus 1945.",
        "Pak Guru PKN: 'Pasal 28 UUD 1945 itu sangat penting bagi kalian sebagai warga negara!'",
        "(Dalam hati) DPR, MPR, MA... yang membuat UU itu DPR. Aku yakin.",
    ]

    # ---- SOAL SEDANG — PKN ----
    _q3_medium = [
        {
            "q": "Yang dimaksud dengan kedaulatan rakyat dalam negara demokrasi adalah...",
            "c": [
                "A. Kekuasaan tertinggi ada di tangan presiden",
                "B. Kekuasaan dipegang sepenuhnya oleh DPR",
                "C. Rakyat memegang kekuasaan tertinggi dalam negara",
                "D. Kekuasaan dibagi antara pemerintah pusat dan militer"
            ],
            "a": 2
        },
        {
            "q": "Mahkamah Konstitusi (MK) berwenang untuk...",
            "c": [
                "A. Membuat undang-undang baru",
                "B. Menguji undang-undang terhadap UUD 1945",
                "C. Mengadili perkara pidana umum",
                "D. Mengangkat menteri kabinet"
            ],
            "a": 1
        },
        {
            "q": "HAM bersifat universal artinya...",
            "c": [
                "A. Berlaku hanya di negara maju",
                "B. Bergantung pada kebiasaan dan budaya setempat",
                "C. Hanya diakui oleh PBB dan negara anggotanya",
                "D. Berlaku bagi seluruh umat manusia di mana pun berada"
            ],
            "a": 3
        },
        {
            "q": "Sistem pemerintahan yang dianut Indonesia berdasarkan UUD 1945 adalah...",
            "c": [
                "A. Parlementer",
                "B. Monarki konstitusional",
                "C. Presidensial",
                "D. Federasi"
            ],
            "a": 2
        },
        {
            "q": "Pemilihan umum di Indonesia diselenggarakan secara rutin setiap...",
            "c": ["A. 3 tahun sekali", "B. 4 tahun sekali", "C. 6 tahun sekali", "D. 5 tahun sekali"],
            "a": 3
        },
    ]

    _q3_medium_narr = [
        "Pak Guru PKN: 'Demokrasi! Dari rakyat, oleh rakyat, untuk rakyat. Siapa yang pegang kuasa?'",
        "(Dalam hati) MK itu hakim konstitusi... mereka menguji UU, bukan membuat UU.",
        "Pak Guru PKN: 'Universal berarti berlaku di mana saja, tidak pilih-pilih negara!'",
        "(Dalam hati) Presidensial... presiden sebagai kepala negara sekaligus kepala pemerintahan.",
        "(Dalam hati) Pemilu 5 tahun sekali. Indonesia baru pemilu besar 2024 kemarin.",
    ]

    # ---- SOAL SUSAH — PKN (7 soal, 30 detik) ----
    _q3_hard = [
        {
            "q": "Amandemen UUD 1945 dilakukan sebanyak...",
            "c": ["A. 2 kali", "B. 3 kali", "C. 5 kali", "D. 4 kali"],
            "a": 3
        },
        {
            "q": "Pasal 33 UUD 1945 mengatur tentang...",
            "c": [
                "A. Hak asasi manusia",
                "B. Sistem pertahanan dan keamanan negara",
                "C. Perekonomian nasional dan kesejahteraan sosial",
                "D. Sistem pendidikan nasional"
            ],
            "a": 2
        },
        {
            "q": "Konvensi Hak Anak diratifikasi oleh Indonesia melalui...",
            "c": [
                "A. UU No. 23 Tahun 2002",
                "B. UU No. 39 Tahun 1999",
                "C. Keppres No. 36 Tahun 1990",
                "D. PP No. 54 Tahun 2007"
            ],
            "a": 2
        },
        {
            "q": "Semboyan 'Bhinneka Tunggal Ika' mengandung makna...",
            "c": [
                "A. Persatuan di atas perbedaan suku dan agama",
                "B. Keadilan sosial bagi seluruh rakyat",
                "C. Musyawarah untuk mencapai mufakat",
                "D. Berbeda-beda tetapi tetap satu jua"
            ],
            "a": 3
        },
        {
            "q": "Prinsip checks and balances dalam sistem pemerintahan Indonesia berarti...",
            "c": [
                "A. Kekuasaan eksekutif lebih tinggi dari legislatif",
                "B. Semua lembaga negara setara dalam pembuatan UU",
                "C. Presiden bertanggung jawab langsung kepada parlemen",
                "D. Kekuasaan antar-lembaga negara saling membatasi dan mengawasi"
            ],
            "a": 3
        },
        {
            "q": "Dasar hukum pembentukan Mahkamah Konstitusi RI adalah...",
            "c": [
                "A. UU No. 14 Tahun 1985",
                "B. UU No. 48 Tahun 2009",
                "C. Pasal 24C UUD 1945",
                "D. Tap MPR No. VI/MPR/2001"
            ],
            "a": 2
        },
        {
            "q": "Hak untuk mendapat pendidikan bagi setiap warga negara diatur dalam...",
            "c": [
                "A. Pasal 27 UUD 1945",
                "B. Pasal 33 UUD 1945",
                "C. Pasal 31 UUD 1945",
                "D. Pasal 28C UUD 1945"
            ],
            "a": 2
        },
    ]

    _q3_hard_narr = [
        "(Dalam hati) Amandemen UUD... 4 kali. Tahun 1999, 2000, 2001, 2002.",
        "Pak Guru PKN: 'Pasal 33! Hafal ini. Ini soal fundamental perekonomian negara!'",
        "(Dalam hati) Keppres No. 36 Tahun 1990... ini tentang konvensi hak anak.",
        "(Dalam hati) Bhinneka Tunggal Ika dari kakawin Sutasoma. Mpu Tantular.",
        "Pak Guru PKN: 'Checks and balances! Tidak ada lembaga yang boleh merajalela sendiri!'",
        "(Dalam hati) Pasal 24C UUD 1945... itu yang mengatur Mahkamah Konstitusi.",
        "(Dalam hati) Hak pendidikan... Pasal 31 UUD 1945. Saya pernah baca ini!",
    ]


# ==========================================
# LABEL UTAMA QUIZ 3
# ==========================================

label quiz3_start:
    $ _quiz_reset()

    if sanity >= 55:
        $ _q3_qs    = _q3_easy
        $ _q3_narr  = _q3_easy_narr
        $ _q3_time  = 60
        $ _q3_name  = "Kuis PKN"
    elif sanity >= 30:
        $ _q3_qs    = _q3_medium
        $ _q3_narr  = _q3_medium_narr
        $ _q3_time  = 60
        $ _q3_name  = "Kuis PKN"
    else:
        $ _q3_qs    = _q3_hard
        $ _q3_narr  = _q3_hard_narr
        $ _q3_time  = 30
        $ _q3_name  = "Kuis PKN — Tingkat Lanjut"

    call screen quiz_screen(_q3_name, _q3_qs, _q3_time, _q3_narr)

    $ (_q3_c, _q3_t, _q3_pct) = _quiz_get_result()
    $ quiz3_score = _q3_pct

    # Update stats silently
    if _q3_pct >= 80:
        $ sanity += 5
        $ quiz_passed = True
    elif _q3_pct < 50:
        $ sanity -= 5
        $ quiz_passed = False
    else:
        $ quiz_passed = True

    "Kuis PKN selesai. Pak Guru mengumpulkan lembar jawaban."
    "(Narasi Internal) Entah berapa yang kujawab benar. Sekarang hanya menunggu."

    return
