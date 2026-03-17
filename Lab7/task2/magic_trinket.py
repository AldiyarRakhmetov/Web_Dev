from typing import Optional

from magic_item import MagicItem

class MagicTrinket(MagicItem):
    def __init__(self, owner, name, desc: Optional[str] = None):
        super().__init__(owner, name, 0, desc)

    def cast(self): #overriden
        print(f"Trinket {self.name} can't cast, trinkets are passive")

    def __str__(self):
        if self.description:
            return f"{self.owner}'s trinket {self.name} [{self.description}]"
        else:
            return f"{self.owner}'s trinket {self.name}, descriptionless"