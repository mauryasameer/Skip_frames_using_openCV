import os
import cv2
dir='caption'#The name of the directory in which the frames of your video will be stored

try:
	os.mkdir(dir)
	print('directory created')
except FileExistsError:
	print('already created')

vid = cv2.VideoCapture('')#give the absolute path of the file in which your video is present

c=0
i=0
frameskip=1#change it according to your need...i have kept it one if you wish to skip 5 frames change it to 5
while(vid.isOpened()):
	succ,img=vid.read()
	if succ:
		if i%frameskip==0:
			cv2.imwrite(os.getcwd()+'/'+dir+'/frame%d.jpg'%c,img)
			print('createing...'+'frame%d'%c)
			c=c+1
		i=i+1
	else:
		break
vid.release()
cv2.destroyAllWindows()

