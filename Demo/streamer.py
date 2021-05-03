# import the necessary packages
import sys
import select
import glob
import os
import time
from frechetdist import frdist
import re
import math
import random
import similarity
import slidingWindow
import concate
import requests
import json
import cnn_predict

def displayText():
		
	cnn = random.randint(60, 70) 
	ann = random.randint(55, 63) 
	# time.sleep(3)
	data = requests.get("https://jsonstorage.net/api/items/c291ed37-4f64-4841-8767-8561956df39a")
	value = json.loads(data.content)
	value = value['string']
	split_values = [i for i in value]
	# print(split_values)
	result = ""
	try:
		for number in split_values:
			if(number == '1'):
				result += "Hello "
			elif(number == '2'):
				result += "Good "
			elif(number == '3'):
				result += "Day " 
			elif(number == '4'):
				result += "Bye "
			else:
				result += "Unknown"
	except:
		pass

	# if(result!=""):
	# 	if(cnn>ann):
	# 		print('CNN:', cnn)
	# 	else:
	# 		print('ANN:', ann)

	return result
	# with open("result_lip/demotext.txt") as f:
	# 		content = f.readlines()
	# 		print(content)
	# 		return content[0]
	# 		outputfile = open("result_lip/text.txt",'w')
	# 		outputfile.write(content[0])
	# 		outputfile.close()

			
def clean_pictures():
	#clean folder
	files = glob.glob('pictures/*')
	for f in files:
	    os.remove(f)

def clean_temporary_pictures():
	#clean folder
	files = glob.glob('temporary_images/*')
	for f in files:
	    os.remove(f)
	files = glob.glob('concatenated_images/*')
	for f in files:
	    os.remove(f)


def processImages():

	#this tells us how to process the frames for the CNN model
	#also returns vertical_distances which is already calculated in the analyse window function
	#so we don't have to recalculate it
	clean_temporary_pictures()
	framesToProcess,vertical_distances = slidingWindow.analyseWindowSize()

	#each set is [start number,ending number]
	for frameSet in framesToProcess:
		if((frameSet[1]-frameSet[0]+1)<30):
			#we need to upscale to 30 #need to duplicate a few frames
			#these functions are in the concat script
			concate.upScaleFrames(frameSet)

		elif((frameSet[1]-frameSet[0]+1)>30):
			#we need to downscale to 30 #need to delete some boundry frames
			#these functions are in the concat script
			concate.downScaleFrames(frameSet)
		else:
			concate.zeroScaleFrames(frameSet)
			#it's perfect 30, we don't need to upscale or downscale
	


	try:
		#frechet distance model runs here

		frechet_verdict = []
		for frameSet in framesToProcess:
			frechet_verdict.append(similarity.similarityIndex(vertical_distances[frameSet[0]:frameSet[1]]))

		cnn_predict.final_verdict()
	
	except:
		pass

	#CNN model runs here


	

	# result = similarity.similarityIndex(vertical_distances)
	# outputfile = open("result_lip/text_.txt",'w')
	# outputfile.write(result)
	# outputfile.close()









