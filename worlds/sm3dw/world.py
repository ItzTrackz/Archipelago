from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as sm3dw_options  

class SM3DWWorld(World):
    """
    Super Mario 3D World is a 3D platformer where players control Mario and friends to save the Sprixie Kingdom from Bowser. 
    Players navigate through various levels, collecting items and power-ups, while overcoming obstacles and enemies. 
    The game features cooperative multiplayer gameplay, allowing up to four players to play together locally or online.
    """

    game = "Super Mario 3D World"

    web = web_world.SM3DWWebWorld()

    options_dataclass = sm3dw_options.sm3dwOptions
    options: sm3dw_options.sm3dwOptions 

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "World 1"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.SM3DWItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    # def fill_slot_data(self) -> Mapping[str, Any]:
    #    # If you need access to the player's chosen options on the client side, there is a helper for that.
    #    return self.options.as_dict(
    #        "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
    #    )
