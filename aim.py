# Import and initialize the pygame library
import random
import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Aim Practice")

#file for keeping high scores
highscore = 0
score = 0
scores = []
def refresh_score():    
    global scores
    f = open('score.txt', "r")
    for line in f:
        scores = line.split("\t")
    scores.pop(-1)
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    f.close()


#Counters for the game
total_hits = 0
hits_on_target = 0
missed_hits = 0

#variables for timer
clock = pygame.time.Clock()
current_time = 0
button_press_time = 0
timer = "start"

# RGB value for white, green, blue and red colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#coordinates for the target
cx = 0
cy = 0

# Set up the drawing window
w = 1280
h = 720
screen = pygame.display.set_mode([w, h])

# what state is the program in
game_state = "menu"
running = True

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

#function to check for collision
def collision():
    global cx
    global cy
    mx, my = pygame.mouse.get_pos()
    if cx - 10 <= mx <= cx + 10 and cy - 10 <= my <= cy + 10: #checks if the user clicked on the target
        return True
    else:
        return False

#function for menu
def menu():
    global game_state
    global running
    global cx
    global cy
    global timer
    global total_hits
    global hits_on_target
    global missed_hits
    
    timer = 'start'
    
    #Counters for the game restarted
    total_hits = 0
    hits_on_target = 0
    missed_hits = 0

    # Fill the background with white
    screen.fill(white)

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False
    
    display_text("Left Click to start!", green, w//2, h//2)

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #start the game    
                screen.fill(white)
                cx = random.randint(10,1270)
                cy = random.randint(111,710)
                pygame.draw.circle(screen, (red), (cx, cy), 10)
                game_state = "game"

#function for the game when running
def game():
    global game_state
    global running
    global cx
    global cy
    global total_hits
    global hits_on_target
    global missed_hits
    global current_time
    global button_press_time
    global timer
    global highscore
    global score

    current_time = pygame.time.get_ticks()
    
    if timer == "start": #record the time at which the game starts
        button_press_time = pygame.time.get_ticks()
        timer = "stop"
    
    #run until the timer goes over 30 seconds
    if current_time - button_press_time < 30000:
        pygame.draw.rect(screen,(white),(w//2 - 50,10,150,40))
        display_text(str((30 -((current_time - button_press_time)//1000))).zfill(2), black, w//2, 15)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            running = False
        
        for event in events:
            if event.type == pygame.QUIT:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    total_hits += 1
                    if collision(): #create a new target everytime the user hits
                        hits_on_target += 1
                        pygame.draw.rect(screen,(white),(0,100,w,h-100))
                        cx = random.randint(10,1270)
                        cy = random.randint(111,710)
                        pygame.draw.circle(screen, (red), (cx, cy), 10)
                    else:
                        missed_hits += 1
    else:
        #after the timer saves the scores to a txt file and changes gamestate to results
        score = (hits_on_target*10)-(missed_hits*5)
        f = open('score.txt', 'a')
        f.write(str(score)+'\t')
        f.close()
        refresh_score()
        highscore = max(scores)
        screen.fill(white)
        game_state = "results"

#function for what to display during the results screen
def results():
    global running
    global highscore
    global score
    global game_state

    #displays stats
    display_text("Hits on Target:  "+str(hits_on_target), green, w//2, h//2 - 40)
    display_text("Hits missed:  "+str(missed_hits), red, w//2, h//2)
    display_text("Total score:  "+str(score), blue, w//2, h//2 + 40)
    display_text("High score:  "+str(highscore), blue, w//2, h//2 + 80)
    display_text("Press R to retry", black, w//2, h//2 + 120)
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False
    elif key[pygame.K_r]: #restarts the game
        game_state = "menu"


while running:
    clock.tick(60)
    
    events = pygame.event.get()
    if game_state == "game":  
        game()
    elif game_state == "menu":
        menu()
    elif game_state == "results":
        results()
    
    pygame.display.flip()


pygame.quit()

