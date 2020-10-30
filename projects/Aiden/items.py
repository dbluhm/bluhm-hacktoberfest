"""Items and item associated stuff."""


class Inventory:
    """Creature inventory."""
    def __init__(self, starting_gold=None, starting_items=None):
        self.gold = starting_gold or 0
        self.items = starting_items or []


# This is the item definition
class Item:
    """
    container for item info
    """
    def __init__(self, hpboost, strboost, spdboost, defboost):
        self.hpboost = hpboost
        self.strboost = strboost
        self.spdboost = spdboost
        self.defboost = defboost


potion = Item(hpboost=5, strboost=0, spdboost=0, defboost=0)


class Market:
    """
    container for item costs
    """
    def __init__(self, cost):
        self.cost = cost
