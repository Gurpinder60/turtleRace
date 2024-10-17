import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "pink", "blue", "green"]
y_positions = [-70, -40, -10, 20, 50]
all_turtles = []

# Set up turtles
for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start the race if the user places a bet
if user_bet:
    is_race_on = True

# Turtle race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.write("You won!", align="center", font=("Arial", 16, "normal"))
            else:
                turtle.write(f"You lost! The {winning_color} turtle won.", align="center", font=("Arial", 16, "normal"))
            break  # Stop the race after a winner is found

        # Move the turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
