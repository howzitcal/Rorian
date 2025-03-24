from _common import *

get_arg("--show-batt") and run_command('gsettings set org.gnome.desktop.interface show-battery-percentage true')
get_arg("--hot-corners") and run_command('gsettings set org.gnome.desktop.interface enable-hot-corners true')
get_arg("--louder") and run_command('gsettings set org.gnome.desktop.sound allow-volume-above-100-percent true')
get_arg("--better-window-buttons") and run_command("gsettings set org.gnome.desktop.wm.preferences button-layout 'appmenu:minimize,maximize,close'")

if get_arg("--dark-theme"):
    run_command("gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'")
    run_command("gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'")

    if get_arg("--install-flatpaks"):
        run_command("sudo flatpak install  --noninteractive -y org.gtk.Gtk3theme.Adwaita-dark")
        run_command("sudo flatpak override --env=GTK_THEME=Adwaita-dark")