---
title: Chromatic Brainwaves
subtitle: Generative Art Algorithm Inspired by Brainwave Patterns
tags: [generative art, algorithm, random, color]
verified: false
---

## Chromatic Brainwaves

### Description
This algorithm generates abstract art pieces resembling brainwave patterns using random color combinations and sinusoidal functions.

### Algorithm Explanation
The algorithm works by creating a series of overlapping sinusoidal waves with random frequencies, amplitudes, and phases. Each wave is assigned a random color. The waves are then combined to create a final image. The algorithm simulates the complex and seemingly random patterns observed in brainwave activity, translating them into visually appealing chromatic compositions.

### The Full Code
```python
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
```

### How to Use
No special instructions are needed. Just run the python code.

### Expected Output
The algorithm will generate an image displaying a series of colorful, overlapping waves. The image will resemble abstract brainwave patterns with smooth color transitions.

### Conclusion
The Chromatic Brainwaves algorithm provides a unique way to visualize randomness and complexity, drawing inspiration from the natural patterns of brainwave activity. The resulting images are abstract and visually engaging, showcasing the beauty of algorithmic art.
