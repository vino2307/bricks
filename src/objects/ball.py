from objects.game_object import GameObject
import pygame
import config


class Ball(GameObject):
    def __init__(self, x, y, radius):
        # Center the rect around ball position
        super().__init__(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.dx = 5  # Change in x (horizontal speed)
        self.dy = -5  # Change in y (vertical speed)

    def draw(self, screen):
        """Render the ball on the screen."""
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (self.x + self.radius, self.y + self.radius),
            self.radius,
        )

    def update(self):
        """Update the ball's position."""
        # check direction of the ball and update the position

        self.x += self.dx
        self.y += self.dy

        # Collision detection with walls
        if self.x <= 0 or self.x + self.width >= config.SCREEN_WIDTH:
            self.dx *= -1  # Reverse direction on x-axis
        if self.y <= 0 or self.y + self.height >= config.SCREEN_HEIGHT:
            self.dy *= -1  # Reverse direction on y-axis
