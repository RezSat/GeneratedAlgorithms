import numpy as np
import matplotlib.pyplot as plt
import random

def generate_chromatic_brainwaves(width=512, height=512, num_waves=50):
    """
    Generates an image of chromatic brainwaves.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        num_waves (int): Number of sinusoidal waves to generate.

    Returns:
        numpy.ndarray: A numpy array representing the image.
    """
    image = np.zeros((height, width, 3))
    x = np.linspace(0, 1, width)

    for _ in range(num_waves):
        frequency = random.uniform(1, 5)
        amplitude = random.uniform(0.1, 0.5)
        phase = random.uniform(0, 2 * np.pi)
        color = (random.random(), random.random(), random.random())

        wave = amplitude * np.sin(2 * np.pi * frequency * x + phase)
        wave_scaled = ((wave + amplitude) / (2 * amplitude)) * height

        for i in range(width):
            y = int(wave_scaled[i])
            if 0 <= y < height:
                image[y, i] = color

    return image

if __name__ == "__main__":
    image = generate_chromatic_brainwaves()

    plt.imshow(image)
    plt.axis('off')
    plt.title('Chromatic Brainwaves')
    plt.show()
