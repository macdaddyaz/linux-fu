#!/usr/bin/env python3
import fileinput
import re
import subprocess
import unittest

LID_DISPLAY = 'eDP-1'
PRIMARY_DISPLAYS = ('HDMI3', 'HDMI-3')
PRIMARY_POS = '0x0'
SECONDARY_POS = '1920x0'
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
        self.is_open = self.lid_state == LID_STATE_OPEN
        self.is_closed = not self.is_open

    @classmethod
    def read_state(cls):
        lid_state = None
        with fileinput.input(files=(LID_STATE_FILE)) as f:
            for line in f:
                if line.startswith(LID_STATE_LINE_START):
                    lid_state = line[LID_STATE_START_POS:].strip()
                    break
        return Lid(lid_state)


class Monitor:
    def __init__(self, monitor_line):
        self.monitor_line = monitor_line
        matches = re.search(r'([0-9]{1,2}): [\S]* ([\d]{3,4})/[\d]{3,4}x([\d]{3,4})/[\d]{3,4}\+([\d]{1,4})\+([\d]{1,4})[\s]*([\S]*)',
                            self.monitor_line)
        self.num = matches.group(1)
        self.output = matches.group(6)
        self.resolution = '{0}x{1}'.format(matches.group(2), matches.group(3))
        self.position = '{0}x{1}'.format(matches.group(4), matches.group(5))

    def __str__(self):
        return self.monitor_line

    def __repr__(self):
        return self.__str__()

    @classmethod
    def read_state(cls):
        xrandr = subprocess.run(['xrandr', '--listmonitors'], universal_newlines=True, stdout=subprocess.PIPE, check=True)
        output = xrandr.stdout
        lines = output.splitlines()
        monitors = [Monitor(l.strip()) for l in lines[1:]]
        return {m.output: m for m in monitors}


def build_xrandr_commands(lid, monitors):
    count = len(monitors)
    commands = []
    for i in range(count):
        command = []
        commands.append(command)
        output = monitors[i].output
        command.extend(['xrandr', '--output', output, '--rotate', 'normal', '--mode', monitors[i].resolution])
        if (lid.is_open and output == LID_DISPLAY) or (lid.is_closed and output in PRIMARY_DISPLAYS):
            command.append('--primary')
        else:
            pass
    return commands


lid = Lid.read_state()
print('lid is {0}'.format(lid.lid_state))
monitors = Monitor.read_state()
print(monitors)

xrandr_commands = build_xrandr_commands(lid, monitors)
for command in xrandr_commands:
    # subprocess.run(cmd)
    print(command)


class CommandTest(unittest.TestCase):
    def test_only_lid(self):
        pass

    def test_only_dual_external(self):
        pass

    def test_lid_and_dual_external(self):
        pass

    def test_only_single_external(self):
        pass
