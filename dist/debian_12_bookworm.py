import os
import sys
import datetime

args = sys.argv


def run_command(command, op=False, can_fail=False):
    log(f"RUNNING COMMAND: '{command}'")
    if not op:
        if os.system(command) != 0 and can_fail == False:
            log(f"COMMAND '{command}' FAILED.", True)
            raise SystemError(f"Command '{command}' failed.")
        log(f"COMMAND '{command}' RAN SUCCESSFULLY.")
    else:
        output = os.popen(command)
        log(f"COMMAND '{command}' RAN.")
        return output.read()


def log(message, error=False):
    print(f"[{'LOG' if not error else 'ERROR'}][{datetime.datetime.now()}][{message}]")


def get_arg(check):
    for arg in args:
        if arg.startswith(check):
            return arg
    return False

######
# FILE: gnome_menu_common
######


def add_folder_to_menu(folder_name, folder_id):
    reg_folders = run_command(
        "gsettings get org.gnome.desktop.app-folders folder-children", True
    )
    reg_folders = (
        reg_folders.replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("\n", "")
        .split(", ")
    )

    if folder_id not in reg_folders:
        run_command(
            f"gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ name {folder_name}"
        )
        run_command(
            f'gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ apps "[]"'
        )

        reg_folders.append(folder_id)
        folders_string = ", ".join([f"'{folder}'" for folder in reg_folders])
        run_command(
            f'gsettings set org.gnome.desktop.app-folders folder-children "[ {folders_string} ]"'
        )
        log(f"Gnome Menu Folder {folder_name}:{folder_id} created.")
    else:
        log(f"{folder_name}:{folder_id} already registered.")


def add_items_to_folder(folder_id, folder_apps):
    apps_in_folder = run_command(
        "gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ apps",
        True,
    )
    apps_in_folder = (
        apps_in_folder.replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("\n", "")
        .split(", ")
    )

    for app in folder_apps:
        if app not in apps_in_folder:
            apps_in_folder.append(app)
            apps_in_folder_string = ", ".join([f"'{app}'" for app in apps_in_folder])
            run_command(
                f'gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ apps "[ {apps_in_folder_string} ]"'
            )
            log(f"App {app} added to Folder:{folder_id}.")
        else:
            log(f"App {app} already in Folder:{folder_id}.")

######
# FILE: apt_update_upgrade
######

run_command("sudo apt-get update")
run_command("sudo apt-get upgrade -yq")
######
# FILE: apt_installs
######

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

######
# FILE: apt_removes
######

apt_removes = get_arg("--apt-remove")

if apt_removes:
    removeables = apt_removes.replace("--apt-remove=", "").replace(",", " ")
    run_command(f"sudo apt-get remove -yq {removeables}")

######
# FILE: gnome_debloat
######

if get_arg("--debloat-gnome"):
    run_command(
        """
    sudo apt-get remove -yq \
        gnome-games \
        gnome-maps \
        synaptic \
        libreoffice* \
        gnome-music* \
        rhythmbox* \
        yelp \
        transmission-* \
        firefox* \
        evolution \
        totem \
        gnome-weather \
        shotwell-* \
        gnome-terminal \
        gnome-console
    """
    )
    run_command("sudo apt-get autoremove -yq")

######
# FILE: install_chrome
######

if get_arg("--install-chrome"):
    run_command(
        "wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O ./chrome.deb"
    )
    run_command("sudo apt-get install -yq ./chrome.deb")
    run_command("rm ./chrome.deb")

######
# FILE: install_docker
######

if get_arg("--install-docker"):
    run_command(
        "for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove -yq $pkg; done"
    )

    # Add Docker's official GPG key:
    run_command("sudo apt-get update")
    run_command("sudo install -m 0755 -d /etc/apt/keyrings")
    run_command(
        "sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc"
    )
    run_command("sudo chmod a+r /etc/apt/keyrings/docker.asc")

    # Add the repository to Apt sources:
    run_command(
        'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null'
    )
    run_command("sudo apt-get update")

    run_command(
        "sudo apt-get install -yq docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
    )
    run_command("sudo usermod -aG docker $USER")

######
# FILE: install_vscode
######

if get_arg("--install-vscode"):
    run_command(
        'echo "code code/add-microsoft-repo boolean true" | sudo debconf-set-selections'
    )
    run_command(
        "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg"
    )
    run_command(
        "sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg"
    )
    run_command(
        'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null'
    )
    run_command("rm -f packages.microsoft.gpg")
    run_command("sudo apt-get update")
    run_command("sudo apt-get install -yq code")

######
# FILE: flatpak_install
######

if get_arg("--install-flatpaks"):
    run_command('sudo apt-get install -yq flatpak gnome-software-plugin-flatpak')
    run_command('sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')

    flatpaks = get_arg("--install-flatpaks").replace("--install-flatpaks=", "").split(",")

    for flatpak in flatpaks:
        run_command(f"sudo flatpak install --noninteractive -y {flatpak}")
