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

    for i, spell in enumerate(spells):
        if not callable(spell):
            raise TypeError(f"All elements in spells must be callable, element at index {i} is {type(spell).__name__}")
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with power {power}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {power} health to {target}"

    def power_check(target: str, power: int) -> str:
        return str(power)

    target: str = "Dragon"

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined_spell(target, 10))}")

    print("\nTesting power amplifier...")
    amplified_check = power_amplifier(power_check, 3)
    print(f"Original: {power_check(target, 10)}, "
          f"Amplified: {amplified_check(target, 10)}")
    amplified_fireball = power_amplifier(fireball, 3)
    print(f"Amplified fireball: {amplified_fireball(target, 10)}")