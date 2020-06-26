#example.py
#written by: Sidumiso Debbie Mabaso
#date: 25 February 2020
#function: this is a game in which the user plays by avoiding contact with the 'enemy' or 'enemies' to win or chase the 'prize' to win 

import pygame           #Imports a game library that lets you use specific functions in your program.
import random           #Import to generate random numbers. 

#Initialize the pygame modules to get everything started.

pygame.init() 

#The screen that will be created needs a width and a height.

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))      #This creates the screen and gives it the width and height specified as a 2 item sequence.

#Creating the player and giving it the image found in this folder (similarly with the enemy, enemy_1,monster and prize images). 

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy_1 = pygame.image.load("enemy.png")
monster = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg") 

#Getting the width and height of the images in order to do boundary detection

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy_1_height = enemy.get_height()
enemy_1_width = enemy.get_width()

monster_height = monster.get_height()
monster_width = monster.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

#Storing the positions of the player, enemy, enemy_1, monster and prize as variables so that they can be changed later.

playerXPosition = 100
playerYPosition = 50

#Making the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy_1XPosition = screen_width
enemy_1YPosition = random.randint(0, screen_height - enemy_1_height)

monsterXPosition = screen_width
monsterYPosition = random.randint(0, screen_height - monster_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)


#Checking if the up or down key is pressed
#Making them to the boolean value of False since they are not as yet pressed

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#the looping structure
while 1:                                                        
    #clears the screen.
    #drawing the player image to the screen at the postion specfied, same goes for enemy_1, monster and the prize
    screen.fill(0)                                             
    screen.blit(player, (playerXPosition, playerYPosition))    
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy_1, (enemy_1XPosition, enemy_1YPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()         #updating the screen. 
    
    #the loops through events in the game.
    
    for event in pygame.event.get():
    
        #checking if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        #Checking if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            #Testing if the key pressed is the one needed.
            #pygame.K_UP represents a keyboard key constant. 
            if event.key == pygame.K_UP:            
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        #Checking if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            #Testing if the key released is the one needed.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False 
            
    #After events are checked for in the for loop above and values are set,
    #Checking the key pressed values and moving the player accordingly.
    
    #The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    #Which means that if in need of the player to move down, the y position should be increased. 
    
    if keyUp == True:
        if playerYPosition > 0 :                               #Making sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:     #Making sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 :                               #Making sure that the user does not move the player out of the window on the left.
            playerXPosition -= 1    
    if keyRight == True:
        if playerXPosition < screen_width - image_width:       #Making sure that the user does not move the player out of the window on the right.
            playerXPosition += 1
        
        
    
    #Checking for collision of the enemy, enemy_1, monster and prize with the player.
    #Need to create bounding boxes around the images of the player, enemy, enemy_1 and prize.
    #Need to test if these boxes intersect and if they do then there is a collision.
    
    #Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    #Updating the playerBox position to the player's position,
    #in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    #Bounding boxes for the enemy, enemy_1, monster and the prize:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy_1Box = pygame.Rect(enemy_1.get_rect())
    enemy_1Box.top = enemy_1YPosition
    enemy_1Box.left = enemy_1XPosition

    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    
    #Testing the collision of boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy_1Box) or playerBox.colliderect(monsterBox):
    
        #Displaying losing status to the user: 
        
        print("You lose!")
       
        #Quitting the game and exiting the window:
        
        pygame.quit()
        exit(0)
        

    #If the enemy, enemy_1, monster, prize are off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width and enemy_1XPosition < 0 - enemy_1_width and monsterXPosition < 0 - monster_width and monsterXPosition < 0 - monster_width and prizeXPosition < 0 - prize_width:

        #Displaying winning status to the user:
        
        print("You win!")
        
        #Quitting the game and exiting the window: 
        pygame.quit()
        
        exit(0)

    #if the user collide with the prize box they win
    elif playerBox.colliderect(prizeBox):

        print("You win!")

        pygame.quit()

        exit(0)
    
    #Making the enemy, enemy_1, monster, and prize approach the player at different speeds:
    
    enemyXPosition -= 0.25
    enemy_1XPosition -= 0.15
    monsterXPosition -= 0.35
    prizeXPosition -= 0.25
    
    #The loop ends here.
  
