import numpy as np
import cv2

# Function to calculate lower and upper HSV limits for a given color in BGR value
def get_limits(color):

    # Inserting the BGR values to convert to HSV
    c = np.uint8([[color]])

    # Convert color from BGR to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # hsvC[0][0][0] accesses the hue value of the input color

    # hsvC[0][0][0] - 10 lowers the hue value by 10 to create a range below the original hue
    # 100, 100 are fixed values for the lower limit of the saturation and value channels, respectively
    lowerLimit = hsvC[0][0][0] - 10, 100, 100

    # hsvC[0][0][0] + 10 raises the hue value by 10 to create a range above the original hue
    # 255, 255 are fixed values for the upper limit of the saturation and value channels, allowing for full saturation and brightness
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    # Convert back to numpy array
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    # Return as tuple
    return lowerLimit, upperLimit
