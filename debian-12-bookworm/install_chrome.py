from _common import *

if get_arg("--install-chrome"):
    run_command(
        "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O ./chrome.deb"
    )
    run_command("sudo apt install -yq ./chrome.deb")
    run_command("rm ./chrome.deb")
