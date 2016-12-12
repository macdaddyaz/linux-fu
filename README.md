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
