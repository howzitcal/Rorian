from _common import *

apt_removes = get_arg("--apt-remove")

if apt_removes:
    removeables = apt_removes.replace("--apt-remove=", "").replace(",", " ")
    run_command(f"sudo apt-get remove -yq {removeables}")