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
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get("power")
            if power is None:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            if power is None or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator 
            

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    res = fireball()
    print(f"Result: {res}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise RuntimeError("The spell collapsed")

    @retry_spell(3)
    def stable_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(unstable_spell())
    print(stable_spell())

    print("\nTesting power validator...")

    @power_validator(10)
    def lightning_bolt(spell_name: str, power: int) -> str:
        return f"{spell_name} strikes with {power} power"

    print(lightning_bolt("Lightning Bolt", 15))
    print(lightning_bolt("Lightning Bolt", 5))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X9"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))