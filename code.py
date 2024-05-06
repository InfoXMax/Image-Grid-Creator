import cv2
import numpy as np
import os

# Function to resize images
def resize_image(image, target_size):
    return cv2.resize(image, target_size)

# Function to create grid of images
def create_image_grid(image_paths, grid_size, output_path):
    # Load images and resize them
    images = []
    for image_path in image_paths:
        image = cv2.imread(image_path)
        resized_image = resize_image(image, (1000, 1000))  # Adjust the size as needed
        images.append(resized_image)

    # Calculate grid dimensions
    rows, cols = grid_size
    grid_width = cols * images[0].shape[1]
    grid_height = rows * images[0].shape[0]

    # Create blank canvas
    grid = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)

    # Fill the canvas with images
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            if idx < len(images):
                y_offset = i * images[idx].shape[0]
                x_offset = j * images[idx].shape[1]
                grid[y_offset:y_offset+images[idx].shape[0], x_offset:x_offset+images[idx].shape[1]] = images[idx]

    # Save the final grid image
    cv2.imwrite(output_path, grid)

# Example usage
image_folder = "./images"
output_path = "output_grid.jpg"
image_paths = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith('.jpg')]

grid_size = (7, 8)  # Number of rows and columns in the grid
create_image_grid(image_paths, grid_size, output_path)
