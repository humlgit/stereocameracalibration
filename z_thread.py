import threading
import time


class myFred(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starte ", self.id)
        time.sleep(self.id*3)
        print("Beende ", self.id)
    
t1 = myFred(1, "t1")
t2 = myFred(2, "t2")

t1.start() #geerbte Methode
t2.start()

print("Beende main fred")

    
    