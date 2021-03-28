# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
import dlib
# import faceAlignment as fa
import sys
import select
import glob
import os
# import predict as pred
# import concate as conc
import time
import pandas as pd 
import matplotlib.pyplot as plt
from frechetdist import frdist
from os import listdir
from os.path import isfile, join
import numpy as np
import re
import math
import similarity

detector = dlib.get_frontal_face_detector() #Face detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Landmark identifier. Set the filename to whatever you named the downloaded file

def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return True
    return False

def find_face_landmark(frame):
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	clahe_image = clahe.apply(gray)

	detections = detector(clahe_image, 1) #Detect the faces in the image

	for k,d in enumerate(detections): #For each detected face
	    shape = predictor(clahe_image, d) #Get coordinates
	    for i in range(1,68): #There are 68 landmark points on each face
	        cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,0,255), thickness=2) #For each point, draw a red circle with thickness2 on the original frame
	return frame

def displayText():
	time.sleep(3)
	with open("result_lip/demotext.txt") as f:
			content = f.readlines()
			print(content)
			outputfile = open("result_lip/text.txt",'w')
			outputfile.write(content[0])
			outputfile.close()
			
def clean_pictures():
	#clean folder
	files = glob.glob('pictures/*')
	for f in files:
	    os.remove(f)
	# files = glob.glob('result_lip/*')
	# for f in files:
	#     os.remove(f)

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def final_area(frame_path):
    
    # try:
	img = cv2.imread(frame_path)
	dets = detector(img)
	#output face landmark points inside retangle
	#shape is points datatype
	#http://dlib.net/python/#dlib.point
	for k, d in enumerate(dets):
	    shape = predictor(img, d)

	vec = np.empty([68, 2], dtype = int)
	for b in range(68):
	    vec[b][0] = shape.part(b).x
	    vec[b][1] = shape.part(b).y
	corners = vec[60:68]
	area = (PolygonArea(corners))
	vertical_distance = ( math.sqrt( pow(abs(vec[66][0]-vec[62][0]),2)+pow(abs(vec[66][1]-vec[62][1]),2) ) )
	horizontal_distance = ( math.sqrt( pow(abs(vec[64][0]-vec[60][0]),2)+pow(abs(vec[64][1]-vec[60][1]),2) ) )
	# print("Vertical Distance: ", vertical_distance)
	# print("Horizontal Distance: ", horizontal_distance)

	# print("Height coords: {} {} ".format(vec[62],vec[66])) #63,67th point
	# print("Width coords: {} {} ".format(vec[60],vec[64])) #61 and 65th point

	return area, vertical_distance, horizontal_distance

    # except:
    #     return -1

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def processImages():

	frames = [f for f in listdir("pictures") if isfile(join("pictures", f))]
	try:
		frames.remove(".DS_Store")
	except:
		pass
	frames.sort(key=natural_keys)
	#now each of these frames are going undergo the facial landmark AREA and VERTICAL height calculation
	path = "pictures"
	areas = []
	vertical_distances = []
	horizontal_distances = []
	try:
		for each_frame in frames:
				if(each_frame!=".DS_Store"):
					a,v,h = final_area(path +"/"+each_frame)
					areas.append(a)
					vertical_distances.append(v)
					horizontal_distances.append(h)

		print("DONE PROCESSING")
		
		area_max = max(areas)
		v_max = max(vertical_distances)
		h_max = max(horizontal_distances)

		new_areas = [i/area_max for i in areas]
		new_vertical_distances = [i/v_max for i in vertical_distances]
		new_horizontal_distances = [i/h_max for i in horizontal_distances]

		# print(new_areas)
		# print("--------------------")
		# print(new_vertical_distances)
		result = similarity.similarityIndex(new_vertical_distances)
		outputfile = open("result_lip/text_.txt",'w')
		outputfile.write(result)
		outputfile.close()
		# print(result)

	except Exception as e:
		print(e)
		#this is triggered when the recording is not even started
		pass



