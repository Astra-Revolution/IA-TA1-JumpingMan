import time
import turtle

from Floor import Floor
from Gen import Gen
from JumpMan import JumpMan
from Population import Population
from Roof import Roof


class Game:
    def __init__(self, width, height):
        self.delay = 0.0000005
        self.screen = [width, height]
        self.wn = turtle.Screen()
        self.wn.title("Jump Man Game")
        self.wn.bgcolor("black")
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)
        self.roof = Roof(width, height)
        self.floor = Floor(width, height, self.roof.point)
        gen = Gen(0, 30, 20)
        # self.jump_man = JumpMan(screen=self.screen, dna=gen, point=self.floor.point)
        self.population = Population(screen=self.screen, point=self.floor.point)

    def move_game(self):
        self.wn.update()
        self.population.move_population()

    def start_game(self):
        while True:
            stop = False
            while not stop:
                self.move_game()
                if self.population.all_alive():
                    self.population.generate_children()
                    stop = True
                #time.sleep(self.delay)


