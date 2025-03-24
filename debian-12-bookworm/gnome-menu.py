from common import *

args = sys.argv

add_folders = [folder.replace("--add-folder=", "").split(":") for folder in args if folder.startswith("--add-folder=")]
add_folder_items = [folder.replace("--add-folder-items=", "").split(":") for folder in args if folder.startswith("--add-folder-items=")]

def log(message):
    print(f"[LOG]: {message}")

for folder in add_folders:
    [folder_name, folder_id] = folder
    reg_folders = os.popen('gsettings get org.gnome.desktop.app-folders folder-children').read()
    reg_folders = reg_folders.replace("[", "").replace("]", "").replace("'", "").replace("\n","").split(", ")

    if(folder_id not in reg_folders):
        os.system(f'gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ name {folder_name}')
        os.system(f'gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/{folder_id}/ apps "[]"')

        reg_folders.append(folder_id)
        folders_string = ", ".join([f"'{folder}'" for folder in  reg_folders])
        os.system(f'gsettings set org.gnome.desktop.app-folders folder-children "[ {folders_string} ]"')
        log(f"Gnome Menu Folder {folder_name}:{folder_id} created.")
    else:
        log(f"{folder_name}:{folder_id} already registered.")


for folder in add_folder_items:
    [folder_id, folder_items] = folder
    folder_items = ", ".join([f"'{folder_item.lstrip().rstrip()}'" for folder_item in folder_items.split(",")])
    print(folder_id, folder_items)

