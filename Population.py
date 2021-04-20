import random
import numpy as np

from Gen import Gen
from JumpMan import JumpMan


class Population:

    def __init__(self, screen, point):
        self.screen = screen
        self.generation = 1
        self.population_size = 50
        min_x = -screen[0] // 2
        self.jumpers = [JumpMan(screen=screen,
                                dna=Gen(random.randint(min_x, 0)), point=point) for _ in range(self.population_size)]

    def move_population(self):
        for jumper in self.jumpers:
            jumper.movement()

    def mutate(self):
        rate = Gen.RATE
        for jumper in self.jumpers:
            if np.random.random() < rate:
                jumper.mutate()

    def generate_children(self):
        new_population = []
        fitness = self.get_final_fitness()
        for i in range(self.population_size // 2):
            parents = np.random.choice(self.population_size, 2, p=fitness)
            child1, child2 = self.jumpers[parents[0]].generate_child(self.jumpers[parents[1]].dna)
            new_population += [child1]
            new_population += [child2]
        for jumper in self.jumpers:
            jumper.body.clear()
            jumper.body.ht()

        del self.jumpers[:]
        self.jumpers = new_population

    def all_alive(self):
        return all(not jumper.alive for jumper in self.jumpers)

    def get_final_fitness(self):
        fitness = [jumper.get_distance_to_goal() for jumper in self.jumpers]
        fitness = np.array(fitness)
        return fitness / fitness.sum()
