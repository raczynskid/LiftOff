def is_sets_valid(sets) -> None:
    sets_over_five = [set for set in sets if set > 5]
    sets_negative = [set for set in sets if set < 0]
    if sets_over_five or sets_negative:
        raise ValueError(f"Invalid number of reps in a set {[set for set in sets if set > 5]}")


def is_passed(sets: list) -> bool:
    is_sets_valid(sets)
    if sum(sets) < 25:
        return False
    return True


def calculate_new_weights(lifts: dict) -> dict:
    for key, value in lifts.items():
        sets = value[-1]
        previous_weight = float(value[0])
        if is_passed(sets):
            lifts[key] = (previous_weight + 2.5, [0, 0, 0, 0, 0])
    return lifts
