from picamera import PiCamera
import errno
import os
import sys
import threading
from datetime import datetime
from time import sleep
import configparser

dir = sys.path[0]
config_path = os.path.join(sys.path[0], "twro.config")
config = configparser.ConfigParser()
config.read(config_path)
image_number=0

#Setting Up camera options

def set_camera_options(camera):
    # Set camera resolution.
    resolution = config.get('Camera', 'resolution')
    res = eval(resolution)
    if res:
        camera.resolution = (
            int(res['width']),
            int(res['height'])
        )

    # Set ISO.
    iso = config.get('Camera', 'iso')
    if iso:
        camera.iso = int(iso)

    # Set shutter speed.
    shutter_millis = config.get('Camera', 'shutter_speed_milis')
    if shutter_millis:
        camera.shutter_speed = int(shutter_millis)
        # Sleep to allow the shutter speed to take effect correctly.
        sleep(1)
        camera.exposure_mode = 'off'

    # Set white balance.
    white_balance = config.get('Camera', 'white_balance')
    if (white_balance != 'None'):
	awb = eval(white_balance)
        camera.awb_mode = 'off'
        camera.awb_gains = (
            int(awb['red_gain']),
            int(awb['blue_gain'])
        )

    # Set camera rotation
    rotation = config.get('Camera', 'rotation')
    if rotation:
        camera.rotation = int(rotation)

    return camera

def set_camera_options_day(camera):
    # Set camera resolution.
    resolution = config.get('Camera', 'resolution')
    res = eval(resolution)
    if res:
        camera.resolution = (
            int(res['width']),
            int(res['height'])
        )

    # Set ISO.
    iso = config.get('Camera', 'iso')
    if iso:
        #camera.iso = int(iso)
        camera.iso = 0

    # Set shutter speed.
    shutter_millis = config.get('Camera', 'shutter_speed_milis')
    if shutter_millis:
        #camera.shutter_speed = int(shutter_millis)
        camera.shutter_speed = 0
        # Sleep to allow the shutter speed to take effect correctly.
        sleep(1)
        camera.exposure_mode = 'off'

    # Set white balance.
    white_balance = config.get('Camera', 'white_balance')
    if (white_balance != 'None'):
        awb = eval(white_balance)
        camera.awb_mode = 'off'
        camera.awb_gains = (
            int(awb['red_gain']),
            int(awb['blue_gain'])
        )

    # Set camera rotation
    rotation = config.get('Camera', 'rotation')
    if rotation:
        camera.rotation = int(rotation)

    return camera


def capture_image(data_dir,time):
    try:
        global image_number

        # Set a timer to take another picture at the proper interval after this
        # picture is taken.
        # Start up the camera.
        camera = PiCamera()
        if (time == 'NPM') or (time == 'NAM'):
            set_camera_options(camera)
        if time == 'DAY':
            set_camera_options_day(camera)

        # Capture a picture.
        img_fname = '/image'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
        print(img_fname)
        camera.capture(data_dir + img_fname)
        camera.close()
#	camera.stop_preview()

        # if (image_number < (config['total_images'] - 1)):
        #     image_number += 1
        # else:
        #     print ('\nTime-lapse capture complete!\n')
        #     # TODO: This doesn't pop user into the except block below :(.
        #     sys.exit()

    except (KeyboardInterrupt):
        print ("\nTime-lapse capture cancelled.\n")
    except (SystemExit):
        print ("\nTime-lapse capture stopped.\n")


# exp_milis = config.get('Camera', 'exposure_milis')

# npm_start = config.get('Schedule', 'npm_start')
# resolution = config.get('Camera', 'resolution')
# res = eval(resolution)

# Kick off the capture process.s
#capture_image()
print("Import Camera Func Success!")
#print("Mission Accomplished~!")
