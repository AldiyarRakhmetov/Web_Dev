from magic_item import MagicItem
from magic_ring import MagicRing
from magic_trinket import MagicTrinket

def main():
    scepter = MagicItem("Aghanim", "Scepter", 105, "A powerful scepter made by Aghanim himself")
    faceRing = MagicRing("Limbok", "Face Ring", 35, "Not a thumb", "A powerful ring, that must not be weared on the thumbs")
    guppyPaw = MagicTrinket("Isaac", "Guppy's Paw")

    items = [scepter, faceRing, guppyPaw]

    for item in items:
        item.cast()
        item.whichSlot()
        print(item, "\n")

if __name__ == "__main__":
    main()