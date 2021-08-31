import threading
import itertools
import time
import csv


class Action:
    def __init__(self, name, price, benefit):
        self.name = name
        self.price = price
        self.benefit = benefit
        

def get_csv():
    with open("data.csv") as csvfile:
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


def get_combinations(l):
    if l:
      result = get_combinations(l[:-1])
      return result + [c + [l[-1]] for c in result]
    else:
      return [[]]
  
  
def calc_price_combination(combination, data):
    result = []
    for i in combination:
        result.append(data.get(i).get("price"))

    return sum(result)

def main():
    data = get_csv()
    
    action_instance = make_instance(data)
    # print(action_instance)
    
    combinations = get_combinations(action_instance)
    print(len(combinations))


    # for i in action_instance:
    #     print(i.name)
    # th1 = Myprocess()
    # th2 = Myprocess()

    # th1.start()
    # th2.start()

    # th1.join()
    # th2.join()

    # print("End")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
