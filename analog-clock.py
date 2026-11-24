import turtle
from datetime import datetime

# window setup
wn = turtle.Screen()
wn.title("Analog Clock")
wn.bgcolor("#1e1e2e")
wn.setup(width=600, height=650)
wn.mode("logo")  # 0 degrees points north (12 o'clock), rotates clockwise
wn.tracer(0)

# clock size
radius = 200

# two turtles: one for the dial (drawn once), one for the moving hands
face = turtle.Turtle()
face.hideturtle()
face.speed(0)

hands = turtle.Turtle()
hands.hideturtle()
hands.speed(0)


def draw_face():
    # outer circle
    face.penup()
    face.goto(0, -radius)
    face.setheading(90)
    face.pendown()
    face.pensize(5)
    face.color("#2b2d42", "#ffffff")
    face.begin_fill()
    face.circle(radius)
    face.end_fill()

    # tick marks (6 degrees per minute)
    for i in range(60):
        face.penup()
        face.goto(0, 0)
        face.setheading(i * 6)

        if i % 5 == 0:
            face.forward(radius - 20)
            face.pensize(3)
            face.pendown()
            face.forward(15)
        else:
            face.forward(radius - 12)
            face.pensize(1)
            face.pendown()
            face.forward(7)

    # hour numbers 1 to 12 (30 degrees each)
    face.color("#2b2d42")
    for hour in range(1, 13):
        face.penup()
        face.goto(0, 0)
        face.setheading(hour * 30)
        face.forward(radius - 40)
        face.sety(face.ycor() - 10)
        face.write(str(hour), align="center", font=("Arial", 16, "bold"))


def draw_hand(angle, length, width, color):
    hands.penup()
    hands.goto(0, 0)
    hands.setheading(angle)
    hands.color(color)
    hands.pensize(width)
    hands.pendown()
    hands.forward(length)


def update_clock():
    now = datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second

    # calculate hand angles
    s_angle = s * 6
    m_angle = (m + s / 60) * 6
    h_angle = (h + m / 60 + s / 3600) * 30

    # clear previous hands
    hands.clear()

    # draw hour, minute, and second hands
    draw_hand(h_angle, radius * 0.50, 6, "#1e1e2e")
    draw_hand(m_angle, radius * 0.72, 4, "#1e1e2e")
    draw_hand(s_angle, radius * 0.82, 2, "#e63946")

    # center pin
    hands.penup()
    hands.goto(0, 0)
    hands.dot(12, "#e63946")

    # digital time and date display
    hands.penup()
    hands.goto(0, -radius - 70)
    hands.color("white")
    time_str = now.strftime("%I:%M:%S %p")
    date_str = now.strftime("%A, %B %d, %Y")
    hands.write(f"{time_str}\n{date_str}", align="center", font=("Arial", 14, "bold"))

    wn.update()
    # repeat every second
    wn.ontimer(update_clock, 1000)


# initial draw
draw_face()
update_clock()

wn.mainloop()
