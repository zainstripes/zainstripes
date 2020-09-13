#September 13, 2020
#Biryani Boys

#Importing pygame
import pygame
import random

#Initializing pygame
pygame.init()

#Defining colour variables
PLAYER = (255, 150, 50)
GRASS = (0, 175, 0)
GREEN = (25, 225, 0)
ROAD = (25, 25, 25)
YELLOW = (225, 200, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 225)
RED = (225, 0, 0)
GREY = (75, 75, 75)
LIGHT_GREY = (150, 150, 150)
BROWN = (100, 50, 0)
PURPLE = (175, 0, 255)
ORANGE = (255, 100, 0)
TEAL = (0, 255, 255)
PEACH = (255, 100, 100)
LAVENDER = (100, 200, 75)
BLACK = (5, 5, 5)

#Setting up pygame window and initializing score variable
info = pygame.display.Info()
width = 700
height = 700
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)
trash_score = 0

#Initializing vehicle, and trash location, and length lists and ranges

#Cars and busses lists for location
rect_x = [5, 645, 5, 645, 5, 645, 5, 645, 5, 645]
rect_y = [620, 580, 495, 460, 418, 380, 220, 185, 143, 105]

#Trains lists for location and length
train_y = [320, 280, 70] 
train_length = [0, 750, 0]

#Trash ranges and lists for location and size
trash_x = [random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655)]
trash_y = [633, 593, 473, 433, 293, 197, 153, 117, 83]
trash_radius = [random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8)]

#Initizalizing key press variables
KEY_UP = False
KEY_DOWN = False
KEY_RIGHT = False
KEY_LEFT = False

#Declaring the font variable for text
font = pygame.font.SysFont("freesansbold.ttf", 125)
font_two = pygame.font.SysFont("Times New Roman", 30)
font_three = pygame.font.SysFont("freesansbold.ttf", 75)
font_four = pygame.font.SysFont("Times New Roman", 20)



#Defining functions that draw the menu, how to play screen, quitting, background, the character, and the trash

#Function for drawing the menu
def drawMenu():
    pygame.draw.rect(screen, PEACH, (0, 0, width, height)) 
    
    title = font.render("     y Road", 1, WHITE) 
    screen.blit(title, pygame.Rect(200, 100, 50, 100))
    title_two = font.render("Trash", 1, LIGHT_GREY) 
    screen.blit(title_two, pygame.Rect(100, 100, 50, 100))    
    subHeading = font_two.render("Cross the             Collect the            Save the       ", 1, WHITE) 
    screen.blit(subHeading, pygame.Rect(100, 200, 50, 20))
    subHeading_two = font_two.render("Roads.", 1, ROAD) 
    screen.blit(subHeading_two, pygame.Rect(200, 200, 50, 20))    
    subHeading_three = font_two.render("Trash.", 1, LIGHT_GREY) 
    screen.blit(subHeading_three, pygame.Rect(383, 200, 50, 20)) 
    subHeading_four = font_two.render("World.", 1, GREEN) 
    screen.blit(subHeading_four, pygame.Rect(538, 200, 50, 20))    

    pygame.draw.rect(screen, WHITE, (150, 300, 400, 100))       
    pygame.draw.rect(screen, PEACH, (155, 305, 390, 90))
    playButton = font_three.render("PLAY", 1, GRASS) 
    screen.blit(playButton, pygame.Rect(285, 325, 50, 20))    
    
    pygame.draw.rect(screen, WHITE, (150, 425, 400, 100))
    pygame.draw.rect(screen, PEACH, (155, 430, 390, 90))   
    howToPlayButton = font_three.render("HOW TO PLAY", 1, WHITE)
    screen.blit(howToPlayButton, pygame.Rect(175, 450, 50, 20))    
    
    pygame.draw.rect(screen, WHITE, (150, 550, 400, 100))
    pygame.draw.rect(screen, PEACH, (155, 555, 390, 90))
    terminateButton = font_three.render("EXIT", 1, RED)
    screen.blit(terminateButton, pygame.Rect(290, 575, 50, 20))
    
    engineText = font_four.render("Powered By:", 1, WHITE)
    screen.blit(engineText, pygame.Rect(15, 15, 50, 20)) 
    engineNameText = font_two.render("Enviro", 1, GREEN)
    screen.blit(engineNameText, pygame.Rect(100, 12, 50, 20))
    engineNameText_two = font_two.render("Engine ©", 1, BLUE)
    screen.blit(engineNameText_two, pygame.Rect(165, 12, 50, 20))
    
    creatorText = font_four.render("InZAIN Creations ©", 1, WHITE) 
    screen.blit(creatorText, pygame.Rect(300, 675, 50, 100))    
    
    pygame.display.flip()

