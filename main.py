import pygame
import time
import random
 
pygame.init()
 
width = 800
height = 600

colour_black = (0,0,0)
colour_white = (255,255,255)

colour_red = (200,0,0)
colour_green = (0,200,0)
colour_blue = (0,0,200)

bright_colour_red = (255,0,0)
bright_colour_green = (0,255,0)
bright_colour_blue = (0,0,255)
 
character_width = 73
character1_width = 73

mr = (width * 0.5)
 
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Escape the Leopard')
clock = pygame.time.Clock()
 
characterImg = pygame.image.load('./images/C1.png')
character1Img = pygame.image.load('./images/C2.png')
Icon = pygame.image.load('./images/game_icon.png').convert_alpha()
bkgd = pygame.image.load('./images/Highway.png').convert()
leopard_image = pygame.image.load('./images/leopard2.png').convert_alpha()
bkgd1 = pygame.image.load('./images/background.jpg')

pygame.display.set_icon(Icon)

pause = False
 
def leopards_Score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Score: "+str(count), True, colour_white)
    gameDisplay.blit(text,(0,0))
    #the above function prints the score on the screen
 
def leopards(leopardx, leopardy, leopardw, leopardh):
    gameDisplay.blit(leopard_image,(leopardx,leopardy))
    #this function us used to print the leopards for character on the left
    
def leopards1(leopardx1, leopardy1, leopardw, leopardh):
    gameDisplay.blit(leopard_image,(leopardx1,leopardy1))
    #this function us used to print the leopards for character on the right 

def character(x,y):
    gameDisplay.blit(characterImg,(x,y))
    #this function us used to print the character on the left
    
def character1(x,y):
    gameDisplay.blit(character1Img,(x,y))
    #this function us used to print the leopards for character on the right
 
def text_to_display(text, font):
    text_on_surface = font.render(text, True, colour_red)
    return text_on_surface, text_on_surface.get_rect()
    #this function is used to draw the given text in the font size on the screen
 
