from random import randrange
from collections import deque
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN

class SnakeGame:
    def __init__(self, args):
        self.width = args.width
        self.height = args.height
        self.block_size = args.block_size
        self.snake_length = args.snake_length
        self.snake_speed = args.snake_speed
        self.window_size = (self.width * self.block_size, self.height * self.block_size)

        self.snake_pos = deque([[args.width // 2 + i, args.height // 2] for i in range(args.snake_length)])

        self.speed_x = 0
        self.speed_y = 0

        self.generate_food()
        
        self.game_over = False
    
    def action(self, direction):
        if direction == K_LEFT and self.speed_x == 0:
            self.speed_x = -self.block_size
            self.speed_y = 0
        elif direction == K_RIGHT and self.speed_x == 0:
            self.speed_x = self.block_size
            self.speed_y = 0
        elif direction == K_UP and self.speed_y == 0:
            self.speed_x = 0
            self.speed_y = -self.block_size
        elif direction == K_DOWN and self.speed_y == 0:
            self.speed_x = 0
            self.speed_y = self.block_size
    
    def update(self):
        self.snake_pos.appendleft([self.snake_pos[0][0] + self.speed_x, self.snake_pos[0][1] + self.speed_y])
        if(not self.get_food()):
            self.snake_pos.pop()
    
    def generate_food(self):
        self.food_pos = self.snake_pos[0]
        while(self.food_pos in self.snake_pos):
            self.food_pos = [randrange(1, (self.width)),
                             randrange(1, (self.height))]
    
    def check_game_over(self):
        if(self.snake_pos[0][0] < 0 or self.snake_pos[0][0] >= self.width or
           self.snake_pos[0][1] < 0 or self.snake_pos[0][1] >= self.height or
           self.snake_pos.count(self.snake_pos[0])>1):
            self.game_over = True
    def get_food(self):
        if(self.snake_pos[0] == self.food_pos):
            self.generate_food()
            return True
        else:
            return False