import turtle as t

def draw_square(side_length = 30, x = -100, y = -100, line_color = "#FF0000", pensize = 1):
	# настройка
	t.penup()
	t.goto(x,y)
	t.pencolor(line_color)
	t.pensize(pen_size)
	t.pendown()

	# рисование
	for number in range(4)
		t.forward(side_lengt)
		t.left(90)

# общая настройка
t.shape("turtle")
t.speed(1)

# выполнение
draw_square(line_color = "#FF6600", x = 150)

# ждём выхода
t.done()