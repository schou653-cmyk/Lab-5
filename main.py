from characters1 import Fighter, Mage, MeleeWeapon, RangedWeapon, MagicWeapon
from combat import attack


def main():
    # Setup fighters & weapons
    aragorn = Fighter("Aragorn", health=100, speed=10)
    gandalf = Mage("Gandalf", health=80, mana=100)
    orc = Fighter("Orc", health=50, speed=5)

    sword = MeleeWeapon("Broadsword", damage=20)
    bow = RangedWeapon("Longbow", damage=15, range=40)
    staff = MagicWeapon("Fire Staff", damage=35, range=25, mana_cost=20)

    print("--- Running Valid Combat Test ---")
    attack(aragorn, sword, orc, distance=0)
    attack(aragorn, bow, orc, distance=20)
    attack(gandalf, staff, orc, distance=15)

    print("\n--- Running Expected Exception Test ---")
    try:
        attack(aragorn, staff, orc, distance=10)
    except TypeError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()