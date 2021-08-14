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
            combinations_list.append(combination)
    return combinations_list


def calc_price_combination(combinations):
    result = []
    # for i in combinations:
    # result.append(data.get(i).get("price"))
    # return sum(result)


def main():
    data = get_json("data.json")
    print(data[0].get("price"))
    combinations = get_combinations(data)
    # calc_price_combination(combinations)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
