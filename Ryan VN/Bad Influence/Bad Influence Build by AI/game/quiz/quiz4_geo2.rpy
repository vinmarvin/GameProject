# ==========================================
# QUIZ 4 — GEOGRAFI 2 (Konteks: Pikiran Retak)
# Dipanggil dari: arc14_scene3
# Mudah/Sedang: 5 soal, 60 detik
# Susah       : 7 soal, 30 detik
# Catatan: Jika sanity < 30, narasi lebih "distorted"
# ==========================================

init python:

    # ---- SOAL MUDAH — Geografi 2 ----
    _q4_easy = [
        {
            "q": "Bentuk muka bumi yang terbentuk akibat pengangkatan kulit bumi disebut...",
            "c": ["A. Palung", "B. Delta", "C. Lembah", "D. Pegunungan"],
            "a": 3
        },
        {
            "q": "Salah satu dampak positif letak geografis Indonesia adalah...",
            "c": [
                "A. Seringnya terjadi gempa bumi",
                "B. Banyaknya gunung berapi aktif",
                "C. Menjadi jalur perdagangan internasional",
                "D. Musim yang tidak menentu"
            ],
            "a": 2
        },
        {
            "q": "Jenis tanah yang paling subur untuk pertanian umumnya adalah...",
            "c": ["A. Tanah laterit", "B. Tanah kapur", "C. Tanah pasir", "D. Tanah vulkanik"],
            "a": 3
        },
        {
            "q": "Hutan hujan tropis di Indonesia tumbuh lebat karena...",
            "c": [
                "A. Curah hujan sangat rendah",
                "B. Musim kering yang sangat panjang",
                "C. Suhu sangat rendah sepanjang tahun",
                "D. Curah hujan tinggi sepanjang tahun"
            ],
            "a": 3
        },
        {
            "q": "Contoh sumber daya alam yang {b}tidak dapat{/b} diperbaharui adalah...",
            "c": ["A. Hutan", "B. Minyak bumi", "C. Air", "D. Tanah pertanian"],
            "a": 1
        },
    ]

    _q4_easy_narr = [
        "(Dalam hati) Gunung... pegunungan... itu terbentuk karena pengangkatan... aku tahu.",
        "(Dalam hati) Coba fokus. Indonesia di jalur perdagangan internasional. Itu pelajaran kelas 7.",
        "(Dalam hati) Tanah vulkanik... abu gunung berapi itu sangat menyuburkan tanah.",
        "(Dalam hati) Hutan tropis... hujan sepanjang tahun. Itu sebabnya Indonesia hijau.",
        "(Dalam hati) Minyak bumi... tidak bisa diperbaharui. Ini pasti makan jutaan tahun.",
    ]

    # ---- SOAL SEDANG — Geografi 2 ----
    _q4_medium = [
        {
            "q": "Natalitas adalah...",
            "c": [
                "A. Angka kematian penduduk",
                "B. Perpindahan penduduk antardaerah",
                "C. Angka kelahiran penduduk",
                "D. Kepadatan penduduk per km²"
            ],
            "a": 2
        },
        {
            "q": "Zona Ekonomi Eksklusif (ZEE) Indonesia membentang sejauh...",
            "c": ["A. 12 mil laut", "B. 350 mil laut", "C. 500 mil laut", "D. 200 mil laut"],
            "a": 3
        },
        {
            "q": "Angin muson barat membawa musim hujan ke Indonesia karena...",
            "c": [
                "A. Berasal dari Benua Australia yang kering",
                "B. Bertiup dari arah timur laut",
                "C. Berasal dari Samudra Hindia yang lembab dan basah",
                "D. Terjadi saat matahari berada di atas Tropic of Cancer"
            ],
            "a": 2
        },
        {
            "q": "Urbanisasi adalah perpindahan penduduk dari...",
            "c": ["A. Kota ke desa", "B. Satu negara ke negara lain", "C. Satu provinsi ke provinsi lain", "D. Desa ke kota"],
            "a": 3
        },
        {
            "q": "Proses masuknya air laut ke daratan akibat naiknya muka air laut disebut...",
            "c": ["A. Abrasi", "B. Sedimentasi", "C. Intrusi air laut", "D. Rob"],
            "a": 3
        },
    ]

    _q4_medium_narr = [
        "(Dalam hati) Natalitas... natal... kelahiran. Itu pasti kelahiran.",
        "(Dalam hati) ZEE... 200 mil laut. Zona perairan eksklusif untuk sumber daya.",
        "(Dalam hati) Angin muson barat... dari barat artinya dari Samudra Hindia. Lembab.",
        "(Dalam hati) Urbanisasi... urban... kota. Jadi dari desa ke kota.",
        "(Dalam hati) Air laut masuk ke daratan... itu banjir rob. Sering di Jakarta.",
    ]

    # ---- SOAL SUSAH — Geografi 2 (7 soal, 30 detik) ----
    _q4_hard = [
        {
            "q": "Perubahan iklim global secara langsung menyebabkan...",
            "c": [
                "A. Penurunan suhu rata-rata bumi",
                "B. Berkurangnya intensitas angin topan dan badai",
                "C. Meningkatnya keanekaragaman hayati secara global",
                "D. Mencairnya es kutub dan naiknya permukaan laut"
            ],
            "a": 3
        },
        {
            "q": "Konsep geografi yang menjelaskan hubungan timbal balik manusia dengan lingkungannya disebut...",
            "c": [
                "A. Konsep pola",
                "B. Konsep lokasi",
                "C. Konsep ekologi",
                "D. Konsep interaksi dan interdependensi"
            ],
            "a": 2
        },
        {
            "q": "Indeks Pembangunan Manusia (IPM/HDI) mengukur tiga dimensi utama, yaitu...",
            "c": [
                "A. Pendapatan, militer, dan teknologi",
                "B. Pertumbuhan ekonomi, inflasi, dan PDB",
                "C. Pendidikan, kesehatan, dan standar hidup/pendapatan",
                "D. Kepadatan penduduk, industri, dan ekspor"
            ],
            "a": 2
        },
        {
            "q": "Gempa bumi tektonik terjadi akibat...",
            "c": [
                "A. Letusan gunung berapi bawah laut",
                "B. Tanah longsor di dasar samudra",
                "C. Aktivitas pertambangan manusia",
                "D. Pergerakan dan patahan lempeng bumi"
            ],
            "a": 3
        },
        {
            "q": "Teori Malthus tentang kependudukan menyatakan bahwa...",
            "c": [
                "A. Pertumbuhan teknologi mengimbangi pertumbuhan penduduk",
                "B. Penduduk bertambah sesuai ketersediaan pangan",
                "C. Pertumbuhan penduduk (deret ukur) lebih cepat dari pangan (deret hitung)",
                "D. Kepadatan penduduk tidak berpengaruh pada krisis pangan"
            ],
            "a": 2
        },
        {
            "q": "Garis kontur yang berdekatan satu sama lain pada peta topografi menandakan...",
            "c": [
                "A. Wilayah datar dan landai",
                "B. Aliran sungai yang panjang",
                "C. Lereng yang sangat curam",
                "D. Zona iklim basah"
            ],
            "a": 2
        },
        {
            "q": "Fenomena Angin Fohn terjadi saat udara...",
            "c": [
                "A. Lembab naik di sisi pegunungan menghadap laut dan turun kering di sisi sebaliknya",
                "B. Dingin dari kutub bergerak ke daerah tropis",
                "C. Panas dari gurun bertiup ke daerah pantai",
                "D. Hangat naik secara vertikal membentuk awan cumulonimbus"
            ],
            "a": 0
        },
    ]

    _q4_hard_narr_normal = [
        "(Dalam hati) Perubahan iklim... es mencair... permukaan laut naik. Ayo fokus!",
        "(Dalam hati) Konsep ekologi... hubungan manusia dan lingkungan. Itu jawabannya.",
        "(Dalam hati) IPM... pendidikan, kesehatan, pendapatan. Tiga pilar manusia.",
        "(Dalam hati) Gempa tektonik... lempeng bergerak... saling bertumbukan.",
        "(Dalam hati) Malthus... populasi tumbuh geometrik, pangan tumbuh aritmatik. Berbahaya.",
        "(Dalam hati) Kontur rapat = lereng curam. Ingat itu dari peta gunung.",
        "(Dalam hati) Angin Fohn... naik basah, turun kering dan panas. Ada di Jawa bagian utara.",
    ]

    _q4_hard_narr_distorted = [
        "(Dalam hati) K-k-kl... iklim... panas... Es yang mencair... seperti kepalaku sekarang.",
        "(Dalam hati) Manusia dan lingkungan... aku bagian mana? Lingkungan yang merusakku?",
        "(Dalam hati) Tiga dimensi... pendidikan... aku bahkan tidak bisa fokus membaca ini.",
        "(Dalam hati) Lempeng... bergerak... bergerak... semuanya terasa bergerak sekarang.",
        "(Dalam hati) Malthus... pangan... kenapa huruf-hurufnya menari? Aku harus menjawab...",
        "(Dalam hati) Kontur... lereng... aku ingin berlari menuruni lereng yang curam itu sekarang.",
        "(Dalam hati) Angin Fohn... naik... turun... aku juga sudah jatuh. Sudah lama.",
    ]


