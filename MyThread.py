import threading
import itertools
import time
import csv


class Action:
    def __init__(self, name, price, benefit):
        self.name = name
        self.price = price
        self.benefit = benefit


class Myprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i < 3:
            print(threading.current_thread())
            time.sleep(0.3)
            i += 1


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


def main():
    data = get_csv()
    action_instance = make_instance(data)
    for i in action_instance:
        print(i.name)

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
