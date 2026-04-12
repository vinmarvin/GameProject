# Copyright 2026 CuteShadow
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# 
#
# Ren'Py Layered Image Visual Editor V3: 1.0
#
# https://cuteshadow.itch.io/layeredimage-visual-editor-v3


#################################################
## CODE
#################################################

init python in director:

    ## Organise a layeredimage.
    def get_ordered_layeredimage_attributes():
        exp_lys_format = {}

        # First, initialise the groups the layeredimage has.
        for group_att in renpy.get_registered_image(state.tag).attributes:
            exp_lys_format[group_att.group] = []

        # Second, add each attribute to each group.
        for group_att in renpy.get_registered_image(state.tag).attributes:
            exp_lys_format[group_att.group].append(group_att.attribute)

        return exp_lys_format


## NEW!
## Image attributes for layeredimages but organised.
screen director_layeredimage_attributes():
    hbox xalign 0.5:
        for group, attributes in director.get_ordered_layeredimage_attributes().items():

            null width 10

            vbox:
                spacing 5

                text "[group!c]" underline True size 26 color "#525252"

                for t in attributes:
                    textbutton "[t!l]":
                        action director.ToggleAttribute(t)
                        alternate director.ToggleNegativeAttribute(t)
                        style "director_button"
                        ypadding 0
                        text_size 26
                        text_hover_color "#346dff"

            # A line.
            null width 8
            add Solid("#b6b6b6", xsize=1, ysize=200) yoffset 10


## The image attributes picker.
screen director_attributes(state):

    vbox:
        xfill True

        use director_statement(state)

        # Special case.
        if isinstance(renpy.get_registered_image(state.tag), LayeredImage):
            
            # NEW!
            # The attributes organised.
            use director_layeredimage_attributes

        else:

            # Normal stuff.
            use director_choices(_("Attributes:")):

                for t in director.get_attributes():
                    textbutton "[t]":
                        action director.ToggleAttribute(t)
                        alternate director.ToggleNegativeAttribute(t)
                        style "director_button"
                        ypadding 0

    # REARRANGED!
        null height 8

        # A line.
        add Solid("#b6b6b6", xysize=(1.0,1)) xalign 0.5

        use director_footer(state)

        null height 20

    text _("Click to toggle attribute, \nright-click to toggle negative attribute.") color "#777777" yoffset -20 at left

    text "[renpy.last_say().who] \"[renpy.last_say().what]\"" color "#4b4b4b" italic True at topright


## NEW!
## The shortcut button that skips to the attributes
## of the currently speaking character.
screen durector_attribute_shortcut(state):
    default add_action = state.lines[-1][2]
    
    textbutton "☻ show [renpy.get_say_image_tag()]...":
        xpos gui._scale(300) - 1
        xanchor 0
        style "director_edit_button"
        xsize 1920
        text_layout "nobreak"
        text_size 20
        text_xalign 0.0
        background "#00000017"
        action add_action, director.SetKind("show"), director.SetTag(renpy.get_say_image_tag())


## The script preview.
screen director_lines(state):

    frame:
        style "empty"
        background Solid("#fff8", xsize=20, xpos=gui._scale(300))

        has vbox:
            xfill True

        viewport:
            scrollbars "vertical"
            ymaximum director.viewport_height
            mousewheel True
            yinitial 1.0
            viewport_yfill False

            has vbox:
                xfill True

            for line_pos, line_text, add_action, change_action in state.lines:

                fixed:
                    yfit True
                    textbutton "+":
                        xpos gui._scale(300)
                        action add_action
                        style "director_edit_button"
                        alt ("add before " + line_text)

                # NEW!
                # The shortcut button skips to the end.
                if renpy.get_say_image_tag() and line_pos==state.lines[-1][0]:
                    use durector_attribute_shortcut(state)

                fixed:
                    yfit True

                    text "[line_pos]":
                        xpos (gui._scale(300) - 10)
                        xanchor 1.0
                        textalign 1.0
                        style "director_text"

                    if change_action:
                        textbutton "✎":
                            action change_action
                            xpos gui._scale(300)
                            style "director_edit_button"
                            alt ("change " + line_text)

                    frame:
                        style "empty"
                        left_padding (gui._scale(300) + 30)

                        text "[line_text!q]" style "director_text"

        null height 14

        fixed:
            yfit True

            hbox:
                xpos (gui._scale(300) + 30)

                textbutton _("Done"):
                    action director.Stop()
                    style "director_action_button"

            use director_move_button()


## The buttons that modify the script.
## Just changed some colors pretty much.
screen director_footer(state):

    null height 14

    fixed:
        yfit True

        hbox style_prefix "director_action":
            xalign 0.5
            spacing 26

            # Remove button.
            if state.change:
                textbutton _("Remove") action director.Remove() text_idle_color "#6d0000"  text_hover_color "#510000"

            # Change/add button.
            if state.change:
                textbutton _("Change") action director.Commit() text_idle_color "#006d02" text_hover_color "#004b01"
            else:
                textbutton _("Add") action director.Commit() text_idle_color "#006d02" text_hover_color "#004b01"

            # Cancel.
            textbutton _("↵Cancel") action director.Cancel()

        # The button that moves the entire director to the top or bottom.
        use director_move_button()
