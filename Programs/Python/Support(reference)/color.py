import cv2
import numpy as np
import skeleton_algorithms as sa
cap = cv2.VideoCapture(1)
cent_contour=[]
while(1):
    # Take each frame
    _, frame = cap.read()
    #frame = cv2.imread('colordet.jpg')

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([161,100,100],dtype = "uint8")
    upper_green = np.array([181,255,255],dtype = "uint8")

    lower_red = np.array([10, 100, 100], dtype="uint8")
    upper_red = np.array([30, 255, 255], dtype="uint8")

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = cv2.erode(mask1, None, iterations=2)
    mask1 = cv2.dilate(mask1, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnts1 = cv2.findContours(mask1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            cent_contour.append(center)


    if len(cnts1) > 0:
        #  find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c1 = max(cnts1, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c1)
        M = cv2.moments(c1)
        center1 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(frame, center1, 5, (0, 0, 255), -1)
            cent_contour.append(center1)
    lin=sa.line_skeleton()

    for index,i in enumerate(lin):
        cv2.circle(frame,tuple(i),3,(0,0,225),3)

    for ind,val in enumerate(cent_contour):
        cv2.line(frame, tuple(lin[ind]), val, (0, 255, 0), 5)

    #res = cv2.bitwise_and(frame,frame, mask= mask)
    #res1 = cv2.bitwise_and(frame, frame, mask=mask1)
    cv2.imshow('live',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()