import pygame
import random

import config
from snake_game import SnakeGame
from utils import *
from gym import Env

class SnakeGameEnv:
    def __init__(self, args):
        self.snake_args = config.get_snake_args()

        pass
def main():
    args = config.get_args()

    snake_game = SnakeGame(args)
    pygame.init()
    pygame.display.set_caption("Snake Game")

    win = pygame.display.set_mode(snake_game.window_size)
    font = pygame.font.SysFont(None, 30)

    while(not snake_game.game_over):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                snake_game.game_over = True
            elif(event.type == pygame.KEYDOWN):
                snake_game.action(event.key)

        snake_game.update()
        snake_game.check_game_over()

        # 繪製遊戲視窗
        win.fill(WHITE)
        for pos in snake_game.snake_pos:
            pygame.draw.rect(win, GREEN, [pos[0]*snake_game.block_size, pos[1]*snake_game.block_size , snake_game.block_size, snake_game.block_size])
        pygame.draw.rect(win, BLUE, [snake_game.snake_pos[0][0]*snake_game.block_size, snake_game.snake_pos[0][1]*snake_game.block_size, snake_game.block_size, snake_game.block_size])
        pygame.draw.rect(win, RED, [snake_game.food_pos[0]*snake_game.block_size, snake_game.food_pos[1]*snake_game.block_size, snake_game.block_size, snake_game.block_size])

        score = font.render(f"Score: {snake_game.score}", True, BLACK)
        win.blit(score, [0, 0])
        pygame.display.update()
        pygame.time.Clock().tick(snake_game.snake_speed)


    # 顯示遊戲結束畫面
    text = font.render("Game Over!", True, BLACK)
    win.blit(text, [(snake_game.width*snake_game.block_size - text.get_width()) // 2, (snake_game.height*snake_game.block_size - text.get_height()) // 2])
    pygame.display.update()

    pygame.quit()
if(__name__ == "__main__"):
    main()
