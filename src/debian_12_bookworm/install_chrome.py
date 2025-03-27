from _common import *

if get_arg("--install-chrome"):
    run_command(
        "wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O ./chrome.deb"
    )
    run_command("sudo apt-get install -yq ./chrome.deb")
    run_command("rm ./chrome.deb")
