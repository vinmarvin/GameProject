# ==========================================
# QUIZ 5 — UAS : MATEMATIKA + BAHASA INDONESIA
# Dipanggil dari: arc16_scene1
# Urutan     : Matematika dulu, baru B.Indonesia (tidak diacak)
# Mudah/Sedang : 10 soal (5+5), 120 detik
# Susah        : 15 soal (7+8), 90 detik
#
# CATATAN: Semua simbol matematika dalam format ASCII
# (^2 = kuadrat, ^3 = kubik, * = kali, - = minus)
# ==========================================

init python:

    # ========================================
    # SOAL MUDAH
    # ========================================

    _q5_easy_math = [
        {
            "q": "Tentukan suku ke-10 dari barisan:\n2, 5, 8, 11, ...",
            "c": ["A. 26", "B. 32", "C. 35", "D. 29"],
            "a": 3
        },
        {
            "q": "Barisan: 1, 4, 9, 16, 25, ...\nSuku ke-7 adalah...",
            "c": ["A. 36", "B. 64", "C. 42", "D. 49"],
            "a": 3
        },
        {
            "q": "Sebuah dadu dilempar sekali.\nPeluang munculnya angka genap adalah...",
            "c": ["A. 1/6", "B. 2/3", "C. 1/3", "D. 1/2"],
            "a": 3
        },
        {
            "q": "Diketahui:\n  2x + y = 10\n  x + y  = 7\nNilai x adalah...",
            "c": ["A. 1", "B. 4", "C. 3", "D. 7"],
            "a": 2
        },
        {
            "q": "Modal Rp150.000, harga jual Rp180.000.\nPersentase keuntungan adalah...",
            "c": ["A. 15%", "B. 25%", "C. 30%", "D. 20%"],
            "a": 3
        },
    ]

    _q5_easy_indo = [
        {
            "q": "Kalimat yang mengandung majas metafora adalah...",
            "c": [
                "A. Hujan membasahi seluruh bumi.",
                "B. Adik menangis keras sekali.",
                "C. Dia berlari secepat angin.",
                "D. Dia adalah singa di medan pertempuran."
            ],
            "a": 3
        },
        {
            "q": "Yang dimaksud dengan 'diksi' dalam penulisan adalah...",
            "c": [
                "A. Cara penempatan tanda baca",
                "B. Penggunaan huruf kapital yang tepat",
                "C. Pilihan kata yang tepat dan sesuai konteks",
                "D. Struktur kalimat yang benar"
            ],
            "a": 2
        },
        {
            "q": "Ciri utama teks narasi adalah...",
            "c": [
                "A. Berisi pendapat dan argumen penulis",
                "B. Menceritakan peristiwa secara kronologis",
                "C. Menjelaskan langkah-langkah suatu proses",
                "D. Membujuk pembaca untuk bertindak"
            ],
            "a": 1
        },
        {
            "q": "Kalimat efektif harus memenuhi syarat...",
            "c": [
                "A. Panjang dan berbunga-bunga",
                "B. Menggunakan banyak sinonim",
                "C. Singkat, jelas, dan tepat sasaran",
                "D. Bersifat kiasan dan puitis"
            ],
            "a": 2
        },
        {
            "q": "Makna peribahasa 'Ada gula ada semut' adalah...",
            "c": [
                "A. Semut selalu mencari gula di mana saja",
                "B. Gula adalah makanan favorit semut",
                "C. Di mana ada keuntungan, banyak orang berdatangan",
                "D. Jika ada makanan maka akan ada hama"
            ],
            "a": 2
        },
    ]

    _q5_easy = _q5_easy_math + _q5_easy_indo

    _q5_easy_narr = [
        "(Dalam hati) Barisan aritmatika... beda = 3, suku ke-10 = 2 + 9*3 = 29.",
        "(Dalam hati) Pola kuadrat: 1^2, 2^2, 3^2... suku ke-7 = 7^2 = 49!",
        "(Dalam hati) Dadu: 2, 4, 6. Tiga angka genap dari 6. Peluang = 3/6 = 1/2.",
        "(Dalam hati) SPLDV... eliminasi y: x = 10 - 7 = 3.",
        "(Dalam hati) Untung = 30.000. Persen = 30/150 * 100 persen = 20 persen.",
        "Pak Guru: 'Majas metafora itu perbandingan langsung, tanpa kata seperti. Ingat!'",
        "(Dalam hati) Diksi... pemilihan kata. Aku ingat ini dari pelajaran menulis puisi.",
        "Pak Guru: 'Narasi itu bercerita, kronologis. Berbeda dari deskripsi atau argumentasi.'",
        "(Dalam hati) Kalimat efektif: singkat, jelas, tidak bertele-tele. Prinsip menulis!",
        "(Dalam hati) Ada gula ada semut... keuntungan menarik banyak pihak.",
    ]

    # ========================================
    # SOAL SEDANG
    # ========================================

    _q5_medium_math = [
        {
            "q": "Nilai dari 2^3 * 2^4 adalah...",
            "c": ["A. 2^6", "B. 4^7", "C. 2^12", "D. 2^7"],
            "a": 3
        },
        {
            "q": "Bentuk sederhana dari (3^2)^3 adalah...",
            "c": ["A. 3^5", "B. 3^8", "C. 9^3", "D. 3^6"],
            "a": 3
        },
        {
            "q": "Harga 2 buku dan 3 pensil = Rp13.000.\nHarga 3 buku dan 2 pensil = Rp12.000.\nHarga 1 pensil adalah...",
            "c": ["A. Rp1.500", "B. Rp3.000", "C. Rp2.000", "D. Rp4.000"],
            "a": 1
        },
        {
            "q": "Diketahui:\n  3x - 2y = 4\n  x  + y  = 3\nNilai 2x + y adalah...",
            "c": ["A. 4", "B. 7", "C. 6", "D. 5"],
            "a": 3
        },
        {
            "q": "Kelompok: 15 laki-laki dan 10 perempuan.\nSatu orang dipilih acak.\nPeluang terpilihnya perempuan adalah...",
            "c": ["A. 1/5", "B. 1/3", "C. 3/5", "D. 2/5"],
            "a": 3
        },
    ]

    _q5_medium_indo = [
        {
            "q": "Perbedaan teks argumentasi dan persuasi terletak pada...",
            "c": [
                "A. Tidak ada perbedaan, keduanya sama",
                "B. Argumentasi lebih pendek dari persuasi",
                "C. Argumentasi paparkan fakta; persuasi dorong tindakan pembaca",
                "D. Persuasi lebih ilmiah dan objektif"
            ],
            "a": 2
        },
        {
            "q": "Konjungsi antarparagraf yang tepat adalah...",
            "c": [
                "A. Dan, atau, tetapi",
                "B. Kemudian, lalu, setelah",
                "C. Karena, sebab, sehingga",
                "D. Selain itu, dengan demikian, oleh karena itu"
            ],
            "a": 3
        },
        {
            "q": "Dalam teks eksposisi, bagian tesis berisi...",
            "c": [
                "A. Simpulan dari argumen yang disampaikan",
                "B. Data dan fakta pendukung",
                "C. Langkah-langkah pemecahan masalah",
                "D. Pernyataan umum yang menjadi dasar tulisan"
            ],
            "a": 3
        },
        {
            "q": "Ciri kebahasaan teks laporan hasil observasi adalah...",
            "c": [
                "A. Kalimat perintah dan ungkapan saran",
                "B. Kalimat retoris dan metafora",
                "C. Kalimat pengandaian dan harapan",
                "D. Kalimat definisi dan klasifikasi"
            ],
            "a": 3
        },
        {
            "q": "Kata 'antara' dalam 'Pilihlah antara dua hal ini'\nberfungsi sebagai...",
            "c": [
                "A. Kata sifat",
                "B. Kata sambung (konjungsi)",
                "C. Kata kerja",
                "D. Kata depan (preposisi)"
            ],
            "a": 3
        },
    ]

    _q5_medium = _q5_medium_math + _q5_medium_indo

    _q5_medium_narr = [
        "(Dalam hati) Pangkat: 2^3 * 2^4 = 2^(3+4) = 2^7. Sifat perkalian pangkat sejenis.",
        "(Dalam hati) Pangkat dari pangkat: (3^2)^3 = 3^(2*3) = 3^6.",
        "(Dalam hati) SPLDV... eliminasi... b=2000, p=3000. Harga 1 pensil = Rp3.000.",
        "(Dalam hati) Substitusi: x=2, y=1... lalu 2x+y = 4+1 = 5.",
        "(Dalam hati) Peluang = 10 dibagi (15+10) = 10/25 = 2/5.",
        "Pak Guru: 'Argumentasi itu bicara fakta. Persuasi itu mengajak bertindak!'",
        "(Dalam hati) Konjungsi antarparagraf... 'selain itu', 'oleh karena itu'.",
        "(Dalam hati) Tesis di eksposisi... pernyataan umum di awal. Baru dibuktikan.",
        "(Dalam hati) Laporan observasi = kalimat definisi. 'X adalah...', 'X merupakan...'",
        "(Dalam hati) 'Antara dua hal' - kata depan. Preposisi.",
    ]

    # ========================================
    # SOAL SUSAH (7 MTK + 8 B.Indo = 15)
    # Format matematika: ASCII-safe, tanpa simbol Unicode yang mungkin tidak dirender
    # ========================================

    _q5_hard_math = [
        {
            "q": "Suku banyak P(x) = x^3 - 3x^2 + 2x - 1.\nNilai P(3) adalah...",
            "c": ["A. 3", "B. 6", "C. 9", "D. 5"],
            "a": 3
        },
        {
            "q": "Sisa pembagian f(x) = 2x^3 + x^2 - 3x + 1\ndibagi (x - 2) menurut Teorema Sisa adalah...",
            "c": ["A. 11", "B. 13", "C. 17", "D. 15"],
            "a": 3
        },
        {
            "q": "Dari 5 kartu bernomor 1-5, diambil 2 sekaligus.\nPeluang terambilnya dua kartu ganjil adalah...",
            "c": ["A. 1/5", "B. 2/5", "C. 3/10", "D. 1/2"],
            "a": 2
        },
        {
            "q": "Matriks A =\n  baris 1 : (1  2)\n  baris 2 : (3  4)\nNilai det(A) adalah...",
            "c": ["A. 2", "B. 10", "C. -4", "D. -2"],
            "a": 3
        },
        {
            "q": "sin 30 * cos 60 + cos 30 * sin 60 = ...",
            "c": ["A. 0", "B. 1/2", "C. akar(3)/2", "D. 1"],
            "a": 3
        },
        {
            "q": "Nilai tan 45 + sin 90 adalah...",
            "c": ["A. 1", "B. akar(2)", "C. 2", "D. 2*akar(2)"],
            "a": 2
        },
        {
            "q": "Matriks A =\n  baris 1 : (2  1)\n  baris 2 : (5  3)\ndet(A) = 1.\nElemen baris-1 kolom-1 dari A^(-1) adalah...",
            "c": ["A. 2", "B. -5", "C. 3", "D. -1"],
            "a": 2
        },
    ]

    _q5_hard_indo = [
        {
            "q": "Intertekstualitas dalam kajian sastra merujuk pada...",
            "c": [
                "A. Kajian gaya bahasa individual pengarang",
                "B. Teknik menulis yang tidak mengacu karya lain",
                "C. Analisis kronologis karya sastra",
                "D. Hubungan suatu teks dengan teks lain yang mempengaruhinya"
            ],
            "a": 3
        },
        {
            "q": "Fungsi kalimat topik dalam sebuah paragraf adalah...",
            "c": [
                "A. Menyimpulkan seluruh isi paragraf",
                "B. Memberikan contoh dari gagasan penjelas",
                "C. Menghubungkan paragraf berikutnya",
                "D. Menyatakan gagasan utama yang dikembangkan"
            ],
            "a": 3
        },
        {
            "q": "Gaya penulisan 'in medias res' berarti...",
            "c": [
                "A. Cerita dimulai dari awal kronologis",
                "B. Cerita menggunakan alur mundur sepenuhnya",
                "C. Cerita dari sudut pandang antagonis",
                "D. Cerita dimulai dari tengah atau puncak konflik"
            ],
            "a": 3
        },
        {
            "q": "Kohesi dalam wacana mengacu pada...",
            "c": [
                "A. Keserasian makna antarkalimat",
                "B. Gaya bahasa yang konsisten",
                "C. Kesesuaian wacana dengan konteks sosial",
                "D. Penggunaan alat gramatikal yang menghubungkan kalimat"
            ],
            "a": 3
        },
        {
            "q": "Perbedaan denotasi dan konotasi adalah...",
            "c": [
                "A. Denotasi = makna kiasan, konotasi = makna harfiah",
                "B. Keduanya merujuk makna yang sama",
                "C. Denotasi untuk puisi, konotasi untuk prosa",
                "D. Denotasi = makna kamus; konotasi = makna asosiasi tambahan"
            ],
            "a": 3
        },
        {
            "q": "Teknik flashback dalam prosa fiksi berfungsi untuk...",
            "c": [
                "A. Memperkenalkan karakter baru tiba-tiba",
                "B. Mempercepat alur ke masa depan",
                "C. Menyisipkan informasi masa lalu yang relevan",
                "D. Mengakhiri cerita dengan resolusi mengejutkan"
            ],
            "a": 2
        },
        {
            "q": "Struktur teks ulasan (resensi) yang lengkap adalah...",
            "c": [
                "A. Judul, orientasi, penilaian, simpulan",
                "B. Abstrak, pendahuluan, isi, penutup",
                "C. Tesis, argumentasi, penegasan ulang",
                "D. Identitas karya, sinopsis, analisis, evaluasi"
            ],
            "a": 3
        },
        {
            "q": "Fungsi paragraf deskriptif dalam sebuah esai adalah...",
            "c": [
                "A. Memaparkan argumen secara logis dengan bukti",
                "B. Menyajikan perbandingan antara dua hal",
                "C. Menggambarkan objek atau peristiwa secara rinci",
                "D. Meyakinkan pembaca tentang kebenaran suatu pernyataan"
            ],
            "a": 2
        },
    ]

    _q5_hard = _q5_hard_math + _q5_hard_indo

    _q5_hard_narr = [
        "(Dalam hati) P(3) = 3^3 - 3*(3^2) + 2*3 - 1 = 27 - 27 + 6 - 1 = 5.",
        "(Dalam hati) Teorema Sisa: f(2) = 2*(2^3) + 2^2 - 3*2 + 1 = 16+4-6+1 = 15.",
        "(Dalam hati) Kartu ganjil ada 3 buah. C(3,2) = 3. Total C(5,2) = 10. P = 3/10.",
        "(Dalam hati) det A = (1*4) - (2*3) = 4 - 6 = -2. Ayo yakin!",
        "(Dalam hati) Ingat rumus sin penjumlahan: sin(A+B). Ini sin(30+60) = sin90 = 1.",
        "(Dalam hati) tan45 = 1, sin90 = 1. Jadi 1 + 1 = 2. Sederhana!",
        "(Dalam hati) Invers matriks 2x2: elemen kiri-atas = d dibagi det = 3/1 = 3.",
        "Pak Guru: 'Intertekstualitas... setiap teks terhubung dengan teks lain dalam jaringan makna.'",
        "(Dalam hati) Kalimat topik menyatakan gagasan utama. Bukan simpulan, bukan contoh.",
        "(Dalam hati) In medias res... langsung mulai dari konflik. Seperti hidupku sekarang.",
        "Pak Guru: 'Kohesi itu alat gramatikal: pronoun, konjungsi, elipsis. Bukan makna!'",
        "(Dalam hati) Denotasi = kamus. Konotasi = asosiasi rasa. Bunga vs harapan.",
        "(Dalam hati) Flashback = kilas balik. Layaknya ingatanku yang selalu kembali.",
        "Pak Guru: 'Resensi itu: identitas karya, sinopsis, analisis, lalu evaluasi!'",
        "(Dalam hati) Deskriptif = menggambarkan. Bukan membuktikan atau membandingkan.",
    ]


