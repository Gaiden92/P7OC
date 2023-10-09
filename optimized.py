# Données
actions = [
             ('action-1', 20, 5),
             ('action-2', 30, 10), 
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
             ('action-20',  114, 18)

 ]

budget_max = 500

def optimized_algo(actions, budget_max):
    actions_triees = sorted(actions, key=lambda x: x[2], reverse=True)

    meilleure_combinaison = []
    montant_depense = 0

    for action in actions_triees:
        if montant_depense + action[1] <= budget_max:
            meilleure_combinaison.append(action)
            montant_depense += action[1]

    return meilleure_combinaison, montant_depense

# Exécution de l'algorithme glouton
resultat_optimized, montant_depense_optimized = optimized_algo(actions, budget_max)

# Affichage du résultat
def display_result(list_result: list) -> None:
    print("Meilleure combinaison d'actions (algorithme optimisé) :")
    resultat_optimized_sort_by_action_name = sorted(list(resultat_optimized), key=lambda a : int(a[0].removeprefix("action-")))
    for actions in resultat_optimized_sort_by_action_name:
        print(f"{actions[0]} : prix de l'action : {actions[1]}€, rendement de l'action : {actions[2]}%")
    print("Montant total dépensé (algorithme optimisé) :", montant_depense_optimized, "euros")
