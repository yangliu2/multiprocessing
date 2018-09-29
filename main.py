from multiprocessing import Pool
import time
from functools import partial

data = [
    ['a', '2'], ['b', '4']
]

def mp_worker(data, additional):
    inputs, the_time = data
    print additional
    print " Processs %s\tWaiting %s seconds" % (inputs, the_time)
    time.sleep(int(the_time))
    print " Process %s\tDONE" % inputs

def mp_handler():
    p = Pool(2)
    data.append(['c', '6'])
    print(data)
    add = "lead"
    p.map(partial(mp_worker, additional=add), data)

if __name__ == '__main__':
    mp_handler()