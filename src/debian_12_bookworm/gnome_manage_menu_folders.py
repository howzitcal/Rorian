from _common import *
from gnome_menu_common import add_folder_to_menu, add_items_to_folder

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

for folder in add_folders:
    [folder_name, folder_id] = folder
    add_folder_to_menu(folder_name, folder_id)


for folder_apps in add_folder_items:
    [folder_id, folder_apps] = folder_apps

    add_items_to_folder(folder_id, folder_apps.split(","))
