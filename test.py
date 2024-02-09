import multiprocessing
import time
from multiprocessing import freeze_support


def dor_smt():
    time.sleep(2)
    return "hello"



if __name__ == '__main__':
    freeze_support()
    p = multiprocessing.Process(target=dor_smt)
    p.start()
    time.sleep(1)
    p.terminate()
