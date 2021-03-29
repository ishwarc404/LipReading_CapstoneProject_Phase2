# import the necessary packages
import sys
import select
import glob
import os
import time
from frechetdist import frdist
import re
import math
import similarity
import slidingWindow
import concate

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



def processImages():

	#this tells us how to process the frames for the CNN model
	#also returns vertical_distances which is already calculated in the analyse window function
	#so we don't have to recalculate it

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
	

	#concat logic to come here


	#CNN model runs here



	#frechet distance model runs here
	result = similarity.similarityIndex(vertical_distances)
	outputfile = open("result_lip/text_.txt",'w')
	outputfile.write(result)
	outputfile.close()



