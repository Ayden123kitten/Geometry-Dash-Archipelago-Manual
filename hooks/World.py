from typing import Any
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

from ..Items import ManualItem
from ..Locations import ManualLocation

from ..Data import game_table, item_table, location_table, region_table

from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat, remove_specific_item

import logging

def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

def before_generate_early(world: World, multiworld: MultiWorld, player: int) -> None:
    pass

def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    from ..Helpers import get_option_value
    import logging

    if isinstance(world.location_table, dict):
        victory_locations = {k: v for k, v in world.location_table.items() if v.get("victory", False)}
        regular_levels = {k: v for k, v in world.location_table.items() if not v.get("victory", False)}
    else:
        victory_locations = [loc for loc in world.location_table if loc.get("victory", False)]
        regular_levels = [loc for loc in world.location_table if not loc.get("victory", False)]

    total_available = len(regular_levels)
    if total_available == 0:
        logging.warning("No regular levels available to filter. Check your other options.")
        return

    mode = get_option_value(multiworld, player, "level_count_mode")

    if mode == 1:
        target_count = get_option_value(multiworld, player, "level_count")
    else:
        percentage = get_option_value(multiworld, player, "level_percentage")
        target_count = max(1, int(round(total_available * (percentage / 100.0))))

    target_count = min(target_count, total_available)

    if isinstance(world.location_table, dict):
        selected_keys = world.random.sample(list(regular_levels.keys()), target_count)
        selected_levels = {k: regular_levels[k] for k in selected_keys}

        for loc in selected_levels.values():
            if "category" not in loc:
                loc["category"] = []
            elif isinstance(loc["category"], str):
                loc["category"] = [loc["category"]]
            if "Included Level" not in loc["category"]:
                loc["category"].append("Included Level")

        world.location_table = {**selected_levels, **victory_locations}
    else:
        selected_levels = world.random.sample(regular_levels, target_count)
        for loc in selected_levels:
            if "category" not in loc:
                loc["category"] = []
            elif isinstance(loc["category"], str):
                loc["category"] = [loc["category"]]
            if "Included Level" not in loc["category"]:
                loc["category"].append("Included Level")

        world.location_table = selected_levels + victory_locations

    included_count = len(selected_levels)

    goal_count_val = get_option_value(multiworld, player, "goal_level_count")
    actual_goal_count = min(goal_count_val, included_count)

    goal_pct_val = get_option_value(multiworld, player, "goal_level_percentage")
    actual_goal_pct_count = max(1, int(round(included_count * (goal_pct_val / 100.0))))

    def update_goal_requires(loc, required_count):
        if isinstance(loc, dict):
            loc["requires"] = {"Included Level": required_count}
        else:
            if hasattr(loc, "requires"):
                loc.requires = {"Included Level": required_count}
            else:
                loc["requires"] = {"Included Level": required_count}

    if isinstance(world.location_table, dict):
        if "Goal: Complete Specific Number of Levels" in world.location_table:
            update_goal_requires(world.location_table["Goal: Complete Specific Number of Levels"], actual_goal_count)
        if "Goal: Complete Percentage of Levels" in world.location_table:
            update_goal_requires(world.location_table["Goal: Complete Percentage of Levels"], actual_goal_pct_count)
    else:
        for loc in world.location_table:
            if loc.get("name") == "Goal: Complete Specific Number of Levels":
                update_goal_requires(loc, actual_goal_count)
            elif loc.get("name") == "Goal: Complete Percentage of Levels":
                update_goal_requires(loc, actual_goal_pct_count)

def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    locationNamesToRemove: list[str] = []


    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    option_keys = ["RemoveCreators", "RemoveSongs", "RemoveSongArtists"]

    categories_to_remove = set()
    for key in option_keys:
        option_obj = getattr(world.options, key, None)
        if option_obj and option_obj.value:
            val = option_obj.value
            if isinstance(val, str):
                categories_to_remove.add(val)
            else:
                categories_to_remove.update(val)

    if not categories_to_remove:
        return item_config

    def has_removed_category(entry):
        categories = entry.get("category", [])
        if isinstance(categories, str):
            categories = [categories]
        return any(cat in categories_to_remove for cat in categories)

    world.item_table = [item for item in world.item_table if not has_removed_category(item)]

    world.location_table = [loc for loc in world.location_table if not has_removed_category(loc)]
    active_location_names = set(loc.get("name") for loc in world.location_table)


    return item_config

def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    itemNamesToRemove: list[str] = []


    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        remove_specific_item(item_pool, item)

    return item_pool



def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

def after_set_rules(world: World, multiworld: MultiWorld, player: int):

    def Example_Rule(state: CollectionState) -> bool:
        return True



def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    count_option = getattr(world.options, "location_count", None)
    if not count_option:
        return

    target_count = count_option.value

    all_locations = [loc.get("name") for loc in world.location_table]

    if len(all_locations) > target_count:
        selected_locations = set(world.random.sample(all_locations, target_count))
        world.location_table = [loc for loc in world.location_table if loc.get("name") in selected_locations]

def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass

def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass


def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:


    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass

def hook_interpret_slot_data(world: World, player: int, slot_data: dict[str, Any]) -> dict[str, Any]:
    """
        Called when Universal Tracker wants to perform a fake generation
        Use this if you want to use or modify the slot_data for passed into re_gen_passthrough
    """
    return slot_data
