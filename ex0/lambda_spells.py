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
        total_power = sum(mage["power"] for mage in mages)
        average_power = total_power / len(mages)
        average_power = round(average_power, 2)
    except ValueError:
        raise ValueError("The list of mages is empty. Cannot compute stats.")
    return {"Strongest": strongest_mage["power"], "Weakest": weakest_mage["power"], "Average": average_power}
