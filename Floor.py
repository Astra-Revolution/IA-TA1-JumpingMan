import turtle

from Position import Position


class Floor:
    def __init__(self, width, height, point):
        self.floors = []

        y = 20
        self.point = None
        while y <= height // 2:
            x = -width // 2
            self.base = y
            while x < width // 2:
                floor = turtle.Turtle()
                floor.speed(0)
                floor.shape("square")
                floor.penup()
                floor.goto(x, -y)
                if point == x and y == 20:
                    color = "blue"
                    self.point = floor
                else:
                    color = "brown"
                floor.color(color)
                floor.direction = "stop"
                x += 20
                self.floors.append(floor)
            y += 20
