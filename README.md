```markdown
# Image Grid Creator

This Python script allows you to create a grid of images by combining multiple images into a single grid layout. It's useful for creating collages or displaying multiple images in a single view.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)

You can install the required libraries using pip:

```bash
pip install opencv-python numpy
```

## Usage

1. Place your images in a folder named `images` in the same directory as the script.
2. Update the `image_folder` variable in the script to point to the directory where your images are stored.
3. Adjust the `grid_size` variable according to the number of rows and columns you want in your grid.
4. Run the script using Python:

```bash
python code.py
```

This will generate a grid image named `output_grid.jpg` in the same directory.

## Customization

You can customize the script according to your needs:

- Adjust the target size of the images by modifying the `resize_image` function.
- Change the output file name by updating the `output_path` variable.
- Experiment with different grid sizes by modifying the `grid_size` variable.

## Example

For example, to create a grid with 7 rows and 8 columns:

```python
grid_size = (7, 8)  # Number of rows and columns in the grid
```
