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
