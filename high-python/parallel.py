import time
from threading import Thread

def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i

class FactorizeThread(Thread):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

numbers = [2139079,1232472,3213932,2314921]

start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)
    #list(factorize(number))
for th in threads:
    th.join()
    print(th.factors)
print(threads)
end = time.time()
print('Time was %.3f' %(end - start))