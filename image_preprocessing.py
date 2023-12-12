import cv2
import numpy as np
"""define functions for image preprocessing"""


#canny edge detection
def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray, (kernel,kernel), 0) #standard eviation set to 0
    canny = cv2.Canny(blur, 50, 150) #50,150 are default thresholding values
    return canny

#get coordinates
# def RGB(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         colorsBGR = [x, y]
#         print(colorsBGR)
# cv2.namedWindow('RGB')
# cv2.setMouseCallback('RGB', RGB)


def region_of_interest(img):
    height = img.shape[0]
    width = img.shape[1]
    mask = np.zeros_like(img)
    triangle = np.array([[(775, 396),(175,715), (1268,719)]], np.int32)
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def houghLines(img):
    houghLines = cv2.HoughLinesP(img, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    return houghLines


def make_point(img, lineSI):
    slope,intercept = lineSI
    height = img.shape[0]
    y1 = int(height)
    y2 = int(y1 * 3.0/5) #assuming y2 is 3/5 of image
    x1 = int((y1-intercept)/slope)
    x2 = int((y2-intercept)/slope)
    return [[x1,y1,x2,y2]]


def average_slope_intercept(img, lines):
  left_fit = []
  right_fit = []
  for line in lines:
    for x1, y1,x2,y2 in line:
      fit = np.polyfit((x1,x2), (y1,y2),1) # poly degree of 1 for lines
      slope = fit[0]
      intercept = fit[1]
      if slope < 0 :
        left_fit.append((slope, intercept))
      else:
        right_fit.append((slope, intercept))
  left_fit_average = np.average(left_fit, axis = 0)
  right_fit_average = np.average(right_fit, axis = 0)
  left_line = make_point(img, left_fit_average)
  right_line = make_point(img, right_fit_average)
  return np.array([left_line, right_line])



def display_lines_average(img, lines):
  line_image = np.zeros_like(img)
  if lines is not None:
    for line in lines:
      for x1,y1,x2,y2 in line:
        cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 10)
  return img