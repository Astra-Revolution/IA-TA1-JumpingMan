import turtle

from Gen import Gen
from Position import Position


class JumpMan:
    def __init__(self, screen, dna: Gen, point):

        self.is_jumping = False
        self.ready = False
        self.dna = dna
        self.screen = screen
        self.goal = point
        self.alive = True
        self.position = Position(self.dna.x, 0)
        self.velocity = Position(20, 0)

        self.body = turtle.Turtle()
        self.body.speed(0)
        self.body.shape("circle")
        self.body.penup()
        self.body.goto(self.position.x, self.position.y)
        self.body.color("white")
        self.body.direction = "stop"

    def mutate(self):
        self.dna.mutate(self.screen)

    def generate_child(self, other: Gen):
        new_dna1, new_dna2 = self.dna.generate_child(other)
        # new_dna1.mutate(self.screen)
        # new_dna2.mutate(self.screen)
        return JumpMan(self.screen, new_dna1, point=self.goal), JumpMan(self.screen, new_dna2, point=self.goal)

    def movement(self):
        if not self.ready and self.alive:
            if self.validate_intersect() and not self.is_jumping:
                self.ready = True
            else:
                self.draw()
                self.move()

    def validate_intersect(self):
        return self.body.distance(self.goal) < 20

    def draw(self):
        self.body.goto(self.position.x, self.position.y)

    def move(self):
        if self.position.x >= self.dna.x and not self.is_jumping:
            self.is_jumping = True
            self.velocity = self.dna.velocity
        self.update_position()

    def update_position(self):
        self.velocity = self.velocity.add(Position(0, -1))
        self.position.x += self.velocity.x
        if not self.validate_intersect():
            self.position.y += self.velocity.y
        self.validate_limits()

    def validate_limits(self):
        x = self.body.xcor()
        y = self.body.ycor()
        limit_x = self.screen[0] // 2 - 20
        limit_y = self.screen[1] // 2 - 20
        if -limit_x < x < limit_x and self.goal.ycor() < y < limit_y:
            self.alive = True
        else:
            self.alive = False

    def get_distance_to_goal(self):
        return self.body.distance(self.goal)
