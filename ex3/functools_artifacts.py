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


def memoized_fibonacci(n: int) -> int:
    pass

def spell_dispatcher() -> Callable[[Any], str]:
    pass
