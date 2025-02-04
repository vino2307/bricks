from pygame import Surface
from objects.game_object import GameObject


class Brick(GameObject):
    def __init__(
        self, x: int, y: int, width: int, height: int, color: tuple = (255, 0, 0)
    ):
        super().__init__(x, y, width, height)
        self.color = color
        self.is_broken = False

    def draw(self, surface: Surface) -> None:
        """Render the brick on the screen.

        Args:
            surface: The pygame surface to draw on
        """
        if not self.is_broken:
            import pygame

            pygame.draw.rect(
                surface, self.color, (self.x, self.y, self.width, self.height)
            )

    def update(self) -> None:
        """Update the brick state."""
        pass  # Bricks are static, no update needed unless hit

    def handle_collision(self) -> None:
        """Handle collision with other game objects."""
        self.is_broken = True
