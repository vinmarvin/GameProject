# ==========================================
# QUIZ 2 — UTS : BAHASA INGGRIS + SEJARAH INDONESIA
# Dipanggil dari: arc10_scene1
# Urutan     : B.Inggris dulu, baru Sejarah (tidak diacak)
# Mudah/Sedang : 10 soal (5+5), 120 detik
# Susah        : 15 soal (7+8), 60 detik
# ==========================================

init python:

    # ========================================
    # SOAL MUDAH
    # ========================================

    _q2_easy_eng = [
        {
            "q": "What is the correct simple past tense form of the verb 'go'?",
            "c": ["A. goed", "B. gone", "C. went", "D. going"],
            "a": 2
        },
        {
            "q": "Choose the correct passive voice:\n'They built the bridge in 1990.'",
            "c": [
                "A. The bridge is built in 1990.",
                "B. The bridge was built in 1990.",
                "C. The bridge built in 1990.",
                "D. The bridge has been build in 1990."
            ],
            "a": 1
        },
        {
            "q": "What does the word 'diligent' mean in Indonesian?",
            "c": ["A. Malas", "B. Pintar", "C. Baik hati", "D. Rajin"],
            "a": 3
        },
        {
            "q": "Which of the following words is a conjunction?",
            "c": ["A. Beautiful", "B. Quickly", "C. Although", "D. Teacher"],
            "a": 2
        },
        {
            "q": "Complete the sentence:\n'She has been studying English ___ three years.'",
            "c": ["A. since", "B. during", "C. ago", "D. for"],
            "a": 3
        },
    ]

    _q2_easy_hist = [
        {
            "q": "Kapan Indonesia memproklamasikan kemerdekaannya?",
            "c": [
                "A. 17 Agustus 1944",
                "B. 18 Agustus 1945",
                "C. 17 Agustus 1945",
                "D. 17 Juli 1945"
            ],
            "a": 2
        },
        {
            "q": "Siapakah yang membacakan teks Proklamasi Kemerdekaan Indonesia?",
            "c": [
                "A. Hatta dan Sjahrir",
                "B. Soekarno dan Hatta",
                "C. Soekarno seorang diri",
                "D. Sjahrir dan Soepomo"
            ],
            "a": 1
        },
        {
            "q": "Nama organisasi bentukan Jepang untuk mempersiapkan kemerdekaan Indonesia adalah...",
            "c": ["A. PPKI", "B. PETA", "C. BPKI", "D. BPUPKI"],
            "a": 3
        },
        {
            "q": "Peristiwa Rengasdengklok terjadi pada tanggal...",
            "c": [
                "A. 15 Agustus 1945",
                "B. 16 Agustus 1945",
                "C. 17 Agustus 1945",
                "D. 14 Agustus 1945"
            ],
            "a": 1
        },
        {
            "q": "Pancasila sebagai dasar negara Indonesia dirumuskan pertama kali oleh...",
            "c": ["A. Mohammad Hatta", "B. Soepomo", "C. Mohammad Yamin", "D. Soekarno"],
            "a": 3
        },
    ]

    _q2_easy = _q2_easy_eng + _q2_easy_hist

    _q2_easy_narr = [
        "(Dalam hati) Grammar dasar dulu... tenang, ini B.Inggris yang paling basic.",
        "Pak Guru: 'Passive voice! Ingat rumusnya: to be + V3!'",
        "(Dalam hati) Vocabulary... diligent. Aku pernah lihat ini di Flash Card semester 1.",
        "Pak Guru: 'Conjunction itu kata penghubung, bukan kata sifat atau kata kerja.'",
        "(Dalam hati) Since atau for? Since untuk titik waktu, for untuk durasi. Ayo!",
        # Sejarah mulai
        "(Dalam hati) Sejarah sekarang. Tanggal proklamasi... yang ini aku pasti tahu.",
        "Pak Guru: 'Proklamasi dibacakan oleh dua tokoh bangsa yang namanya diabadikan sejarah.'",
        "(Dalam hati) BPUPKI... Badan Penyelidik Usaha Persiapan Kemerdekaan Indonesia.",
        "(Dalam hati) Rengasdengklok... 16 Agustus 1945. Soekarno-Hatta dibawa ke sana.",
        "(Dalam hati) Pancasila dirumuskan pertama kali... saat sidang BPUPKI 1 Juni 1945.",
    ]

    # ========================================
    # SOAL SEDANG
    # ========================================

    _q2_medium_eng = [
        {
            "q": "Choose the sentence with the CORRECT use of subjunctive mood:",
            "c": [
                "A. If I was you, I would study harder.",
                "B. If I am you, I would study harder.",
                "C. If I be you, I would study harder.",
                "D. If I were you, I would study harder."
            ],
            "a": 3
        },
        {
            "q": "Identify the type of the underlined clause:\n'The student {u}who won the competition{/u} is my friend.'",
            "c": [
                "A. Adverbial clause",
                "B. Noun clause",
                "C. Relative (adjective) clause",
                "D. Conditional clause"
            ],
            "a": 2
        },
        {
            "q": "What is the closest synonym of the word 'magnificent'?",
            "c": ["A. Terrible", "B. Ordinary", "C. Splendid", "D. Quiet"],
            "a": 2
        },
        {
            "q": "'The committee ___ yet to announce their decision.'\nChoose the correct verb:",
            "c": ["A. are", "B. were", "C. is", "D. have"],
            "a": 2
        },
        {
            "q": "Which sentence correctly uses reported speech?\nDirect: 'He said: I will come tomorrow.'",
            "c": [
                "A. He said he will come tomorrow.",
                "B. He said he comes tomorrow.",
                "C. He said he came tomorrow.",
                "D. He said he would come the next day."
            ],
            "a": 3
        },
    ]

    _q2_medium_hist = [
        {
            "q": "Konferensi Meja Bundar (KMB) 1949 menghasilkan kesepakatan bahwa...",
            "c": [
                "A. Indonesia bergabung dalam persemakmuran Belanda",
                "B. Irian Barat langsung diserahkan kepada RI",
                "C. Belanda mengakui kedaulatan RI pada 27 Desember 1949",
                "D. Pemerintahan RI dipindahkan ke Yogyakarta"
            ],
            "a": 2
        },
        {
            "q": "Peristiwa Gerakan 30 September/PKI (G30S) terjadi pada tahun...",
            "c": ["A. 1963", "B. 1964", "C. 1966", "D. 1965"],
            "a": 3
        },
        {
            "q": "Sistem pemerintahan Demokrasi Terpimpin diterapkan pada masa...",
            "c": [
                "A. Orde Baru",
                "B. Reformasi",
                "C. Revolusi Fisik",
                "D. Orde Lama (1959–1965)"
            ],
            "a": 3
        },
        {
            "q": "Tragedi Trisakti 12 Mei 1998 menjadi pemicu utama dari...",
            "c": [
                "A. Deklarasi Kemerdekaan",
                "B. Pembentukan Orde Baru",
                "C. Gerakan mahasiswa menuntut reformasi dan mundurnya Soeharto",
                "D. Pembubaran DPR"
            ],
            "a": 2
        },
        {
            "q": "Perjanjian Linggarjati (1947) menetapkan Belanda mengakui de facto wilayah RI meliputi...",
            "c": [
                "A. Seluruh kepulauan Indonesia",
                "B. Jawa, Bali, dan Kalimantan",
                "C. Jawa, Borneo, dan Sulawesi",
                "D. Jawa, Sumatera, dan Madura"
            ],
            "a": 3
        },
    ]

    _q2_medium = _q2_medium_eng + _q2_medium_hist

    _q2_medium_narr = [
        "(Dalam hati) Subjunctive... 'If I were' bukan 'If I was'. Ingat itu!",
        "Pak Guru: 'Relative clause menerangkan kata benda sebelumnya, bukan keterangan waktu.'",
        "(Dalam hati) Magnificent... megah... splendid! Itu dia!",
        "(Dalam hati) Committee adalah kata kolektif singular, jadi pakainya 'is'.",
        "Pak Guru: 'Reported speech mengubah tense dan pronoun. Hati-hati!'",
        # Sejarah mulai
        "(Dalam hati) KMB... 27 Desember 1949. Tanggal pengakuan kedaulatan penuh.",
        "Pak Guru: 'G30S adalah salah satu peristiwa paling kelam dalam sejarah Indonesia.'",
        "(Dalam hati) Demokrasi Terpimpin... Soekarno, Dekrit Presiden 5 Juli 1959.",
        "(Dalam hati) Trisakti 1998... mahasiswa gugur... memantik reformasi besar.",
        "(Dalam hati) Linggarjati itu 1947... wilayah de facto: Jawa, Sumatera, Madura.",
    ]

    # ========================================
    # SOAL SUSAH (7 B.Inggris + 8 Sejarah = 15)
    # ========================================

    _q2_hard_eng = [
        {
            "q": "Choose the most appropriate word for the blank:\n'The scientist's findings were ___ by subsequent research.'",
            "c": ["A. alleviated", "B. precipitated", "C. corroborated", "D. ameliorated"],
            "a": 2
        },
        {
            "q": "Identify the figure of speech:\n'The wind whispered secrets through the ancient trees.'",
            "c": ["A. Simile", "B. Metaphor", "C. Hyperbole", "D. Personification"],
            "a": 3
        },
        {
            "q": "Which sentence correctly uses the present perfect continuous tense?",
            "c": [
                "A. She has working on this project since Monday.",
                "B. She is been working on this project since Monday.",
                "C. She has been working on this project since Monday.",
                "D. She had working on this project since Monday."
            ],
            "a": 2
        },
        {
            "q": "Choose the correct indirect speech:\nDirect: 'He asked: How long have you been waiting?'",
            "c": [
                "A. He asked how long I have been waiting.",
                "B. He asked how long have I been waiting.",
                "C. He asked how long I am waiting.",
                "D. He asked how long I had been waiting."
            ],
            "a": 3
        },
        {
            "q": "The word 'ambiguous' means...",
            "c": [
                "A. Clear and easy to understand",
                "B. Open to more than one interpretation",
                "C. Extremely confident",
                "D. Impossibly difficult"
            ],
            "a": 1
        },
        {
            "q": "In academic writing, a 'thesis statement' refers to...",
            "c": [
                "A. The topic sentence of each paragraph",
                "B. The bibliography section",
                "C. The conclusion paragraph",
                "D. The main argument or central claim of an essay"
            ],
            "a": 3
        },
        {
            "q": "Choose the sentence with CORRECT use of semicolon:",
            "c": [
                "A. The exam was difficult; because most students failed.",
                "B. The exam was difficult; however, most students passed.",
                "C. The exam was; difficult most students passed.",
                "D. The exam was difficult; they also studied."
            ],
            "a": 1
        },
    ]

    _q2_hard_hist = [
        {
            "q": "Isi tuntutan 'Tritura' yang digaungkan mahasiswa pada 1966 adalah...",
            "c": [
                "A. Bubarkan PKI, bubarkan kabinet Dwikora, dan turunkan harga",
                "B. Tiga resolusi PBB tentang Indonesia",
                "C. Tiga janji Soekarno kepada rakyat",
                "D. Tiga perjanjian damai dengan Belanda"
            ],
            "a": 0
        },
        {
            "q": "Perjanjian Roem-Royen (1949) menetapkan bahwa...",
            "c": [
                "A. Belanda mengakui kemerdekaan Indonesia sepenuhnya",
                "B. Yogyakarta langsung diserahkan kepada RI",
                "C. Indonesia menghentikan gerilya dan Belanda membebaskan tahanan politik RI",
                "D. Indonesia bergabung ke Uni Indonesia–Belanda"
            ],
            "a": 2
        },
        {
            "q": "Operasi Trikora (1961–1962) bertujuan untuk...",
            "c": [
                "A. Membebaskan Timor Timur dari Portugis",
                "B. Mengusir Inggris dari Malaysia",
                "C. Memadamkan pemberontakan PRRI/Permesta",
                "D. Merebut kembali Irian Barat dari Belanda"
            ],
            "a": 3
        },
        {
            "q": "Supersemar (Surat Perintah Sebelas Maret) ditandatangani pada...",
            "c": [
                "A. 11 Maret 1965",
                "B. 11 Maret 1967",
                "C. 11 Maret 1968",
                "D. 11 Maret 1966"
            ],
            "a": 3
        },
        {
            "q": "Dampak krisis moneter 1997–1998 di Indonesia yang paling signifikan adalah...",
            "c": [
                "A. Rupiah menguat terhadap dolar AS",
                "B. Inflasi turun drastis di bawah 5%",
                "C. Rupiah melemah drastis, sempat tembus Rp16.000 per dolar",
                "D. Pertumbuhan ekonomi Indonesia mencapai 10%"
            ],
            "a": 2
        },
        {
            "q": "Sidang BPUPKI dua periode menghasilkan...",
            "c": [
                "A. Pembentukan PPKI dan BKR",
                "B. Rancangan UUD 1945 dan Piagam Jakarta",
                "C. Proklamasi dan Pancasila",
                "D. Rancangan UUD dan pembentukan TNI"
            ],
            "a": 1
        },
        {
            "q": "Perjanjian Renville (1948) merugikan Indonesia karena...",
            "c": [
                "A. Indonesia mendapat lebih banyak wilayah dari Belanda",
                "B. Indonesia memperoleh pengakuan internasional penuh",
                "C. Indonesia harus membentuk negara federal",
                "D. Indonesia kehilangan wilayah yang sebelumnya dikuasai TNI"
            ],
            "a": 3
        },
        {
            "q": "Peran Mohammad Hatta dalam Proklamasi 17 Agustus 1945 adalah...",
            "c": [
                "A. Pengetik naskah proklamasi",
                "B. Pembaca teks proklamasi",
                "C. Penandatangan proklamasi bersama Soekarno",
                "D. Penyelenggara dan protokol upacara proklamasi"
            ],
            "a": 2
        },
    ]

    _q2_hard = _q2_hard_eng + _q2_hard_hist

    _q2_hard_narr = [
        "(Dalam hati) Corroborated... itu artinya diperkuat / dikonfirmasi. Ayo ingat!",
        "(Dalam hati) Angin yang berbisik... bukan majas manusia yang bicara secara harfiah? Personifikasi!",
        "Pak Guru: 'Present perfect continuous: has/have been + V-ing. Jangan ketukar!'",
        "(Dalam hati) Indirect speech + question... tense mundur! Had been waiting!",
        "(Dalam hati) Ambiguous... ambigu... dua arti. Itu pasti B.",
        "Pak Guru: 'Thesis statement bukan judul! Itu klaim utama esaimu!'",
        "(Dalam hati) Semicolon sebelum 'however'... itu konstruksi yang benar!",
        # Sejarah mulai
        "(Dalam hati) Tritura 1966... tiga tuntutan mahasiswa. Aku ingat ini dari film dokumenter.",
        "Pak Guru: 'Perjanjian Roem-Royen itu solusi kompromi, bukan pengakuan penuh.'",
        "(Dalam hati) Trikora... Tri = tiga, Kora = koreksi? Atau Komando Rakyat?",
        "(Dalam hati) Supersemar... 11 Maret 1966. Soekarno memberi mandat kepada Soeharto.",
        "(Dalam hati) 1998... nilai tukar amblas... krisis moneter Asia menghantam Indonesia.",
        "Pak Guru: 'BPUPKI bersidang dua kali: pertama merumuskan dasar negara, kedua merancang UUD.'",
        "(Dalam hati) Renville... kenapa namanya dari kapal perang? Karena ditandatangani di atas kapal itu!",
        "(Dalam hati) Hatta menandatangani proklamasi bersama Soekarno. Dua founding fathers.",
    ]


