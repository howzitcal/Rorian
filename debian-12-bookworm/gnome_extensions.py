from _common import *

if get_arg("--dock"):
    run_command(
        "wget -c https://github.com/micheleg/dash-to-dock/releases/latest/download/dash-to-dock@micxgx.gmail.com.zip -O ./dash-to-dock.zip"
    )
    run_command("gnome-extensions install ./dash-to-dock.zip")
