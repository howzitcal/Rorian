from _common import *
from gnome_manage_menu_folders import add_folder_to_menu

if get_arg("--tidy-menu"):
    add_folder_to_menu('Accessories' ,'accessories')
    add_folder_to_menu('Utils' ,'utils')
    add_folder_to_menu('UI' ,'ui')
    add_folder_to_menu('System' ,'system')