from _common import *

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
