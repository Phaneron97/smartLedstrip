import threading

class ThreadManager(threading.Thread):
    def __init__(self, target=None, args=()):
        super().__init__(target=target, args = args)
        self.target = target
        self.args = args

    def start(self): # start thread
        super().start()

    def terminate(self, timeout=None): # main thread waits until the thread join is called on has finished executing
        super().join(timeout)

    def alive(self): # Check if thread is running
        return super().is_alive()