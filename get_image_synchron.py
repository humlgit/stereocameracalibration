"""BSD 2-Clause License

Copyright (c) 2019, Allied Vision Technologies GmbH
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import sys
from typing import Optional, Tuple
from vimba import *
import time
from datetime import datetime
import cv2

def print_preamble():
    print('///////////////////////////////////////////')
    print('/// Vimba API Synchronous Grab Example ///')
    print('///////////////////////////////////////////\n')


def print_usage():
    print('Usage:')
    print('    python asynchronous_grab.py [/x] [-x] [camera_id]')
    print('    python asynchronous_grab.py [/h] [-h]')
    print()
    print('Parameters:')
    print('    /x, -x      If set, use AllocAndAnnounce mode of buffer allocation')
    print('    camera_id   ID of the camera to use (using first camera if not specified)')
    print()


def abort(reason: str, return_code: int = 1, usage: bool = False):
    print(reason + '\n')

    if usage:
        print_usage()

    sys.exit(return_code)


def parse_args() -> Tuple[Optional[str], AllocationMode]:
    args = sys.argv[1:]
    argc = len(args)

    allocation_mode = AllocationMode.AnnounceFrame
    cam_id = ""
    for arg in args:
        if arg in ('/h', '-h'):
            print_usage()
            sys.exit(0)
        elif arg in ('/x', '-x'):
            allocation_mode = AllocationMode.AllocAndAnnounceFrame
        elif not cam_id:
            cam_id = arg

    if argc > 2:
        abort(reason="Invalid number of arguments. Abort.", return_code=2, usage=True)
    
    print("allocation=", allocation_mode)
    return (cam_id if cam_id else None, allocation_mode)


def get_camera(camera_id: Optional[str]) -> Camera:
    with Vimba.get_instance() as vimba:
        if camera_id:
            try:
                return vimba.get_camera_by_id(camera_id)

            except VimbaCameraError:
                abort('Failed to access Camera \'{}\'. Abort.'.format(camera_id))

        else:
            cams = vimba.get_all_cameras()
            if not cams:
                abort('No Cameras accessible. Abort.')

            return cams[0]


def setup_camera(cam: Camera):
    with cam:
        # Try to adjust GeV packet size. This Feature is only available for GigE - Cameras.
        try:
            cam.GVSPAdjustPacketSize.run()

            while not cam.GVSPAdjustPacketSize.is_done():
                pass


        except (AttributeError, VimbaFeatureError):
            pass



def frame_handler(cam: Camera, frame: Frame):
    dt = datetime.now()
    dt.microsecond
    print("Current Time =", dt)
    print("frame= ", frame, " frame_time= ", frame.get_timestamp())
    print('{} acquired {}'.format(cam, frame), flush=True)
    time.sleep(3) # time between captures frames
    cam.queue_frame(frame)
    
    #TODO: show/save frames  
    '''
    frame_prim.convert_pixel_format(PixelFormat.Mono8)
    cv2.imwrite('frame2.jpg', frame_prim.as_opencv_image())
                    
    frame_sec.convert_pixel_format(PixelFormat.Mono8)
    cv2.imwrite('frame2.jpg', frame_sec.as_opencv_image())
    '''

def main():
    print_preamble()
    cam_id, allocation_mode = parse_args()  # cam_id = None, allocation_mode = 0

    with Vimba.get_instance() as vimba:
        cams = vimba.get_all_cameras()
        
        print("get1= ", cams[0].get_id())                               # out: DEV_0xA47010F06B00B
        print("get2= ", vimba.get_camera_by_id("DEV_0xA47010F06B00B"))  # out: Camera(id=DEV_0xA47010F06B00B)
        print("get3= ", cams) # out: cams= (<vimba.camera.Camera object at 0x0000022D3BCAD950>, <vimba.camera.Camera object at 0x0000022D2B01B8D0>)
        
        with get_camera(cams[0].get_id()) as cam_primary:
            with get_camera(cams[1].get_id()) as cam_secondary:
                #setup_camera(cam)              # only for GigE Cameras
                print('Press <enter> to stop Frame acquisition.')

                try:
                    # Start Streaming with a custom a buffer of 10 Frames (defaults to 5)
                    cam_primary.start_streaming(handler=frame_handler, buffer_count=10, allocation_mode=allocation_mode)
                    cam_secondary.start_streaming(handler=frame_handler, buffer_count=10, allocation_mode=allocation_mode)

                    input()
                    

                finally:
                    cam_primary.stop_streaming()
                    cam_secondary.stop_streaming()

if __name__ == '__main__':
    main()
