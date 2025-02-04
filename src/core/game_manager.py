import pygame
from objects.brick import Brick
from objects.ball import Ball
from objects.paddle import Paddle
import config


class BrickBreakerGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.running = True
        brick_width = 60  # making bricks wider
        spacing = 10
        bricks_per_row = config.SCREEN_WIDTH // (brick_width + spacing)
        x_offset = (
            config.SCREEN_WIDTH - (bricks_per_row * (brick_width + spacing) - spacing)
        ) // 2

        self.bricks = [
            Brick(
                x * (brick_width + spacing) + x_offset,
                y * (15 + spacing) + 50,
                width=brick_width,
                height=15,
            )
            for y in range(config.BRICK_ROWS)
            for x in range(bricks_per_row)
        ]
        self.paddle = Paddle(350, 550, width=60, height=2)
        self.ball = Ball(700, 300, 5)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.ball.update()
        if self.check_collision(self.ball, self.paddle):
            self.ball.dy *= -1

    def check_collision(self, ball, paddle):
        return ball.rect.colliderect(paddle.rect)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        pygame.display.flip()
