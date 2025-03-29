#!/usr/bin/env bash

COLORSCHEME=DoomOne

### AUTOSTART PROGRAMS ###
# lxsession &
picom --daemon &
nm-applet &
# "$HOME"/.local/bin/apartmen_mod.sh &

"$HOME"/.screenlayout/home.sh &
sleep 1
# conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."
