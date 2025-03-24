from _common import *
from gnome_manage_menu_folders import add_folder_to_menu, add_items_to_folder

if get_arg("--tidy-menu"):
    add_folder_to_menu("Accessories", "accessories")
    add_folder_to_menu("Utils", "utils")
    add_folder_to_menu("UI", "ui")
    add_folder_to_menu("System", "system")

    add_items_to_folder(
        "utils",
        [
            "org.gnome.Characters.desktop",
            "org.gnome.font-viewer.desktop",
            "org.gnome.Cheese.desktop",
            "teminator.desktop",
        ],
    )

    add_items_to_folder(
        "accessories",
        [
            "org.gnome.TextEditor.desktop",
            "org.gnome.FileRoller.desktop",
            "org.gnome.SoundRecorder.desktop",
            "org.gnome.eog.desktop",
            "org.gnome.Calendar.desktop",
            "org.gnome.Evince.desktop",
            "org.gnome.clocks.desktop",
            "org.gnome.Contacts.desktop",
            "simple-scan.desktop",
            "org.gnome.Calculator.desktop",
        ],
    )

    add_items_to_folder(
        "system",
        [
            "org.gnome.DiskUtility.desktop",
            "org.gnome.seahorse.Application.desktop",
            "nm-connection-editor.desktop",
            "org.gnome.baobab.desktop",
            "org.gnome.Logs.desktop",
            "software-properties-gtk.desktop",
            "im-config.desktop",
            "org.gnome.Settings.desktop",
            "gnome-system-monitor.desktop",
        ],
    )

    add_items_to_folder(
        "ui", ["org.gnome.tweaks.desktop", "org.gnome.Extensions.desktop"]
    )
