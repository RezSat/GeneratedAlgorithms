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
