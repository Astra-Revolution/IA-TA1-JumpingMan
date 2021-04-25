import random
import numpy as np

from Position import Position


class Gen:
    RATE = 0.005
    VX_LIMIT = 20
    VY_LIMIT = 20

    def __init__(self, x, vx=None, vy=None):
        self.x = x
        vx = vx if vx else random.randint(-Gen.VX_LIMIT, Gen.VX_LIMIT)
        vy = vy if vy else random.randint(0, Gen.VY_LIMIT)
        self.velocity = Position(vx, vy)

    def mutate(self, screen):
        index = random.randint(0, 2)
        if index == 1:
            self.velocity.x = random.randint(-Gen.VX_LIMIT, Gen.VX_LIMIT)
        else:
            self.velocity.y = random.randint(0, Gen.VY_LIMIT)

    def generate_child(self, other_gen: "Gen"):
        gen = self.get_array_of_properties()
        other = other_gen.get_array_of_properties()
        size = len(gen)
        cuter = random.randint(0, size-1)
        new_gen1 = gen[:cuter] + other[cuter:]
        new_gen2 = other[:cuter] + gen[cuter:]
        return Gen(new_gen1[0], new_gen1[1], new_gen1[2]), Gen(new_gen2[0], new_gen2[1], new_gen2[2])

    def get_array_of_properties(self):
        return [self.x, self.velocity.x, self.velocity.y]