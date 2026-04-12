# ==========================================
# ARC 7: SOCIAL AFTERMATH
# Cek Flag: cheated / honest_effort
# Cek Status: sanity (intensitas bisikan)
# Catatan: ARC 6 tidak ada dalam dokumen desain
# ==========================================

# --- SCENE 1: THE WHISPERS ---
label arc7_scene1:
    scene bg_school_corridor_noon with fade
    show mc anxious at center

    "Koridor sekolah terasa lebih panjang dari biasanya. Setiap kali aku lewat, aku bisa mendengar suara bisikan yang berhenti seketika saat aku menoleh."
    "\"Eh, lihat... itu anak baru yang dari sekolah elit itu kan?\""
    "\"Katanya dia pindah karena masalah besar. Nilai ujiannya juga mencurigakan...\""
    mc "(Menunduk, mempercepat langkah)"
    "(Narasi Internal) Paranoia mulai merayap. Apa mereka tahu tentang sekolah lamaku? Atau mereka membicarakan soal ujian kemarin? Rasanya semua mata sedang menghakimiku."

    jump arc7_scene2


# --- SCENE 2: THE WARNING ---
label arc7_scene2:
    show stevia worried at right

    s "[nama_mc], bisa bicara sebentar? Ada desas-desus yang nggak enak soal ujian kemarin."

    if cheated:
        show stevia disappointed
        s "Aku melihatmu melirik ke arah Rangga berkali-kali kemarin. Aku harap itu cuma perasaanku saja, tapi... guru-guru mulai memperhatikan."
    else:
        show stevia calm
        s "Nilaimu mungkin belum sempurna, tapi aku bangga kamu mengerjakannya sendiri. Jangan dengarkan apa yang dikatakan orang-orang di belakangmu."

    show mc sad
    mc "Aku cuma mencoba bertahan di sini, Stev. Kenapa semuanya terasa begitu sulit?"

    jump arc7_scene3


# --- SCENE 3: THE PROVOCATION ---
label arc7_scene3:
    show rangga smirk at left
    show ucup neutral at center

    r "Woi, pahlawan kita! Kenapa mukanya ditekuk gitu? Harusnya lo seneng, sekarang seisi sekolah tahu siapa lo."
    u "Iya nih, reputasi lo lagi naik daun, bro. Walaupun isinya nggak semuanya bagus."
    show rangga serious
    r "(Mendekat ke [nama_mc]) Denger, [nama_mc]. Di sekolah ini, lo nggak butuh nilai bagus buat dihargai. Lo cuma butuh orang-orang yang tepat buat jaga punggung lo."
    show stevia worried
    s "Berhenti menghasutnya, Rangga! Dia hanya ingin sekolah dengan tenang!"

    jump arc7_scene4


# --- SCENE 4: THE BIG CHOICE #5 (RESPONDING TO RUMORS) ---
label arc7_scene4:
    show mc anxious at center

    "Kamu merasa terpojok. Rumor itu semakin liar, dan sekarang kamu harus menentukan bagaimana kamu akan menghadapi dunia luar."

    menu:
        "Bela Diri (Stand Your Ground)":
            $ friendship_stevia += 8
            $ friendship_rangga -= 7
            $ sanity += 5
            $ stand_ground = True

            show mc neutral
            mc "Aku pindah ke sini untuk memulai awal yang baru. Terserah kalian mau bilang apa, aku nggak peduli."
            show stevia calm
            s "Bagus, [nama_mc]. Pertahankan sikap itu."
            show rangga annoyed
            r "Cih. Sok berani. Kita lihat seberapa lama lo bisa bertahan sendirian."
            hide rangga with moveoutleft
            hide ucup

        "Cari Perlindungan Rangga (Lean on Rangga)":
            $ friendship_stevia -= 10
            $ friendship_rangga += 15
            $ sanity -= 12
            $ rely_on_rangga = True

            show mc anxious
            mc "Ngga... gue beneran nggak nyaman sama omongan mereka. Lo bilang lo bisa bantu, kan?"
            show rangga smirk
            r "Nah! Itu baru bener. Mulai sekarang, siapa pun yang berani nyenggol lo, berarti berurusan sama gue."
            show stevia disappointed
            s "[nama_mc]... kamu membuat kesalahan besar dengan bergantung padanya."
            hide stevia with moveoutright

        "Diam dan Lari (Run Away)":
            $ friendship_stevia -= 2
            $ friendship_rangga -= 2
            $ sanity -= 15
            $ run_away = True

            show mc sad
            "(Berlari meninggalkan mereka berdua tanpa kata-kata)"
            "Kamu memilih untuk melarikan diri, namun suara bisikan itu justru terdengar semakin keras di kepalamu."
            hide rangga
            hide stevia
            hide ucup

    jump arc7_scene5


# --- SCENE 5: THE ISOLATION ---
label arc7_scene5:
    hide rangga
    hide stevia
    hide ucup
    scene bg_school_rooftop_noon with fade
    show mc sad at center

    "(Narasi Internal) Aku sendirian lagi. Di mana pun aku berada, bayangan masa lalu dan tekanan masa kini seolah tidak memberiku ruang untuk bernapas."
    mc "Sampai kapan aku harus berlari?"

    jump arc8_scene1
