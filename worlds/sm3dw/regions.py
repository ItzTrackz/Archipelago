from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SM3DWWorld

def create_and_connect_regions(world: SM3DWWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: SM3DWWorld) -> None:

    world_1 = Region("World 1", world.player, world.multiworld)

def connect_regions(world: SM3DWWorld) -> None:
    world_1 = world.get_region("World 1")
    