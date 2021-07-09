#from picamera import PiCamera
import errno
import os
import sys
import threading
from datetime import datetime
from time import sleep
import configparser

dir = sys.path[0]
config_path = os.path.join(sys.path[0], "config.twro")
config = configparser.ConfigParser()
config.read(config_path)
image_number=0

def create_timestamped_dir(dir):
    try:
        os.makedirs(dir)
        print("Directory created!")
    except OSError as e:
        print("Directory exist!")
        if e.errno != errno.EEXIST:
            raise

#Setting Up camera options

def set_camera_options(camera):
    # Set camera resolution.
    resolution = config.get('Camera', 'resolution')
    res = eval(resolution)
    if res:
        camera.resolution = (
            res['width'],
            res['height']
        )

    # Set ISO.
    iso = config.get('Camera', 'iso')
    if iso:
        camera.iso = iso

    # Set shutter speed.
    shutter_millis = config.get('Camera', 'shutter_speed_milis')
    if shutter_millis:
        camera.shutter_speed = shutter_millis
        # Sleep to allow the shutter speed to take effect correctly.
        sleep(1)
        camera.exposure_mode = 'off'

    # Set white balance.
    white_balance = config.get('Camera', 'white_balance')
    awb = eval(white_balance)
    if white_balance:
        camera.awb_mode = 'off'
        camera.awb_gains = (
            awb['red_gain'],
            awb['blue_gain']
        )

    # Set camera rotation
    rotation = config.get('Camera', 'rotation')
    if config['rotation']:
        camera.rotation = rotation

    return camera


def daymin_now_val():
    a = datetime.now()
    daymin = (a.hour * 60) + a.minute
    return daymin

def time2daymin_val(time):
    hm = time.split(":")
    daymin = int((int(hm[0])*60) + int(hm[1]))
    return daymin

def capture_image():
    try:
        global image_number

        # Set a timer to take another picture at the proper interval after this
        # picture is taken.
        npm_interval = int(config.get('Schedule', 'npm_interval'))
        PM_capt = config.get('Schedule', 'enable_night_pm')
        npm_s = config.get('Schedule', 'npm_start')
        npm_e = config.get('Schedule', 'npm_end')

        nam_interval = int(config.get('Schedule', 'nam_interval'))
        AM_capt = config.get('Schedule', 'enable_night_am')
        nam_s = config.get('Schedule', 'nam_start')
        nam_e = config.get('Schedule', 'nam_end')

        bool_npm = ( (daymin_now_val()>time2daymin_val(npm_s)) and (daymin_now_val()<time2daymin_val(npm_e)) )

        bool_nam = (daymin_now_val()>time2daymin_val(nam_s)) and (daymin_now_val()<time2daymin_val(nam_e))

        if ((PM_capt == 'True') and bool_npm):
            thread = threading.Timer(int(npm_interval), capture_image).start()

        if ((AM_capt == 'True') and bool_nam):
            thread = threading.Timer(int(nam_interval), capture_image).start()

        # Start up the camera.
        camera = PiCamera()
        set_camera_options(camera)

        # Capture a picture.
        img_fname = '/image'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
        print(img_fname)
        camera.capture(data_dir + img_fname)
        camera.close()

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

# Create directory based on current timestamp.
master_dir = config.get('Storage', 'master_dir')

data_dir = os.path.join(
    sys.path[0],
    str(master_dir) +'data-' + datetime.now().strftime('%Y-%m-%d')
    #str(master_dir) +'series-' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
)

# Create directory with current time stamp
create_timestamped_dir(data_dir)

# Print where the files will be saved
print("\nFiles will be saved in: " + str(data_dir) + "\n")

# Kick off the capture process.s
capture_image()

print("Mission Accomplished~!")
