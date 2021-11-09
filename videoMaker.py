#ffmpeg -framerate 8 -pattern_type glob -i '2021*.jpg' -c:v libx264 -r 15 -pix_fmt yuv420p output.mp4
#ffmpeg -framerate 8 -pattern_type glob -i 'image*.jpg' -c:v libx264 -r 15 -pix_fmt yuv420p 'nightLapse.mp4'

import errno
import os
import sys
from datetime import datetime
from time import sleep

print('Success Importing videoMaker')
def makeVideo(dirIN,name,dirOUT,vname):
    input = str(dirIN)+str(name)
    output = str(dirOUT)+str(vname)
    cmd = 'ffmpeg -framerate 8 -pattern_type glob -i \''+input+'\' -c:v libx264 -r 15 -pix_fmt yuv420p \''+output+'\''
    print(cmd)
    os.system(cmd)
    print('Success!')
