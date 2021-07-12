import errno
import os
import sys
from datetime import datetime
from time import sleep

print("Succes Importing dir Management")
def create_timestamped_dir(dir):
    try:
        os.makedirs(dir)
        print("Directory created!")
    except OSError as e:
        print("Directory exist!")
        if e.errno != errno.EEXIST:
            raise
