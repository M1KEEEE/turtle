def build_house(base_x = -500, base_y = -500):
    """
        base_x - x левого нижнего угла дома
        base_y - y левого нижнего угла дома
    """
    print(f"Бригада построит дом в {base_x} и {base_y}")

    def build_base():
        print("Приехала бригада фундамента")


    def build_walls():
        print("Приехала бригада стен")


    def build_roof():
        print("Приехала бригада крыши")


    build_base()
    build_walls()
    build_roof()

build_house(base_x = 0, base_y = 0)