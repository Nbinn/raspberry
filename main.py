import scheduler
import time


count = 0

def Test():
    print("Hello\n")
def Test2():
    global count
    count += 1
    print ("Task2\n")


Sche = scheduler.Scheduler()
Sche.SCH_Init()

task1=Sche.SCH_Add_Task(Test, DELAY= 0, PERIOD=1000)
task2=Sche.SCH_Add_Task(Test2, DELAY= 0, PERIOD=1000)



while(1):
    Sche.SCH_Update()
    Sche.SCH_Dispatch_Tasks()
    
    if count == 5:
        Sche.SCH_Delete(task2)
        count += 1

    time.sleep(0.1)
