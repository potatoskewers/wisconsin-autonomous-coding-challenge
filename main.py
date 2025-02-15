import cv2
import numpy as np
from scipy.stats import linregress

# Load the image
image = cv2.imread('../wisconsin-autonomous-coding-challenge/red.png')
answer = image.copy()
bounding_boxes = []
left_side_coordinates = []
right_side_coordinates = []

def mask_red():
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define the lower and upper bounds for red in Hue Saturation and Value
    #define the higher and lower bounds to capture brighter red colors
    lower_red1 = np.array([0, 170, 180])
    upper_red1 = np.array([10, 255, 255])

    #define the higher and lower bounds to capture darker red colors
    lower_red2 = np.array([170, 150, 150])
    upper_red2 = np.array([180, 255, 255])

    red_mask_1 = cv2.inRange(hsv, lower_red1, upper_red1) # Create a mask for the two red areas
    red_mask_2 = cv2.inRange(hsv, lower_red2, upper_red2)

    #Combine the two masks
    mask = cv2.bitwise_or(red_mask_1, red_mask_2)
    return mask
def generate_contours(mask):
    # Draw bounding rectangles around the red areas
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Save the red areas with significant size
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        bounding_boxes.append((x, y, w, h))
        center_x = x + w // 2
        center_y = y + h // 2
        radius = max(w, h) // 2
        if radius > 10:
            if center_x < image.shape[1] // 2:
                left_side_coordinates.append((center_x, center_y))
            else:
                right_side_coordinates.append((center_x, center_y))
def draw_lines():
    # Draw the red guidelines
    zipped_left_x, zipped_left_y = zip(*left_side_coordinates)
    zipped_right_x, zipped_right_y, = zip(*right_side_coordinates)
    #perform linear regression on the left and right side cone coordinates
    left_slope, left_intercept, left_r_value, left_p_value, left_std_err = linregress(zipped_left_x, zipped_left_y)
    right_slope, right_intercept, right_r_value, right_p_value, right_std_err = linregress(zipped_right_x, zipped_right_y)
    #draw the red guidelines on the image starting from first cone to last cone
    cv2.line(answer, (left_side_coordinates[0][0], int(left_side_coordinates[0][0]*left_slope + left_intercept)), (left_side_coordinates[-1][0], int(left_side_coordinates[-1][0] * left_slope + left_intercept)), (0, 0, 255), 4)
    cv2.line(answer, (right_side_coordinates[0][0], int(right_side_coordinates[0][0] * right_slope + right_intercept)), (right_side_coordinates[-1][0], int(right_side_coordinates[-1][0] * right_slope + right_intercept)), (0, 0, 255), 4)

#driver code
if __name__ == "__main__":
    # Check if the image was loaded successfully
    if image is None:
        print("Failed to load image.")
    else:
        generate_contours(mask_red())
        draw_lines()
        # Display the result
        cv2.imshow('Red Guidelines', answer)
        cv2.imwrite('../wisconsin-autonomous-coding-challenge/answer.png', answer)

        # press any key to close the image and stop the program
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Program has ended.")