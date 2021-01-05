# initialize libraries
import pygame
import random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# RGB value for colours.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255,255,0)

#keeps track of the players score
score = 0

# Set up the drawing window
w = 960
h = 540
screen = pygame.display.set_mode([w, h])
screen.fill(white)

#coordinates to generate the blocks
by = random.randint(100,h - 100)
bx = w-100
bdt = -2.5 #movement of the block

#creates obstacles
def blocks():
    global by
    global bx
    pygame.draw.rect(screen, (blue), (bx,0,100,h))
    pygame.draw.rect(screen, (white), (bx,by,100,80 ))

# what state is the program in
game_state = "menu"
running = True

#coordinates for the bird
fx = h//2
fy = w//3

#motion of the bird
dx = 0
dy = 1.8

#function to decide whether you have lost the game
def lose():
    global bx,fx,by

    if bx <= fx <= bx + 100: #bird touches the obstacle
        if  by + 8 <= fy <= by + 72:
            return False
        else:
            return True
    elif fy < 10: #bird touches the ceiling 
        return False
    elif fy > w-10: #bird touches the ground
        return False

#function for the game start menu screen
def menu():
    global score
    global game_state
    
    screen.fill(white)

    score = 0
    
    display_text('Press the space key to start!', (black), w//2, h//2)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(white)
                game_state = 'game'

#function for displaying text
def display_text(string, colour, x, y):
    # create a font object.
    font = pygame.font.Font('freesansbold.ttf', 32)
 
    # create a text suface object, on which text is drawn on it.
    text = font.render(string, True, colour, white)

    # copying the text surface object to the display surface object at the center coordinate.
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (x, y)

    screen.blit(text, textRect)

#function for what to do when the game is being played
def game():
    global fx
    global fy
    global running
    global dx
    global dy
    global bx
    global by
    global game_state
    global score
    global bdt

    bx = bx + bdt
    
    if bx < w // 20: #adds a point to the user's score if he manages to go through the obstacle and increases the speed
        screen.fill(white)
        by = random.randint(100,h - 100)
        score += 1
        bdt -= 0.1
        bx = w - 100
        
    
    blocks() #calls the function to generate blocks
    
    #generates white rectangle to cover up the previously drawn shapes from the bird and obstacle 
    pygame.draw.rect(screen, (white), (bx + 100, 0, 100, 960 ))
    pygame.draw.rect(screen, (white ), (fx - 10, fy - 10, 20, 20 ))
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False


    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fy = max(0, fy - 40)

    fy = min(540, fy+dy) #movement of the bird
    
    display_text(str(score), (black), w//2, 30)
    
    pygame.draw.circle(screen, (yellow), (fx, fy), 10)
    
    if lose():
        game_state = 'results'
    
def results():
    global game_state

    screen.fill(white)

    display_text('score: '+str(score), (black), w//2, h//2)
    display_text('Press R to retry', (black), w//2, h//2 + 30)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_state = 'menu'

#runs until the user presses the escape key to quit
while running:
    clock.tick(60)
    
    events = pygame.event.get()
    if game_state == 'game':
        game()
    elif game_state == 'results':
        results()
    elif game_state == 'menu':
        menu()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()

pygame.quit()
