from collections.abc import Callable
import functools
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__} ...")
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_spend = end_time - start_time
        print(f"Spell completed in {time_spend:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    pass

def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass