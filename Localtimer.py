from time import sleep,time
import threading
timerShouldClose=False
class Timer:
    def __init__(self):
        self.start_time = time()
        self.end_time = None
        self.is_running = True
        self.total_time = 0.0
        self.print_time()

    def print_time(self):
        while self.is_running:
            current_time = time()
            elapsed_time = current_time - self.start_time
            print(f" {elapsed_time:.2f} s", end='\r')
            sleep(.1)  

    def stop(self):
        self.is_running = False
        self.end_time = time()
        self.total_time = self.end_time - self.start_time
        print(f"Total time: {self.total_time:.2f} s")

    def __del__(self):
        if self.total_time == 0.0:
            self.stop()
def _s_():
    TIMER=Timer()
    while not timerShouldClose:
        pass
    TIMER.__del__()
def init_timer():
    threading.Thread(target=_s_).start()
def stop_timer():
    global timerShouldClose
    timerShouldClose=True

