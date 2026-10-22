from characters1 import Character, Mage, Weapon, MagicWeapon


def attack(attacker: Character, weapon: Weapon, target: Character, distance: int) -> None:
    """Handles combat interactions between characters using weapons."""
    if distance < 0:
        raise ValueError("Attack distance cannot be negative.")

    # 1. Only Mages can use a MagicWeapon
    if isinstance(weapon, MagicWeapon) and not isinstance(attacker, Mage):
        raise TypeError(f"Illegal Weapon: Only Mages can use {weapon.name}, but {attacker.name} is a {type(attacker).__name__}.")

    # 2. Only weapons with a range attribute can be used at distances > 0
    if not hasattr(weapon, "range") and distance > 0:
        raise ValueError(f"Out of Reach: {weapon.name} has no range attribute and cannot attack at distance {distance} > 0.")

    # 3. Weapons with a range cannot be used at distances above that range
    if hasattr(weapon, "range") and distance > weapon.range:
        raise ValueError(f"Out of Range: Distance {distance} exceeds {weapon.name}'s maximum range of {weapon.range}.")

    # Deduct damage from target
    target.health = max(0, target.health - weapon.damage)
    print(f"{attacker.name} attacked {target.name} with {weapon.name} at distance {distance}m for {weapon.damage} dmg! ({target.name} HP: {target.health})")