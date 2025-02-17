from abc import ABC, abstractmethod
import pygame


class GameObject(ABC):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._rect = pygame.Rect(x, y, width, height)

    @property
    def rect(self):
        self._rect.x = self.x
        self._rect.y = self.y
        return self._rect

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self):
        pass

        # @abstractmethod
        # def points(self):
        #     pass

        # def on_collision(self, other):
        #     pass

        # def after_collision(self, other):
        # pass