#Function for drawing the how to play screen    
def drawHowToPlay():
    screen.fill(LAVENDER)
    howToText = font_two.render("It is the year 2055, and pollution has overridden the city of", 1, WHITE) 
    screen.blit(howToText, pygame.Rect(50, 50, 50, 20))
    howToText = font_two.render("EcoVille. The citizens of the once world-renowned", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 75, 50, 20))
    howToText = font_two.render("eco-friendly and environmentally-concious metropolis have", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 100, 50, 20))
    howToText = font_two.render("littered throughout the area, utterly disrupting life in the", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 125, 50, 20))
    howToText = font_two.render("city. Being the top enviro-agent you are, you are tasked with", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 150, 50, 20))   
    howToText = font_two.render("collecting the trash. There's a catch, though. All of the trash", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 175, 50, 20))   
    howToText = font_two.render("is located either on roads or on train tracks. If you get hit,", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 200, 50, 20))     
    howToText = font_two.render("you die. If you fail to collect trash, you are fired. Good Luck.", 1, WHITE)
    screen.blit(howToText, pygame.Rect(50, 225, 50, 20))  
    howToText = font_two.render("Movement:", 1, WHITE)
    screen.blit(howToText, pygame.Rect(100, 350, 50, 20)) 
    howToText = font_four.render("Use the arrow keys to move your character", 1, WHITE)
    screen.blit(howToText, pygame.Rect(25, 380, 50, 20))  
    howToText = font_four.render("up, down, left, and right.", 1, WHITE)
    screen.blit(howToText, pygame.Rect(75, 400, 50, 20))    
    howToText = font_two.render("Objective:", 1, WHITE)
    screen.blit(howToText, pygame.Rect(480, 350, 50, 20))  
    howToText = font_four.render("You start on the beginning grass", 1, WHITE)
    screen.blit(howToText, pygame.Rect(425, 380, 50, 20))  
    howToText = font_four.render("(at the bottom), nd cross the roads", 1, WHITE)
    screen.blit(howToText, pygame.Rect(420, 400, 50, 20))
    howToText = font_four.render("to get to the end grass (at the top).", 1, WHITE)
    screen.blit(howToText, pygame.Rect(423, 420, 50, 20)) 
    howToText = font_four.render("Collect at least 5 trash pieces to win.", 1, WHITE)
    screen.blit(howToText, pygame.Rect(415, 440, 50, 20))     
    howToText = font_two.render("(Click anywhere to return to start game.)", 1, WHITE)
    screen.blit(howToText, pygame.Rect(140, 550, 50, 20))    
    pygame.display.flip()
    
#Function for quitting the game
def executeQuitGame():
    quit()    

def drawWin():
    screen.fill(YELLOW)
    winText = font.render("YOU SAVED", 1, ROAD) 
    screen.blit(winText, pygame.Rect(100, 240, 50, 20)) 
    winText = font.render("THE WORLD", 1, ROAD) 
    screen.blit(winText, pygame.Rect(90, 360, 50, 20))     
    pygame.display.flip()
    
