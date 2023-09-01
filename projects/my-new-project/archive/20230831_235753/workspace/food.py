import pygame
import random

class Food:
    def __init__(self):
        self.block_size = 20
        self.position = (0, 0)
        self.generate()

    def generate(self):
        x = random.randint(0, 31) * self.block_size
        y = random.randint(0, 23) * self.block_size
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], self.block_size, self.block_size))
