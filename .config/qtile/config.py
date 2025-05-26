import os
import subprocess
from libqtile import hook
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from general_configs import mod
from keys import keys
from groups import groups
from layout import layouts, floating_layout
from bar import init_screens

keys = keys
groups = groups
layouts = layouts
floating_layout = floating_layout

if __name__ in ["config", "__main__"]:
    screens = init_screens()

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
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
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])
    wifi_name = subprocess.check_output(
        "sleep 1; nmcli -t -f active,ssid dev wifi | egrep '^yes'"
    )
    wifi_name = wifi_name.lower()
    if "seven" in wifi_name:
        subprocess.call([home + "/.screenlayout/apartment.sh"])
    elif "pixel" in wifi_name:
        subprocess.call([home + "/.screenlayout/leptop.sh"])
    else:
        subprocess.call([home + "/.screenlayout/home.sh"])


wmname = "LG3D"
