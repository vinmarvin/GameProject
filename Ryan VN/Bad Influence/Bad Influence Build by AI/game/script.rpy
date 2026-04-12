# ==========================================
# BAD INFLUENCE — SCRIPT UTAMA
# Pusat Deklarasi Karakter, State & Alur
# ==========================================

# --- DEFINISI KARAKTER ---
define mc  = Character("[nama_mc]",    color="#ADD8E6")
define s   = Character("[nama_stevia]",color="#FFB6C1")
define r   = Character("[nama_rangga]",color="#FF4500")
define pg  = Character("Pak Guru",     color="#4CAF50")
define ig  = Character("Ibu Guru",     color="#8BC34A")
define u   = Character("Ucup",         color="#FFD700")
# Narasi menggunakan narrator bawaan Ren'Py (string biasa tanpa define)

# --- DEFINISI IMAGE KARAKTER ---
image pg neutral = "images/char/teacher1.png"

# ==========================================
# STATE — NAMA KARAKTER
# ==========================================
default nama_mc     = "MC"
default nama_stevia = "Stevia"
default nama_rangga = "Rangga"

# ==========================================
# STATE — STATISTIK
# Status Awal ARC 1: Sanity=50, FRS=20, FRR=20
# ==========================================
default sanity            = 50
default friendship_stevia = 20   # FRS
default friendship_rangga = 20   # FRR

# ==========================================
# FLAGS — KEPUTUSAN STORY
# ==========================================

# ARC 1
default defend_stevia  = False
default passive_start  = False

# ARC 2
default disturb_rangga = False
default avoid_conflict = False

# ARC 3 + 4 (Route Lock)
default join_rangga      = False
default uncertain        = False
default trust_stevia     = False
default bad_route_lock   = False
default stevia_route_lock= False

# ARC 5
default took_smoke   = False
default refused_init = False
default quiz_bonus   = False
default emotional_bond = False

# ARC 7
default stand_ground    = False
default rely_on_rangga  = False
default run_away        = False

# ARC 9 / 10
default took_cheat    = False
default cheated       = False
default honest_effort = False

# ARC 11
default recovery_path  = False
default denial_path    = False
default isolation_path = False

# ARC 13
default took_package    = False
default refused_package = False

# ARC 15 — FINAL
default final_path = "none"   # "stevia" | "rangga" | "isolation"

# ==========================================
# STATE — QUIZ MINI-GAME
# ==========================================
default quiz1_score = 0
default quiz2_score = 0
default quiz3_score = 0
default quiz4_score = 0
default quiz5_score = 0
default quiz_passed = False


# ==========================================
# LABEL START
# ==========================================
label start:

    scene black with fade

    label pilih_nama:
        $ nama_mc = renpy.input("Siapa namamu?")
        $ nama_mc = nama_mc.strip()

        if not nama_mc:
            $ nama_mc = "Aditya"

        $ nama_cek = nama_mc.lower()

        if nama_cek == "stevia":
            "Sistem" "Tunggu dulu... Stevia itu nama ketua kelas kita! Jangan nyamar jadi dia."
            jump pilih_nama

        elif nama_cek == "rangga":
            "Sistem" "Hadeh, ngapain pakai nama si cowok nyebelin itu? Ganti!"
            jump pilih_nama

        elif nama_cek == "ucup":
            "Sistem" "Nama 'ucup' sudah dipakai figuran kantin. Cari nama lebih keren!"
            jump pilih_nama

        elif nama_cek == "mc":
            "Sistem" "Ayolah... masa namamu cuma 'MC' doang?"
            jump pilih_nama

    $ nama_stevia = "Stevia"
    $ nama_rangga = "Rangga"

    jump arc1_scene1