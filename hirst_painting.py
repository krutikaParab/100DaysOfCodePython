# getting a rgb colors from painting or jpg
"""import colorgram
color_list = [(245, 243, 238),
              (247, 242, 244),
              (248, 245, 241),
              (202, 164, 189),
              (128, 0, 0),
              (165, 42, 42),
              (240, 128, 128),
              (233, 150, 122),
              (250, 128, 114),
              (0, 250, 154),
              (102, 205, 170),
              (139, 0, 139),
              (245, 245, 220),
              (127, 255, 212)
              ]
colour_list = []
colors = colorgram.extract('image.jpg', 30)
#print(colors)
for color in colors:
    # colour_list.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r, g, b)
    colour_list.append(rgb_tuple)
"""

# hist painting program code
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

colour_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
number_of_dots = 100

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
