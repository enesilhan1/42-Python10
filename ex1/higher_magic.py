from collections.abc import Callable

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    if not callable(spell1):
        raise TypeError(f"spell1 must be callable, got {type(spell1).__name__}")
    if not callable(spell2):
        raise TypeError(f"spell2 must be callable, got {type(spell2).__name__}")
    
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    pass

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass

def spell_sequence(spells: list[Callable]) -> Callable:
    pass


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with power {power}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {power} health to {target}"