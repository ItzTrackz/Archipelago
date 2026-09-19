from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class Goal(Choice):
    """
    Select world you want to beat to goal.
    (You will have to finish the entire world to goal.)
    
    """
    display_name = "Goal"
    option_world_1 = 0
    option_world_2 = 1  
    option_world_3 = 2
    option_world_4 = 3
    option_world_5 = 4
    option_world_6 = 5
    option_world_castle = 6
    option_world_bowser = 7
    option_world_star = 8
    option_world_crown = 9
    default = 7

class RandomizeWorlds(Toggle):
    """
    Randomize the worlds in the game.
    """

    display_name = "Randomize Worlds"

class StartingCharacter(Choice):
    """
    Select starting character.
    """

    display_name = "Starting Character"
    option_mario = 0
    option_luigi = 1  
    option_peach = 2
    option_toad = 3
    default = 0

class TrapPercentage(Range):
    """
    The percentage of traps in the game.
    """

    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    # Range options must define an explicit default value.
    default = 10

class BonkLink(Toggle):
    """
    If enabled, Bonk Link will be enabled which means you bonk whenever another 3d Mario bonks.
    (As of now this is only SM3DW and SMO, but more games will be added in the future. [If the dev wants to ofc])
    """

    display_name = "Bonk Link"


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class APQuestOptions(PerGameCommonOptions):
    goal: Goal
    randomize_worlds: RandomizeWorlds
    starting_character: StartingCharacter
    trap_percentage: TrapPercentage
    bonk_link: BonkLink

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Goal, RandomizeWorlds, StartingCharacter, TrapPercentage, BonkLink],
    ),
]
