import threading

class ThreadManager(threading.Thread):
    def __init__(self, target=None, args=()):
        super().__init__(target=target, args = args)
        self.target = target
        self.args = args
        self._running = threading.Event()

    def start(self): # start thread
        self._running.set()
        super().start()

    def terminate(self, timeout=None): # main thread waits until the thread join is called on has finished executing
        print("thread will be joined after loop ends")
        self._running.clear()
        super().join(timeout)

    def alive(self): # Check if thread is running\
        print("current thread is alive")
        return super().is_alive()