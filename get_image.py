import cv2
from vimba import *
from datetime import datetime

with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    with cams[0] as cam:
        dt_img1 = datetime.now()
        dt_img1.microsecond 
        frame = cam.get_frame()
        frame.convert_pixel_format(PixelFormat.Bgr8)
        #cv2.imwrite('frame1.jpg', frame.as_opencv_image())
        image=cv2.rotate(frame.as_opencv_image(), cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite('Cam1_Frm1_Spr.jpg', image)
        cam.stop_streaming()

    with cams[1] as cam:
        dt_img2 = datetime.now()
        dt_img2.microsecond
        frame = cam.get_frame()
        frame.convert_pixel_format(PixelFormat.Bgr8)
        #cv2.imwrite('frame2.jpg', frame.as_opencv_image())
        image=cv2.rotate(frame.as_opencv_image(), cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite('Cam2_Frm1_Spr.jpg', image)
        cam.stop_streaming()

    with cams[0] as cam:
        dt_img3 = datetime.now()
        dt_img3.microsecond 
        frame = cam.get_frame()
        frame.convert_pixel_format(PixelFormat.Bgr8)
        #cv2.imwrite('frame3.jpg', frame.as_opencv_image())
        image=cv2.rotate(frame.as_opencv_image(), cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite('Cam1_Frm2_Spr.jpg', image)
        cam.stop_streaming()

    print("Cam1_Frm1_Spr_Time =", dt_img1)
    print("Cam2_Frm1_Spr_Time =", dt_img2) 
    print("Cam1_Frm2_Spr_Time =", dt_img3) 
    