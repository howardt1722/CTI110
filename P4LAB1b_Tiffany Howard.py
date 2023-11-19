# Import the turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen size and color
t.pensize(5)
t.pencolor("purple")

# Draw a letter t
t.left(90) # Turn left 90 degrees
t.forward(100) # Move forward 100 units
t.backward(50) # Move backward 50 units
t.right(90) # Turn right 90 degrees
t.forward(50) # Move forward 50 units

# Move to the next position
t.penup() # Lift the pen up
t.forward(20) # Move forward 20 units
t.pendown() # Put the pen down

# Draw a letter h
t.left(90) # Turn left 90 degrees
t.forward(100) # Move forward 100 units
t.backward(50) # Move backward 50 units
t.right(90) # Turn right 90 degrees
t.forward(50) # Move forward 50 units
t.left(90) # Turn left 90 degrees
t.forward(50) # Move forward 50 units
t.backward(100) # Move backward 100 units

# Exit the turtle window
turtle.done()