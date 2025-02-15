# Wisconsin Autonomous Perception Coding Challenge
***
### Table of Contents:
1. [Answer](#answer)
2. [Installation Guide](#installation-guide)
3. [Methodology](#methodology)
   1. [What I tried](#what-i-tried)
   2. [What didn't work](#what-didnt-work)
4. [Libraries used](#libraries-used)
<hr style="border: 2px solid grey;">

## Answer
___

![answer.png](answer.png)

<hr style="border: 2px solid grey;">

## Installation Guide:
***
1. Clone the repository and navigate to the repository:
```bash
git clone https://github.com/potatoskewers/wisconsin-autonomous-coding-challenge.git
cd ../wisconsin-autonomous-coding-challenge
```
2. Install the Requirements in terminal:
```bash  
pip install -r requirements.txt
```
3. Make sure you have Python 3.10 installed on your system. You can check your Python version with:
```bash
python --version
```
4. Run the script. the script will output the image with the guidelines drawn between the cones 
5. Press any button to close the image.
<hr style="border: 2px solid grey;">

## Methodology:
***
To implement the specification, I used the following steps:
1. I implemented a mask that would filter out the pixels that were not red.
2. Then, I used the mask to create contour edges around the red pixels.
3. I drew rectangles that encapsulate the contour edges.
4. If half of the long side of the rectangle is greater than 10 pixels, 
then save the middle of the rectangle as a coordinate.
5. Create two lists of coordinates, one for the left side of the rectangle and one for the right side of the rectangle.
6. For each list, perform linear regression on the image to find a best fit line for the coordinates
7. Draw a best fit line on the image between the first point and the last image.
8. Print results to the console.
## What I tried:
***
- I tried to use the cv2.threshold() function to filter out the red pixels, but it seemed to not be as accurate as using the cv2.inRange() function.
- I used two layers to capture the darker red colors and the lighter red colors of the cone
- I drew rectangles around the contours to encapsulate the midpoint of the rectangle.
- To draw the boundary guidelines, I used linear regression to find the best fit line for the coordinates.


## What didn't work:
- Originally, I tried to use thresholding to filter out the red pixels, but when drawing contours later it seemed to be less accurate.
  - When adding a threshold to the pixels, it seemed to also pick up pixel color values on the wall and from other lights in the background
- I tried to use just one layer for the red pixel mask, but it seemed to not be able to filter out the red pixels as well as using all two layers.
- I also tried to use the cv2.HoughLines() function to find the best fit line for the coordinates, but I couldn't get it to detect a line between the cones.
- For obtaining the coordinates of each of the cones, I also tried drawing circles around the contours, but it seemed to be less accurate and more volatile than drawing rectangles.

<hr style="border: 2px solid grey;">

## Libraries used:
***
```python
numpy==2.2.2
opencv-python==4.11.0.86
scipy==1.15.1
```
