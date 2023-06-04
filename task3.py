import physical

class Task3:
    status = 1
    counter = 0
    toggle = 0

    def __init__(self) -> None:
        self.status = 1
        self.counter = 0
        print("INIT")
        pass

    ## chay 100 ms
    def run(self):
        
        
        if self.status == 1:
            print("status: ",self.status)
            print("Sending command: ")

            if self.toggle:
                physical.setDevice1(True)
                self.toggle = 1 - self.toggle
            else:
                physical.setDevice1(False)
                self.toggle = 1 - self.toggle

            self.counter = 0
            self.status = 2
            pass


        elif self.status == 2:
            self.counter += 1
            if (self.counter >= 5):
                self.status = 3
                self.counter = 0
                print("Reading command: ",self.status)
            pass


        elif self.status == 3:
            self.counter +=1


            if (self.counter >= 10 ):
                self.status = 2
                self.counter = 0
            
            print("status: ",self.status)
            pass
