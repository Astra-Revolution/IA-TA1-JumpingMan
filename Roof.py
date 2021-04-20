import turtle


class Roof:
    def __init__(self, width, height):
        self.roofs = []
        x = width // 4
        self.point = x+20
        for _ in range(3):
            x -= 20
            y = height // 2
            for j in range(8):
                y -= 20
                roof = turtle.Turtle()
                roof.speed(0)
                roof.shape("square")
                roof.penup()
                roof.goto(x, y)
                roof.color("brown")
                roof.direction = "stop"
                self.roofs.append(roof)
