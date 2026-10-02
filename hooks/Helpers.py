import re
from typing import Optional, Any
from BaseClasses import MultiWorld

def _get_opt(multiworld: MultiWorld, player: int, name: str) -> int:
    opt = getattr(multiworld.worlds[player].options, name, None)
    return opt.value if opt is not None else 0

def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    # Handle Update categories
    if category_name.startswith("Update "):
        version_map = {
            "1.0": 1, "1.1": 2, "1.2": 3, "1.3": 4, "1.4": 5, "1.5": 6,
            "1.6": 7, "1.7": 8, "1.8": 9, "1.9": 10, "2.0": 11, "2.1": 12, "2.2": 13
        }
        version_str = category_name.replace("Update ", "")
        version_num = version_map.get(version_str)
        if version_num:
            return _get_opt(multiworld, player, "min_update") <= version_num and \
                   _get_opt(multiworld, player, "max_update") >= version_num

    # Handle Difficulty categories
    difficulty_map = {
        "N/A": 1, "Auto": 2, "Easy": 3, "Normal": 4, "Hard": 5, "Harder": 6,
        "Insane": 7, "Easy Demon": 8, "Medium Demon": 9, "Hard Demon": 10,
        "Insane Demon": 11, "Extreme Demon": 12
    }
    if category_name in difficulty_map:
        diff_num = difficulty_map[category_name]
        # NOTE: Fixed a logic bug here. It should be min <= X and max >= X to check if X is within the range.
        return _get_opt(multiworld, player, "min_difficulty") <= diff_num and \
               _get_opt(multiworld, player, "max_difficulty") >= diff_num

    # Handle Rating categories
    rating_map = {
        "Rated": 1, "Featured": 2, "Epic": 3, "Legendary": 4, "Mythic": 5
    }
    if category_name in rating_map:
        rating_num = rating_map[category_name]
        return _get_opt(multiworld, player, "min_rating") <= rating_num and \
               _get_opt(multiworld, player, "max_rating") >= rating_num

    return None

def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
