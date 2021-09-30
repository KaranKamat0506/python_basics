import time
class Delay:
    def __init__(self) -> None:
        print("Object is initialised here.")
    def __del__(self):
        print("Doing all the cleanup process.")

t=Delay()
t=None
time.sleep(3)
print("Completed")