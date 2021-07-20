# initialize libraries

import pygame
import os
import sys
import random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# RGB value for colours.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255,255,0)

#set up a drawing window
infoObject = pygame.display.Info()
w = infoObject.current_w
h = infoObject.current_h - 140
screen = pygame.display.set_mode([w, h])
screen.fill(black)

# what state is the program in
game_state = "start"
running = True

px = random.randint(10, w-20)
py = random.randint(10, h-20)


#variables used to generate the snake
coord = [w//2, h//2,w//2+w//60, h//2,w//2+w//60, h//2,w//2+w//60, h//2,w//2+w//60, h//2,w//2+w//60, h//2, w//2+w//60, h//2, w//2+w//60, h//2, w//2+w//60, h//2]
i = 1
dx = 10
x = 3
direction = 'right'
length = 20


def display_text(string, colour, x, y):
    # create a font object.
    font = pygame.font.Font('freesansbold.ttf', 32)
 
    # create a text suface object, on which text is drawn on it.
    text = font.render(string, True, colour, black)

    # copying the text surface object to the display surface object at the center coordinate.
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (x, y)

    screen.blit(text, textRect)
def start():
    global game_state
    screen.fill(black)
    display_text("Press the space key to start!", red, w//2, h//2)
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        game_state = 'game'

def game():
    global coord, i, direction, dx, length, x
    global px, py
    global running
    global game_state

    screen.fill(black)

    pygame.draw.rect(screen, (green), (px,py, w//60, w//60 ))

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False
    elif key[pygame.K_d] and not direction == 'left':
        direction = 'right'
    elif key[pygame.K_w] and not direction == 'down':
        direction = 'up'
    elif key[pygame.K_a] and not direction == 'right':
        direction = 'left'
    elif key[pygame.K_s] and not direction == 'up':
        direction = 'down'
    elif key[pygame.K_v]:
        length +=2

    if direction == 'right':
        dx = w//60
        coord.append(coord[-2] + dx)
        coord.append(coord[-2])
    elif direction == 'left':
        dx = -w//60 + 1
        coord.append(coord[-2] + dx)
        coord.append(coord[-2])
    elif direction == 'up':
        dx = -w//60 + 1
        coord.append(coord[-2])
        coord.append(coord[-2] + dx)
    elif direction == 'down':
        dx = w//60
        coord.append(coord[-2])
        coord.append(coord[-2] + dx)
    
    while i <= length:
        if coord[-i-1] > w:
            coord[-i-1] = 5
        if coord[-i-1] < 0:
            coord[-i-1] = w-5
        if coord[-i] > h:
            coord[-i] = 5
        if coord[-i] < 0:
            coord[-i] = h-5

        if i == 1:
            pygame.draw.rect(screen, (red), (coord[-i-1],coord[-i], w//60, w//60 ))
        else:
            pygame.draw.rect(screen, (blue), (coord[-i-1],coord[-i], w//60, w//60 ))
        i = i + 2
    
    while x <= length:
        if coord[-1] == coord[-x] and coord[-2] == coord[-x-1]:
            game_state = "end"
        x = x + 2

    if direction == "right": 
        if px <= (coord[-2] + (w//60))  <= (px + (w//60)) and py - 8  <= (coord[-1] + ((w//60)//2)) <= (py + 8 +(w//60)):
            length += 2
            px = random.randint(100, w-50)
            py = random.randint(50, h-50)
    elif direction == "left":
        if px <= coord[-2]  <= (px + (w//60)) and py - 8  <= (coord[-1] + ((w//60)//2)) <= (py + 8 +(w//60)):
            length += 2
            px = random.randint(100, w-50)
            py = random.randint(50, h-50)
    elif direction == 'up':
        if px - 8 <= (coord[-2] + (w//60)//2)  <= (px + 8 +(w//60)) and py  <= coord[-1] <= (py + (w//60)):
            length += 2
            px = random.randint(100, w-50)
            py = random.randint(50, h-50)
    else:
        if px - 8 <= (coord[-2] + (w//60)//2)  <= (px + 8 +(w//60)) and py  <= (coord[-1] + (w//60)) <= (py + (w//60)):
            length += 2
            px = random.randint(100, w-50)
            py = random.randint(50, h-50)

    if len(coord) > length: #removes old values from the list which are no longer needed
        coord.pop(0)
        coord.pop(0)
    
    i = 1
    x = 3
    

def end():
    global game_state

    screen.fill(black)
    display_text("Press R to retry", white, w//2, h//2)
    display_text("score: "+str(length*10), red, w//2, h//2 + 50)
    key = pygame.key.get_pressed()
    if key[pygame.K_r]:
        os.execl(sys.executable, sys.executable, *sys.argv)

    
    
#runs until the user presses the escape key to quit
def main():
    global running

    while running:
        clock.tick(20)
        
        events = pygame.event.get()
        if game_state == 'game':
            game()

        elif game_state == "end":
            end()
        
        elif game_state == 'start':
            start()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            return None

        pygame.display.flip()

main()

pygame.quit()
