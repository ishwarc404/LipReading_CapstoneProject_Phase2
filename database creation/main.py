# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
import dlib
import sys
import select
import glob
import os
import time
from os import listdir
from os.path import isfile, join
import numpy as np
import re
import math
import string
import random

def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return True
    return False



def randomstring():
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(10))

# construct the argument parse and parse the arguments
# n is the max iteration number the program waits for "press Enter"
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=1000,
	help="# of frames to loop over for FPS test")
args = vars(ap.parse_args())

while True:
	# clean_pictures() --- we do not need to clean pictures now
	print("[INFO] sampling THREADED frames from webcam...")
	vs = WebcamVideoStream(src=0).start()
	fps = FPS().start()
	record_index=1
	triggered=heardEnter()
	if triggered==True:
		print("Triggered: Start speaking")
		triggered=False
		newfolderpath = randomstring()
		os.mkdir("pictures/" + newfolderpath)
	# loop over some frames...this time using the threaded stream
		while fps._numFrames < 30:
			# grab the frame from the threaded video stream and resize it
			# to have a maximum width of 400 pixels
			frame = vs.read()
			# frame = cv2.resize(frame, (512, 256))
			triggered=heardEnter()

			print("frames: "+str(fps._numFrames)+" heardEnter: "+str(triggered)+ " record_index: "+str(record_index))

			if triggered==True:
				print("Triggered: Stop speaking")
				# sys.exit(0)
				break

			
			cv2.imwrite("pictures/" + newfolderpath + "/" + str(record_index)+".jpg", frame)
			record_index=record_index+1

			key= 0xFF & cv2.waitKey(35)
			# update the FPS counter
			fps.update()

	# stop the timer and display FPS information
	fps.stop()
	vs.stop()

	time.sleep(2)


