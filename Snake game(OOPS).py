import pygame
import time
import random
pygame.init()
width=800
heigth=600
dis=pygame.display.set_mode((width,heigth))

pygame.display.set_caption('snake game')
game_over=False

red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
yellow=(255,255,102)
green=(0,255,0)
x1_change=0
y1_change=0
clock=pygame.time.Clock()
snake_speed=15


snake_block=10
font_style=pygame.font.SysFont("bahnschrift",30)
score_font=pygame.font.SysFont("comicasansms",35)
def your_score(score):
    value=score_font.render("your score"+str(score),True,yellow)
    dis.blit(value,[0,0])
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])
def message(msg,color):
    mesg =font_style.render(msg,True,color)
    dis.blit(mesg,[width/6,heigth/3])
def gameloop():
    snake_speed=10
    game_over=False
    game_close=False
    x1=width/2
    y1=heigth/2
    x1_change=0
    y1_change=0
    snake_list=[]
    Length_of_snake=1
    foodx=round(random.randrange(0,width-100-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,heigth-100-snake_block)/10.0)*10.0
    
    
    while not game_over:
        while game_close==True:
            dis.fill(white)
            message("you lost!press Q-quit or C-play again",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    snake_speed=15
                elif event.key==pygame.K_i:
                    snake_speed=25
                elif event.key==pygame.K_d:
                    snake_speed=30
                elif event.key ==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
        if x1>=width or x1<0 or y1>=heigth or y1<0:
            game_close=True

        x1=x1+x1_change
        y1=y1+y1_change
        dis.fill(blue)
        if Length_of_snake%4!=0:
            pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
        else:
            pygame.draw.rect(dis,red,[foodx,foody,snake_block+5,snake_block+5])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_list)
       
        your_score(Length_of_snake-1)
        
        
        
        pygame.display.update()
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,heigth-snake_block)/10.0)*10.0
            Length_of_snake+=1
        if Length_of_snake-1>10:
            snake_speed=15
        if Length_of_snake-1>20:
            snake_speed=18
        if Length_of_snake-1>40:
            snake_speed=25
        
        dis.blit(score_font.render("press e for easy, i for intermediate,d for difficult",True,white),[0,30])
        clock.tick(snake_speed)



    pygame.quit()
    quit()
gameloop()
