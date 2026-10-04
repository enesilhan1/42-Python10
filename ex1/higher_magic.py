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
    
    if not callable(base_spell):
        raise TypeError(f"base_spell must be callable, got {type(base_spell).__name__}")
    
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition):
        raise TypeError(f"condition must be callable, got {type(condition).__name__}")
    if not callable(spell):
        raise TypeError(f"spell must be callable, got {type(spell).__name__}")
        
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional

def spell_sequence(spells: list[Callable]) -> Callable:
    pass


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with power {power}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {power} health to {target}"