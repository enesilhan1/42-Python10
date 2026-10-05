from typing import Any
from collections.abc import Callable
import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0
    
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    try:
        func = operations[operation]
    except KeyError:
        raise ValueError(f"Unknown operation: {operation}")
    

    return functools.reduce(func, spells)

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, 50, "fire")
    ice = functools.partial(base_enchantment, 50, "ice")
    lightning = functools.partial(base_enchantment, 50, "lightning")

    return {"fire": fire, "ice": ice, "lightning": lightning}

@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    

def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def base_func(spell: Any) -> str:
        return "Unknown spell type"

    @base_func.register
    def int_type(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @base_func.register
    def str_type(name: str) -> str:
        return f"Enchantment: {name}"

    @base_func.register
    def list_type(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return base_func


if __name__ == "__main__":
    print("Testing spell reducer...")
    numbers: list[int] = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(numbers, 'add')}")
    print(f"Product: {spell_reducer(numbers, 'multiply')}")
    print(f"Max: {spell_reducer(numbers, 'max')}")
    print(f"Min: {spell_reducer(numbers, 'min')}")
    try:
        spell_reducer(numbers, "divide")
    except ValueError as e:
        print(f"Error: {e}")
    print(f"Empty list: {spell_reducer([], 'add')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} enchantment ({power} power) on {target}"

    enchantments = partial_enchanter(base_enchantment)
    for enchant in enchantments.values():
        print(enchant("Sword"))