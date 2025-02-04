from objects.game_object import GameObject
import config
import pygame


class Paddle(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        """Render the paddle on the screen."""

        pygame.draw.rect(
            pygame.display.get_surface(),
            (255, 255, 255),
            (self.x, self.y, self.width, self.height),
        )

    def update(self, direction):
        """Update the paddle's position based on user input."""
        if direction == "left":
            self.x -= 5  # Move left
        elif direction == "right":
            self.x += 5  # Move right

        # Ensure the paddle stays within the screen bounds
        self.x = max(0, min(self.x, config.SCREEN_WIDTH - self.width))
