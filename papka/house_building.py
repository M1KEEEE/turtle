import turtle as t


def build_house(base_x = -500, base_y = -500, base_width = 100, base_heigth = 10, base_fill = "#000000",  walls_x = 0, walls_y = 0, walls_width =0, walls_height = 0, walls_fill = "#000000", roof_x = 0, roof_y = 0, roof_width = 0, roof_height = 0, roof_fill = "#000000"):
    """
        base_x — X левого нижнего угла фундамента
        base_y — Y левого нижнего угла фундамента

        base_width — ширина фундамента
        base_heigth — высота фундамента
        base_fill — цвет заливки фундамента

        walls_x - считаем автоматически
        walls_y - считаем автоматически
        walls_width - спрашиваем у заказчика
        walls_height - спрашиваем у заказчика
        walls_fill - спрашиваем у заказчика

        roof_x - считаем автоматически
        roof_y - считаем автоматически
        roof_width - спрашиваем у заказчика
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
    """
    t.speed(1)


    def draw_rectangle(base_x, base_y, base_width, base_height, base_fill):
        t.penup()
        t.goto(base_x, base_y)
        t.setheading(0)
        t.pendown()
        t.fillcolor(base_fill)
        t.begin_fill()
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.end_fill()


    def build_base(base_x, base_y, base_width, base_heigth, base_fill):
        draw_rectangle(base_x, base_y, base_width, base_heigth, base_fill)


    def build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill):
        print("Приехала бригада стен")
        walls_x = 10
        walls_y = 10
        draw_rectangle(walls_x, walls_y, walls_width, walls_height, walls_fill)


    def build_roof():
        print("Приехала бригада крыши")


    build_base(base_x, base_y, base_width, base_heigth, base_fill)
    build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill)
    build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill)


build_house(base_x = 0, base_y = 0, base_width = 200, base_heigth = 10, base_fill = "#660000")
t.done()
