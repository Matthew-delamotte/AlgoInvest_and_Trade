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

def calc_benefice_combinaison(combinaison):
    result = []
    for i in combinaison:
        result.append(
            (float(i[1]) * (1 + float(i[2]))) / 100
        )
    return sum(result)

def main():
    data = get_csv("dataset1.csv")
    
    while '0.0' in l:
      del l[l.index('a')]
    
    empty_list = []
    count_total = 500
    for i in sorted(data, key=lambda x: float(x[2])/100/float(x[1]), reverse=True): # tri des action par le rendement
        if float(i[1]) <= count_total:    # si prix de l'action <= au prix total du sac a dos
            empty_list.append(i)
            count_total = count_total - float(i[1])   # décremente du prix de l'action (budget restant)
    
    print(calc_benefice_combinaison(empty_list))
    print()
    print(empty_list)   
   


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
