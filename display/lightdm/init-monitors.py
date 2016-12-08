#!/usr/bin/env python3
import fileinput
import subprocess

##
## Global constants
## These values might change from system to system, or from version to version
##
LID_DISPLAY = 'eDP-1'
PRIMARY_DISPLAYS = ['HDMI3', 'HDMI-3']
LID_STATE_OPEN = 'open'
LID_STATE_FILE = '/proc/acpi/button/lid/LID0/state'
LID_STATE_LINE_START = 'state:'
# 0-based indexing...
LID_STATE_START_POS = 12

##
## Script
##

class Lid:
    def __init__(self, lid_state):
        self.lid_state = lid_state

    def is_open(self):
        return self.lid_state == LID_STATE_OPEN

    @classmethod
    def read_state(cls):
        lid_state = None
        with fileinput.input(files=(LID_STATE_FILE)) as f:
            for line in f:
                if line.startswith(LID_STATE_LINE_START):
                    lid_state = line[LID_STATE_START_POS:]
                    break
        return Lid(lid_state)

class Monitors:
    def __init__(self):
        pass

    @classmethod
    def read_state(cls):
        pass

lid = Lid.read_state()
monitors = Monitors.read_state()
