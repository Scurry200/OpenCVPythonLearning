import cv2
import numpy as np
print("package imported")
#reads image
# img = cv2.imread("Resources/shapes.png")
# #displays image
# cv2.imshow("Output", img)
# #infinite delay so image appears until you close it and doesn't close out on its own
# cv2.waitKey(0)



# #collects video
# cap = cv2.VideoCapture("Resources/video.mp4")
# #video is a bunch of images, so while loop is made to process image by image
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     #adds delay and to break loop, press q
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#uses webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# #changes brightness for clarity
# cap.set(10,100)
# while True:
#       success, img = cap.read()
#       cv2.imshow("video", img)
#       #adds delay and to break loop, press q
#       if cv2.waitKey(1) & 0xFF ==ord('q'):
#          break





#chapter 1
# img = cv2.imread("Resources/shapes.png")
# #converts image to grayscale
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# #blurs image with gaussian blur
# #ksize is amount of blur, has to be odd numbers only
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#
# cv2.imshow("Gray image", imgGray)
# cv2.imshow("blur image", imgBlur)
# cv2.waitKey(0)
# img = cv2.imread("Resources/shapes.png")
# # #creates kernel matrix, np.uint8 is for color pixel between 0 and 255
# # kernel = np.ones((5,5), np.uint8)
# # #detect edges
# # # canny(image name, threshold size(10 x 10 in next line), the lower the threshold, the more sensitive it is(detectsmore lines and edges)
# # imgCanny = cv2.Canny(img,15,15)
# # #increase thiccness of edges, iterations gives command for how thick the lines should be, greater iteration value means greater thiccness
# # imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# #
# # #makes lines thinner
# # imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
# # cv2.imshow("Canny image", imgCanny)
# # cv2.imshow("dilation image", imgDilation)
# # cv2.imshow("eroded image", imgEroded)
# # cv2.waitKey(0)

#
#
# img = cv2.imread("Resources/shapes.png")
# # #prints dimensions of image(height, width, number of channels(bgr)
# # print(img.shape)
# # #dimensions to resize have to be in this order: (width, height), can increase width and height as well
# # imgResize = cv2.resize(img, (300, 200))
# # cv2.imshow("image", img)
# # cv2.imshow("image resize", imgResize)
#
#
# #image cropping(make an img matrix, with dimensions(heightStartingPoint:HeightEndingPoint, widthStartingPoint:widthEndingPoint)
# imgCropped = img[0:200,200:500]
# cv2.imshow("image cropping", imgCropped)
# cv2.waitKey(0)





# 0 in color means black
#(512,512) is matrix size and 3 represents the number of channels(RGB)
# img = np.zeros((512,512,3),np.uint8)
# print(img)
# array with dimensions of where full blue is(200-300 heightm 100-300 width
# img[200:300, 100:300]= 255,0,0

#creates line between pixel in coordinates 0,0, and coordinates 300, 300 with line color green(0,255, 0) with thiccness 3
# cv2.line(img, (0,0), (300, 300), (0,255, 0), 3)
# img.shape[] is an option but not sure what it does

# .rectangle(image, starting point, ending diagonal point, color, thiccness)
# cv2.FILLED fills the rectangle with the color in the color parameter
# cv2.rectangle(img,(0,0), (250,350),(0,0,255), 2, cv2.FILLED)

# cv2.circle(image, center, radius, color, thiccness)
# cv2.circle(img, (400,50),30, (255,255, 0),5)

# .putText(image, text, starting point of where text starts in pixels, font, font size, color, thiccness)
# cv2.putText(img, "this is where we put text", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150, 0), 1)
# cv2.imshow("image", img)
# cv2.waitKey(0)






#warp perspective, figure out what this is(basically better cropping)

# img = cv2.imread("Resources/AcetoFive.jpg")
# cv2.imshow("image", img)
#
# width,height = 250,350
# # creating a list of 4 arrays in an array with pixel coordinates
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix,(width, height))
# cv2.waitKey(0)
















