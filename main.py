import pandas as pd
import tableprint as tp

from optimized import algorithme_dynamique
from bruteforce import algorithme_force_brute

BUDGET_MAX = 500

### Fichier de donnée 1 ###
def createData(file: str)-> list:

    # Dataframe pour le fichier dataset
    dataset = pd.read_csv(file)

    # Remplacement des valeurs null
    dataset[["price", "profit"]].fillna(0, axis=1)

    # Filtrage des données inférieur ou égal à 0
    datas_filter = (dataset["price"] > 0) & (dataset["profit"] > 0)
    dataset_filter = dataset[datas_filter]

    data = list(
        zip(
            dataset_filter["name"],
            (dataset_filter["price"] * 100).astype(int),
            (dataset_filter["price"] * 100).astype(int) * dataset_filter["profit"] / 100,
        )
    )

    return data

data1 = createData("data/dataset1_Python+P7.csv")
data2 = createData("data/dataset2_Python+P7.csv")


def display_result(*tuple):
    total_profit, liste_combinaisons = tuple
    total_budget_utiliser = sum([i[1] for i in liste_combinaisons])

    print("Meilleure combinaison :", len(liste_combinaisons), "actions")
    headers = tp.header(["Action", "Prix", "Rendement" ,"Profit"], 15)
    print(headers)
    for action in liste_combinaisons:
        nom_action = action[0]
        prix_action = action[1] / 100 
        profit = action[2] / 100
        rendement = (profit * 100) / prix_action
        row = tp.row([nom_action, f"{prix_action}€", f"{round(rendement, 2)}%", f"{round(profit, 2)}€"], 15)
        print(row)
    bottom = tp.bottom(4, 15)
    print(bottom)
    print("Profit total réalisé :", round(total_profit / 100, 2), "€")
    print("Coût total :", total_budget_utiliser / 100, "€")


display_result(*algorithme_dynamique(BUDGET_MAX,data1))
display_result(*algorithme_dynamique(BUDGET_MAX,data2))