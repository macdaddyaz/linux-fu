#!/bin/sh
# Reset wireless interface after resume by unloading and reloading the module
# Adjust $interface and $module as needed
# $ sudo cp pm-wifi-resume.sh /etc/pm/sleep.d/75_wifi-resume
# $ sudo chown root.root /etc/pm/sleep.d/75_wifi-resume
# $ sudo chmod 0755 /etc/pm/sleep.d/75_wifi-resume

# network interface name and module
interface="wlp3s0"
module="iwlwifi"

# syslog tag
tag="wifi-resume"

case $1 in
    hibernate|suspend)
        # do nothing
        :
    ;;
    resume|thaw)
        if [ -z "$(iwgetid --raw ${interface})" ]; then
            modprobe --syslog --remove --remove-dependencies ${module}
            modprobe --syslog ${module}
            logger --tag $tag "${module} reloaded"
            journal_id=$(journalctl --new-id)
            logger --journald <<END
MESSAGE_ID=${journal_id}
MESSAGE=${module} reloaded
PRIORITY=5
END
        fi
        ;;
esac