def drawScreen(character_x, character_y):
    global trash_score
    
    pygame.draw.rect(screen, GRASS, (0, 0, width, height))
    
    pygame.draw.rect(screen, ROAD, (0, 575, width, 75))
    pygame.draw.rect(screen, YELLOW, (0, 610, width, 4))
    
    pygame.draw.rect(screen, ROAD, (0, 375, width, 75)) 
    pygame.draw.rect(screen, ROAD, (0, 450, width, 75))   
    pygame.draw.rect(screen, YELLOW, (0, 450, width, 4))
    pygame.draw.rect(screen, WHITE, (0, 410, width, 1))
    pygame.draw.rect(screen, WHITE, (0, 490, width, 1))  
    
    pygame.draw.rect(screen, BROWN, (0, 275, width, 75))
    pygame.draw.rect(screen, BLACK, (0, 310, width, 3)) 
    pygame.draw.rect(screen, GREY, (0, 284, width, 3))
    pygame.draw.rect(screen, GREY, (0, 297, width, 3))    
    pygame.draw.rect(screen, GREY, (0, 324, width, 3))
    pygame.draw.rect(screen, GREY, (0, 337, width, 3))    
    
    pygame.draw.rect(screen, ROAD, (0, 100, width, 75)) 
    pygame.draw.rect(screen, ROAD, (0, 175, width, 75))   
    pygame.draw.rect(screen, YELLOW, (0, 175, width, 4))
    pygame.draw.rect(screen, WHITE, (0, 135, width, 1))
    pygame.draw.rect(screen, WHITE, (0, 215, width, 1)) 
    
    pygame.draw.rect(screen, BROWN, (0, 65, width, 35)) 
    pygame.draw.rect(screen, GREY, (0, 74, width, 3))  
    pygame.draw.rect(screen, GREY, (0, 87, width, 3))
    
    scoreDisplay = font_two.render("Score: " + str(trash_score), 1, WHITE)
    screen.blit(scoreDisplay, pygame.Rect(450, 25, 50, 20))     
    
    for trash_counter in range(0, 9):
        pygame.draw.circle(screen, LIGHT_GREY, ((trash_x[trash_counter]), trash_y[trash_counter]), trash_radius[trash_counter])
        trash_counter += 1
    
    pygame.draw.circle(screen, PLAYER, (character_x, character_y), 10)
    pygame.display.flip()



#Defining functions that draw the various vehicles
def drawFirstCar(rect_x, rect_y):
    pygame.draw.rect(screen, BLUE, (rect_x[0], rect_y[0], 50, 25))
    
def drawSecondCar(rect_x, rect_y):
    pygame.draw.rect(screen, RED, (rect_x[1], rect_y[1], 50, 25))
    
def drawThirdCar(rect_x, rect_y):
    pygame.draw.rect(screen, ORANGE, (rect_x[2], rect_y[2], 50, 25))
    
def drawFourthCar(rect_x, rect_y):
    pygame.draw.rect(screen, GREEN, (rect_x[3], rect_y[3], 50, 25))
    
def drawBus(rect_x, rect_y):
    pygame.draw.rect(screen, YELLOW, (rect_x[4], rect_y[4], 100, 25))   
    
def drawSixthCar(rect_x, rect_y):
    pygame.draw.rect(screen, PURPLE, (rect_x[5], rect_y[5], 50, 25))
    
def drawSeventhCar(rect_x, rect_y):
    pygame.draw.rect(screen, TEAL, (rect_x[6], rect_y[6], 50, 25))
    
def drawEigthCar(rect_x, rect_y):
    pygame.draw.rect(screen, PEACH, (rect_x[7], rect_y[7], 50, 25))
    
def drawNinthCar(rect_x, rect_y):
    pygame.draw.rect(screen, LAVENDER, (rect_x[8], rect_y[8], 100, 25))
    
