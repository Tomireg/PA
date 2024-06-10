import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

class SnakeGame:
    def __init__(self):
        self.snake_speed = 15
        self.window_x = 720
        self.window_y = 480
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.fruit_position = [random.randrange(1, (self.window_x // 10)) * 10, random.randrange(1, (self.window_y // 10)) * 10]
        self.fruit_spawn = True

    def update_direction(self, change_to):
        if change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def update(self):
        if self.direction == 'UP':
            self.snake_position[1] -= 10
        if self.direction == 'DOWN':
            self.snake_position[1] += 10
        if self.direction == 'LEFT':
            self.snake_position[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_position[0] += 10

        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_position[0] == self.fruit_position[0] and self.snake_position[1] == self.fruit_position[1]:
            self.score += 10
            self.fruit_spawn = False
        else:
            self.snake_body.pop()

        if not self.fruit_spawn:
            self.fruit_position = [random.randrange(1, (self.window_x // 10)) * 10, random.randrange(1, (self.window_y // 10)) * 10]

        self.fruit_spawn = True

        if self.snake_position[0] < 0 or self.snake_position[0] > self.window_x - 10:
            return False
        if self.snake_position[1] < 0 or self.snake_position[1] > self.window_y - 10:
            return False
        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                return False
        return True

    def get_state(self):
        return {
            'snake_position': self.snake_position,
            'snake_body': self.snake_body,
            'fruit_position': self.fruit_position,
            'score': self.score
        }

game = SnakeGame()