# Python recursive


def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


# print(factorielle(5))


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


# print(fibo(9))


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
 
def combinations(n, k, min_n=0, accumulator=None):
    if accumulator is None:
        accumulator = []
    if k == 0:
        return [accumulator]
    else:
        return [l for x in range(min_n, n)
                for l in combinations(n, k - 1, x + 1, accumulator + [x + 1])]

result = combinations(len(data), 10)


import threading                                                                

def process(items, start, end):                                                 
    for item in items[start:end]:                                               
        try:                                                                    
            api.my_operation(item)                                              
        except Exception:                                                       
            print('error with item')                                            


def split_processing(items, num_splits=4):                                      
    split_size = len(items) // num_splits                                       
    threads = []                                                                
    for i in range(num_splits):                                                 
        # determine the indices of the list this thread will handle             
        start = i * split_size                                                  
        # special case on the last chunk to account for uneven splits           
        end = None if i+1 == num_splits else (i+1) * split_size                 
        # create the thread                                                     
        threads.append(                                                         
            threading.Thread(target=process, args=(items, start, end)))         
        threads[-1].start() # start the thread we just created                  

    # wait for all threads to finish                                            
    for t in threads:                                                           
        t.join()                                                                



split_processing(items)