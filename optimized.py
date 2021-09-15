import itertools
import time
import csv
from operator import itemgetter

def get_csv(csv_name):
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
        return data_read

def calc_price_combination(combination):
    result = []
    for i in combination:
        result.append(float(i[1]))
        
    return sum(result)

def calc_benefit_combination(combination):
    result = []
    for i in combination:
        result.append(
            (float(i[1]) * (1 + float(i[2]))) / 100
        )
    return sum(result)

def delete_wrong_data(actions):
    for action in actions:
        if float(action[1]) <= 0 or float(action[2]) <= 0:
            actions.remove(action)
    
    return actions

def scan_file(data):
    for i in range(6):
        clear_data = delete_wrong_data(data)
    
    return clear_data
    
def sorting_data(data):
    action_list = []
    count_total = 500
    for i in sorted(data, key=lambda x: float(x[2])/100/float(x[1]), reverse=True): # tri des action par le rendement
        if float(i[1]) <= count_total:    # si prix de l'action <= au prix total du sac a dos
            action_list.append(i)
            count_total = count_total - float(i[1])   # décremente du prix de l'action (budget restant)
    
    return action_list

def main():
    data = get_csv("dataset2.csv")
    data_clear = scan_file(data)
    action_list= sorting_data(data_clear)
    
    print()
    print(f"Le meilleur investissement est:")
    for action in action_list:
        print(action[0])
    print()
    print(f"Avec un benefice de: {calc_benefit_combination(action_list)}€ après 2 ans")
    print(f"Pour un cout d'achat total de: {calc_price_combination(action_list)}€")
    
    


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