#
# img = cv2.imread("Resources/shapes.png")
#
# #helps stack an image multiple times and resizes as well
# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
#
# # stackimages(scale, matrices of images(each row has its own matrix))
# # stackimages() can also have grayscale images as well
# imgStack = stackImages(.25, ([img,img,img, img], [img, img, img,img]) )
#
#
#
# cv2.imshow("stack images", imgStack)
#
#
#
# #combining images horizontally
# # imgHor = np.hstack((img, img))
# # cv2.imshow("horizontal", imgHor)
# #
# # #combining images vertically
# # imgVer = np.vstack((img,img))
# # cv2.imshow("vert", imgVer)
#
# #when using these commands, pictures have to be in RGB format, and the image sizes are as is
# cv2.waitKey(0)






# def empty(a):
#     pass
# path = "Resources/download.jpg"
#
#
# #trackbar lets us move a button left to right to show range of hues(0-179)
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640,240)
# cv2.createTrackbar("Hue minimum", "TrackBars", 0,179, empty)
# cv2.createTrackbar("Hue maximum", "TrackBars", 179,179, empty)
# cv2.createTrackbar("saturation minimum", "TrackBars", 0,255, empty)
# cv2.createTrackbar("saturation maximum", "TrackBars", 59,255, empty)
# cv2.createTrackbar("value minimum", "TrackBars", 195,255, empty)
# cv2.createTrackbar("value maximum", "TrackBars", 247,255, empty)
#
#
#
# #tracking live data of hue with while loop
# while True:
#         img = cv2.imread(path)
#         imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         hue_min = cv2.getTrackbarPos("Hue minimum", "TrackBars")
#         hue_max = cv2.getTrackbarPos("Hue maximum", "TrackBars")
#         sat_min = cv2.getTrackbarPos("saturation minimum", "TrackBars")
#         sat_max = cv2.getTrackbarPos("saturation maximum", "TrackBars")
#         val_min = cv2.getTrackbarPos("value minimum", "TrackBars")
#         val_max = cv2.getTrackbarPos("value maximum", "TrackBars")
#         print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
#         lower = np.array([hue_min, sat_min,val_min])
#         upper = np.array([hue_max,sat_max,val_max])
#         #provides filtered out image based on live trackbar data
#         mask = cv2.inRange(imgHSV, lower, upper)
#         #only allowing for certain colors to show
#         imgResult = cv2.bitwise_and(img, img, mask=mask)
#
#
#         cv2.imshow("original", img)
#         cv2.imshow("hsv", imgHSV)
#
#     #use mask image to test out trackbars and find optimal minimum and maximum hue, sat, and val values and replace the original min and max values with these values found
#         cv2.imshow("masked image", mask)
#
#         cv2.imshow("masked image with some color", imgResult)
#         cv2.waitKey(1)

#
# def stackImages(scale, imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
#                                                 None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank] * rows
#         hor_con = [imageBlank] * rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver
#
#
# def getContours(img):
#     contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area > 500:
#             cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt, True)
#             # print(peri)
#             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
#             print(len(approx))
#             objCor = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)
#
#             if objCor == 3:
#                 objectType = "Tri"
#             elif objCor == 4:
#                 aspRatio = w / float(h)
#                 if aspRatio > 0.98 and aspRatio < 1.03:
#                     objectType = "Square"
#                 else:
#                     objectType = "Rectangle"
#             elif objCor > 4:
#                 objectType = "Circles"
#             else:
#                 objectType = "None"
#
#             cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(imgContour, objectType,
#                         (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
#                         (0, 0, 0), 2)
#
#
# path = 'Resources/shapess.png'
# img = cv2.imread(path)
# imgContour = img.copy()
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# imgCanny = cv2.Canny(imgBlur, 50, 50)
# getContours(imgCanny)
#
# imgBlank = np.zeros_like(img)
# imgStack = stackImages(0.8, ([img, imgGray, imgBlur],
#                              [imgCanny, imgContour, imgBlank]))
#
# cv2.imshow("Stack", imgStack)
# cv2.waitKey(0)
#




#
# # face detection
# faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# img = cv2.imread("Resources/face.jpg")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1,4)
#
# #create boundary box
# for (x,y,w,h) in faces:
#     cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0), 2)
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)




