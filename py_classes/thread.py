import threading
# import pigpioi


class Thread(threading.Thread):
    def __init__(self, target=None, *args):
        super().__init__()
        self.target = target
        self.args = args
        self._stop_event = threading.Event()

    def run(self):
        self.target(*self.args)

    def stop(self):
        self._stop_event.set()