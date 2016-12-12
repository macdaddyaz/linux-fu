#!/bin/sh
# Hook systemd to ensure that PM script is executed
# $ sudo cp systemd-wifi-resume.sh /lib/systemd/system-sleep/wifi-resume
# $ sudo chown root.root /lib/systemd/system-sleep/wifi-resume
# $ sudo chmod 0755 /lib/systemd/system-sleep/wifi-resume

set -e

if [ "$2" = "suspend" ] || [ "$2" = "hybrid-sleep" ]; then
    case "$1" in
        pre)
            # do nothing
            :
            ;;
        post)
            /etc/pm/sleep.d/75_wifi-resume resume
            ;;
    esac
fi
