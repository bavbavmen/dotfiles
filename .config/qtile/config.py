import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
import colors

from general_configs import *
from keys import keys
from groups import groups
from layout import layouts, floating_layout
from bar import *



extension_defaults = widget_defaults.copy()

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
    wifi_name = subprocess.check_output("sleep 1; nmcli -t -f active,ssid dev wifi | egrep '^yes'")
    wifi_name = wifi_name.lower()
    if "seven" in wifi_name:
        subprocess.call([home + '/.screenlayout/apartment.sh'])
    elif "pixel" in wifi_name:
        subprocess.call([home + '/.screenlayout/leptop.sh'])
    else:
        subprocess.call([home + '/.screenlayout/home.sh'])




wmname = "LG3D"
