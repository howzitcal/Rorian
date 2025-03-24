from _common import *

add_folders = [
    folder.replace("--add-folder=", "").split(":")
    for folder in args
    if folder.startswith("--add-folder=")
]
add_folder_items = [
    folder.replace("--add-folder-items=", "").split(":")
    for folder in args
    if folder.startswith("--add-folder-items=")
]


def add_folder_to_menu(folder_name, folder_id):
    reg_folders = run_command(
        "gsettings get org.gnome.desktop.app-folders folder-children", True
    )
    reg_folders = (
        reg_folders.replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("\n", "")
        .split(", ")
    )

    if folder_id not in reg_folders:
        run_command(
            f"gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ name {folder_name}"
        )
        run_command(
            f'gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ apps "[]"'
        )

        reg_folders.append(folder_id)
        folders_string = ", ".join([f"'{folder}'" for folder in reg_folders])
        run_command(
            f'gsettings set org.gnome.desktop.app-folders folder-children "[ {folders_string} ]"'
        )
        log(f"Gnome Menu Folder {folder_name}:{folder_id} created.")
    else:
        log(f"{folder_name}:{folder_id} already registered.")


def add_items_to_folder(folder_id, folder_items):
    print(folder_id)
    print(folder_items)


for folder in add_folders:
    [folder_name, folder_id] = folder
    add_folder_to_menu(folder_name, folder_id)


for folder in add_folder_items:
    [folder_id, folder_items] = folder
    folder_items = ", ".join(
        [
            f"'{folder_item.lstrip().rstrip()}'"
            for folder_item in folder_items.split(",")
        ]
    )
    add_items_to_folder(folder_id, folder_items)
