import os
from multiprocessing import Process
from time import sleep


def task1():
    while True:
        print('--------任务1',os.getpid(),'===',os.getppid())
        sleep(1)


def task2():
    while True:
        print('--------任务2',os.getpid(),'===',os.getppid())
        sleep(0.5)



if __name__ == '__main__':
    p1 = Process(target=task1, name='任务1')
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name='任务2')
    p2.start()
    print(p2.name)
