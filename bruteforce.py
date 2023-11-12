# Algorithme Force brute (tester toute les combinaisons)
def algorithme_force_brute(
    budget: int, actions: list, actions_selection: list = []
) -> tuple:
    """Fonctions algorithmique permettant de retrouver la meilleure
    combinaison d'action par force brute.

    Arguments:
        actions -- une liste d'action.
        budget -- un entier.

    Returns:
        Un tupple contenant la liste des meilleurs actions
        et le profit réalisé.
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
