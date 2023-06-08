import time

print("Sensors and Actuators")
import serial.tools.list_ports


# def getPort():
#     ports = serial.tools.list_ports.comports()
#     N = len(ports)
#     commPort = "None"
#     for i in range(0, N):
#         port = ports[i]
#         strPort = str(port)
#         if "ttyUSB" in strPort:
#             splitPort = strPort.split(" ")
#             commPort = (splitPort[0])
#     return commPort
#     ##return "/dev/ttyUSB0"

#
# portName = getPort()

ser = serial.Serial(port="COM4", baudrate=9600)
ser2 = serial.Serial(port="COM8", baudrate=9600)

# if portName != "None":

#     try:
#         ser = serial.Serial(port=portName, baudrate=9600)
#         ser2 = serial.Serial(port="COM8", baudrate=9600)
#     except:
        


print(ser)

relay1_ON  = [0, 6, 0, 0, 0, 255, 200, 91]
relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    time.sleep(1)
    print(serial_read_data(ser))




def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0


temp = 0
mois = 0

soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    global temp
    
    ser.write(soil_temperature)
    time.sleep(1)

    temp = serial_read_data(ser)/100

    return temp

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    global mois
    
    ser.write(soil_moisture)
    time.sleep(1)

    mois = serial_read_data(ser)/100

    return mois

while True:
    print("TEST RELAY")
    print(readTemperature())
    ##setDevice1(True)
    time.sleep(1)
    ##setDevice1(False)
    print(readMoisture())

    time.sleep(1)

    result = "cm4," + str(temp) + "," + str(mois)
    ser2.write(result.encode())

    time.sleep(10)