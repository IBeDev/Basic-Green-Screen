import cv2
import numpy as np

# Load the original image with the green background
original_image = cv2.imread('Green_background.jpg')

# Load the Angkor Wat image to use as the new background
background_image = cv2.imread('Angkor_Wat.jpg')

# Resize the background image to match the original image's size
background_image = cv2.resize(background_image, (original_image.shape[1], original_image.shape[0]))

# Define the green color range
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# Convert the original image to HSV color space
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# Create a mask for the green background
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Invert the mask to get the foreground
mask_inv = cv2.bitwise_not(mask)

# Use the mask to extract the foreground from the original image
foreground = cv2.bitwise_and(original_image, original_image, mask=mask_inv)

# Use the inverse mask to extract the region from the background image
background = cv2.bitwise_and(background_image, background_image, mask=mask)

# Combine the foreground and the new background
combined_image = cv2.add(foreground, background)

# Save the result
cv2.imwrite('combined_image.jpg', combined_image)

# Display the result
cv2.imshow('Final Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
