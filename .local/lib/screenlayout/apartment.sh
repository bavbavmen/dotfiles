#!/bin/sh
xrandr --output eDP-1 --mode 1920x1080 --pos 2560x280 --rotate normal --output DP-1 --off --output DP-2 --off --output HDMI-1 --off --output HDMI-1-0 --primary --mode 2560x1440 --pos 0x0 --rotate normal
export WALLPAP=$(find ~/Pictures/wallpaper/light -type f | shuf -n 1)
sleep 1
nitrogen --set-zoom-fill $WALLPAP --head=1
nitrogen --set-zoom-fill $WALLPAP --head=0
sleep 2
