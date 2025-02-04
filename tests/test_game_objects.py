import unittest
from src.objects.ball import Ball
from src.objects.brick import Brick
from src.objects.paddle import Paddle

class TestGameObjects(unittest.TestCase):

    def setUp(self):
        self.ball = Ball(100, 100, 10)
        self.brick = Brick(50, 50, 30, 10)
        self.paddle = Paddle(200, 300, 60, 10)

    def test_ball_initialization(self):
        self.assertEqual(self.ball.x, 100)
        self.assertEqual(self.ball.y, 100)
        self.assertEqual(self.ball.radius, 10)

    def test_brick_initialization(self):
        self.assertEqual(self.brick.x, 50)
        self.assertEqual(self.brick.y, 50)
        self.assertEqual(self.brick.width, 30)
        self.assertEqual(self.brick.height, 10)

    def test_paddle_initialization(self):
        self.assertEqual(self.paddle.x, 200)
        self.assertEqual(self.paddle.y, 300)
        self.assertEqual(self.paddle.width, 60)
        self.assertEqual(self.paddle.height, 10)

if __name__ == '__main__':
    unittest.main()