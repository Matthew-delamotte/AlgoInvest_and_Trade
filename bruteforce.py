import itertools
import time

action = {
    "1": {"price": 20, "benefit": 5},
    "2": {"price": 30, "benefit": 10},
    "3": {"price": 50, "benefit": 15},
    "4": {"price": 70, "benefit": 20},
    "5": {"price": 60, "benefit": 17},
    "6": {"price": 80, "benefit": 25},
    "7": {"price": 22, "benefit": 7},
    "8": {"price": 26, "benefit": 11},
    "9": {"price": 48, "benefit": 13},
    "10": {"price": 34, "benefit": 27},
    "11": {"price": 42, "benefit": 17},
    "12": {"price": 110, "benefit": 9},
    "13": {"price": 38, "benefit": 23},
    "14": {"price": 14, "benefit": 1},
    "15": {"price": 18, "benefit": 3},
    "16": {"price": 8, "benefit": 8},
    "17": {"price": 4, "benefit": 12},
    "18": {"price": 10, "benefit": 14},
    "19": {"price": 24, "benefit": 21},
    "20": {"price": 114, "benefit": 18},
}


def get_combinations():
    combinations_list = []
    for L in range(0, len(action) + 1):
        for combination in itertools.combinations(action, L):
            combinations_list.append(combination)
    return combinations_list


def calc_benefice_combinaison(combinaison):
    result = []
    for i in combinaison:
        result.append((action.get(i).get("price") * action.get(i).get("benefit")) / 100)

    return sum(result)


def calc_price_combination(combinaison):
    result = []
    for i in combinaison:
        result.append(action.get(i).get("price"))

    return sum(result)


def get_best_result():
    max_benefit = 0
    max_combination = 0
    for combination in get_combinations():
        if (
            calc_benefice_combinaison(combination) > max_benefit
            and calc_price_combination(combination) <= 500
        ):
            max_benefit = calc_benefice_combinaison(combination)
            max_combination = combination
    return max_benefit, max_combination


def main():
    max_benefit, max_combination = get_best_result()
    print(f"Le meilleur investissement est: actions {max_combination}")
    print(f"Avec un benefice de: {max_benefit}€ après 2 ans")
    print(f"Pour un cout d'achat total de: {calc_price_combination(max_combination)}€")
    # print(len(get_combinations()))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
