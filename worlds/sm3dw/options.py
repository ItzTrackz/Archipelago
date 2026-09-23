from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, DeathLink

class Goal(Choice):
    """
    Select world you want to beat to goal.
    (You WILL have to finish the entire world to goal.)
    """
    
    display_name = "Goal"
    
    option_world_1 = 0
    option_world_4 = 3
    option_world_castle = 6
    option_world_bowser = 7
    option_world_flower = 10
    option_world_crown = 11
    default = 7

class RandomizeWorlds(Toggle):
    """
    Randomize the worlds in the game.
    You will start with a Random World that is NOT your goal world. (unless your goal world is World 1)
    However many worlds are in between that world and your goal world will never be more.
    Also the only world unlocks will be the worlds between world 1 and your goal world. 
    """

    display_name = "Randomize Worlds"

class StartingCharacter(Choice):
    """
    Select the character you want to start with. (Or choose Random)
    """

    display_name = "Starting Character"
    
    option_mario = 0
    option_luigi = 1  
    option_peach = 2
    option_toad = 3
    option_roselina = 4
    option_random = 5
    
    default = 0

class SplitStarsByWorld(DefaultOnToggle):
    """
    Stars are split up by World, instead of being one Multiple McGuffins.
    """
    display_name = "Split Stars By World"

class GoalCastleAccess(Range):
    """
    How much percentage of stars you need to access your goal castle.
    (If you have Split Stars By World on then its the percentage of stars in your goal world)
    """
    
    display_name = "Goal Castle Percentage"

    range_start = 0
    range_end = 100

    default = 90

class GoldenFlagSanity(Toggle):
    """
    Randomizes Golden Flags into the location pool.
    """
    display_name = "Golden Flag Sanity"

class BossSanity(Choice):
    """
    Off: Beating any sort of boss does not send a check
    Bosses Only: Beating a Boss in a Castle sends a check
    Mini-Bosses Only: Beating a Mini-Boss (Not in a castle) sends a check
    All: Beating any type of Boss Sends a check.
    """
    
    display_name = "Boss Sanity"
    option_off = 0
    option_bosses_only = 1
    option_mini_bosses_only = 2
    option_all = 3

    default = 3

class TrapPercentage(Range):
    """
    The percentage of traps in the game.
    """

    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    # Range options must define an explicit default value.
    default = 10


#Links

class SM3DWDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__+ "/n     In Super Mario 3D World, Mario dying in any way will send a DeathLink."

class SM3DWBonkLink(Toggle):
    """
    If enabled, Bonk Link will be enabled which means you bonk whenever another 3d Mario bonks.
    (As of now this is only SM3DW, but more games will be added in the future. [If the dev wants to ofc])
    """
    display_name = "Bonk Link"


@dataclass
class SM3DWOptions(PerGameCommonOptions):
    goal: Goal
    randomize_worlds: RandomizeWorlds
    starting_character: StartingCharacter
    split_stars_by_world: SplitStarsByWorld
    goal_castle_access: GoalCastleAccess
    golden_flag_sanity: GoldenFlagSanity
    boss_sanity: BossSanity
    trap_percentage: TrapPercentage
    death_link: SM3DWDeathLink
    bonk_link: SM3DWBonkLink
    

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Goal, RandomizeWorlds, StartingCharacter, SplitStarsByWorld, GoalCastleAccess, GoldenFlagSanity, BossSanity, TrapPercentage],
    ),
    OptionGroup(
        "Links to the Multiworld",
        [SM3DWDeathLink, SM3DWBonkLink],
    ),
]
