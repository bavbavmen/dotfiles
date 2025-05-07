import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
import colors

from keys import keys
from general_configs import *

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
            # mod1 + cntl + letter of group = switch to group and move focused window
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Move focused window to group and follow {}".format(i.name),
            ),
        ]
    )

