# ==========================================
# QUIZ SYSTEM — UI SCREEN & PYTHON UTILITIES
# ==========================================

init -1 python:

    _quiz_correct = 0
    _quiz_total   = 0

    def _quiz_reset():
        global _quiz_correct, _quiz_total
        _quiz_correct = 0
        _quiz_total   = 0

    def _quiz_record(is_correct):
        global _quiz_correct, _quiz_total
        _quiz_total += 1
        if is_correct:
            _quiz_correct += 1

    def _quiz_get_result():
        if _quiz_total == 0:
            return (0, 0, 0)
        pct = int(_quiz_correct * 100 / _quiz_total)
        return (_quiz_correct, _quiz_total, pct)


# ==========================================
# STYLES
# ==========================================

style quiz_outer_frame is frame:
    background "#0e0e2eee"
    padding (28, 20, 28, 20)

style quiz_inner_q_frame is frame:
    background "#08082299"
    padding (18, 14)
    xfill True

style quiz_sep is frame:
    background "#FFD70066"
    ysize 2
    xfill True

style quiz_choice_btn is button:
    background "#1a1a5a"
    hover_background "#3535cc"
    padding (14, 10)
    xsize 480
    ysize 68

style quiz_choice_btn_text is button_text:
    color "#EEEEEE"
    hover_color "#FFFFFF"
    size 17
    xalign 0.5
    yalign 0.5
    text_align 0.5

style quiz_dialog_frame is frame:
    background "#06061aee"
    padding (24, 14)

style quiz_timer_red is text:
    color "#FF3333"
    bold True
    size 24

style quiz_timer_yel is text:
    color "#FFAA00"
    bold True
    size 24

style quiz_timer_green is text:
    color "#44DD88"
    bold True
    size 24


# ==========================================
# MAIN QUIZ SCREEN — Full Screen Layout
# ==========================================

screen quiz_screen(quiz_name, questions, time_limit, narrations, bg_path="images/bg/quizbg.jpg"):

    default current_q = 0
    default time_left = time_limit

    # ---- Background ----
    add bg_path fit "cover"
    add "#00000099"

    # ---- Timer tick ----
    timer 1.0 repeat True action [
        If(time_left > 1,
           SetScreenVariable("time_left", time_left - 1),
           Return(False))
    ]

    # ============================================================
    # QUIZ BOX — Full screen width, fills most of vertical space
    # ============================================================
    frame:
        style "quiz_outer_frame"
        xpos 15
        ypos 8
        xsize config.screen_width - 30
        ysize config.screen_height - 110

        vbox:
            spacing 12
            xfill True

            # --- Header ---
            hbox:
                xfill True
                text quiz_name:
                    size 26
                    color "#FFD700"
                    bold True
                    xalign 0.0
                text "Soal [current_q + 1] / [len(questions)]":
                    size 17
                    color "#9999CC"
                    xalign 1.0
                    yalign 1.0

            # Separator
            frame:
                style "quiz_sep"

            # --- Question ---
            frame:
                style "quiz_inner_q_frame"
                text questions[current_q]["q"]:
                    size 19
                    color "#FFFFFF"
                    xalign 0.5
                    text_align 0.5

            null height 6

            # --- 2x2 Choices ---
            $ _q = questions[current_q]

            grid 2 2:
                xspacing 24
                yspacing 16
                xalign 0.5

                textbutton _q["c"][0]:
                    style "quiz_choice_btn"
                    action [
                        Function(_quiz_record, 0 == _q["a"]),
                        If(current_q >= len(questions) - 1,
                           Return(True),
                           SetScreenVariable("current_q", current_q + 1))
                    ]

                textbutton _q["c"][1]:
                    style "quiz_choice_btn"
                    action [
                        Function(_quiz_record, 1 == _q["a"]),
                        If(current_q >= len(questions) - 1,
                           Return(True),
                           SetScreenVariable("current_q", current_q + 1))
                    ]

                textbutton _q["c"][2]:
                    style "quiz_choice_btn"
                    action [
                        Function(_quiz_record, 2 == _q["a"]),
                        If(current_q >= len(questions) - 1,
                           Return(True),
                           SetScreenVariable("current_q", current_q + 1))
                    ]

                textbutton _q["c"][3]:
                    style "quiz_choice_btn"
                    action [
                        Function(_quiz_record, 3 == _q["a"]),
                        If(current_q >= len(questions) - 1,
                           Return(True),
                           SetScreenVariable("current_q", current_q + 1))
                    ]

            null height 6

            # --- Timer ---
            $ _tc_style = "quiz_timer_red" if time_left <= 10 else ("quiz_timer_yel" if time_left <= 30 else "quiz_timer_green")

            hbox:
                xalign 0.5
                spacing 12
                text "Sisa Waktu:":
                    size 20
                    color "#AAAACC"
                    yalign 0.5
                text "[time_left] detik":
                    style _tc_style
                    yalign 0.5

    # ============================================================
    # DIALOG / NARRATION — Pinned to bottom
    # ============================================================
    frame:
        style "quiz_dialog_frame"
        xpos 15
        ypos config.screen_height - 100
        xsize config.screen_width - 30
        ysize 92

        if current_q < len(narrations):
            text narrations[current_q]:
                size 16
                color "#CCCCEE"
                xalign 0.5
                yalign 0.5
                text_align 0.5
                italic True
        else:
            text "...":
                size 16
                color "#CCCCEE"
                xalign 0.5
                yalign 0.5
