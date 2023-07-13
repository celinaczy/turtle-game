import turtle as t
import random

screen = t.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win? Enter a color")

print(user_bet)

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]


for i in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()




