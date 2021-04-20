class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, vector):
        new_x = self.x + vector.x
        new_y = self.y + vector.y
        return Position(new_x, new_y)
