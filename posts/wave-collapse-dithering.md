---
title: Wave Collapse Dithering
subtitle: Dithering algorithm using wave collapse function.
tags: [image processing, dithering, wave collapse, random]
verified: true
---

## Small Description

This algorithm implements a dithering technique using a wave collapse function to distribute color quantization errors, creating a unique visual effect on images.

## Algorithm Explanation

The algorithm works as follows:

1.  **Input:** A 2D array representing an image (pixel values).
2.  **Initialization:** Define a set of possible pixel values (e.g., 0 and 255 for black and white).
3.  **Wave Collapse Function:** For each pixel in the image:
    *   Quantize the pixel value to the nearest value in the defined set.
    *   Calculate the quantization error (difference between the original value and the quantized value).
    *   Distribute the error to neighboring pixels using a weighted distribution (similar to Floyd-Steinberg dithering, but with random weights). The weights are determined by a "wave collapse" function that introduces randomness and spatial correlation.
4.  **Output:** A dithered image (2D array of pixel values).

## The Full Code

```python
import random

def wave_collapse_dithering(image, colors):
    width = len(image[0])
    height = len(image)
    dithered_image = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            old_pixel = image[y][x]
            new_pixel = min(colors, key=lambda color: abs(color - old_pixel))
            dithered_image[y][x] = new_pixel
            quant_error = old_pixel - new_pixel

            # Distribute the error to neighboring pixels with random weights
            # Wave collapse inspired distribution
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            valid_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < width and 0 <= ny < height]

            for nx, ny in valid_neighbors:
                weight = random.uniform(0.1, 0.3)  # Random weight for error distribution
                image[ny][nx] += quant_error * weight

    return dithered_image

# Example Usage (Illustrative)
if __name__ == '__main__':
    # Create a sample image (grayscale)
    image = [[random.randint(0, 255) for _ in range(50)] for _ in range(50)]

    # Define the color palette (black and white)
    colors = [0, 255]

    # Apply the dithering algorithm
    dithered_image = wave_collapse_dithering(image, colors)

    # Print the dithered image (for demonstration)
    for row in dithered_image:
        print("".join(["#" if pixel == 255 else " " for pixel in row]))
```

## How to Use

To use the algorithm:

1.  Provide a 2D array representing the image. Each element in the array should be a pixel value (e.g., an integer between 0 and 255 for grayscale images).
2.  Define a list of colors to which the image will be dithered (e.g., `[0, 255]` for black and white).
3.  Call the `wave_collapse_dithering` function with the image and the color palette.
4.  The function will return a new 2D array representing the dithered image.

## Expected Output

The output will be a dithered image, where the original pixel values have been approximated using the defined color palette. The dithering pattern will exhibit a "wave collapse" effect due to the random error distribution. The example code prints a text-based representation of the dithered image, where "#" represents white pixels and " " represents black pixels.

## Conclusion

The "Wave Collapse Dithering" algorithm provides a unique dithering effect by incorporating a wave collapse inspired random error distribution. This results in visually interesting patterns compared to traditional dithering methods.