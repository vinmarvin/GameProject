# ==========================================
# ARC 11: THE CONSEQUENCE (TURNING POINT)
# Cek Flag: cheated / honest_effort
# Cek Status: sanity
# ==========================================

# --- SCENE 1: THE RED MARKS ---
label arc11_scene1:
    scene bg_classroom_day with fade
    show mc anxious at center

    "Guru baru saja meninggalkan kelas setelah membagikan lembar hasil UTS. Suasana kelas yang tadinya tegang kini berubah menjadi riuh rendah suara murid yang membandingkan nilai."
    mc "(Menatap lembar kertas dengan angka merah yang mencolok) Nilai ini... lebih buruk dari yang aku kira."
    "(Narasi Internal) Dadaku terasa sesak. Setiap angka merah ini seolah meneriakkan kegagalanku. Apakah aku memang ditakdirkan untuk tetap menjadi orang yang kalah, tak peduli di sekolah mana pun aku berada?"

    jump arc11_scene2


# --- SCENE 2: TWO REACTIONS ---
label arc11_scene2:
    show stevia worried at right
    show rangga smirk at left

    s "[nama_mc]... kamu gapapa? Aku lihat nilaimu... Kita bisa perbaiki ini bareng-bareng kalau kamu mau. Jangan menyerah sekarang."
    r "Halah, baru segitu aja udah kayak mau kiamat. Santai aja, Bro. Nilai itu cuma angka di atas kertas sampah. Hidup nggak berhenti di sini cuma gara-gara satu ujian."
    show mc sad
    mc "(Hanya diam, menatap kedua arah dengan bingung)"

    jump arc11_scene3


# --- SCENE 3: THE CROSSROADS (LORONG SEKOLAH) ---
label arc11_scene3:
    scene bg_school_hallway_sunset with fade
    show stevia calm at right
    show rangga smirk at left
    show mc neutral at center

    "Bel pulang berbunyi. Langkah kaki [nama_mc] terhenti di persimpangan koridor. Di satu sisi ada harapan untuk bangkit, di sisi lain ada ajakan untuk melupakan segalanya."

    jump arc11_scene4


# --- SCENE 4: THE BIG CHOICE (ARAH HIDUP) ---
label arc11_scene4:
    menu:
        "Ikut Stevia (Recovery Path)":
            $ friendship_stevia += 15
            $ sanity += 10
            $ recovery_path = True

            show mc neutral
            mc "Mungkin... mungkin aku memang butuh bantuanmu, Stev. Ayo ke perpustakaan."
            show stevia calm
            s "Pilihan bagus. Kita mulai dari bagian yang paling sulit. Aku akan menemanimu."
            hide rangga with moveoutleft
            "[nama_mc] berjalan ke arah perpustakaan bersama Stevia."

        "Ikut Rangga (Denial Path)":
            $ friendship_rangga += 15
            $ sanity -= 20
            $ denial_path = True

            show mc neutral
            mc "Bener kata lo, Ngga. Gue butuh udara segar. Ayo cabut sekarang."
            show rangga smirk
            r "Nah! Gitu dong! Lupain soal kertas sampah itu. Kita punya cara yang lebih asik buat ngerayain 'kebebasan' sore ini."
            hide stevia with moveoutright
            "[nama_mc] berjalan ke arah parkiran bersama Rangga."

        "Pulang Sendiri (Isolation Path)":
            $ sanity -= 5
            $ isolation_path = True

            show mc sad
            mc "Maaf, aku mau sendiri dulu. Aku mau langsung pulang."
            show stevia disappointed
            s "Oh... oke. Tapi jangan terlalu lama memendamnya sendiri ya."
            show rangga neutral
            r "Yaudah, balik sana ke rumah. Dasar nggak asik."
            hide rangga with moveoutleft
            hide stevia with moveoutright
            "[nama_mc] berjalan lurus sendirian keluar gerbang."

    jump arc11_scene5


# --- SCENE 5: REFLECTION IN THE DARK ---
label arc11_scene5:
    hide stevia
    hide rangga
    scene bg_mc_room_night with fade
    show mc sad at center

    "(Narasi Internal) Aku telah mengambil langkah pertama. Tapi kenapa rasanya duniaku tetap tidak tenang? Jalur mana pun yang kupilih... aku merasa sedang mempertaruhkan sesuatu yang berharga."
    mc "Besok... segalanya akan menjadi lebih berat."

    jump arc12_scene1