def drawTenthCar(rect_x, rect_y):
    pygame.draw.rect(screen, BROWN, (rect_x[9], rect_y[9], 50, 25))
        
def drawTrain(train_length):
    pygame.draw.rect(screen, GREY, (0, train_y[0], train_length[0], 25))
    
def drawSecondTrain(train_length):
    pygame.draw.rect(screen, GREY, (train_length[1], train_y[1], 10000, 25))
    
def drawThirdTrain(train_length):
    pygame.draw.rect(screen, GREY, (0, train_y[2], train_length[2], 25))

#Defining time, and location of character varaibles    
myClock = pygame.time.Clock()    
running = True
character_x = width//2
character_y = 675

#Defining the game toggle variable
menu = True
playGame = False
howToPlay = False
quitGame = False
win = False



#Main game loop
while running:
    
    for evnt in pygame.event.get(): #Code for checking all events
        if evnt.type == pygame.QUIT:
            running = False
            
        #Checking for the menu screen toggle
        if menu == True:
            drawMenu()
            character_x = width//2
            character_y = 675
            trash_score = 0           
            pygame.display.flip()
            trash_x = [random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655), random.randint(5, 655)]
            trash_y = [633, 593, 473, 433, 293, 197, 153, 117, 83]
            trash_radius = [random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8), random.randint(4, 8)]
            for trash_counter in range(0, 9):
                pygame.draw.circle(screen, LIGHT_GREY, ((trash_x[trash_counter]), trash_y[trash_counter]), trash_radius[trash_counter])
                trash_counter += 1             
        
        #Checing for mouse clicks on button
        if evnt.type == pygame.MOUSEBUTTONUP:
            mx, my = evnt.pos
            if mx > 155 and mx < 155 + 390 and my > 305 and my < 305 + 90:
                playGame = True
                menu = False
        if evnt.type == pygame.MOUSEBUTTONUP:
            mx, my = evnt.pos
            if mx > 155 and mx < 155 + 390 and my > 430 and my < 430 + 90:
                howToPlay = True
                menu = False
        if evnt.type == pygame.MOUSEBUTTONUP:
            mx, my = evnt.pos
            if mx > 155 and mx < 155 + 390 and my > 555 and my < 555 + 90:
                quitGame = True 

        #Check for key press    
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_UP:
                KEY_UP = True 
            if evnt.key == pygame.K_DOWN:
                KEY_DOWN = True                
            if evnt.key == pygame.K_LEFT:
                KEY_LEFT = True
            if evnt.key == pygame.K_RIGHT:
                KEY_RIGHT = True
        
        #Check for key release      
        if evnt.type == pygame.KEYUP:
            if evnt.key == pygame.K_UP:
                KEY_UP = False 
            if evnt.key == pygame.K_DOWN:
                KEY_DOWN = False                 
            if evnt.key == pygame.K_LEFT:
                KEY_LEFT = False
            if evnt.key == pygame.K_RIGHT:
                KEY_RIGHT = False
    
    #Checking for game toggle
    if playGame == True:     
        
        #Code for moving the character            
        if KEY_UP == True:
            character_y = character_y - 1
        if KEY_DOWN == True:
            character_y = character_y + 1
        if KEY_LEFT == True:
            character_x = character_x - 1
        if KEY_RIGHT == True:
            character_x = character_x + 1
        
        #Calling the functions that draw new images onto frame (vehicles)
        drawScreen(character_x, character_y)
        drawFirstCar(rect_x, rect_y)
        drawSecondCar(rect_x, rect_y)
        drawThirdCar(rect_x, rect_y)
        drawFourthCar(rect_x, rect_y)
        drawBus(rect_x, rect_y)
        drawSixthCar(rect_x, rect_y)
        drawSeventhCar(rect_x, rect_y)
        drawEigthCar(rect_x, rect_y)
        drawNinthCar(rect_x, rect_y)
        drawTenthCar(rect_x, rect_y)
        drawTrain(train_length)
        drawSecondTrain(train_length)
        drawThirdTrain(train_length)
        pygame.display.flip() #Updating or refreshing the frames of pygame
        myClock.tick(1000) #Makes pygame run smoother through FPS, using this code
        
        #Moving the vehicles
        rect_x[0] = rect_x[0] + random.randint(2, 4)
        rect_x[1] = rect_x[1] - random.randint(4, 6)
        rect_x[2] = rect_x[2] + random.randint(3, 5)
        rect_x[3] = rect_x[3] - random.randint(5, 7)
        rect_x[4] = rect_x[4] + random.randint(4, 6)
        rect_x[5] = rect_x[5] - random.randint(6, 8)
        rect_x[6] = rect_x[6] + random.randint(5, 7)
        rect_x[7] = rect_x[7] - random.randint(7, 9)
        rect_x[8] = rect_x[8] + random.randint(5, 7)
        rect_x[9] = rect_x[9] - random.randint(8, 10)
        train_length[0] = train_length[0] + 50
        train_length[1] = train_length[1] - 25
        train_length[2] = train_length[2] + 50
        
        #Checking for vehicle interaction with the boundaries
        if rect_x[0] > 700:
            rect_x[0] = 0
        if rect_x[1] < -50:
            rect_x[1] = 750
        if rect_x[2] > 700:
            rect_x[2] = 0    
        if rect_x[3] < -50:
            rect_x[3] += 750 
        if rect_x[4] > 715:
            rect_x[4] = -15
        if rect_x[5] < -50:
            rect_x[5] += 750   
        if rect_x[6] > 715:
            rect_x[6] = -15 
        if rect_x[7] < -50:
            rect_x[7] += 750
        if rect_x[8] > 715:
            rect_x[8] = -15  
        if rect_x[9] < -50:
            rect_x[9] += 750   
        if train_length[0] == 10000:
            train_length[0] = -7500
        if train_length[1] == -7500:
            train_length[1] = 7500 
        if train_length[2] == 7500:
            train_length[2] = -7500    
            
        #Checking for character interaction with the boundaries
        if character_x > 685:
            character_x = 685
        if character_x < 15:
            character_x = 15    
        if character_y > 685:
            character_y = 685
        if character_y < 15:
            character_y = 15    
            
        #Checking for character collision with vehicles
        if character_x >= rect_x[0] - 20 and character_x <= rect_x[0] + 50 and character_y >= rect_y[0] - 10 and character_y <= rect_y[0] + 30:
            playGame = False
            menu = True
        elif character_x >= rect_x[1] and character_x <= rect_x[1] + 20 and character_y >= rect_y[1] - 10 and character_y <= rect_y[1] + 35:
            menu = True
            playGame = False
        elif character_x > rect_x[2] - 20 and character_x < rect_x[2] + 50 and character_y >= rect_y[2] - 10 and character_y <= rect_y[2] + 35:
            menu = True 
            playGame = False
        elif character_x > rect_x[3] and character_x < rect_x[3] + 20 and character_y >= rect_y[3] - 10 and character_y <= rect_y[3] + 35:
            menu = True 
            playGame = False
        elif character_x > rect_x[4] - 50 and character_x < rect_x[4] + 100 and character_y >= rect_y[4] - 10 and character_y <= rect_y[4] + 25:
            menu = True 
            playGame = False
        elif character_x > rect_x[5] and character_x < rect_x[5] + 20 and character_y >= rect_y[5] - 10 and character_y <= rect_y[5] + 35:
            menu = True
            playGame = False
        elif character_x > rect_x[6] - 20 and character_x < rect_x[6] + 50 and character_y >= rect_y[6] - 10 and character_y <= rect_y[6] + 35:
            menu = True 
            playGame = False
        elif character_x > rect_x[7] and character_x < rect_x[7] + 20 and character_y >= rect_y[7] - 10 and character_y <= rect_y[7] + 35:
            menu = True 
            playGame = False
        elif character_x > rect_x[8] - 100 and character_x < rect_x[8] + 100 and character_y >= rect_y[8] - 10 and character_y <= rect_y[8] + 35:
            menu = True 
            playGame = False
        elif character_x > rect_x[9] and character_x < rect_x[9] + 50 and character_y >= rect_y[9] - 10 and character_y <= rect_y[9] + 35:
            menu = True 
            playGame = False
        elif character_x < train_length[0] and character_y < train_y[0] + 35 and character_y >= train_y[0] - 10:
            menu = True
            playGame = False
        elif character_x > train_length[1] and character_y < train_y[1] + 35 and character_y >= train_y[1] - 10:
            menu = True
            playGame = False
        elif character_x < train_length[2] and character_y <= train_y[2] + 30 and character_y >= train_y[2] - 10:
            menu = True 
            playGame = False
        
        #Checking for character collision with trash
        if character_x <= trash_x[0] + 20 and character_x >= trash_x[0] - 20 and character_y <= trash_y[0] + 10 and character_y >= trash_y[0] - 10:
            trash_x[0] = 1000
            trash_y[0] = 1000
            trash_score += 1
        if character_x <= trash_x[1] + 20 and character_x >= trash_x[1] - 20 and character_y <= trash_y[1] + 10 and character_y >= trash_y[1] - 10:
            trash_x[1] = 1000
            trash_y[1] = 1000            
            trash_score += 1 
        if character_x <= trash_x[2] + 20 and character_x >= trash_x[2] - 20 and character_y <= trash_y[2] + 10 and character_y >= trash_y[2] - 10:
            trash_x[2] = 1000
            trash_y[2] = 1000            
            trash_score += 1
        if character_x <= trash_x[3] + 20 and character_x >= trash_x[3] - 20 and character_y <= trash_y[3] + 10 and character_y >= trash_y[3] - 10:
            trash_x[3] = 1000
            trash_y[3] = 1000            
            trash_score += 1
        if character_x <= trash_x[4] + 20 and character_x >= trash_x[4] - 20 and character_y <= trash_y[4] + 10 and character_y >= trash_y[4] - 10:
            trash_x[4] = 1000
            trash_y[4] = 1000            
            trash_score += 1  
        if character_x <= trash_x[5] + 20 and character_x >= trash_x[5] - 20 and character_y <= trash_y[5] + 10 and character_y >= trash_y[5] - 10:
            trash_x[5] = 1000
            trash_y[5] = 1000            
            trash_score += 1 
        if character_x <= trash_x[6] + 20 and character_x >= trash_x[6] - 20 and character_y <= trash_y[6] + 10 and character_y >= trash_y[6] - 10:
            trash_x[6] = 1000
            trash_y[6] = 1000            
            trash_score += 1 
        if character_x <= trash_x[7] + 20 and character_x >= trash_x[7] - 20 and character_y <= trash_y[7] + 10 and character_y >= trash_y[7] - 10:
            trash_x[7] = 1000
            trash_y[7] = 1000            
            trash_score += 1 
        if character_x <= trash_x[8] + 20 and character_x >= trash_x[8] - 20 and character_y <= trash_y[8] + 10 and character_y >= trash_y[8] - 10:
            trash_x[8] = 1000
            trash_y[8] = 1000            
            trash_score += 1     
     
        #Checking for character reaching the end
        if character_y < 150 and trash_score > 4:
            win = True
            pygame.display.flip()
    
    #Checking for player win
    if win == True:
        drawWin()
    #Checking for how to play screen toggle  
    if howToPlay == True:
        drawHowToPlay()
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            howToPlay = False
            menu = True
            pygame.display.flip()
    
    #Checking to quit the game    
    if quitGame == True:
        executeQuitGame()

#Exiting pygame    
quit()