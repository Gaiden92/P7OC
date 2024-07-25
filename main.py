import pandas as pd
import tableprint as tp

from time import time

from optimized import algorithme_dynamique
from bruteforce import algorithme_force_brute

# 1er fichier de données (20 actions)
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


# Fichier de donnée csv (1000 actions)
def createData(file: str) -> list:
    """Génère un filtrage des données à partir d'un fichier CSV.

    Arguments:
        file -- str : un fichier csv.

    Returns:
        list: une liste contenant les données filtrées.
    """
    # Test de l'existence du fichier
    try:
        dataset = pd.read_csv(file)
    except FileNotFoundError:
        print("Le fichier :", file, "n'existe pas.")
        exit()

    # Filtrage des données inférieur ou égal à 0
    datas_filter = (dataset["price"] >= 0) & (dataset["profit"] >= 0)
    dataset_filter = dataset[datas_filter]

    # Création de la liste à partir du dataframe filtré.
    data = list(
        zip(
            dataset_filter.name,
            round(dataset_filter.price * 100).astype(int),
            round(dataset_filter.price * 100).astype(int) *
            dataset_filter.profit / 100
        )
    )

    return data


def display_result(tuple, float_in_data=False) -> None:
    """Affiche les résultats de l'algorithme de force brute
    ou de l'algorithme optimisé.

    Arguments:
        tuple -- Un tuple contenant la liste des meilleurs
        combinaisons et le profit total réalisé.

    Keyword Arguments:
        float_in_data -- bool
        True : Si les données contiennent un float (default: {False})
    """

    division = 100 if float_in_data else 1
    total_profit, liste_combinaisons = tuple
    liste_combinaisons_trier = sorted(liste_combinaisons, key=lambda x: x[0])
    total_budget_utiliser = sum([i[1] for i in liste_combinaisons_trier])

    print("Meilleure combinaison :", len(liste_combinaisons_trier), "actions")
    headers = tp.header(
                            [
                                "Action",
                                "Prix",
                                "Rendement",
                                "Profit"
                            ],
                            15
                        )
    print(headers)
    for action in liste_combinaisons_trier:
        nom_action = action[0]
        prix_action = action[1] / division
        profit = action[2] / division
        rendement = (profit * 100) / prix_action
        row = tp.row(
                        [
                            nom_action,
                            f"{prix_action}€",
                            f"{round(rendement, 2)}%",
                            f"{round(profit, 3)}€"
                        ],
                        15
                    )
        print(row)
    bottom = tp.bottom(4, 15)
    print(bottom)
    print("Profit total réalisé :", round(total_profit / division, 2), "€")
    print("Coût total :", round(total_budget_utiliser / division, 2), "€")


# Fonction pour exécuter et mesurer le temps
def mesure_du_temps(budget: int, actions: list, algorithme: tuple) -> tuple:
    """Calcule le temps écoulé d'un algorithme donnée.

    Arguments:
        budget -- int: budget
        list_actions -- list: la liste des actions
        algorithme -- tupple: l'algorithme à mesurer
    """
    lancement_timer = time()
    _, _ = algorithme(budget, actions)
    temps_total = time() - lancement_timer

    return round(temps_total, 3), len(actions)


def main():
    MAX_BUDGET = 500
    DATA_FILE_1 = "data/dataset1_Python+P7.csv"
    DATA_FILE_2 = "data/dataset2_Python+P7.csv"

    data1 = createData(DATA_FILE_1)
    data2 = createData(DATA_FILE_2)

    separator = "="*100

    print("Résultats algorithme optimisé pour 20 actions")
    display_result(algorithme_dynamique(MAX_BUDGET, actions))
    
    print(separator)
    
    print("Résultats algorithme de force brute pour 20 actions")
    display_result(algorithme_force_brute(MAX_BUDGET, actions))

    print(separator)

    print("Résultats algorithme optimisé pour le fichier de data n°1")
    display_result(algorithme_dynamique(MAX_BUDGET*100, data1), True)
    
    print(separator)

    print("Résultats algorithme optimisé pour le fichier de data n°2")
    display_result(algorithme_dynamique(MAX_BUDGET*100, data2), True)


if __name__ == "__main__":
    main()
