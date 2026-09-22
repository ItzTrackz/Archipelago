from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.sm3dw.options import StartingCharacter, Goal, SplitStarsByWorld, RandomizeWorlds

from BaseClasses import Item, ItemClassification


if TYPE_CHECKING:
    from .world import SM3DWWorld

ITEM_NAME_TO_ID = {
    #Character Unlocks
    "Mario Character Unlock": 1,
    "Luigi Character Unlock": 2,
    "Toad Character Unlock": 3,
    "Peach Character Unlock": 4,
    "Roselina Character Unlock": 5,
    #World Unlocks
    "Progressive World Unlock": 52,
    "World 1 Unlock": 6,
    "World 2 Unlock": 7,
    "World 3 Unlock": 8,
    "World 4 Unlock": 9,
    "World 5 Unlock": 10,
    "World 6 Unlock": 11,
    "World Castle Unlock": 12,
    "World Bowser Unlock": 13,
    "World Star Unlock": 14,
    "World Flower Unlock": 15,
    "World Mushroom Unlock": 16,
    "World Crown Unlock": 17,
    #Random Character Unlocks
    "Plessy Unlock": 18,
    "P-Switches": 19,
    "?-! Switches": 20,
    "Captain Toad": 21,
    "Swapping Blocks": 22,
    "Bomb Helmets": 23,
    "Double Cherry": 24,
    "Cat Suit": 25,
    "Gold Cat Suit": 26,
    "Fire Flower": 27,
    "Boomerang Suit": 28,
    "Helicopter Helmet": 29,
    "Shoe Skis": 30,
    "Goomba Helmet": 31,
    "Green Star Coin Rings": 32,
    #Stars
    "World 1 Star": 33,
    "World 2 Star": 34,
    "World 3 Star": 35,
    "World 4 Star": 36,
    "World 5 Star": 37,
    "World 6 Star": 38,
    "World Castle Star": 39,
    "World Bowser Star": 40,
    "World Star Star": 41,
    "World Flower Star": 42,
    "World Mushroom Star": 43,
    "World Crown Star": 44,
    "Star": 45,
    #Filler Items
    "1-UP": 46,
    "15-UP": 47,
    "Random Powerup": 48,
    "Fill up Extra Power-Up Slot": 49,
    "Smol Trap": 50,
    "Bonk Trap": 51,

}



DEFAULT_ITEM_CLASSIFICATIONS = {
    #Character Unlocks
    "Mario Character Unlock": ItemClassification.progression,
    "Luigi Character Unlock": ItemClassification.progression,
    "Toad Character Unlock": ItemClassification.progression,
    "Peach Character Unlock": ItemClassification.progression,
    "Roselina Character Unlock": ItemClassification.progression,
    #World Unlocks
    "Progressive World Unlock": ItemClassification.progression,
    "World 1 Unlock": ItemClassification.progression,
    "World 2 Unlock": ItemClassification.progression,
    "World 3 Unlock": ItemClassification.progression,
    "World 4 Unlock": ItemClassification.progression,
    "World 5 Unlock": ItemClassification.progression,
    "World 6 Unlock": ItemClassification.progression,
    "World Castle Unlock": ItemClassification.progression,
    "World Bowser Unlock": ItemClassification.progression,
    "World Star Unlock": ItemClassification.progression,
    "World Flower Unlock": ItemClassification.progression,
    "World Mushroom Unlock": ItemClassification.progression,
    "World Crown Unlock": ItemClassification.progression,
    #Random Character Unlocks
    "Plessy Unlock": ItemClassification.progression,
    "P-Switches Unlock": ItemClassification.progression,
    "?-! Switches": ItemClassification.progression,
    "Captain Toad Levels": ItemClassification.progression,
    "Swapping Blocks": ItemClassification.progressive,
    "Bomb Helmets": ItemClassification.progressive,
    "Double Cherry": ItemClassification.progressive,
    "Cat Suit": ItemClassification.progressive,
    "Gold Cat Suit": ItemClassification.progressive,
    "Fire Flower": ItemClassification.progressive,
    "Boomerang Suit": ItemClassification.progressive,
    "Helicopter Helmet": ItemClassification.progressive,
    "Shoe Skis": ItemClassification.useful,
    "Goomba Helmet": ItemClassification.useful,
    "Green Star Coin Rings": ItemClassification.progressive,
    #Stars
    "World 1 Star": ItemClassification.progression,
    "World 2 Star": ItemClassification.progression,
    "World 3 Star": ItemClassification.progression,
    "World 4 Star": ItemClassification.progression,
    "World 5 Star": ItemClassification.progression,
    "World 6 Star": ItemClassification.progression,
    "World Castle Star": ItemClassification.progression,
    "World Bowser Star": ItemClassification.progression,
    "World Star Star": ItemClassification.progression,
    "World Flower Star": ItemClassification.progression,
    "World Mushroom Star": ItemClassification.progression,
    "World Crown Star": ItemClassification.progression,
    "Star": ItemClassification.progressive,
    #Filler Items
    "1-UP": ItemClassification.filler,
    "15-UP": ItemClassification.filler,
    "Random Powerup": ItemClassification.filler,
    "Fill up Extra Power-Up Slot": ItemClassification.filler,
    "Smol Trap": ItemClassification.trap,
    "Bonk Trap": ItemClassification.trap,
}

