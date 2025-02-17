---
title: Fractal Tree Generator with Random Branching Angles
subtitle: Generates a fractal tree with random branching.
tags: [fractal, tree, recursion, random, graphics]
verified: true
---

# Fractal Tree Generator with Random Branching Angles

## Description

This algorithm generates a fractal tree structure where the branching angles and lengths are randomly determined at each level of recursion.

## Algorithm Explanation

The algorithm works as follows:

1.  Start with a trunk of a specified length.
2.  Recursively branch from the end of the trunk.
3.  At each branching point:
    *   Generate a random number of branches (e.g., 2-4).
    *   For each branch:
        *   Generate a random angle relative to the current direction.
        *   Generate a random length for the branch (usually shorter than the parent branch).
        *   Recursively call the function to create a new branch.
4.  The recursion stops when the branch length becomes smaller than a certain threshold.

## The Full Code

```python
import random
import turtle

def fractal_tree(pen, trunk_length, angle_range, length_reduction, min_length, stack):
    if trunk_length > min_length:
        # Draw the trunk
        pen.forward(trunk_length)

        # Generate a random number of branches
        num_branches = random.randint(2, 4)

        for _ in range(num_branches):
            # Generate a random angle
            angle = random.randint(-angle_range, angle_range)

            # Generate a random length
            branch_length = int(trunk_length * (length_reduction + random.uniform(-0.2, 0.2))) # Add some randomness to length reduction

            # Save the current position and heading
            stack.append((pen.position(), pen.heading()))

            pen.left(angle)

            # Recursive call
            fractal_tree(pen, branch_length, angle_range, length_reduction, min_length, stack)

            # Restore the previous position and heading
            pen.penup()
            position, heading = stack.pop()
            pen.goto(position)
            pen.setheading(heading)
            pen.pendown()


# Example usage:
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# turtle = turtle.Turtle()
# turtle.speed(0)  # Fastest speed
# turtle.left(90)  # Start facing upwards
# fractal_tree(turtle, 100, 45, 0.7, 10)
# screen.mainloop()

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    pen = turtle.Turtle()
    pen.speed(0)  # Fastest speed
    pen.hideturtle()
    pen.left(90)  # Start facing upwards
    stack = []
    fractal_tree(pen, 100, 45, 0.7, 10, stack)
    turtle.done()
```

## How to Use

To use the algorithm, you need to have the `turtle` module installed.  Create a `turtle.Screen` and a `turtle.Turtle` object.  Call the `fractal_tree` function with the turtle object, initial trunk length, angle range, length reduction factor, and minimum length.  The `screen.mainloop()` function keeps the window open until it is closed manually.

## Expected Output

The output will be a graphical representation of a fractal tree. The tree will have a random structure due to the random branching angles and lengths.

## Conclusion

This "Fractal Tree Generator with Random Branching Angles" algorithm creates visually appealing fractal trees with a unique and unpredictable structure.
