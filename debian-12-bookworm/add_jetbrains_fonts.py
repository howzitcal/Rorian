from _common import *

if get_arg("--jetbrains-mono"):
    run_command(
        "wget https://raw.githubusercontent.com/calobyte/nubuntu/refs/heads/main/fonts/jetbrains-fonts.tar -O ./jetbrains-fonts.tar"
    )
    run_command(
        'sudo tar -xf ./jetbrains-fonts.tar -C /usr/share/fonts/truetype/ --wildcards "*.ttf"'
    )
    run_command("c-cache -f")
    run_command(
        "gsettings set org.gnome.desktop.interface monospace-font-name 'Jetbrains Mono 13'"
    )
