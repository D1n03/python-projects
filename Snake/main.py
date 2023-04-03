from platform import python_branch
import pygame
import sys
from snake import Snake
from food import Food

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock() 

#DONT FORGET ABOUT THE SPEED 
score = 0
speed = 12

snake = Snake()
food = Food()

while (True):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDir("R")
            if event.key == pygame.K_LEFT:
                snake.changeDir("L")
            if event.key == pygame.K_UP:
                snake.changeDir("U")
            if event.key == pygame.K_DOWN:
                snake.changeDir("D")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    foodPos = food.generate()

    if snake.move(foodPos):
        score += 100
        food.setFoodEaten(True)
        if speed < 20:
            speed += 0.5

    window.fill(pygame.Color(0, 0, 0))

    for position in snake.body:
        pygame.draw.rect(window, pygame.Color(0,128,0), pygame.Rect(position[0], position[1], 10, 10))

    pygame.draw.rect(window, pygame.Color(255, 0, 0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snake.CheckisDead():
        pygame.quit()
        sys.exit()

    pygame.display.set_caption("Snake | Score:" + str(score))
    pygame.display.flip()
    fps.tick(speed)