def artifact_sorter(artifacts: list[dict]) -> list[dict]:
     return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))  

def spell_transformer(spells: list[str]) -> list[str]:
    res = list(map(lambda spell: "* "+spell+" *", spells))
    return res

def mage_stats(mages: list[dict]) -> dict:

    try:
        strongest_mage = max(mages, key=lambda mage: mage["power"])
        weakest_mage = min(mages, key=lambda mage: mage["power"])
        total_power = sum(map(lambda mage: mage["power"], mages))
        average_power = total_power / len(mages)
        average_power = round(average_power, 2)
    except ValueError:
        raise ValueError("The list of mages is empty. Cannot compute stats.")
    return {"max_power": strongest_mage["power"], "min_power": weakest_mage["power"], "avg_power": average_power}


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "relic"}
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} "
        f"power) comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
        )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))