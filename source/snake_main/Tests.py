import pytest
from snake_main.Snake_Main import Snake, Food


def SnakeStart():
    snake = Snake(600, 400, 20)
    assert snake.segments == [(100, 100), (80, 100), (60, 100)]
    assert snake.OldDir == "Right"
    assert snake.NewDir == "Right"
    assert snake.width == 600
    assert snake.height == 400
    assert snake.seg_size == 20


def SnakeMove():
    snake = Snake(600, 400, 20)
    snake.move()
    assert snake.segments[0] == (120, 100)


def FoodChecker():
    food = Food(600, 400, 20)
    assert food.position != (0, 0)


def CheckFoodPos():
    food = Food(600, 400, 20)
    initial_position = food.position
    food.GiveRandomPosSnake()
    assert food.position != initial_position

if __name__ == "__main__":
    pytest.main()
