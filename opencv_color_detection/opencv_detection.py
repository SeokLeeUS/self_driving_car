import cv2
import numpy as np
img = cv2.imread('traffic_red.jpg')
#image = np.flip(imgaxis = 1)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,120,70])
upper_red=np.array([10,255,255])
mask1 = cv2.inRange(hsv,lower_red,upper_red)

lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv,lower_red,upper_red)

mask1 = mask1 + mask2


mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
mask1 = cv2.dilate(mask1, np.ones((3,3),np.uint8))
mask2 = cv2.bitwise_not(mask1)
 
#creating an inverted mask to segment out the cloth from the frame
#mask2 = cv2.bitwise_not(mask1)
 
 
#Segmenting the cloth out of the frame using bitwise and with the inverted mask
res1 = cv2.bitwise_and(img,img,mask=mask1)

# creating image showing static background frame pixels only for the masked region
res2 = cv2.bitwise_and(img, img, mask = mask2)
 
 
#Generating the final output
final_output = cv2.addWeighted(res1,1,res2,1,0)
cv2.imshow("magic",final_output)
cv2.waitKey(0)