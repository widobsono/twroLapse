from picamera import PiCamera
import errno
import os
import sys
import threading
from datetime import datetime
from time import sleep
import configparser
from fractions import Fraction

dir = sys.path[0]
config_path = os.path.join(sys.path[0], "twro.config")
config = configparser.ConfigParser()
config.read(config_path)
image_number=0

#Setting Up camera options
#on progress

def capture_image(data_dir,time):
    try:
        global image_number

        # Set a timer to take another picture at the proper interval after this
        # picture is taken.
        # Start up the camera.

        if (time == 'NPM') or (time == 'NAM'):
            #Capture a picture.
            shutter_millis = int(config.get('Camera', 'shutter_speed_milis'))
            rotation = int(config.get('Camera', 'rotation'))
            resolution = config.get('Camera', 'resolution')
            res = eval(resolution)
            wd = int(res['width'])
            hd = int(res['height'])
            iso = int(config.get('Camera', 'iso'))
            img_fname = '/imageNIGHT'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
            print(img_fname)
            save_img  = data_dir + img_fname
            cmd = 'raspistill -t 10 -bm -ex off -ISO {} -ag 1 -ss {} -st -o {} -w {} -h {} -rot {}'.format(iso,shutter_millis ,save_img,wd,hd,rotation)
            print(cmd)
            os.system(cmd)

        if time == 'DAY':
            shutter_day = int(config.get('Camera', 'shutter_speed_milis_day'))
            rotation = int(config.get('Camera', 'rotation'))
            resolution = config.get('Camera', 'resolution')
            res = eval(resolution)
            wd = int(res['width'])
            hd = int(res['height'])
            iso = int(config.get('Camera', 'iso'))
            img_fname = '/imageDAY'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
            save_img  = data_dir + img_fname
            print(img_fname)
            cmd = 'raspistill -t 10 -bm -ex off -ISO {} -ag 1 -ss {} -st -o {} -w {} -h {} -rot {}'.format(iso,shutter_day ,save_img,wd,hd,rotation)
            print(cmd)
            os.system(cmd)


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
