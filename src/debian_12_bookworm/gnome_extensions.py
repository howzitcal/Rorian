from _common import *

run_command("mkdir -p $HOME/.local/share/gnome-shell/extensions/")

if get_arg("--dock"):
    run_command(
        "wget -c https://github.com/micheleg/dash-to-dock/releases/latest/download/dash-to-dock@micxgx.gmail.com.zip -O ./dash-to-dock.zip"
    )
    run_command(
        "unzip -o -q ./dash-to-dock.zip -d $HOME/.local/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com"
    )
    run_command("gnome-extensions enable dash-to-dock@micxgx.gmail.com")
# https://unsplash.com/photos/DjlKxYFJlTc/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzQyODQ2MTA2fA&force=true&w=2400
