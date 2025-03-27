from _common import *


if get_arg("--dock"):
    run_command(
        'gdbus call --session --dest org.gnome.Shell.Extensions --object-path /org/gnome/Shell/Extensions --method org.gnome.Shell.Extensions.InstallRemoteExtension "dash-to-dock@micxgx.gmail.com"',
        False,
        False,
    )

    run_command(
        "gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false"
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
