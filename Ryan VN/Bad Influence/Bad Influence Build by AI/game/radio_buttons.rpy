init python:
    class RadioButtonGroup:
        """Plugin oleh Wendy-Nam (MIT License)
        Sumber: https://github.com/Wendy-Nam/RenPy-RadioButtonGroup
        Dimodifikasi untuk quiz Bad Influence: tambah scoring & feedback.
        """

        def __init__(self, options, actions=None):
            self.selected = []
            self.options  = [(idx, opt) for idx, opt in enumerate(options)]
            if (actions is None) or (len(actions) < len(options)):
                self.actions = [NullAction() for _ in range(len(options))]
            else:
                self.actions = actions[:len(options)]

        def set_option(self, option_id, max_choice=1):
            if option_id in self.selected:
                self.selected.remove(option_id)
            else:
                if len(self.selected) >= max_choice:
                    num_to_remove = len(self.selected) - max_choice + 1
                    del self.selected[:num_to_remove]
                self.selected.append(option_id)

        def is_selected(self, option_id):
            return option_id in self.selected

        def get_selected_index(self):
            return sorted(self.selected)

        def get_selected_values(self):
            selection = self.get_selected_index()
            return [self.options[idx][1] for idx in selection]

        def reset(self):
            self.selected = []


# ============================================================
# SCREEN: Soal Pilihan Ganda (1 jawaban) — Gaya Quiz Sekolah
# ============================================================
screen radio_quiz(rb_group, question_text, time_left=None):
    modal True

    # Overlay gelap di belakang
    add "#000000CC"

    # Kotak soal — background solid gelap agar teks putih terlihat
    frame:
        xalign 0.5
        yalign 0.5
        xsize 820
        padding (40, 36)
        background "#1A1A2E"

        vbox:
            spacing 16

            # Garis dekoratif atas
            add Solid("#4A90D9"):
                xsize 740
                ysize 3
                xalign 0.5

            null height 4

            # Teks pertanyaan
            text question_text:
                size 24
                color "#F0F0F0"
                xalign 0.5
                text_align 0.5
                layout "subtitle"

            # Timer (opsional)
            if time_left is not None:
                text "Waktu: [time_left]s":
                    size 18
                    color "#FFC857"
                    xalign 0.5

            null height 8

            # Pilihan jawaban
            for option_id, option_text in rb_group.options:
                $ selected = rb_group.is_selected(option_id)
                textbutton option_text:
                    action Function(rb_group.set_option, option_id, 1)
                    xsize 740
                    ysize 52
                    xalign 0.5
                    text_align 0.0
                    left_padding 20
                    if selected:
                        background "#1E6F50"
                        text_color "#FFFFFF"
                    else:
                        background "#2C2C3E"
                        text_color "#CCCCCC"
                    hover_background "#3A5A72"
                    text_size 20

            null height 8

            # Garis dekoratif bawah
            add Solid("#333355"):
                xsize 740
                ysize 1
                xalign 0.5

            null height 6

            # Tombol Jawab
            if rb_group.selected:
                textbutton "▶  Jawab":
                    action Return()
                    xalign 0.5
                    xsize 200
                    ysize 46
                    background "#2ECC71"
                    text_color "#FFFFFF"
                    text_size 21
                    hover_background "#27AE60"
            else:
                text "— Pilih salah satu jawaban —":
                    xalign 0.5
                    color "#666688"
                    size 17


# ============================================================
# SCREEN: Feedback setelah menjawab
# ============================================================
screen quiz_feedback(is_correct, explanation):
    modal True
    add "#000000CC"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 680
        padding (44, 36)
        background "#1A1A2E"

        vbox:
            spacing 16
            xalign 0.5

            if is_correct:
                text "✓  BENAR!":
                    size 34
                    color "#2ECC71"
                    xalign 0.5
            else:
                text "✗  SALAH":
                    size 34
                    color "#E74C3C"
                    xalign 0.5

            add Solid("#333355"):
                xsize 580
                ysize 1
                xalign 0.5

            text explanation:
                size 19
                color "#E0E0E0"
                xalign 0.5
                text_align 0.5
                layout "subtitle"

            null height 10

            textbutton "Lanjutkan →":
                action Return()
                xalign 0.5
                xsize 190
                ysize 44
                background "#3A3A5E"
                hover_background "#5555AA"
                text_color "#FFFFFF"
                text_size 20


# ============================================================
# SCREEN: Hasil Akhir Quiz
# ============================================================
screen quiz_result(score, total, bonus_sanity, bonus_frs):
    modal True
    add "#000000CC"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 580
        padding (50, 40)
        background "#1A1A2E"

        vbox:
            spacing 18
            xalign 0.5

            text "— Hasil Ujian —":
                size 26
                color "#FFD700"
                xalign 0.5

            add Solid("#FFD70055"):
                xsize 460
                ysize 2
                xalign 0.5

            text "[score] / [total] Jawaban Benar":
                size 34
                color "#FFFFFF"
                xalign 0.5

            null height 4

            if bonus_sanity > 0:
                text "+ [bonus_sanity]  Sanity":
                    size 21
                    color "#2ECC71"
                    xalign 0.5
            elif bonus_sanity < 0:
                text "[bonus_sanity]  Sanity":
                    size 21
                    color "#E74C3C"
                    xalign 0.5

            if bonus_frs != 0:
                text "+ [bonus_frs]  Friendship Stevia":
                    size 21
                    color "#FFB6C1"
                    xalign 0.5

            null height 10

            textbutton "Selesai":
                action Return()
                xalign 0.5
                xsize 160
                ysize 44
                background "#3A3A5E"
                hover_background "#5555AA"
                text_color "#FFFFFF"
                text_size 20
