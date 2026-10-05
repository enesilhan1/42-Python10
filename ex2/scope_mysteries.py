from collections.abc import Callable


def mage_counter() -> Callable:
    count: int = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> Callable:
    total_power: int = initial_power
    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator

def enchantment_factory(enchantment_type: str) -> Callable:
    pass

def memory_vault() -> dict[str, Callable]:
    pass
