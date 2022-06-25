import threading
import time


def func1(x):
    time.sleep(2)
    print(f'Task {x} is done.')

def func2(x):
    time.sleep(1)
    print(f'Task {x} is done.')

worker1 = threading.Thread(target=func1, args=(1,))
worker2 = threading.Thread(target=func2, args=(2,))
worker1.start()
worker2.start()
