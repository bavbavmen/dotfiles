#!/bin/sh

export WALLPAP=$(find ~/Pictures/wallpaper/light -type f | shuf -n 1)
sleep 1
nitrogen --set-zoom-fill $WALLPAP
sleep 2
