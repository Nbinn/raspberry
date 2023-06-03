# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from scheduler import *
# from task1 import *
# from task2 import *
# from task3 import *
import random
import time
import sys
from Adafruit_IO import MQTTClient
import time

AIO_USERNAME = "jackwrion12345"
AIO_KEY = "aio_bisq78jFskfklOk7jb6e8hVAaSY4"


client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.connect()
client.loop_background()
time.sleep(5)


scheduler = Scheduler()
scheduler.SCH_Init()



def mqttTask():
    value = random.randint(0, 100)
    client.publish("door", value)
    time.sleep(30)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
scheduler.SCH_Add_Task(mqttTask,2000,1000)
while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
