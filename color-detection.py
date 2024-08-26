import cv2
from PIL import Image
from util import get_limits

# Select webcam
# cap is a video capture object
cap = cv2.VideoCapture(0)

# Yellow color in BGR color space
yellow = [0, 255, 255]

while True:
    # ret (boolean) returns true if frame successfully read and returns false if there is an error
    # frame is an image captured by webcam, it is represented as a numpy array 
    ret, frame = cap.read()

    # Convert color space of image from BGR to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Getting the lower and upper limit of the color with the get_limits function
    lowerLimit, upperLimit = get_limits(color=yellow)

    # lower_bound and upper_bound is used to define range of colors in HSV space to detect
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Converts the mask (numpy array) into a PIL object
    mask_ = Image.fromarray(mask)

    # Find the bounding box 
    # It returns tuple of four values left, upper, right, lower
    bbox = mask_.getbbox()

    # Drawing the bounding box
    if bbox is not None:
        # Coordinates of bounding box
        x1, y1, x2, y2 = bbox

        # Draws a rectangle on the frame
        # x1 and y1 top left corner
        # x2 and y2 bottom right corner
        # (0, 255, 0) is green color so the rectangle drawin is green
        # 5 is the thickness of the rectangle's border
        frame = cv2.rectangle(frame, (x1, y1) , (x2, y2), (0, 255, 0), 5)

    # Visualize the frame
    cv2.imshow('frame', frame)

    # if user presses q it quits the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object
cap.release()

# Close all OpenCV windows that were opened
cv2.destroyAllWindows()
