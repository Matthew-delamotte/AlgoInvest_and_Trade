import json
import itertools
import time


def get_json(json_file):
    with open(json_file) as jsonfile:
        data = json.load(jsonfile)
    return data


# def get_benefit(data):
#     result = {}
#     for i in data:
#         result[i] = {
#             "price": data.get(i).get("price"),
#             "benefit": (data.get(i).get("price") * data.get(i).get("benefit")) / 100
#         }

#     return dict(
#         sorted(result.items(), key=lambda item: item[1]["benefit"], reverse=True)
#     )


# def increment_list(benefit, seuil, liste_final):
#     x = list(get_benefit(benefit).values())[0]
#     if x.get("price") + seuil <= 500 and len(benefit) > 0:
#         liste_final.append(list(get_benefit(benefit).keys())[0])
#         seuil = x.get("price") + seuil
#         del benefit[list(get_benefit(benefit).keys())[0]]
#         increment_list(benefit, seuil, liste_final)
#     elif len(benefit) > 0:
#         del benefit[list(get_benefit(benefit).keys())[0]]
#         increment_list(benefit, seuil, liste_final)
#     else:
#         return liste_final
# print(list(get_benefit(data).values())[0])
# print(list(get_benefit(data).keys())[0])


# class Action:
#     def __init__(self, name, price, benefit):
#         self.name = name
#         self.price = price
#         self.benefit = benefit


# def main():
# data = [
#     Action("1", 20, 5),
#     Action("2", 30, 10),
#     Action("3", 50, 15),
#     Action("4", 70, 20),
#     Action("5", 70, 20),
#     Action("6", 70, 20),
#     Action("7", 70, 20),
#     Action("8", 70, 20),
#     Action("9", 70, 20),
#     Action("10", 70, 20),
#     Action("11", 70, 20),
#     Action("12", 70, 20),
#     Action("13", 70, 20),
#     Action("14", 70, 20),
#     Action("15", 70, 20),
#     Action("16", 70, 20),
#     Action("17", 70, 20),
#     Action("18", 70, 20),
#     Action("19", 70, 20),
#     Action("20", 70, 20),
# ]
# print(data)


def main():
    pass


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))


def get_combinations():
    combinations_list = []
    for L in range(10, len(action) + 1 - 5):
        for combination in itertools.combinations(action, L):
            combinations_list.append(combination)
    return combinations_list
