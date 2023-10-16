# Données
actions = [
    ("action-1", 20, 5),
    ("action-2", 30, 10),
    ('action-3', 50, 15),
    ('action-4', 70, 20),
    ('action-5', 60, 17),
    ('action-6', 80, 25),
    ('action-7', 22, 7),
    ('action-8', 26, 11),
    ('action-9', 48, 13),
    ('action-10', 34, 27),
    ('action-11', 42, 17),
    ('action-12', 110, 9),
    ('action-13', 38, 23),
    ('action-14', 14, 1),
    ('action-15', 18, 3),
    ('action-16', 8, 8),
    ('action-17', 4, 12),
    ('action-18', 10, 14),
    ('action-19', 24, 21),
    ('action-20', 114, 18)
]

budget_max = 500

# Algorithme Force brute (tester toute les combinaisons)
def algorithme_force_brute(actions: list, budget: int) -> tuple:
    """Fonctions algorithmique permettant de retrouver la meilleure combinaison d'action par force brute.

    Arguments:
        actions -- une liste d'action.
        budget -- un entier.

    Returns:
        Un tupple contenant la liste des meilleurs actions, le profit réalisé et le coût total.
    """
    total_profit = 0
    meilleure_combinaison = None

    for i in range(2**len(actions)):
        combinaison = []
        cout_total = 0
        profit = 0

        for j in range(len(actions)):
            if (i >> j) & 1:
                combinaison.append(actions[j])
                cout_total += actions[j][1]
                profit += actions[j][2]

        if cout_total <= budget and profit > total_profit:
            total_depense = cout_total
            total_profit = profit
            meilleure_combinaison = combinaison

    return meilleure_combinaison, total_profit, total_depense
