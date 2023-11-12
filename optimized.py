def algorithme_dynamique(budget: int, actions: list) -> tuple:
    """Fonctions algorithmique permettant de retrouver la meilleure
    combinaison d'action par optimisation.

    Arguments:
        actions -- une liste d'action.
        budget -- un entier.

    Returns:
        Un tupple contenant le profit réalisé et la liste des meilleurs actions
        .
    """

    n = len(actions)
    tableau = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            nom, cout, profit = actions[i - 1]

            if cout > j:
                tableau[i][j] = tableau[i - 1][j]
            else:
                tableau[i][j] = max(
                    tableau[i - 1][j], tableau[i - 1][j - cout] + profit
                )

    combinaison = []
    j = budget

    for i in range(n, 0, -1):
        if tableau[i][j] != tableau[i - 1][j]:
            nom, cout, profit = actions[i - 1]
            combinaison.append((nom, cout, profit))

            j -= cout

    return tableau[n][budget], combinaison
