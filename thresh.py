import cv2
import time 

cam = cv2.VideoCapture('test.mp4')
cam.set(3,640)
cam.set(4,480)
video_capture = cam
frame_num = 0
scene_num = 0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    time.sleep(0.01)
    print ret
    if ret:
        frame_num = frame_num+1
        print frame_num
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if frame_num == 1:
            firstFrame = gray
            if frame_num == 10:
            	frame_num= 0
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            frameDelta = cv2.absdiff(firstFrame, gray)
            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            for c in cnts:
            # if the contour is too small, ignore it
                if cv2.contourArea(c) < 10:
                    continue
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Display the resulting frame
		# cv2.imshow('Video', thresh)
		# cv2.imshow('Video', frameDelta)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
		# print frame_num
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
