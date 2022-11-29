import cv2
from vimba import *
from datetime import datetime

with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    print("cams=", cams)
    with cams[0] as cam:
        #dt_img1 = datetime.now()
        #dt_img1.microsecond 
        frame = cam.get_frame()
        #frame.convert_pixel_format(PixelFormat.Mono8)
        #cv2.imwrite('frame.jpg', frame.as_opencv_image())
        cv2.imwrite('frame1.jpg')
        cam.stop_streaming()    
    with cams[1] as cam:
        #dt_img2 = datetime.now()
        #dt_img2.microsecond
        frame = cam.get_frame()
        #frame.convert_pixel_format(PixelFormat.Mono8)
        #cv2.imwrite('frame2.jpg', frame.as_opencv_image())
        cv2.imwrite('frame2.jpg',
        cam.stop_streaming()

    #print("Current Time Image 1 =", dt_img1)
    #print("Current Time Image 2 =", dt_img2)  