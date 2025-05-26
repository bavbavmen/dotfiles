from libqtile import bar, widget
from libqtile.config import Screen
from general_configs import colors

widget_defaults = dict(
    font="Hack Nerd Font Bold", fontsize=12, padding=1, background=colors["mantle"]
)


def init_widgets_list():
    return [
        widget.Spacer(length=8),
        # widget.Image(
        #          filename = "~/.config/qtile/icons/infinity-icon.png",
        #          scale = "False",
        #          mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
        #          ),
        widget.Prompt(
            font="Hack Nerd Font Mono", fontsize=14, foreground=colors["blue"]
        ),
        widget.GroupBox(
            fontsize=15,
            margin_y=6,
            margin_x=1,
            padding_y=1,
            padding_x=2,
            borderwidth=2,
            active=colors["lavender"],
            inactive=colors["overlay0"],
            rounded=False,
            highlight_color=colors["base"],
            highlight_method="line",
            this_current_screen_border=colors["sky"],
            this_screen_border=colors["sky"],
            other_current_screen_border=colors["base"],
            other_screen_border=colors["overlay0"],
        ),
        widget.TextBox(
            text="|",
            font="Hack Nerd Font Mono",
            foreground=colors["overlay0"],
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayout(
            foreground=colors["blue"],
            padding=5,
        ),
        widget.TextBox(
            text="|",
            font="Hack Nerd Font Mono",
            foreground=colors["overlay0"],
            padding=2,
            fontsize=14,
        ),
        # widget.TextBox(
        #          text = '|',
        #          font = "Hack Nerd Font Mono",
        #          foreground = colors["overlay0"],
        #          padding = 2,
        #          fontsize = 14
        #          ),
        widget.WindowName(foreground=colors["text"], padding=4, max_chars=40),
        widget.Spacer(length=bar.STRETCH),
        widget.Clock(
            foreground=colors["text"],
            padding=6,
            format="%H:%M:%S",
            fontsize=18,
        ),
        widget.Spacer(length=bar.STRETCH),
        widget.Volume(
            foreground=colors["green"],
            padding=6,
            fmt="{}",
        ),
        widget.KeyboardLayout(
            configured_keyboards=["us", "il"],
            foreground=colors["teal"],
            padding=6,
            fmt="{}",
        ),
        widget.Clock(
            foreground=colors["sky"],
            padding=6,
            format="%m/%d",
            fontsize=14,
        ),
        widget.Systray(),
        widget.Spacer(length=8),
    ]


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[-1:-3:-1]
    return widgets_screen2


# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),


def init_screens():
    # return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin=[7, 7, 1, 7], size=28)),
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), margin=[0, 0, 0, 0], size=28)
        ),
        # Screen(top=bar.Bar(widgets=init_widgets_screen2(), margin=[8, 12, 0, 12], size=28)),
        Screen(
            top=bar.Bar(widgets=init_widgets_screen2(), margin=[0, 0, 0, 0], size=28)
        ),
    ]
    # Screen(top=bar.Bar(widgets=init_widgets_screen2(), margin=[7, 7, 1, 7], size=28))]
