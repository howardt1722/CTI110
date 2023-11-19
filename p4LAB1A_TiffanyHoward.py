# Import the turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen size and color
t.pensize(7)
t.pencolor("green")

# Draw a square
for i in range(4): # Repeat 4 times
  t.forward(100) # Move forward 100 units
  t.right(90) # Turn right 90 degrees

# Move to the next position
t.penup() # Lift the pen up
t.forward(150) # Move forward 150 units
t.pendown() # Put the pen down

# Draw a triangle
for i in range(3): # Repeat 3 times
  t.forward(100) # Move forward 100 units
  t.left(120) # Turn left 120 degrees

# Exit the turtle window
turtle.done()