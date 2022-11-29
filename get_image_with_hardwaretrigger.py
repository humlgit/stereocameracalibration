import cv2
from vimba import *
from datetime import datetime
import serial
import time
from matplotlib import pyplot as plt

#ser = serial.Serial()
# initialize bus
#ser.baudrate = 9600
#ser.port = 'COM3'
#ser.open()
#print("serial communication = ", ser.is_open)

with Vimba.get_instance() as vimba:
    with vimba.get_all_cameras() as cams:

        cam_primary = cams[0]
        cam_secondary = cams[1]

#time.sleep(2)
        frame_primary = cam_primary.queue_frame()
        frame_secondary = cam_secondary.queue_frame()
#ser.write(b'\n')
        frame_primary.convert_pixel_format(PixelFormat.Mono8)
        frame_secondary.convert_pixel_format(PixelFormat.Mono8)
        cv2.imwrite('frame.jpg', frame_primary.as_opencv_image())
        cv2.imwrite('frame2.jpg', frame_secondary.as_opencv_image())

        cams.stop_streaming()




#print("Current Time Image 1 =", dt_img1)
#print("Current Time Image 2 =", dt_img2)  


# close serial bus
#ser.close()
#print("serial communication = ", ser.is_open)

