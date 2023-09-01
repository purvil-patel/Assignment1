import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.snake = Snake()
        self.food = Food()
        self.game_over = False

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        while not self.game_over:
            self.update()
            self.handle_input()
            self.draw()
            self.clock.tick(10)

        pygame.quit()

    def update(self):
        self.snake.move()
        self.snake.check_collision(self.width, self.height)
        if self.snake.collides_with(self.food):
            self.snake.grow()
            self.food.generate()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.start()
