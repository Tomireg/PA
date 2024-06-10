import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import random

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

        pygame.init()
        pygame.display.set_caption('Classic Snake')
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        self.fps = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        self.change_to = 'RIGHT'
            if self.change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'
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
            self.game_window.fill(self.black)

            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.game_window, self.white, pygame.Rect(self.fruit_position[0], self.fruit_position[1], 10, 10))

            if self.snake_position[0] < 0 or self.snake_position[0] > self.window_x - 10:
                self.game_over()
            if self.snake_position[1] < 0 or self.snake_position[1] > self.window_y - 10:
                self.game_over()
            for block in self.snake_body[1:]:
                if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                    self.game_over()
            self.show_score(1, self.white, 'times new roman', 20)
            pygame.display.update()
            self.fps.tick(self.snake_speed)

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(self.score), True, self.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.window_x / 2, self.window_y / 4)
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

if __name__ == '__main__':
    SnakeGame().run()