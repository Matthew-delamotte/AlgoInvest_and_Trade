import itertools
import time
import csv

class Action:
    def __init__(self, name, price, benefit):
        self.name = name
        self.price = price
        self.benefit = benefit

def get_csv(csv_name):
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
        return data_read

def make_instance(data):
    action_instance = []
    for info in data:
        action = Action(info[0], info[1], info[2])
        action_instance.append(action)
    return action_instance

def get_combinations(data):
    combinations_list = []
    for L in range(10, len(data) + 1):
        for combination in itertools.combinations(data, L):
            combinations_list.append(combination)
    return combinations_list


def calc_benefit_combination(combination):
    result = []
    for action in combination:
        result.append((int(action.benefit) * (1 + int(action.price))) / 100)

    return sum(result)


def calc_price_combination(combination):
    result = []
    for action in combination:
        result.append(int(action.price))

    return sum(result)


def get_best_result():
    max_benefit = 0
    max_combination = 0
    for combination in get_combinations():
        if (
            calc_benefit_combination(combination) > max_benefit
            and calc_price_combination(combination) <= 500
        ):
            max_benefit = calc_benefit_combination(combination)
            max_combination = combination
    return max_benefit, max_combination


def main():
    data = get_csv("data.csv")
    action_instance = make_instance(data)
    combinations = get_combinations(action_instance)
    print(calc_price_combination(combinations[1478]))
    # print(get_combinations())
    # max_benefit, max_combination = get_best_result()
    # print(f"Le meilleur investissement est: actions {max_combination}")
    # print(f"Avec un benefice de: {max_benefit}€ après 2 ans")
    # print(f"Pour un cout d'achat total de: {calc_price_combination(max_combination)}€")
    # # print(len(get_combinations()))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
