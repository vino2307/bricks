from pygame import Surface
import pygame
from enum import Enum

from objects.game_object import GameObject


class BrickColor(Enum):
    WEAK = (255, 200, 200)  # Light red
    NORMAL = (255, 100, 100)  # Medium red
    STRONG = (255, 0, 0)  # Strong red
    SUPER = (180, 0, 0)  # Dark red


class BrickType(Enum):
    WEAK = {
        "durability": 1,
        "base_color": BrickColor.WEAK.value,
        "points": 10,
    }  # Light red
    NORMAL = {
        "durability": 2,
        "base_color": BrickColor.NORMAL.value,
        "points": 20,
    }  # Medium red
    STRONG = {
        "durability": 3,
        "base_color": BrickColor.STRONG.value,
        "points": 30,
    }  # Strong red
    SUPER = {
        "durability": 4,
        "base_color": BrickColor.SUPER.value,
        "points": 50,
    }  # Dark red


class Brick(GameObject):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: tuple = (255, 0, 0),
        brick_type: BrickType = BrickType.NORMAL,
    ):
        super().__init__(x, y, width, height)
        self.color = color
        self.base_color = brick_type.value["base_color"]
        self.durability = brick_type.value["durability"]
        self.hits_remaining = self.durability
        self.points = brick_type.value["points"]
        self.is_broken = False

    def draw(self, surface: Surface) -> None:
        """Render the brick on the screen."""


class BrickType(Enum):
    WEAK = {
        "durability": 1,
        "base_color": BrickColor.WEAK.value,
        "points": 10,
    }  # Light red
    NORMAL = {
        "durability": 2,
        "base_color": BrickColor.NORMAL.value,
        "points": 20,
    }  # Medium red
    STRONG = {
        "durability": 3,
        "base_color": BrickColor.STRONG.value,
        "points": 30,
    }  # Strong red
    SUPER = {
        "durability": 4,
        "base_color": BrickColor.SUPER.value,
        "points": 50,
    }  # Dark red


class Brick(GameObject):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        base_color: tuple = (255, 0, 0),
        brick_type: BrickType = BrickType.NORMAL,
    ):
        super().__init__(x, y, width, height)
        self.base_color = brick_type.value["base_color"]
        self.durability = brick_type.value["durability"]
        self.hits_remaining = self.durability
        self.points = brick_type.value["points"]
        self.is_broken = False

    def draw(self, surface: Surface) -> None:
        """Render the brick on the screen."""
        if not self.is_broken:
            # Darken the color based on remaining durability
            if self.hits_remaining == 4:
                self.base_color = BrickColor.STRONG.value
            elif self.hits_remaining == 3:
                self.base_color == BrickColor.NORMAL.value
            elif self.hits_remaining == 2:
                self.base_color = BrickColor.WEAK.value
            print(self.base_color)
            pygame.draw.rect(
                surface, self.base_color, (self.x, self.y, self.width, self.height)
            )
            pygame.draw.rect(
                surface, (0, 0, 0), (self.x, self.y, self.width, self.height), 1
            )  # Outline

    def update(self) -> None:
        """Update the brick state."""
        pass  # Bricks are static, no update needed unless hit

    def handle_collision(self, ball) -> int:
        """Handle collision with ball and return points.

        Args:
            ball: The ball object that collided with the brick

        Returns:
            int: Points awarded for breaking this brick
        """
        if self.is_broken or not self.rect.colliderect(ball.rect):
            return 0  # No collision or already broken

        # Reduce durability
        else:
            self.hits_remaining -= 1
            if self.hits_remaining == 0:
                self.is_broken = True
                points = self.points
            else:
                points = 0
                # Determine which side was hit and reverse ball velocity
        if ball.rect.bottom >= self.rect.top and ball.dy < 0:
            ball.dy *= -1  # Hit from below
        elif ball.rect.top <= self.rect.bottom and ball.dy > 0:
            ball.dy *= -1  # Hit from above
        elif ball.rect.right >= self.rect.left and ball.dx > 0:
            ball.dx *= -1  # Hit from left
        elif ball.rect.left <= self.rect.right and ball.dx < 0:
            ball.dx *= -1  # Hit from right

        return points
