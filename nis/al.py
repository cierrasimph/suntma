import cv2
import numpy as np

# Load the main image
img = cv2.imread('main_image.jpg')

# Define the bounding boxes of the sub_imgs
sub_img_boxes = [
    (100, 100, 200, 200),  # (x1, y1, x2, y2) coordinates of the bounding box
    (300, 300, 400, 400),
    # Add more bounding boxes as needed
]

# Loop through each sub_img bounding box
for i, box in enumerate(sub_img_boxes):
    x1, y1, x2, y2 = box
    sub_img = img[y1:y2, x1:x2]  # Crop the ROI
    cv2.imwrite(f'sub_img_{i}.jpg', sub_img)  # Save the cropped image
