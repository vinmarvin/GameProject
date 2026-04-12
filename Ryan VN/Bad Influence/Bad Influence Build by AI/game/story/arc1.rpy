# ==========================================
# ARC 1: NEW SCHOOL
# Sanity Awal: 50 | FRS: 20 | FRR: 20
# ==========================================

# --- SCENE 1: THE FRESH START ---
label arc1_scene1:
    scene bg_school_gate_morning with fade
    show mc anxious at center

    "Hari ini adalah hari pertama. Identitas baru, lingkungan baru. Namun, bayangan masa lalu tidak pernah benar-benar pergi."
    mc "(Menarik napas panjang) Sekolah baru, identitas baru. Semoga kali ini aku bisa bertahan tanpa jadi sasaran empuk seperti di sekolah lama."
    "MC melangkah masuk. Gerbang besar ini terasa seperti mulut raksasa yang siap menelan siapa saja yang tidak bisa menyesuaikan diri."

    jump arc1_scene2


# --- SCENE 2: THE ENCOUNTER ---
label arc1_scene2:
    scene bg_school_hallway_morning with dissolve
    show mc anxious at left
    show stevia calm at right

    s "Hei! Kamu murid pindahan baru itu, ya?"
    mc "(Terlonjak kaget) I.. iya. Aku [nama_mc]."
    s "Santai saja, nggak perlu gugup begitu. Aku Stevia, Ketua Kelas 11A. Sepertinya kita sekelas."
    show mc neutral
    mc "Oh, salam kenal, Stevia."
    "Saat Stevia berbalik untuk menunjukkan jalan, langkahnya terlihat sedikit berbeda. Ada jeda yang tidak sinkron pada kaki kirinya—sebuah sisa dari masa lalu yang ia simpan rapat-rapat."

    jump arc1_scene3


# --- SCENE 3: THE UNTOUCHABLE ---
label arc1_scene3:
    scene bg_school_hallway_morning with dissolve
    show mc neutral at left
    show stevia calm at right
    show rangga smirk at center

    r "Minggir dari jalan gue, Pincang."
    show stevia worried
    s "Rangga! Koridor ini luas, nggak perlu sengaja menabrak orang!"
    r "(Menoleh ke [nama_mc]) Wih, siapa nih? Mainan baru lo, Stev? Nama lo siapa, Anak Baru?"
    show mc anxious
    mc "A.. aku [nama_mc]."
    r "[nama_mc]? Nama yang aneh. Kenalin, gue Rangga. Orang yang bakal bikin hidup lo di sini jadi 'menarik'—kalau lo tahu cara mainnya."
    s "Jangan dengerin dia, [nama_mc]. Ayo pergi."
    show rangga serious
    r "(Menghalangi jalan Stevia) Gue belum selesai ngomong, Stev. Lo makin berani ya sejak punya 'ajudan' baru?"

    jump arc1_scene4


# --- SCENE 4: THE BIG CHOICE #0 (PRE-PATH) ---
label arc1_scene4:
    "Situasi memanas. Trauma lamamu berbisik: \"Jangan ikut campur jika ingin selamat.\" Tapi nuranimu melihat Stevia yang sudah membantumu sejak tadi."

    menu:
        "Hentikan Rangga (Defend Stevia)":
            $ friendship_stevia += 7
            $ friendship_rangga -= 5
            $ sanity += 2
            $ defend_stevia = True

            mc "Cukup, Rangga. Dia cuma mau nunjukin jalan ke kelas."
            show rangga annoyed
            r "Cih. Pahlawan kesiangan. Oke, gue inget muka lo, [nama_mc]."
            hide rangga with moveoutright
            show stevia calm
            s "Makasih ya... nggak banyak orang yang berani tegur dia."

        "Diam Saja (Passive)":
            $ sanity -= 2
            $ passive_start = True

            show mc anxious
            "(Menunduk, menghindari kontak mata)"
            show stevia disappointed
            s "(Menghela napas) Ya sudah... ayo kita ke kelas saja."
            show rangga smirk
            r "Pinter. Lo tahu mana posisi yang aman."
            hide rangga with moveoutright

    jump arc1_scene5


# --- SCENE 5: CLOSING ARC 1 ---
label arc1_scene5:
    hide stevia
    scene bg_classroom_morning with fade
    show mc neutral at center

    "Bel masuk berbunyi. [nama_mc] duduk di bangkunya, merasakan atmosfer kelas yang mulai berisik. Di belakangnya, Rangga duduk santai; Stevia duduk di barisan depan dengan kaku."
    show mc sad
    mc "Hari pertama, dan aku sudah berada di tengah api."

    jump arc2_scene1
