# Données
actions = [
    ("action-1", 20, 5),
    ("action-2", 30, 10),
    ("action-3", 50, 15),
    ("action-4", 70, 20),
    ("action-5", 60, 17),
    ("action-6", 80, 25),
    ("action-7", 22, 7),
    ("action-8", 26, 11),
    ("action-9", 48, 13),
    ("action-10", 34, 27),
    ("action-11", 42, 17),
    ("action-12", 110, 9),
    ("action-13", 38, 23),
    ("action-14", 14, 1),
    ("action-15", 18, 3),
    ("action-16", 8, 8),
    ("action-17", 4, 12),
    ("action-18", 10, 14),
    ("action-19", 24, 21),
    ("action-20", 114, 18),
]


# Algorithme Force brute (tester toute les combinaisons)
def algorithme_force_brute(budget: int, actions: list, actions_selection=[]) -> tuple:
    """Fonctions algorithmique permettant de retrouver la meilleure combinaison d'action par force brute.

    Arguments:
        actions -- une liste d'action.
        budget -- un entier.

    Returns:
        Un tupple contenant la liste des meilleurs actions et le profit réalisé.
    """
    if actions:
        val1, listVal1 = algorithme_force_brute(budget, actions[1:], actions_selection)
        action = actions[0]
        if action[1] <= budget:
            val2, listVal2 = algorithme_force_brute(
                budget - action[1], actions[1:], actions_selection + [action]
            )
            if val1 < val2:
                return val2, listVal2

        return val1, listVal1
    else:
        return sum([i[2] for i in actions_selection]), sorted(
            actions_selection, key=lambda x: x[0]
        )
