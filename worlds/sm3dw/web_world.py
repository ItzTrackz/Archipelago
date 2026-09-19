from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


# For our game to display correctly on the website, we need to define a WebWorld subclass.
class SM3DWWebWorld(WebWorld):
    game = "Super Mario 3D World"

    theme = "grassFlowers"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Super Mario 3D World for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ItzTrackz"],
    )

    tutorials = [setup_en]

    option_groups = option_groups