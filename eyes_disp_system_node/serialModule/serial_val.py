import serial
import time

class SerialUART:
    def __init__(self, port = '/dev/ttyACM0', speed = 9600, timeOut = None, debaug = True):
        if debaug == True:
            print('port = ', port)
            print('speed = ',speed)
            print('timeOut = ', timeOut)

        self.ser = serial.Serial(port, speed, timeout=timeOut)

    def writeStr(self, strs):
        self.ser.write(str(strs).encode())

    def writeStrln(self, strs):
        self.ser.write(str(strs + '\n').encode())

    def readStr(self):
        strs0 = str(self.ser.readline())
        strs1 = strs0.split("'")
        strs2 = strs1[1].split("\\")
        return strs2[0]

    def close(self):
        self.ser.close()