import turtle
import random
import time

# ----- تنظیمات صفحه -----
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # برای اینکه صفحه خودکار آپدیت نشه و ما کنترلش کنیم

# ----- سر مار -----
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ----- غذا -----
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ----- بدن مار (لیست خالی، با خوردن غذا پر می‌شه) -----
body = []

# ----- نمایش امتیاز -----
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 18, "normal"))


# ----- توابع تغییر جهت -----
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# ----- حرکت سر مار -----
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


# ----- بازنشانی بازی بعد از باخت -----
def reset_game():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for part in body:
        part.goto(1000, 1000)  # بدن رو از صفحه بیرون می‌فرستیم
    body.clear()
    score = 0
    pen.clear()
    pen.write("Score: 0", align="center", font=("Arial", 18, "normal"))


# ----- کلیدها -----
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# ----- حلقه‌ی اصلی بازی -----
while True:
    screen.update()

    # برخورد با دیوار
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        reset_game()

    # خوردن غذا
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280) // 20 * 20,
                  random.randint(-280, 280) // 20 * 20)

        new_part = turtle.Turtle()
        new_part.shape("square")
        new_part.color("lightgreen")
        new_part.penup()
        body.append(new_part)

        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

    # هر تکه‌ی بدن جای تکه‌ی قبلی خودش می‌ره (از آخر به اول)
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())
    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    move()

    # برخورد با بدن خودش
    for part in body:
        if part.distance(head) < 20:
            reset_game()
            break

    time.sleep(0.1)