# ==========================================
# LABEL UTAMA QUIZ 5 (UAS)
# ==========================================

label quiz5_start:
    $ _quiz_reset()

    if sanity >= 55:
        $ _q5_qs    = _q5_easy
        $ _q5_narr  = _q5_easy_narr
        $ _q5_time  = 120
        $ _q5_name  = "UAS — Matematika & Bahasa Indonesia"
    elif sanity >= 30:
        $ _q5_qs    = _q5_medium
        $ _q5_narr  = _q5_medium_narr
        $ _q5_time  = 120
        $ _q5_name  = "UAS — Matematika & Bahasa Indonesia"
    else:
        $ _q5_qs    = _q5_hard
        $ _q5_narr  = _q5_hard_narr
        $ _q5_time  = 90
        $ _q5_name  = "UAS — Tingkat Akhir"

    call screen quiz_screen(_q5_name, _q5_qs, _q5_time, _q5_narr)

    $ (_q5_c, _q5_t, _q5_pct) = _quiz_get_result()
    $ quiz5_score = _q5_pct

    # Update stats silently tanpa reveal skor
    if _q5_pct >= 80:
        $ sanity += 5
        $ quiz_passed = True
    elif _q5_pct < 50:
        $ sanity -= 5
        $ quiz_passed = False
    else:
        $ quiz_passed = True

    "Waktu ujian telah habis. Lembar jawaban dikumpulkan satu per satu."
    "(Narasi Internal) Aku tidak tahu berapa yang kujawab benar. Sekarang hanya perlu menunggu."

    return