######
# FILE: add_jetbrains_fonts
######

if get_arg("--jetbrains-mono"):
    run_command(
        "wget https://raw.githubusercontent.com/calobyte/rorian/refs/heads/main/public/fonts/jetbrains-fonts.tar -O ./jetbrains-fonts.tar"
    )
    run_command(
        'sudo tar -xf ./jetbrains-fonts.tar -C /usr/share/fonts/truetype/ --wildcards "*.ttf"'
    )
    run_command("fc-cache -f")
    run_command(
        "gsettings set org.gnome.desktop.interface monospace-font-name 'Jetbrains Mono 13'"
    )
    run_command("rm ./jetbrains-fonts.tar")

######
# FILE: gnome_manage_menu_folders
######

add_folders = [
    folder.replace("--add-menu-folder=", "").split(":")
    for folder in args
    if folder.startswith("--add-menu-folder=")
]
add_folder_items = [
    folder.replace("--add-menu-folder-items=", "").split(":")
    for folder in args
    if folder.startswith("--add-menu-folder-items=")
]

for folder in add_folders:
    [folder_name, folder_id] = folder
    add_folder_to_menu(folder_name, folder_id)


for folder_apps in add_folder_items:
    [folder_id, folder_apps] = folder_apps

    add_items_to_folder(folder_id, folder_apps.split(","))

######
# FILE: gnome_tidy_menu
######

if get_arg("--tidy-menu"):
    run_command('gsettings set org.gnome.desktop.app-folders folder-children "[]"')
    add_folder_to_menu("Accessories", "accessories")
    add_folder_to_menu("Utils", "utils")
    add_folder_to_menu("UI", "ui")
    add_folder_to_menu("System", "system")

    add_items_to_folder(
        "utils",
        [
            "org.gnome.Characters.desktop",
            "org.gnome.font-viewer.desktop",
            "org.gnome.Cheese.desktop",
            "terminator.desktop",
        ],
    )

    add_items_to_folder(
        "accessories",
        [
            "org.gnome.TextEditor.desktop",
            "org.gnome.FileRoller.desktop",
            "org.gnome.SoundRecorder.desktop",
            "org.gnome.eog.desktop",
            "org.gnome.Calendar.desktop",
            "org.gnome.Evince.desktop",
            "org.gnome.clocks.desktop",
            "org.gnome.Contacts.desktop",
            "simple-scan.desktop",
            "org.gnome.Calculator.desktop",
        ],
    )

    add_items_to_folder(
        "system",
        [
            "org.gnome.DiskUtility.desktop",
            "org.gnome.seahorse.Application.desktop",
            "nm-connection-editor.desktop",
            "org.gnome.baobab.desktop",
            "org.gnome.Logs.desktop",
            "software-properties-gtk.desktop",
            "im-config.desktop",
            "org.gnome.Settings.desktop",
            "gnome-system-monitor.desktop",
        ],
    )

    add_items_to_folder(
        "ui", ["org.gnome.tweaks.desktop", "org.gnome.Extensions.desktop"]
    )

######
# FILE: gnome_enhancements
######

get_arg("--show-batt") and run_command('gsettings set org.gnome.desktop.interface show-battery-percentage true')
get_arg("--hot-corners") and run_command('gsettings set org.gnome.desktop.interface enable-hot-corners true')
get_arg("--louder") and run_command('gsettings set org.gnome.desktop.sound allow-volume-above-100-percent true')
get_arg("--better-window-buttons") and run_command("gsettings set org.gnome.desktop.wm.preferences button-layout 'appmenu:minimize,maximize,close'")

if get_arg("--dark-theme"):
    run_command("gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'")
    run_command("gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'")

    if get_arg("--install-flatpaks"):
        run_command("sudo flatpak install  --noninteractive -y org.gtk.Gtk3theme.Adwaita-dark")
        run_command("sudo flatpak override --env=GTK_THEME=Adwaita-dark")
######
# FILE: gnome_extensions
######


if get_arg("--dock"):
    run_command(
        'gdbus call --session --dest org.gnome.Shell.Extensions --object-path /org/gnome/Shell/Extensions --method org.gnome.Shell.Extensions.InstallRemoteExtension "dash-to-dock@micxgx.gmail.com"',
        False,
        True,
    )

    run_command(
        "gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 40"
    )
    run_command(
        "gsettings set org.gnome.shell.extensions.dash-to-dock dock-position 'BOTTOM'"
    )
    run_command(
        "gsettings set org.gnome.shell.extensions.dash-to-dock multi-monitor true"
    )
    run_command(
        "gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'previews'"
    )
    run_command(
        "gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed false"
    )

# https://unsplash.com/photos/DjlKxYFJlTc/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzQyODQ2MTA2fA&force=true&w=2400
