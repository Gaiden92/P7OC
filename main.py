import pandas as pd
import tableprint as tp


from optimized import algorithme_dynamique, actions
from bruteforce import algorithme_force_brute


# Fichier de donnée
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
    print(tuple)
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

def verifSienna(list, file):
    for element in list:
        for i in range(0,len(file)):
            if element in file[i]:
                print(file[i])

def main():
    MAX_BUDGET = 500
    DATA_FILE_1 = "data/dataset1_Python+P7.csv"
    DATA_FILE_2 = "data/dataset2_Python+P7.csv"

    data1 = createData(DATA_FILE_1)
    data2 = createData(DATA_FILE_2)

    sienna_results = [  
                    "Share-ECAQ",
                    "Share-IXCI",
                    "Share-FWBE",
                    "Share-ZOFA",
                    "Share-PLLK",
                    "Share-YFVZ",
                    "Share-ANFX",
                    "Share-PATS",
                    "Share-NDKR",
                    "Share-ALIY",
                    "Share-JWGF",
                    "Share-JGTW",
                    "Share-FAPS",
                    "Share-VCAX",
                    "Share-LFXB",
                    "Share-DWSK",
                    "Share-XQII",
                    "Share-ROOM"
                ]
    
    # display_result(algorithme_dynamique(MAX_BUDGET * 100, data1), float_in_data=True)
    # display_result(algorithme_dynamique(MAX_BUDGET * 100, data2), float_in_data=True)


if __name__ == "__main__":  
    main()