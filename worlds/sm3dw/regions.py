from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from worlds.sm3dw.options import Goal, GoldenFlagSanity, BossSanity

if TYPE_CHECKING:
    from .world import SM3DWWorld

def create_and_connect_regions(world: SM3DWWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: SM3DWWorld) -> None:

    world_1 = Region("World 1", world.player, world.multiworld)

    regions = [world_1]

    if world.options.goal == (Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_2 = Region("World 2", world.player, world.multiworld)
        world_3 = Region("World 3", world.player, world.multiworld)
        world_4 = Region("World 4", world.player, world.multiworld)
        regions.append(world_2)
        regions.append(world_3)
        regions.append(world_4)

    if world.options.goal == (Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_5 = Region("World 5", world.player, world.multiworld)
        world_6 = Region("World 6", world.player, world.multiworld)
        world_castle = Region("World Castle", world.player, world.multiworld)
        regions.append(world_5)
        regions.append(world_6)
        regions.append(world_castle)

    if world.options.goal == (Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_bowser = Region("World Bowser", world.player, world.multiworld)
        regions.append(world_bowser)

    if world.options.goal == (Goal.option_world_flower, Goal.option_world_crown):
        world_star = Region("World Star", world.player, world.multiworld)
        world_mushroom = Region("World Mushroom", world.player, world.multiworld)
        world_flower = Region("World Flower", world.player, world.multiworld)
        regions.append(world_star)
        regions.append(world_mushroom)
        regions.append(world_flower)

    if world.options.goal == Goal.option_world_crown:
        world_crown = Region("World Crown", world.player, world.multiworld)
        regions.append(world_crown)

    if world.options.golden_flag_sanity == True and world.options.goal == (Goal.option_world_1, Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_1_golden_flags = Region("World 1 Golden Flags", world.player, world.multiworld)
        regions.append(world_1_golden_flags)

    if world.options.boss_sanity == True and world.options.goal == (Goal.option_world_1, Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_1_bosses = Region("World 1 Bosses", world.player, world.multiworld)
        regions.append(world_1_bosses)

    if world.options.golden_flag_sanity == True and world.options.goal == (Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_2_golden_flags = Region("World 2 Golden Flags", world.player, world.multiworld)
        world_3_golden_flags = Region("World 3 Golden Flags", world.player, world.multiworld)
        world_4_golden_flags = Region("World 4 Golden Flags", world.player, world.multiworld)
        regions.append(world_4_golden_flags)
        regions.append(world_2_golden_flags)
        regions.append(world_3_golden_flags)

    if world.options.boss_sanity == True and world.options.goal == (Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_2_bosses = Region("World 2 Bosses", world.player, world.multiworld)
        world_3_bosses = Region("World 3 Bosses", world.player, world.multiworld)
        world_4_bosses = Region("World 4 Bosses", world.player, world.multiworld)
        regions.append(world_2_bosses)
        regions.append(world_3_bosses)
        regions.append(world_4_bosses)

    if world.options.golden_flag_sanity == True and world.options.goal == (Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_castle_golden_flags = Region("World Castle Golden Flags", world.player, world.multiworld)
        regions.append(world_castle_golden_flags)

    if world.options.boss_sanity == True and world.options.goal == (Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_castle_bosses = Region("World Castle Bosses", world.player, world.multiworld)
        regions.append(world_castle_bosses)

    if world.options.golden_flag_sanity == True and world.options.goal == (Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_bowser_golden_flags = Region("World Bowser Golden Flags", world.player, world.multiworld)
        regions.append(world_bowser_golden_flags)

    if world.options.boss_sanity == True and world.options.goal == (Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown):
        world_bowser_bosses = Region("World Bowser Bosses", world.player, world.multiworld)
        regions.append(world_bowser_bosses)
    if world.options.golden_flag_sanity == True and world.options.goal == (Goal.option_world_flower, Goal.option_world_crown):
        world_star_golden_flags = Region("World Star Golden Flags", world.player, world.multiworld)
        world_mushroom_golden_flags = Region("World Mushroom Golden Flags", world.player, world.multiworld)
        world_flower_golden_flags = Region("World Flower Golden Flags", world.player, world.multiworld)
        regions.append(world_star_golden_flags)
        regions.append(world_mushroom_golden_flags)
        regions.append(world_flower_golden_flags)

    if world.options.boss_sanity == True and world.options.goal == (Goal.option_world_flower, Goal.option_world_crown):
        world_star_bosses = Region("World Star Bosses", world.player, world.multiworld)
        world_mushroom_bosses = Region("World Mushroom Bosses", world.player, world.multiworld)
        world_flower_bosses = Region("World Flower Bosses", world.player, world.multiworld)
        regions.append(world_star_bosses)
        regions.append(world_mushroom_bosses)
        regions.append(world_flower_bosses)

    if world.options.golden_flag_sanity == True and world.options.goal == (Goal.option_world_crown):
        world_crown_golden_flags = Region("World Crown Golden Flags", world.player, world.multiworld)
        regions.append(world_crown_golden_flags)

    if world.options.boss_sanity == True and world.options.goal == (Goal.option_world_crown):
        world_crown_bosses = Region("World Crown Bosses", world.player, world.multiworld)
        regions.append(world_crown_bosses)

    world.multiworld.regions += regions
    
    

def connect_regions(world: SM3DWWorld) -> None:

    world_1 = world.get_region("World 1")
    