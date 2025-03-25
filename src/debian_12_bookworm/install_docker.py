from _common import *

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
