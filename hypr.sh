#!/bin/bash

r=$1
xres=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1)
yres=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2)
nxres=$(echo $(echo $xres \* $r +0.5| bc) / 1 | bc)
nyres=$(echo $(echo $yres \* $r +0.5| bc) / 1 | bc)
output=$(xrandr --current | grep ' connected' | uniq | awk '{print $1}' | cut -d ' ' -f1)
xrandr --output $output --mode $xres"x"$yres --scale $r"x"$r --panning $nxres"x"$nyres
