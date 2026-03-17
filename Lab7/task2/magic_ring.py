from typing import Optional

from magic_item import MagicItem

class MagicRing(MagicItem):
    slot = "hand"

    def __init__(self, owner, name, manaCost, finger, desc: Optional[str] = None):
        super().__init__(owner, name, manaCost, desc)
        self.finger = finger.lower()

    def whichSlot(self): #overriden
        print(f"{self.name} goes to {self.slot} slot, specifically in the {self.finger} finger(s)")
        return f"{self.slot}, {self.finger}"
    
    def __str__(self):
        if self.description:
            return f"{self.owner}'s ring {self.name} that costs {self.manaCost} mana to use [{self.description}]"
        else:
            return f"{self.owner}'s ring {self.name} that costs {self.manaCost} mana to use, descriptionless"