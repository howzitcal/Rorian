from _common import *

if get_arg("--install-flatpaks"):
    run_command('sudo apt-get install -yq flatpak gnome-software-plugin-flatpak')
    run_command('sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')

    flatpaks = get_arg("--install-flatpaks").replace("--install-flatpaks=", "").split(",")

    for flatpak in flatpaks:
        run_command(f"sudo flatpak install --noninteractive -y {flatpak}")