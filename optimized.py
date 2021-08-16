import json
import itertools
import time


def get_json(json_file):
    with open(json_file) as jsonfile:
        data = json.load(jsonfile)
    return data


def get_combinations(data):
    combinations_list = []
    for L in range(0, len(data) + 1):
        for combination in itertools.combinations(data, L):
            if calc_price_combination(combination, data) <= 500:
                combinations_list.append(combination)

    return combinations_list


def calc_price_combination(combination, data):
    result = []
    for i in combination:
        result.append(data.get(i).get("price"))
    return sum(result)


data = {
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


def main():
    # data = get_json("data.json")
    combinations = get_combinations(data)

    # for i in data:
    #     print(data.get(i).get("price"))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
