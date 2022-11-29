from vimba import *
import cv2
import threading


with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    print(cams)
    vimba.get_all_features()
    
    cam_primary = cams[0].get_id()      # output: DEV_0xA47010F06B00B
    #cam_primary = cams[0]              # output: Camera(id=DEV_0xA47010F06B00B)
    cam_secondary = cams[1].get_id()



#print(cam_primary.get_frame())
print(cam_primary)
print(cam_secondary)

#frame_primary = cam_primary.get_frame()
#frame_secondary = cam_secondary.get_frame()
#frame_primary.convert_pixel_format(PixelFormat.Mono8)
#cv2.imwrite('frame.jpg', frame_primary.as_opencv_image())


#print(cam_primary)





'''
from pypylon import pylon

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

camera.TriggerSource.SetValue("Line1")
camera.TriggerMode.SetValue("On")

camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)


'''


def main():
    num_pics = 10
    i = 0
    with vimba.Vimba.get_instance() as vmb:
        cams = vmb.get_all_cameras()
        with cams[0] as cam:
            
            
            print(cam.get_pixel_format())
            #cam.load_settings(settings_file, vimba.camera.PersistType.All)
            cam.set_pixel_format(vimba.camera.PixelFormat.BayerRG8)
            for i in range(num_pics):
                frame, id = cams.frame_queue.get()
                cv2.imwrite('%s.jpg' %(i), frame)
                


if __name__ == "__main__":
    main()

