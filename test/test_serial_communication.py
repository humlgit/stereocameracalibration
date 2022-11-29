# Python code transmits a byte to Arduino /Microcontroller

import serial
import time

with serial.Serial() as ser:
    # initialize bus
    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.open()
    print("serial communication = ", ser.is_open)
    
    for i in range(20):
        # send message (arduino is waiting for "\n")
        time.sleep(2)
        bytesSent = ser.write(b'\n')
        # prints length of recived string
        print("string lenght = ", bytesSent)

    # close serial bus
    ser.close()
    print("serial communication = ", ser.is_open)

