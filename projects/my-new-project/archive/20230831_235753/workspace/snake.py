import pygame

class Snake:
    def __init__(self):
        self.size = 1
        self.block_size = 20
        self.speed = self.block_size
        self.direction = "RIGHT"
        self.body = [(self.block_size, self.block_size)]

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= self.speed
        elif self.direction == "DOWN":
            y += self.speed
        elif self.direction == "LEFT":
            x -= self.speed
        elif self.direction == "RIGHT":
            x += self.speed
        self.body.insert(0, (x, y))
        if len(self.body) > self.size:
            self.body.pop()

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def grow(self):
        self.size += 1

    def check_collision(self, width, height):
        x, y = self.body[0]
        if x < 0 or x >= width or y < 0 or y >= height:
            pygame.quit()
            raise Exception("Game Over: Collision with walls")
        if self.body[0] in self.body[1:]:
            pygame.quit()
            raise Exception("Game Over: Collision with itself")

    def collides_with(self, other):
        return self.body[0] == other.position

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, self.block_size, self.block_size))

