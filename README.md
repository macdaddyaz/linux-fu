# Linux-Fu

Just a bunch of customizations and tweaks I've made to my Linux
workstation.

## LightDM

The tweaks to the LightDM display manager are under `display/lightdm`.

Copy everything in that directory to `/etc/lightdm`, and make sure it is
all owned by `root`. Make sure the Python script is executable by
`root`, and you have Python 3 in your path.

## WiFi on Resume

There are some scripts to ensure that WiFi works after the system
resumes from sleep or hibernate. They are located under `power/wifi`.
See the individual scripts for installation instructions, or run the
`install.sh` script.

## Sudoers to recover from VPN crashes

When the VPN crashes, and the user is authenticated via Active Directory
(via Samba), then it can be difficult to recover. The VPN agent gets stuck
with a broken connection to the VPN. In order to sever that connection and
reset the VPN, `sudo` must be used. However, `sudo` attempts to contact the
domain controller over the broken VPN. This process takes a very long time,
both to prompt the user for the password, then to execute the command.

To help alleviate the difficulty, I tweaked the sudoers to allow recovery
commands without prompting for a password:

```
$ sudo systemctl restart vpnagentd.service
$ sudo killall vpnagentd
```

One or both of these can be used to reset the VPN agent back to a state
where the VPN can be reconnected. Since no password is needed, then executing
the commands should be at least somewhat faster, and typing your password wrong
won't extend the process.
