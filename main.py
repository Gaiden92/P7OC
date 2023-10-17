import pandas as pd
import tableprint as tp

from optimized import algorithme_dynamique
from bruteforce import algorithme_force_brute

BUDGET_MAX = 500

### Fichier de donnée 1 ###
# Dataframe pour le fichier dataset1
dataset1 = pd.read_csv("data/dataset1_Python+P7.csv")

# Remplacement des valeurs null
dataset1[["price", "profit"]].fillna(0, axis=1)

# Filtrage des données inférieur ou égal à 0
datas_filter = (dataset1["price"] > 0) & (dataset1["profit"] > 0)
dataset1_filter = dataset1[datas_filter]

data1 = list(
    zip(
        dataset1_filter["name"],
        dataset1_filter["price"],
        dataset1_filter["price"] * dataset1_filter["profit"] / 100,
    )
)


### Fichier de donnée 2 ###
# Dataframe pour le fichier dataset2
dataset2 = pd.read_csv("data/dataset2_Python+P7.csv")

# Remplacement des valeurs null
dataset2[["price", "profit"]].fillna(0, axis=1)

# Filtrage des données inférieur ou égal à 0
datas_filter = (dataset2["price"] > 0) & (dataset2["profit"] > 0)
dataset2_filter = dataset2[datas_filter]

data2 = list(
    zip(
        dataset2_filter["name"],
        dataset2_filter["price"],
        dataset2_filter["price"] * dataset2_filter["profit"] / 100,
    )
)


def display_result(*tuple):
    total_profit, liste_combinaisons = tuple
    total_budget_utiliser = sum([i[1] for i in liste_combinaisons])

    print("Meilleure combinaison :")
    headers = tp.header(["Action", "Prix", "Profit"], 15)
    print(headers)
    for action in liste_combinaisons:
        nom_action = action[0]
        prix_action = action[1]
        profit = action[2]
        row = tp.row([nom_action, f"{prix_action}€", f"{round(profit, 2)}€"], 15)
        print(row)
    bottom = tp.bottom(3, 15)
    print(bottom)
    print("Profit total réalisé :", round(total_profit, 2), "€")
    print("Coût total :", round(total_budget_utiliser, 2), "€")


display_result(*algorithme_dynamique(BUDGET_MAX, data1))
# display_result(*algorithme_force_brute(BUDGET_MAX, data1))

display_result(*algorithme_dynamique(BUDGET_MAX, data2))
# display_result(*algorithme_force_brute(BUDGET_MAX, data2[0:20]))
