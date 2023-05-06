import threading

class Thread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            # Do some work
            pass

    def stop(self):
        self._stop_event.set()