#python script to convert all webp,png,jpeg images in a directory to jpg format
#requires opencv

import os
import cv2 as cv

#fill in your origin directory i.e where your images to be converted are located
#example: origin = '/home/praveen/origin'
origin = ''

#fill in your destination directory i.e where your converted images to be stored
#example: origin = '/home/praveen/destination'
destination = ''

included_ext = ['webp','jpeg','png']
arr=[fn for fn in os.listdir(origin) if any(fn.endswith(ext) for ext in included_ext)]
i=0

for ele in arr:
	#print(ele)
	image_name = ele
	output_image_name = image_name[:-5]
	image= cv.imread(image_name)
	i = i+1
	cv.imwrite(output_image_name+'.jpg',image)
	
print(i)