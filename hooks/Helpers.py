from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:

    if category_name == "Update 1.0":
        return get_option_value(multiworld, player, "min_update") >= 1 and get_option_value(multiworld, player, "max_update") <= 1
    if category_name == "Update 1.1":
        return get_option_value(multiworld, player, "min_update") >= 2 and get_option_value(multiworld, player, "max_update") <= 2
    if category_name == "Update 1.2":
        return get_option_value(multiworld, player, "min_update") >= 3 and get_option_value(multiworld, player, "max_update") <= 3
    if category_name == "Update 1.3":
        return get_option_value(multiworld, player, "min_update") >= 4 and get_option_value(multiworld, player, "max_update") <= 4
    if category_name == "Update 1.4":
        return get_option_value(multiworld, player, "min_update") >= 5 and get_option_value(multiworld, player, "max_update") <= 5
    if category_name == "Update 1.5":
        return get_option_value(multiworld, player, "min_update") >= 6 and get_option_value(multiworld, player, "max_update") <= 6
    if category_name == "Update 1.6":
        return get_option_value(multiworld, player, "min_update") >= 7 and get_option_value(multiworld, player, "max_update") <= 7
    if category_name == "Update 1.7":
        return get_option_value(multiworld, player, "min_update") >= 8 and get_option_value(multiworld, player, "max_update") <= 8
    if category_name == "Update 1.8":
        return get_option_value(multiworld, player, "min_update") >= 9 and get_option_value(multiworld, player, "max_update") <= 9
    if category_name == "Update 1.9":
        return get_option_value(multiworld, player, "min_update") >= 10 and get_option_value(multiworld, player, "max_update") <= 10
    if category_name == "Update 2.0":
        return get_option_value(multiworld, player, "min_update") >= 11 and get_option_value(multiworld, player, "max_update") <= 11
    if category_name == "Update 2.1":
        return get_option_value(multiworld, player, "min_update") >= 12 and get_option_value(multiworld, player, "max_update") <= 12
    if category_name == "Update 2.2":
        return get_option_value(multiworld, player, "min_update") >= 13 and get_option_value(multiworld, player, "max_update") <= 13

    if category_name == "Tiny":
        return get_option_value(multiworld, player, "min_length") >= 1 and get_option_value(multiworld, player, "max_length") <= 1
    if category_name == "Short":
        return get_option_value(multiworld, player, "min_length") >= 2 and get_option_value(multiworld, player, "max_length") <= 2
    if category_name == "Medium":
        return get_option_value(multiworld, player, "min_length") >= 3 and get_option_value(multiworld, player, "max_length") <= 3
    if category_name == "Long":
        return get_option_value(multiworld, player, "min_length") >= 4 and get_option_value(multiworld, player, "max_length") <= 4
    if category_name == "XL":
        return get_option_value(multiworld, player, "min_length") >= 5 and get_option_value(multiworld, player, "max_length") <= 5

    if category_name == "N/A":
        return get_option_value(multiworld, player, "min_difficulty") >= 1 and get_option_value(multiworld, player, "max_difficulty") <= 1
    if category_name == "Auto":
        return get_option_value(multiworld, player, "min_difficulty") >= 2 and get_option_value(multiworld, player, "max_difficulty") <= 2
    if category_name == "Easy":
        return get_option_value(multiworld, player, "min_difficulty") >= 3 and get_option_value(multiworld, player, "max_difficulty") <= 3
    if category_name == "Normal":
        return get_option_value(multiworld, player, "min_difficulty") >= 4 and get_option_value(multiworld, player, "max_difficulty") <= 4
    if category_name == "Hard":
        return get_option_value(multiworld, player, "min_difficulty") >= 5 and get_option_value(multiworld, player, "max_difficulty") <= 5
    if category_name == "Harder":
        return get_option_value(multiworld, player, "min_difficulty") >= 6 and get_option_value(multiworld, player, "max_difficulty") <= 6
    if category_name == "Insane":
        return get_option_value(multiworld, player, "min_difficulty") >= 7 and get_option_value(multiworld, player, "max_difficulty") <= 7
    if category_name == "Easy Demon":
        return get_option_value(multiworld, player, "min_difficulty") >= 8 and get_option_value(multiworld, player, "max_difficulty") <= 8
    if category_name == "Medium Demon":
        return get_option_value(multiworld, player, "min_difficulty") >= 9 and get_option_value(multiworld, player, "max_difficulty") <= 9
    if category_name == "Hard Demon":
        return get_option_value(multiworld, player, "min_difficulty") >= 10 and get_option_value(multiworld, player, "max_difficulty") <= 10
    if category_name == "Insane Demon":
        return get_option_value(multiworld, player, "min_difficulty") >= 11 and get_option_value(multiworld, player, "max_difficulty") <= 11
    if category_name == "Extreme Demon":
        return get_option_value(multiworld, player, "min_difficulty") >= 12 and get_option_value(multiworld, player, "max_difficulty") <= 12

    if category_name == "Rated":
        return get_option_value(multiworld, player, "min_rating") >= 1 and get_option_value(multiworld, player, "max_rating") <= 1
    if category_name == "Featured":
        return get_option_value(multiworld, player, "min_rating") >= 2 and get_option_value(multiworld, player, "max_rating") <= 2
    if category_name == "Epic":
        return get_option_value(multiworld, player, "min_rating") >= 3 and get_option_value(multiworld, player, "max_rating") <= 3
    if category_name == "Legendary":
        return get_option_value(multiworld, player, "min_rating") >= 4 and get_option_value(multiworld, player, "max_rating") <= 4
    if category_name == "Mythic":
        return get_option_value(multiworld, player, "min_rating") >= 5 and get_option_value(multiworld, player, "max_rating") <= 5

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
