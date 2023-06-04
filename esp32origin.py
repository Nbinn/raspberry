import time

print("ESP32")
import serial.tools.list_ports

def getPort():
    # ports = serial.tools.list_ports.comports()
    # N = len(ports)
    # commPort = "None"
    # for i in range(0, N):
    #     port = ports[i]
    #     strPort = str(port)
    #     if "USB Serial" in strPort:
    #         splitPort = strPort.split(" ")
    #         commPort = (splitPort[0])
    # return commPort
    #return "/dev/ttyUSB0"
    return "COM8"


portName = getPort()
print(portName)

if portName != "None":
    try:
        ser = serial.Serial(port=portName, baudrate=9600)
    except:
        ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)

def sendCMD(cmd):
    EOC = ""
    ser.write((str(cmd) + EOC).encode())




# Process on RECEIVING.....
mess = ""
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    # if splitData[1] == "TEMP":
    #     client.publish("bbc-temp", splitData[2])

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode('unicode_escape')
        ##mess = mess + ser.read(bytesToRead).decode("UTF-8").strip()
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

#######





while True:
    sendCMD("a")
    time.sleep(1)
    readSerial()
    time.sleep(1)