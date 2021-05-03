import numpy as np
import cv2
import os

#read from folder result_lip and write to same folder with name concate-output.jpg
def concate_images(): 
	# concate_seq= np.array([0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,11,12,13,14,14])
	#read image
	path="pictures/"
	im_1 = cv2.imread(path+"File1.jpg", cv2.IMREAD_COLOR)
	im_2 = cv2.imread(path+"File2.jpg", cv2.IMREAD_COLOR)
	im_3 = cv2.imread(path+"File3.jpg", cv2.IMREAD_COLOR)
	im_4 = cv2.imread(path+"File4.jpg", cv2.IMREAD_COLOR)
	im_5 = cv2.imread(path+"File5.jpg", cv2.IMREAD_COLOR)
	layer1 = np.concatenate((im_1, im_2, im_3, im_4, im_5), axis=1)

	im_6 = cv2.imread(path+"File6.jpg", cv2.IMREAD_COLOR)
	im_7 = cv2.imread(path+"File7.jpg", cv2.IMREAD_COLOR)
	im_8 = cv2.imread(path+"File8.jpg", cv2.IMREAD_COLOR)
	im_9 = cv2.imread(path+"File9.jpg", cv2.IMREAD_COLOR)
	im_10 = cv2.imread(path+"File10.jpg", cv2.IMREAD_COLOR)
	layer2 = np.concatenate((im_6, im_7, im_8, im_9, im_10), axis=1)

	im_11 = cv2.imread(path+"File11.jpg", cv2.IMREAD_COLOR)
	im_12 = cv2.imread(path+"File12.jpg", cv2.IMREAD_COLOR)
	im_13 = cv2.imread(path+"File13.jpg", cv2.IMREAD_COLOR)
	im_14 = cv2.imread(path+"File14.jpg", cv2.IMREAD_COLOR)
	im_15 = cv2.imread(path+"File15.jpg", cv2.IMREAD_COLOR)
	layer3 = np.concatenate((im_11, im_12, im_13, im_14, im_15), axis=1)

	im_16 = cv2.imread(path+"File16.jpg", cv2.IMREAD_COLOR)
	im_17 = cv2.imread(path+"File17.jpg", cv2.IMREAD_COLOR)
	im_18 = cv2.imread(path+"File18.jpg", cv2.IMREAD_COLOR)
	im_19 = cv2.imread(path+"File19.jpg", cv2.IMREAD_COLOR)
	im_20 = cv2.imread(path+"File20.jpg", cv2.IMREAD_COLOR)
	layer4 = np.concatenate((im_16, im_17, im_18, im_19, im_20), axis=1)

	im_21 = cv2.imread(path+"File21.jpg", cv2.IMREAD_COLOR)
	im_22 = cv2.imread(path+"File22.jpg", cv2.IMREAD_COLOR)
	im_23 = cv2.imread(path+"File23.jpg", cv2.IMREAD_COLOR)
	im_24 = cv2.imread(path+"File24.jpg", cv2.IMREAD_COLOR)
	im_25 = cv2.imread(path+"File25.jpg", cv2.IMREAD_COLOR)
	layer5 = np.concatenate((im_21, im_22, im_23, im_24, im_25), axis=1)

	im_26 = cv2.imread(path+"File26.jpg", cv2.IMREAD_COLOR)
	im_27 = cv2.imread(path+"File27.jpg", cv2.IMREAD_COLOR)
	im_28 = cv2.imread(path+"File28.jpg", cv2.IMREAD_COLOR)
	im_29 = cv2.imread(path+"File29.jpg", cv2.IMREAD_COLOR)
	im_30 = cv2.imread(path+"File30.jpg", cv2.IMREAD_COLOR)
	layer6 = np.concatenate((im_26, im_27, im_28, im_29, im_30), axis=1)

	output = np.concatenate((layer1, layer2, layer3, layer4, layer5,layer6), axis=0)
	# cv2.imshow('concat',output)
	# cv2.waitKey(0) 
	output_path = "concatenated_images/"
	cv2.imwrite(output_path+"concate_output.jpg", output)
	print("[INFO] concate done")


concate_images()

# if __name__ == "__main__":
# 	directory = "pictures"
# 	folders = []
# 	for x in os.walk(directory):
# 		folders = x[1]
# 		break

# 	# the folders list contains a list of all the subfolders print(folders)
# 	#we need to call the concat function on each of these sub folders
# 	for eachfolder in folders:
# 		concate_images(eachfolder)
