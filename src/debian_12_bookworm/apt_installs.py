from _common import *

apt_installs = get_arg("--apt-install")

# required installes for Rorbian
run_command(
    "sudo apt install -yq gnome-shell-extensions gnome-tweaks wget gpg apt-transport-https ca-certificates curl terminator git lsb-release fasttrack-archive-keyring"
)
run_command(
    'echo "deb http://deb.debian.org/debian $(lsb_release -cs)-backports main contrib" | sudo tee /etc/apt/sources.list.d/backports.list'
)
run_command(
    'echo "deb http://fasttrack.debian.net/debian-fasttrack/ $(lsb_release -cs)-fasttrack main contrib" | sudo tee /etc/apt/sources.list.d/fasttrack.list'
)
run_command(
    'echo "deb http://fasttrack.debian.net/debian-fasttrack/ $(lsb_release -cs)-backports-staging main contrib" | sudo tee -a /etc/apt/sources.list.d/fasttrack.list'
)
run_command("sudo apt update")

if apt_installs:
    installables = apt_installs.replace("--apt-install=", "").replace(",", " ")
    run_command(f"sudo apt-get install -yq {installables}")
