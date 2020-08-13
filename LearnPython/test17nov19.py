import os


class Color:

    def __init__(self, color):      #Constructor method
        self.color = color
        #self.name = Const.TEJA
        #self.name = "NoName"

    def find_color(self):           # Action Method
        print(os.getcwd())
        print(self.color)

    def find1(self):
        print(self.color)

    def find2(self):
        print(self.color)

    def find3(self):
        print(self.color)


def main():
    Color("red").find_color()
    Color("blue").find_color()
    Color("green").find_color()
    Color("yellow").find_color()

    c = Color("red")
    c.find_color()
    c.find1()


# Boiler Plate
if __name__ == '__main__':
    main()