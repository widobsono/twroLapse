#from picamera import PiCamera
import errno
import os
import sys
import threading
from datetime import datetime
from time import sleep
import configparser

#local Lib
import dirManagement
import twroLapse as tL
import videoMaker as vM

dir = sys.path[0]
config_path = os.path.join(sys.path[0], "twro.config")
config = configparser.ConfigParser()
config.read(config_path)

npm_s = config.get('Schedule', 'npm_start')
npm_e = config.get('Schedule', 'npm_end')

nam_s = config.get('Schedule', 'nam_start')
nam_e = config.get('Schedule', 'nam_end')

day_s = config.get('Schedule', 'day_start')
day_e = config.get('Schedule', 'day_end')

#datetime.now().strftime('%Y-%m-%d')
#datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

npm_inv = int(config.get('Schedule', 'npm_interval'))
nam_inv = int(config.get('Schedule', 'nam_interval'))
day_inv = int(config.get('Schedule', 'day_interval'))
rst_inv = int(config.get('Schedule', 'rst_interval')) * 3600 #hours to seconds

prev_npm = 0
prev_nam = 0
prev_day = 0
prev_rst = 0

npm_B = config.get('Schedule', 'enable_night_pm')
nam_B = config.get('Schedule', 'enable_night_am')
day_B = config.get('Schedule', 'enable_day')
# print(npm_B, nam_B, day_B)

def daymin_now_val():
    a = datetime.now()
    daymin = (a.hour * 60) + a.minute
    return daymin

def time2daymin_val(time):
    hm = time.split(":")
    daymin = int((int(hm[0])*60) + int(hm[1]))
    return daymin

master_dir = config.get('Storage', 'master_dir')
ct_dir = eval(config.get('Storage', 'dir_creation'))
ct_dir_latch = 0
data_dir = 0
startup_dir = 0
print(ct_dir["t1"])
def masterDir():
    # Create directory based on current timestamp.
    data_dir = os.path.join(
        sys.path[0],
        str(master_dir) +'data-' + datetime.now().strftime('%Y-%m-%d')
        #str(master_dir) +'series-' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    )

    # Create directory with current time stamp
    dirManagement.create_timestamped_dir(data_dir)

    # Print where the files will be saved
    print("\nFiles will be saved in: " + str(data_dir) + "\n")
    return data_dir

#Video Settings
video_B = config.get('Storage', 'enable_video')
video_T = eval(config.get('Storage', 'create_video_time'))
video_latch = 0
print("Create Video:", video_B)


while True:
    #epoch for interval
    #timer Boolean

    #Function to reset latching variable
    if ( (epoch2000 - prev_rst) > rst_inv ):
        prev_rst = epoch2000
        video_latch = 0
        ct_dir_latch = 0

    if (startup_dir < 1):
        data_dir = masterDir()
        startup_dir = 5
        ct_dir_latch = 3

    if (ct_dir_latch < 1):
        for key, value in ct_dir.items():
            if ( (daymin_now_val()==time2daymin_val(value)) ):
                data_dir = masterDir()
                ct_dir_latch = 3

    epoch2000 = (datetime.now() - datetime(2000, 1, 1)).total_seconds()
    bool_npm = ( (daymin_now_val()>time2daymin_val(npm_s)) and (daymin_now_val()<time2daymin_val(npm_e)) )
    bool_nam = ( (daymin_now_val()>time2daymin_val(nam_s)) and (daymin_now_val()<time2daymin_val(nam_e)) )
    bool_day = ( (daymin_now_val()>time2daymin_val(day_s)) and (daymin_now_val()<time2daymin_val(day_e)) )
    #Timer Boolean END

    if ((npm_B == 'True') and (bool_npm)):
        #Calling Night Camera
        if ( (epoch2000 - prev_npm) > npm_inv ):
            prev_npm = epoch2000
            print("night_Lapse+PM")
            tL.capture_image(data_dir,'NPM')
        #End Night camera

    if ((nam_B == 'True') and (bool_nam)):
        #Calling Night Camera
        if ( (epoch2000 - prev_nam) > nam_inv ):
            prev_nam = epoch2000
            print("night_Lapse+AM")
            tL.capture_image(data_dir,'NAM')
        #End Night camera

    if ((day_B == 'True') and (bool_day)):
        #Calling Day Camera
        if ( (epoch2000 - prev_day) > day_inv ):
            prev_day = epoch2000
            print("dayLapse")
            tL.capture_image(data_dir,'DAY')
        #End Day camera

    if ( (video_B == 'True') and (video_latch < 1) ):
        for key, value in video_T.items():
            if (daymin_now_val()==time2daymin_val(value)):
                output = '/videoLapse'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.mp4'
                vM.makeVideo(data_dir,'/image*.jpg',data_dir,output)
                video_latch = 5

    sleep(0.5)
