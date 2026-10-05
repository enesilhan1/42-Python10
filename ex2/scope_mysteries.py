from collections.abc import Callable
from typing import Any

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
    def ench_item(item: str) -> str:
        return f"{enchantment_type} {item}"
    return ench_item

def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}
    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        else:
            return "Memory not found"
    return{"store": store, "recall": recall}
        
