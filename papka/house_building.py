import turtle as t

def build_house(base_x = -500, base_y = -500, base_width = 100, base_height = 10, base_fill = "#000000"):
    """
        base_x - x левого нижнего угла дома
        base_y - y левого нижнего угла дома

        base_width - ширина фундамента
        base_height - высота фундамента
        base_fill
    """
    t.speed(1)

    def draw_rectandle(width = 0, height = 0, fill = "#000000"):
        t.fillcolor(fill)
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

    def build_base():
        print(f"Приехала бригада фундамента и копает котлован в {base_x} и {base_y}")
        t.penup()
        t.goto(base_x, base_y)
        t.setheading(0)
        t.pendown()

        #рисование
        draw_rectandle(base_width, base_height, base_fill)

    def build_walls():
        print("Приехала бригада стен")


    def build_roof():
        print("Приехала бригада крыши")


    build_base()
    build_walls()
    build_roof()


build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#660000")
t.done()
