from _common import *

apt_installs = get_arg("--apt-install")

# required installes for Rorbian
run_command("sudo apt install -yq gnome-shell-extensions gnome-tweaks wget gpg apt-transport-https ca-certificates curl")

if apt_installs:
    installables = apt_installs.replace("--apt-install=", "").replace(",", " ")
    run_command(f"sudo apt-get install -yq {installables}")
