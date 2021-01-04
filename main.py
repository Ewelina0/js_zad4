from random import randint
from timeit import default_timer as timer

import time

from random import randint

long_list = [randint(0, 3000) for element in range(1000000)]


def foo1(long_list):
    print("---------------------- Metoda 1 -------------------------")
    start = time.time()
    for i in long_list:
        if i == -1:
            print('found')
            break
    end = time.time()
    print('mineło: ', end - start, 'sekund')


def foo2(long_list):
    print("---------------------- Metoda 2 -------------------------")
    start = time.time()
    for i in range(1000000):
        if long_list[i] == -1:
            print('found')
            break
    end = time.time()
    print('mineło: ', end - start, 'sekund')


def foo3(long_list):
    print("---------------------- Metoda 3 -------------------------")
    t = time.process_time()
    for i in range(1000000):
        if long_list[i] == -1:
            print('found')
            break
    elapsed_time = time.process_time() - t
    print('mineło', elapsed_time, 'sekund')


def foo4(long_list):
    print("---------------------- Metoda 4 -------------------------")
    t = time.process_time()
    for i in long_list:
        if i == -1:
            print('found')
            break
    elapsed_time = time.process_time() - t
    print('mineło', elapsed_time, 'sekund')


if __name__ == '__main__':
    long_list = [randint(0, 3000) for element in range(1000000)]
    foo1(long_list)
    foo2(long_list)
    foo3(long_list)
    foo4(long_list)
