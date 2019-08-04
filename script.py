import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#here we have imported the cascadeclassifier for recognisation
imp_img = cv2.VideoCapture("elon.jpg")#here we have done the image importing

res, img = imp_img.read()#here we are reading the image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#here the classifier is trained for black and grey only we are converting to grey

faces = detect.detectMultiScale(gray, 1.3, 5)#(color,scalefactor,minNeighbor)and her e are giving the imgae name,scalefactor,and minNegihbor

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w , y+h), (255,256,0), 2)#here we are giving the cordinates fro the image


cv2.imshow("elon", img)#here we are showing the image

cv2.waitKey(0)#this the time for the closing of opened window
imp_img.release()#this key is for release the windows
cv2.destroyAllWindows()# this is for destroying all the windows