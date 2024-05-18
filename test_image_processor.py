import os
from image_processing_dev import crop_image, convert_to_black_and_white, apply_sepia_filter

# Define paths for input and output images
input_image_path = 'sample_image.jpg'
cropped_image_path = 'cropped_image.jpg'
bw_image_path = 'bw_image.jpg'
sepia_image_path = 'sepia_image.jpg'

# Define crop area (left, upper, right, lower)
crop_area = (100, 100, 300, 300)

# Test crop_image function
crop_image(input_image_path, cropped_image_path, crop_area)
print(f"Cropped image saved to {cropped_image_path}")

# Test convert_to_black_and_white function
convert_to_black_and_white(input_image_path, bw_image_path)
print(f"Black and white image saved to {bw_image_path}")

# Test apply_sepia_filter function
apply_sepia_filter(input_image_path, sepia_image_path)
print(f"Sepia image saved to {sepia_image_path}")

# Check if the output files exist to verify that the functions worked
if os.path.exists(cropped_image_path):
    print("Crop function test passed.")
else:
    print("Crop function test failed.")

if os.path.exists(bw_image_path):
    print("Black and white conversion test passed.")
else:
    print("Black and white conversion test failed.")

if os.path.exists(sepia_image_path):
    print("Sepia filter application test passed.")
else:
    print("Sepia filter application test failed.")