# ==========================================
# LABEL UTAMA QUIZ 4
# ==========================================

label quiz4_start:
    $ _quiz_reset()

    # Pilih narasi berdasarkan kondisi mental MC
    if sanity < 30:
        $ _q4_hard_narr = _q4_hard_narr_distorted
    else:
        $ _q4_hard_narr = _q4_hard_narr_normal

    if sanity >= 55:
        $ _q4_qs    = _q4_easy
        $ _q4_narr  = _q4_easy_narr
        $ _q4_time  = 60
        $ _q4_name  = "Kuis Geografi"
    elif sanity >= 30:
        $ _q4_qs    = _q4_medium
        $ _q4_narr  = _q4_medium_narr
        $ _q4_time  = 60
        $ _q4_name  = "Kuis Geografi"
    else:
        $ _q4_qs    = _q4_hard
        $ _q4_narr  = _q4_hard_narr
        $ _q4_time  = 30
        $ _q4_name  = "Kuis Geografi — Mode Kritis"

    call screen quiz_screen(_q4_name, _q4_qs, _q4_time, _q4_narr)

    $ (_q4_c, _q4_t, _q4_pct) = _quiz_get_result()
    $ quiz4_score = _q4_pct

    # Update stats silently
    if _q4_pct >= 80:
        $ sanity += 5
        $ quiz_passed = True
    elif _q4_pct < 50:
        $ sanity -= 5
        $ quiz_passed = False
    else:
        $ quiz_passed = True

    "Kuis selesai. Lembar jawaban dikumpulkan."
    "(Narasi Internal) Aku tidak tahu hasilnya. Kepalaku masih terlalu penuh untuk peduli."

    return
