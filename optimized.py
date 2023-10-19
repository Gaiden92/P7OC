from time import time

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

budget_max = 500


def algorithme_dynamique(budget: int, actions: list) -> tuple:
    """Fonctions algorithmique permettant de retrouver la meilleure
    combinaison d'action par optimisation.

    Arguments:
        actions -- une liste d'action.
        budget -- un entier.

    Returns:
        Un tupple contenant la liste des meilleurs actions et
        le profit réalisé.
    """
    start_time = time()
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
    print("Temps écoulé :", round(time() - start_time, 2), "secondes")
    return tableau[n][budget], combinaison
