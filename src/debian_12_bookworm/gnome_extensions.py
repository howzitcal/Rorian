from _common import *


if get_arg("--dock"):
    run_command(
        'gdbus call --session --dest org.gnome.Shell.Extensions --object-path /org/gnome/Shell/Extensions --method org.gnome.Shell.Extensions.InstallRemoteExtension "dash-to-dock@micxgx.gmail.com" || true'
    )

# https://unsplash.com/photos/DjlKxYFJlTc/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzQyODQ2MTA2fA&force=true&w=2400
