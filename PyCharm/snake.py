import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameScreen = pygame.display.set_mode((display_width,display_height))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)


clock = pygame.time.Clock()

pygame.display.set_caption("YILAN");

def message_to_screen(message,type):
    font = pygame.font.SysFont(None,25)
    screen_text = font.render(message,True,type)
    gameScreen.blit(screen_text,[display_width/4,display_height/2])
    pygame.display.update()

def snake(size_of_block,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameScreen,green,[XnY[0],XnY[1],size_of_block,size_of_block])


def gameLoop():
    FPS = 10  # frame per second
    size_of_block = 10
    lead_x = display_width / 2
    lead_y = display_height / 2

    direction_x = 0
    direction_y = 0


    snakeList = []
    snakeLenght = 1
    randAppleX = round(random.randrange(0,display_width - size_of_block)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - size_of_block)/10.0)*10.0

    gameClose = False
    gameOver = False
    while not gameClose:
        while gameOver == True:
            gameScreen.fill(white)
            message_to_screen("Kaybettin! Yeniden başlamak için boşluk tuşuna basınız!\nÇıkmak için -> Q",red)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            print(event)
            lead_x_change = 0
            lead_y_change = 0
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change -= size_of_block
                    direction_x = -10
                    direction_y = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change += size_of_block
                    direction_x = 10
                    direction_y = 0
                if event.key == pygame.K_UP:
                    lead_y_change -= size_of_block
                    direction_x = 0
                    direction_y = -10
                elif event.key == pygame.K_DOWN:
                    lead_y_change += size_of_block
                    direction_x = 0
                    direction_y = 10
            lead_x += lead_x_change
            lead_y += lead_y_change
            if lead_x >= display_width or lead_x < size_of_block or lead_y >= display_height or lead_y < 0:
                gameOver = True
        gameScreen.fill(white)
        pygame.draw.rect(gameScreen, red, (randAppleX, randAppleY, size_of_block, size_of_block))

        lead_x += direction_x
        lead_y += direction_y


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLenght:
            del snakeList[0]

        snake(size_of_block,snakeList)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - size_of_block) / 10.0) * 10.0
            snakeLenght += 1
        clock.tick(FPS)
        print(clock)

    pygame.quit()

gameLoop()


