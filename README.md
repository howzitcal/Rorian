# rorian

Python script to setup debian

```shell
sudo apt-get install -yq curl python3 && curl -s https://raw.githubusercontent.com/calobyte/rorian/refs/heads/main/dist/debian_12_bookworm.py | python3 - \
--apt-install=aria2,htop \
--install-flatpaks=com.bitwarden.desktop,org.localsend.localsend_app,com.usebruno.Bruno,com.ultimaker.cura,com.obsproject.Studio,com.github.xournalpp.xournalpp,org.kde.kdenlive,page.kramo.Sly,org.onlyoffice.desktopeditors \
--debloat-gnome \
--install-vscode \
--install-chrome \
--install-docker \
--louder \
--hot-corners \
--show-batt \
--better-window-buttons \
--dock \
--jetbrains-mono \
--tidy-menu \
--dark-theme \
--add-menu-folder=Dev:dev \
--add-menu-folder-items=dev:code.desktop
```