def caught():
    Big_Text = pygame.font.SysFont("comicsansms",110)
    text_Surf, text_Rect = text_to_display("You were eaten", Big_Text)
    text_Rect.center = ((width/2),(height/2))
    gameDisplay.blit(text_Surf, text_Rect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key_to_press("Play Again",150,450,100,50,colour_green,bright_colour_green,main_loop)
        key_to_press("Quit",550,450,100,50,colour_blue,bright_colour_blue,game_exit)

        pygame.display.update()
        clock.tick(15)
        #after the user loses the game, this function gets called and it asks the user whether he wants to play again or quit 
        #the above function caught is written with reference to https://pythonprogramming.net/changing-pygame-icon/

def key_to_press(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
   
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    text_Surf, text_Rect = text_to_display(msg, smallText)
    text_Rect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(text_Surf, text_Rect)

    #the above function key_to_press is written with reference to https://pythonprogramming.net/changing-pygame-icon/
    

def game_exit():
    pygame.quit()
    quit()
    #this function exits the game 

def unpause():
    global pause
    pause = False
    #this function unpauses the game when the user had paused the game 

def paused():

    Big_Text = pygame.font.SysFont("comicsansms",115)
    text_Surf, text_Rect = text_to_display("Paused", Big_Text)
    text_Rect.center = ((width/2),(height/2))
    gameDisplay.blit(text_Surf, text_Rect)
    

    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        

        key_to_press("Continue",150,450,100,50,colour_green,bright_colour_green,unpause)
        key_to_press("Quit",550,450,100,50,colour_blue,bright_colour_blue,game_exit)

        pygame.display.update()
        clock.tick(15)
        #this fuction pauses the game when space bar is pressed and also shows the pause screen


def intro_screen():

    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(bkgd1,(0,0))
        Big_Text = pygame.font.SysFont("comicsansms",85)
        text_Surf, text_Rect = text_to_display("Escape the Leopard", Big_Text)
        text_Rect.center = ((width/2),(height/2))
        gameDisplay.blit(text_Surf, text_Rect)

        key_to_press("PLAY",350,375,100,50,colour_green,bright_colour_green,main_loop)
        key_to_press("Quit",350,450,100,50,colour_blue,bright_colour_blue,game_exit)

        pygame.display.update()
        clock.tick(15)
        #this functions displays the introduction screen and asks the user whether he wants to play or quit
        
        
    
    

    
def main_loop():
    global pause

    pygame.mixer.music.load('Sound.mp3')
    pygame.mixer.music.play(-1)

    x = (width * 0.2)
    y = (height * 0.716)

    x1 = (width * 0.8)
    y1 = (height * 0.7)
 
    x_change = 0

    x1_change = 0 
 
    leopard_startx = random.randrange(0, width*0.5 - 36)
    leopard_startx1 = random.randrange(width*0.5 + 36, width)
    leopard_starty1 = -600
    leopard_starty = -400
    leopard_speed = 4
    leopard_width = 73
    leopard_height = 50
 
    leopardCount = 1
 
    Score = 0
 
    gameExit = False

    b_1 = 0
    c_1 = 0
    b_2 = 0
    c_2 = -height
    
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:    #this command is used th move the characters when the defined key is presses
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                        x_change = 5
                if event.key == pygame.K_LEFT:
                        x1_change = -5
                if event.key == pygame.K_RIGHT:
                        x1_change = 5
                if event.key == pygame.K_SPACE:  #when space bar is pressed, game is paused 
                    pause = True
                    paused()
            
                    
 
            if event.type == pygame.KEYUP:                                    #this command stops the movement of the character when key is released  
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x1_change = 0  
        x += x_change                 #this command moves the character according to the above event
        if x > mr - character_width : #this command adds constraints on the movement of the left character
            x = mr - character_width
        x1 += x1_change
        if x1 < mr:                   #this command adds constraints on the movement of the right character
            x1 = mr

        c_1 += 5
        c_2 += 5
        
        gameDisplay.blit(bkgd,(b_1,c_1))
        gameDisplay.blit(bkgd,(b_2,c_2))
        if c_1 > height:
            c_1 = -height
        if c_2 > height:
            c_2 = -height

        #the above lines of the codes rolls the background screen to give a moving effect
            
        
        leopards(leopard_startx, leopard_starty, leopard_width, leopard_height)
        leopards1(leopard_startx1, leopard_starty1, leopard_width, leopard_height)
 
        
        leopard_starty += leopard_speed   #changes the position of leopards to give a sense to the user that they are coming down
        leopard_starty1 += leopard_speed
        character(x,y)
        character1(x1,y1)
        leopards_Score(Score)
 
        if x < character_width * 0.25:
            x= character_width * 0.25

        if x1 > width - character_width:
            x1 = width - character_width

        #The above lines makes sure that characters that the characters don't move out of the screen
         
        if leopard_starty > height:
            leopard_startx = random.randrange(0,width * 0.5 - 36)
            leopard_starty = random.randrange(-200,-100)
            Score += 1
            leopard_speed += 0.5   #increases the speed with which leopards come down

        #The above lines of lines of code is randomly adding new leopards on the left side one after the other

        if leopard_starty1 > height:
            leopard_starty1 = random.randrange(-100,0)
            leopard_startx1 = random.randrange(width * 0.5 + 36, width-leopard_width)
            Score += 1
            leopard_speed += 0.5   #increases the speed with which leopards come down

        #The above lines of code is randomly adding new leopards on the right side one after the other
 
        if y < leopard_starty+leopard_height:
            if x > leopard_startx and x < leopard_startx + leopard_width or x+character_width > leopard_startx and x + character_width < leopard_startx+leopard_width:
                caught()

        if y1 < leopard_starty1+leopard_height:
            if x1 > leopard_startx1 and x1 < leopard_startx1 + leopard_width or x1+character_width > leopard_startx1 and x1 + character_width < leopard_startx1+leopard_width:
                caught()
        #The above lines check whether the character is caught by leopard, if so calls the caught() function

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

intro_screen()
main_loop()
pygame.quit()
quit()