class SM3DWItem(Item):
    game = "Super Mario 3D World"

def get_random_filler_item_name(world: SM3DWWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_percentage:
        if world.random.randint(0, 1) == 0:
            return "Bonk Trap"
        else:
            return "Smol Trap"    

    rand_filler = world.random.randint(0, 3)

    if rand_filler == 0:
            return "1-UP"
    elif rand_filler == 1:
            return "15-UP"
    elif rand_filler == 2:
            return "Random Powerup"
    elif rand_filler == 3:
            return "Fill up Extra Power-Up Slot"

def create_item_with_correct_classification(world: SM3DWWorld, name: str) -> SM3DWItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return SM3DWItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

    #TODO if name == "World Crown Unlock" and world.options.

def create_all_items(world: SM3DWWorld) -> None:

    itempool: list [Item] = [
        world.create_item("Plessy Unlock"),
        world.create_item("P-Switches"),
        world.create_item("?-! Switches"),
        world.create_item("Captain Toad"),
        world.create_item("Swapping Blocks"),
        world.create_item("Bomb Helmets"),
        world.create_item("Double Cherry"),
        world.create_item("Cat Suit"),
        world.create_item("Gold Cat Suit"),
        world.create_item("Fire Flower"),
        world.create_item("Boomerang Suit"),
        world.create_item("Helicopter Helmet"),
        world.create_item("Shoe Skis"),
        world.create_item("Goomba Helmet"),
        world.create_item("Green Star Coin Rings"),
    ]
    # if world.options.hammer == True:
    #     itempool.append(world.create_item(""))


    #options Character Unlocks
    if world.options.character == StartingCharacter.option_mario:
        starting_mario_character = world.create_item("Mario Character Unlock")
        world.push_precollected(starting_mario_character)

        itempool.append(world.create_item("Luigi Character Unlock"))
        itempool.append(world.create_item("Toad Character Unlock"))
        itempool.append(world.create_item("Peach Character Unlock"))
        itempool.append(world.create_item("Roselina Character Unlock"))
    
    if world.options.character == StartingCharacter.option_luigi:
        starting_luigi_character = world.create_item("Luigi Character Unlock")
        world.push_precollected(starting_luigi_character)

        itempool.append(world.create_item("Mario Character Unlock"))
        itempool.append(world.create_item("Toad Character Unlock"))
        itempool.append(world.create_item("Peach Character Unlock"))
        itempool.append(world.create_item("Roselina Character Unlock"))
    
    if world.options.character == StartingCharacter.option_toad:
        starting_toad_character = world.create_item("Toad Character Unlock")
        world.push_precollected(starting_toad_character)

        itempool.append(world.create_item("Luigi Character Unlock"))
        itempool.append(world.create_item("Mario Character Unlock"))
        itempool.append(world.create_item("Peach Character Unlock"))
        itempool.append(world.create_item("Roselina Character Unlock"))
    
    if world.options.character == StartingCharacter.option_peach:
        starting_peach_character = world.create_item("Peach Character Unlock")
        world.push_precollected(starting_peach_character)

        itempool.append(world.create_item("Luigi Character Unlock"))
        itempool.append(world.create_item("Toad Character Unlock"))
        itempool.append(world.create_item("Mario Character Unlock"))
        itempool.append(world.create_item("Roselina Character Unlock"))
    
    if world.options.character == StartingCharacter.option_roselina:
        starting_roselina_character = world.create_item("Roselina Character Unlock")
        world.push_precollected(starting_roselina_character)

        itempool.append(world.create_item("Luigi Character Unlock"))
        itempool.append(world.create_item("Toad Character Unlock"))
        itempool.append(world.create_item("Peach Character Unlock"))
        itempool.append(world.create_item("Mario Character Unlock"))
    
    if world.options.character == StartingCharacter.option_random:
        character_rand = world.random.randint(0 ,4)

        if character_rand == 0:
            starting_mario_character = world.create_item("Mario Character Unlock")
            world.push_precollected(starting_mario_character)

            itempool.append(world.create_item("Luigi Character Unlock"))
            itempool.append(world.create_item("Toad Character Unlock"))
            itempool.append(world.create_item("Peach Character Unlock"))
            itempool.append(world.create_item("Roselina Character Unlock"))
        
        elif character_rand == 1:
            starting_luigi_character = world.create_item("Luigi Character Unlock")
            world.push_precollected(starting_luigi_character)
            
            itempool.append(world.create_item("Mario Character Unlock"))
            itempool.append(world.create_item("Toad Character Unlock"))
            itempool.append(world.create_item("Peach Character Unlock"))
            itempool.append(world.create_item("Roselina Character Unlock"))
        
        elif character_rand == 2:
            starting_toad_character = world.create_item("Toad Character Unlock")
            world.push_precollected(starting_toad_character)

            itempool.append(world.create_item("Luigi Character Unlock"))
            itempool.append(world.create_item("Mario Character Unlock"))
            itempool.append(world.create_item("Peach Character Unlock"))
            itempool.append(world.create_item("Roselina Character Unlock"))
        
        elif character_rand == 3:
            starting_peach_character = world.create_item("Peach Character Unlock")
            world.push_precollected(starting_peach_character)

            itempool.append(world.create_item("Luigi Character Unlock"))
            itempool.append(world.create_item("Toad Character Unlock"))
            itempool.append(world.create_item("Mario Character Unlock"))
            itempool.append(world.create_item("Roselina Character Unlock"))
        
        elif character_rand == 4:
            starting_roselina_character = world.create_item("Roselina Character Unlock")
            world.push_precollected(starting_roselina_character)

            itempool.append(world.create_item("Luigi Character Unlock"))
            itempool.append(world.create_item("Toad Character Unlock"))
            itempool.append(world.create_item("Peach Character Unlock"))
            itempool.append(world.create_item("Mario Character Unlock"))
    
    #World Stars
    if world.options.split_stars_by_world and world.options.goal == Goal.option_world_1:
        itempool.append(world.create_item("World 1 Star"))
        #loop 24
    
    elif world.options.split_stars_by_world and world.options.goal == Goal.option_world_4:

        itempool.append(world.create_item("World 2 Star"))
        #loop 24
        
        itempool.append(world.create_item("World 3 Star"))
        #loop 31

        itempool.append(world.create_item("World 4 Star"))
        #loop 30

    elif world.options.split_stars_by_world and world.options.goal == Goal.option_world_castle:
        itempool.append(world.create_item("World 5 Star"))
        #loop 31

        itempool.append(world.create_item("World 6 Star"))
        #loop 32

        itempool.append(world.create_item("World Castle Star"))
        #loop 32

    elif world.options.split_stars_by_world and world.options.goal == Goal.option_world_bowser:
        itempool.append(world.create_item("World Bowser Star"))
        #loop 39

    elif world.options.split_stars_by_world and world.options.goal == Goal.option_world_mushroom:
        itempool.append(world.create_item("World Star Star"))
        #loop

        itempool.append(world.create_item("World Flower Star"))
        #loop

        itempool.append(world.create_item("World Mushroom Star"))
        #loop

    elif world.options.split_stars_by_world and world.options.goal == Goal.option_world_crown:
        itempool.append(world.create_item("World Crown Star"))
        #loop
    
    elif world.options.split_stars_by_world == False and world.options.goal == Goal.option_world_1:
        itempool.append(world.create_item("Star"))
        #loop 24

    elif world.options.split_stars_by_world == False and world.options.goal == Goal.option_world_4:
        itempool.append(world.create_item("Star"))
        #loop 109
    
    elif world.option.split_stars_by_world == False and world.option.goal == Goal.option_world_castle:
        itempool.append(world.create_item("Star"))
        #loop 204

    elif world.option.split_stars_by_world == False and world.option.goal == Goal.option_world_bowser:
        itempool.append(world.create_item("Star"))
        #loop 243
    
    elif world.option.split_stars_by_world == False and world.option.goal == Goal.option_world_mushroom:
        itempool.append(world.create_item("Star"))
        #loop 243 + Star + Flower + Mushroom

    elif world.option.split_stars_by_world == False and world.option.goal == Goal.option_world_crown:
        itempool.append(world.create_item("Star"))
        #loop 243 + Star + Flower + Mushroom + Crown
    
    #Randomize Worlds
    if world.option.randomize_worlds and world.option.goal == Goal.option_world_1:
        itempool.append(world.create_item("World 1 Unlock"))
    
    elif world.option.randomize_worlds and world.option.goal == Goal.option_world_4:
        world_4_rand = world.random.randint(0, 2)

        if world_4_rand == 0:
            starting_world_1 = world.create_item("World 1 Unlock")
            world.push_precollected(starting_world_1)
            
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
        elif world_4_rand == 1:
            starting_world_2 = world.create_item("World 2 Unlock")
            world.push_precollected(starting_world_2)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
        elif world_4_rand == 2:
            starting_world_3 = world.create_item("World 3 Unlock")
            world.push_precollected(starting_world_3)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
    
    elif world.option.randomize_worlds and world.option.goal == Goal.option_world_castle:
        world_castle_rand = world.randint(0, 5)

        if world_castle_rand == 0:
            starting_world_1 = world.create_item("World 1 Unlock")
            world.push_precollected(starting_world_1)
            
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))

        elif world_castle_rand == 1:
            starting_world_2 = world.create_item("World 2 Unlock")
            world.push_precollected(starting_world_2)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))

        elif world_castle_rand == 2:
            starting_world_3 = world.create_item("World 3 Unlock")
            world.push_precollected(starting_world_3)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))    
        
        elif world_castle_rand == 3:
            starting_world_4 = world.create_item("World 4 Unlock")
            world.push_precollected(starting_world_4)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
        
        elif world_castle_rand == 4:
            starting_world_5 = world.create_item("World 5 Unlock")
            world.push_precollected(starting_world_5)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
        
        elif world_castle_rand == 5:
            starting_world_2 = world.create_item("World 6 Unlock")
            world.push_precollected(starting_world_2)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))

    elif world.option.randomize_worlds and world.option.goal == Goal.option_world_bowser:
        world_bowser_rand = world.random.randint(0, 6)
        
        if world_bowser_rand == 0:
            starting_world_1 = world.create_item("World 1 Unlock")
            world.push_precollected(starting_world_1)
            
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))

        elif world_bowser_rand == 1:
            starting_world_2 = world.create_item("World 2 Unlock")
            world.push_precollected(starting_world_2)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))   
            
        elif world_bowser_rand == 2:
            starting_world_3 = world.create_item("World 3 Unlock")
            world.push_precollected(starting_world_3)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))

        elif world_bowser_rand == 3:
            starting_world_4 = world.create_item("World 4 Unlock")
            world.push_precollected(starting_world_4)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
        
        elif world_bowser_rand == 4:
            starting_world_5 = world.create_item("World 5 Unlock")
            world.push_precollected(starting_world_5)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
        
        elif world_bowser_rand == 5:
            starting_world_6 = world.create_item("World 6 Unlock")
            world.push_precollected(starting_world_6)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
        
        elif world_bowser_rand == 6:
            starting_world_castle = world.create_item("World Castle Unlock")
            world.push_precollected(starting_world_castle)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
    
    elif world.option.randomize_worlds and world.option.goal == Goal.option_world_mushroom:
        world_mush_rand = world.random.randint(0, 9)

        if world_mush_rand == 0:
            starting_world_1 = world.create_item("World 1 Unlock")
            world.push_precollected(starting_world_1)
            
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 1:
            starting_world_2 = world.create_item("World 2 Unlock")
            world.push_precollected(starting_world_2)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 2:
            starting_world_3 = world.create_item("World 3 Unlock")
            world.push_precollected(starting_world_3)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 3:
            starting_world_4 = world.create_item("World 4 Unlock")
            world.push_precollected(starting_world_4)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 4:
            starting_world_5 = world.create_item("World 5 Unlock")
            world.push_precollected(starting_world_5)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 5:
            starting_world_6 = world.create_item("World 6 Unlock")
            world.push_precollected(starting_world_6)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 6:
            starting_world_castle = world.create_item("World Castle Unlock")
            world.push_precollected(starting_world_castle)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 7:
            starting_world_bowser = world.create_item("World Bowser Unlock")
            world.push_precollected(starting_world_bowser)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
        
        elif world_mush_rand == 8:
            starting_world_star = world.create_item("World Star Unlock")
            world.push_precollected(starting_world_star)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            
        elif world_mush_rand == 9:
            starting_world_flower = world.create_item("World Flower Unlock")
            world.push_precollected(starting_world_flower)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))

    elif world.option.randomize_worlds and world.option.goal == Goal.option_world_crown:
        world_crown_rand = world.random.randint(0, 10)

        if world_crown_rand == 0:
            starting_world_1 = world.create_item("World 1 Unlock")
            world.push_precollected(starting_world_1)
            
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 1:
            starting_world_2 = world.create_item("World 2 Unlock")
            world.push_precollected(starting_world_2)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 2:
            starting_world_3 = world.create_item("World 3 Unlock")
            world.push_precollected(starting_world_3)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 3:
            starting_world_4 = world.create_item("World 4 Unlock")
            world.push_precollected(starting_world_4)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 4:
            starting_world_5 = world.create_item("World 5 Unlock")
            world.push_precollected(starting_world_5)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 5:
            starting_world_6 = world.create_item("World 6 Unlock")
            world.push_precollected(starting_world_6)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 6:
            starting_world_castle = world.create_item("World Castle Unlock")
            world.push_precollected(starting_world_castle)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 7:
            starting_world_bowser = world.create_item("World Bowser Unlock")
            world.push_precollected(starting_world_bowser)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
        
        elif world_crown_rand == 8:
            starting_world_star = world.create_item("World Star Unlock")
            world.push_precollected(starting_world_star)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
            
        elif world_crown_rand == 9:
            starting_world_flower = world.create_item("World Flower Unlock")
            world.push_precollected(starting_world_flower)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Mushroom Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))

        elif world_crown_rand == 10:
            starting_world_mush = world.create_item("World Mushroom Unlock")
            world.push_precollected(starting_world_mush)
            
            itempool.append(world.create_item("World 1 Unlock"))
            itempool.append(world.create_item("World 2 Unlock"))
            itempool.append(world.create_item("World 3 Unlock"))
            itempool.append(world.create_item("World 4 Unlock"))
            itempool.append(world.create_item("World 6 Unlock"))
            itempool.append(world.create_item("World Castle Unlock"))
            itempool.append(world.create_item("World Bowser Unlock"))
            itempool.append(world.create_item("World Star Unlock"))
            itempool.append(world.create_item("World 5 Unlock"))
            itempool.append(world.create_item("World Flower Unlock"))
            itempool.append(world.create_item("World Crown Unlock"))
    
    elif world.option.randomize_world == False and world.option.goal == Goal.option_world_1:
        starting_progressive_world = world.create.item("Progressive World Unlock")
        world.push_precollected(starting_progressive_world)
    
    elif world.option.randomize_world == False and world.option.goal == Goal.option_world_4:
        starting_progressive_world = world.create.item("Progressive World Unlock")
        world.push_precollected(starting_progressive_world)

        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
    
    elif world.option.randomize_world == False and world.option.goal == Goal.option_world_castle:
        starting_progressive_world = world.create.item("Progressive World Unlock")
        world.push_precollected(starting_progressive_world)

        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
    
    elif world.option.randomize_world == False and world.option.goal == Goal.option_world_bowser:
        starting_progressive_world = world.create.item("Progressive World Unlock")
        world.push_precollected(starting_progressive_world)

        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
    
    elif world.option.randomize_world == False and world.option.goal == Goal.option_world_mushroom:
        starting_progressive_world = world.create.item("Progressive World Unlock")
        world.push_precollected(starting_progressive_world)

        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))

    elif world.option.randomize_world == False and world.option.goal == Goal.option_world_crown:
        starting_progressive_world = world.create.item("Progressive World Unlock")
        world.push_precollected(starting_progressive_world)

        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
        itempool.append(world.create_item("Progressive World Unlock"))
    
    
        
            
            


