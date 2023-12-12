import cv2
from image_preprocessing import *


#read image
capture = cv2.VideoCapture("test_video/Fast Driving Car On Straight Road.mp4")
while True:
    ret, frame = capture.read()
    if not ret:
        break
    canny_img = canny(frame)
    masked_img = region_of_interest(canny_img)
    lines = houghLines(masked_img)
    average_lines = average_slope_intercept(frame, lines)
    line_image = display_lines_average(frame, average_lines)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == 27: #esc key
        break

cv2.destroyAllWindows()