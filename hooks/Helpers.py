import re
from typing import Optional, Any
from BaseClasses import MultiWorld
from ..Helpers import get_option_value

def get_excluded_level_ids(multiworld: MultiWorld, player: int) -> set[str]:
    option = getattr(multiworld.worlds[player].options, "exclude_level_ids", None)
    if option is None:
        return set()

    value_str = str(option.value)
    excluded = set()
    for part in value_str.split(','):
        part = part.strip()
        if part.isdigit():
            excluded.add(part)
    return excluded

def is_level_excluded(name: str, excluded_ids: set[str]) -> bool:
    if not excluded_ids:
        return False
    match = re.search(r'\((\d+)\)', name)
    if match and match.group(1) in excluded_ids:
        return True
    return False

def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:

    if category_name == "Update 1.0":
        return get_option_value(multiworld, player, "min_update") <= 1 and get_option_value(multiworld, player, "max_update") >= 1
    if category_name == "Update 1.1":
        return get_option_value(multiworld, player, "min_update") <= 2 and get_option_value(multiworld, player, "max_update") >= 2
    if category_name == "Update 1.2":
        return get_option_value(multiworld, player, "min_update") <= 3 and get_option_value(multiworld, player, "max_update") >= 3
    if category_name == "Update 1.3":
        return get_option_value(multiworld, player, "min_update") <= 4 and get_option_value(multiworld, player, "max_update") >= 4
    if category_name == "Update 1.4":
        return get_option_value(multiworld, player, "min_update") <= 5 and get_option_value(multiworld, player, "max_update") >= 5
    if category_name == "Update 1.5":
        return get_option_value(multiworld, player, "min_update") <= 6 and get_option_value(multiworld, player, "max_update") >= 6
    if category_name == "Update 1.6":
        return get_option_value(multiworld, player, "min_update") <= 7 and get_option_value(multiworld, player, "max_update") >= 7
    if category_name == "Update 1.7":
        return get_option_value(multiworld, player, "min_update") <= 8 and get_option_value(multiworld, player, "max_update") >= 8
    if category_name == "Update 1.8":
        return get_option_value(multiworld, player, "min_update") <= 9 and get_option_value(multiworld, player, "max_update") >= 9
    if category_name == "Update 1.9":
        return get_option_value(multiworld, player, "min_update") <= 10 and get_option_value(multiworld, player, "max_update") >= 10
    if category_name == "Update 2.0":
        return get_option_value(multiworld, player, "min_update") <= 11 and get_option_value(multiworld, player, "max_update") >= 11
    if category_name == "Update 2.1":
        return get_option_value(multiworld, player, "min_update") <= 12 and get_option_value(multiworld, player, "max_update") >= 12
    if category_name == "Update 2.2":
        return get_option_value(multiworld, player, "min_update") <= 13 and get_option_value(multiworld, player, "max_update") >= 13

    if category_name == "N/A":
        return get_option_value(multiworld, player, "min_difficulty") <= 1 and get_option_value(multiworld, player, "max_difficulty") >= 1
    if category_name == "Auto":
        return get_option_value(multiworld, player, "min_difficulty") <= 2 and get_option_value(multiworld, player, "max_difficulty") >= 2
    if category_name == "Easy":
        return get_option_value(multiworld, player, "min_difficulty") <= 3 and get_option_value(multiworld, player, "max_difficulty") >= 3
    if category_name == "Normal":
        return get_option_value(multiworld, player, "min_difficulty") <= 4 and get_option_value(multiworld, player, "max_difficulty") >= 4
    if category_name == "Hard":
        return get_option_value(multiworld, player, "min_difficulty") <= 5 and get_option_value(multiworld, player, "max_difficulty") >= 5
    if category_name == "Harder":
        return get_option_value(multiworld, player, "min_difficulty") <= 6 and get_option_value(multiworld, player, "max_difficulty") >= 6
    if category_name == "Insane":
        return get_option_value(multiworld, player, "min_difficulty") <= 7 and get_option_value(multiworld, player, "max_difficulty") >= 7
    if category_name == "Easy Demon":
        return get_option_value(multiworld, player, "min_difficulty") <= 8 and get_option_value(multiworld, player, "max_difficulty") >= 8
    if category_name == "Medium Demon":
        return get_option_value(multiworld, player, "min_difficulty") <= 9 and get_option_value(multiworld, player, "max_difficulty") >= 9
    if category_name == "Hard Demon":
        return get_option_value(multiworld, player, "min_difficulty") <= 10 and get_option_value(multiworld, player, "max_difficulty") >= 10
    if category_name == "Insane Demon":
        return get_option_value(multiworld, player, "min_difficulty") <= 11 and get_option_value(multiworld, player, "max_difficulty") >= 11
    if category_name == "Extreme Demon":
        return get_option_value(multiworld, player, "min_difficulty") <= 12 and get_option_value(multiworld, player, "max_difficulty") >= 12

    if category_name == "Rated":
        return get_option_value(multiworld, player, "min_rating") <= 1 and get_option_value(multiworld, player, "max_rating") >= 1
    if category_name == "Featured":
        return get_option_value(multiworld, player, "min_rating") <= 2 and get_option_value(multiworld, player, "max_rating") >= 2
    if category_name == "Epic":
        return get_option_value(multiworld, player, "min_rating") <= 3 and get_option_value(multiworld, player, "max_rating") >= 3
    if category_name == "Legendary":
        return get_option_value(multiworld, player, "min_rating") <= 4 and get_option_value(multiworld, player, "max_rating") >= 4
    if category_name == "Mythic":
        return get_option_value(multiworld, player, "min_rating") <= 5 and get_option_value(multiworld, player, "max_rating") >= 5

    return None

def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
