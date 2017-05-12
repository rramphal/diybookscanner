#!/usr/bin/env python
#
# Scanning script for the Noisebridge book scanner with a single camera.

import sys
import subprocess
import re
import time
import os

GPHOTO = 'gphoto2'
IMG_FORMAT = 'img%05d.jpg'

def snap(camera, filename):
    '''Starts a process to capture and save an image with the given
    camera.'''
    return subprocess.Popen([GPHOTO, '--capture-image-and-download',
                             '--force-overwrite', '--port', camera,
                             '--filename', filename])

def wait(process):
    '''Wait for process to end.'''
    while process.poll() is None:
        time.sleep(0.1)
    assert process.returncode == 0

# On Mac, the PTPCamera process takes control of the camera, so kill it.
devnull = open(os.devnull, 'w')
subprocess.call(["killall", "PTPCamera"], stderr=devnull)  # ignore output
devnull.close()

print 'detecting camera'
gphoto_output = subprocess.check_output([GPHOTO, '--auto-detect'])
cameras = re.findall('usb:\d*,\d*', gphoto_output)
if len(cameras) is not 1:
    print 'Failed to find camera. Results for "'+GPHOTO+' --auto-detect":'
    print gphoto_output
    sys.exit(1)
camera = cameras[0]

# main scanning loop
img_num = 0
while True:
    x = raw_input('\nReady. Press enter to capture, image number to jump, q to quit: ')
    if x == 'q':  # quit
        break
    if x == '':  # take next picture
        process = snap(camera, IMG_FORMAT % img_num)
        wait(process)
	img_num += 2
        continue
    try:  # assume x is an image number to jump to
        img_num = int(x) // 2 * 2  # convert to even number
    except ValueError:
        print 'unrecognized command'
        continue
