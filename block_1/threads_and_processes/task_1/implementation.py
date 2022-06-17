import multiprocessing

import threading
from threading import Thread

class Composer:

    front = multiprocessing.Process(target=self.aaa)
    back = multiprocessing.Process()

    def start(self):
        self.front.start()
        self.back.start()
        self.front.join()
        self.back.join()

    def get_front(self):
        return self.front

    def aaa(self):
        return 6







