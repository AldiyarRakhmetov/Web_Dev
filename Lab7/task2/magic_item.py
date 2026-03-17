from typing import Optional

class MagicItem:
    slot = "accessory"
    mana = 100

    def __init__(self, owner, name, manaCost, desc: Optional[str] = None):
        self.owner = owner
        self.name = name
        self.manaCost = manaCost
        self.description = desc

    def cast(self):
        if (self.mana - self.manaCost < 0):
            print(f"{self.name} couldn't cast, not enough mana")
        else:
            self.mana -= self.manaCost
            print(f"{self.name} casted ({self.mana} mana left)")
    
    def whichSlot(self):
        print(f"{self.name} goes to any {self.slot} slot")
        return self.slot
    
    def __str__(self):
        if self.description:
            return f"{self.owner}'s {self.name} that costs {self.manaCost} mana to use [{self.description}]"
        else:
            return f"{self.owner}'s {self.name} that costs {self.manaCost} mana to use, descriptionless"