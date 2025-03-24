from _common import *

if get_arg("--debloat-gnome"):
    run_command("""
    sudo apt remove -yq \
        gnome-games \
        gnome-maps \
        synaptic \
        libreoffice* \
        gnome-music* \
        rhythmbox* \
        yelp \
        transmission-* \
        firefox* \
        evolution \
        totem \
        gnome-weather \
        shotwell-* \
        gnome-terminal \
        gnome-console
    """)