# ==========================================
# LABEL UTAMA QUIZ 2 (UTS)
# ==========================================

label quiz2_start:
    $ _quiz_reset()

    if sanity >= 55:
        $ _q2_qs    = _q2_easy
        $ _q2_narr  = _q2_easy_narr
        $ _q2_time  = 120
        $ _q2_name  = "UTS — Bahasa Inggris & Sejarah Indonesia"
    elif sanity >= 30:
        $ _q2_qs    = _q2_medium
        $ _q2_narr  = _q2_medium_narr
        $ _q2_time  = 120
        $ _q2_name  = "UTS — Bahasa Inggris & Sejarah Indonesia"
    else:
        $ _q2_qs    = _q2_hard
        $ _q2_narr  = _q2_hard_narr
        $ _q2_time  = 60
        $ _q2_name  = "UTS — Tingkat Lanjut"

    call screen quiz_screen(_q2_name, _q2_qs, _q2_time, _q2_narr)

    $ (_q2_c, _q2_t, _q2_pct) = _quiz_get_result()
    $ quiz2_score = _q2_pct

    # Update stats silently
    if _q2_pct >= 80:
        $ sanity += 5
        $ quiz_passed = True
    elif _q2_pct < 50:
        $ sanity -= 5
        $ quiz_passed = False
    else:
        $ quiz_passed = True

    "Waktu UTS habis. Pengawas mulai mengumpulkan lembar jawaban."
    "(Narasi Internal) Entah berapa yang kujawab dengan benar. Sekarang hanya bisa menunggu."

    return
