# Green Screen Background Replacement

This Python script replaces the green background in an image with a new background image using OpenCV.

## Prerequisites

Ensure you have Python and the required dependencies installed:

```bash
pip install opencv-python numpy
```

## How It Works

1. Loads an image with a green background (`Green_background.jpg`).
2. Loads a new background image (`Angkor_Wat.jpg`).
3. Resizes the background image to match the original image.
4. Detects and masks the green background using HSV color space.
5. Combines the subject with the new background.
6. Saves and displays the final result.

## Usage

Place your images in the same directory and run the script:

```bash
python script.py
```

## Output

The final image is saved as `combined_image.jpg` and displayed on the screen.
