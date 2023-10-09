from itertools import combinations

# Données
actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ('action-3', 50, 15),
    ('action-4', 70, 20),
    ('action-5', 60, 17),
    ('action-6', 80, 25),
    ('action-7', 22, 7),
    ('action-8', 26, 11),
    ('action-9', 48, 13),
    ('action-10',  34, 27),
    ('action-11',  42, 17),
    ('action-12',  110, 9),
    ('action-13',  38, 23),
    ('action-14',  14, 1),
    ('action-15',  18, 3),
    ('action-16',  8, 8),
    ('action-17',  4, 12),
    ('action-18',  10, 14),
    ('action-19',  24, 21),
    ('action-20',  114, 18),
]

budget_max = 500

def force_brute_optimisation(actions, budget_max):
    meilleure_combinaison = None
    meilleur_profit = 0
    meilleure_depense = 0

    # Génération de toutes les combinaisons possibles d'indices d'actions
    for r in range(1, len(actions) + 1):
        for combinaison_indices in combinations(range(len(actions)), r):
            combinaison = [actions[i] for i in combinaison_indices]
            somme_depensee = sum(action[1] for action in combinaison)

            if somme_depensee <= budget_max:
                profit = sum(action[1] * action[2] / 100 for action in combinaison)

                if profit > meilleur_profit:
                    meilleure_combinaison = combinaison
                    meilleur_profit = profit
                    meilleure_depense = somme_depensee

    return meilleure_combinaison, meilleure_depense

# Exécution de l'algorithme
resultat, montant_depense = force_brute_optimisation(actions, budget_max)

# Affichage du résultat
print("Meilleure combinaison d'actions :", resultat)
print("Montant total dépensé :", montant_depense, "euros")