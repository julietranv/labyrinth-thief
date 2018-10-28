# ---------------------------------------------------------------------#
# Labyrinth Thief Game by Julie Tran                                   #
# October 26, 2015                                                     #
# This game has two levels                                             #
# Level 1 must be completed successfully before Level 2 can be started #
# ---------------------------------------------------------------------#
#
import pygame, sys
from pygame.locals import *
from Person import *
from Guard import *
from wall import *

# Setup the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define Maze structures for Levels 1 & 2
row = 12
col = 16
row1 = row - 1
col1 = col - 1

# Maze for Level 1:
Maze1 = [[0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1],
         [0,1,0,1,0,0,0,1,1,1,1,0,1,0,0,0],
         [0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0],
         [0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1],
         [0,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0],
         [0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0],
         [0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0],
         [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0],
         [0,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0],
         [0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1],
         [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
         [0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,2]]

# Maze for Level 2:
Maze2 = [[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0],
         [1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0],
         [0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0],
         [0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0],
         [0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0],
         [0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0],
         [0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0],
         [0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0],
         [0,1,1,0,0,0,0,1,1,1,1,0,0,1,0,0],
         [0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0],
         [1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,0],
         [1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,2]]

# Always start out with Level 1
Level = 1
Maze = Maze1

# Function to end game
def endGame():
   pygame.quit()
   sys.exit()

# Function to wait for key pressed if Win
#    Key "2" is used to enter Level 2
def waitForKeyPress():
   while True:
      for event in pygame.event.get():
         if event.type == QUIT:
            endGame()
         if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
               endGame()
            elif event.key == K_2:
               Level = 2
               Maze = Maze2
               return
# Function to wait for key pressed if Lose
#    Key "n" is used to start a new game at the current level
def waitForKeyPress2():
   while True:
      for event in pygame.event.get():
         if event.type == QUIT:
            endGame()
         if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
               endGame()
            elif event.key == K_n:
               return

# Function to display text
def drawText(text, font, surface, x, y):
   textobj = font.render(text, True, (255, 255, 255), (0, 0, 255))
   textRect = textobj.get_rect()
   textRect.topleft = (x, y)
   surface.blit(textobj, textRect)

# Function to create a Maze structure
def drawMaze(window):
    # load image of a wall cell 
    image = pygame.image.load("wall.gif")
    # load image of the treasure box
    image2 = pygame.image.load("treasure.png")
    
    # Create variables to keep track of where to draw Maze walls
    i = 0
    j = 0
    
    # Outer loop runs as long as i is 
    # not beyond the last maze row
    while (i < row):
        
        # Inner loop runs as long as j is 
        # not beyond the last maze column
        while (j < col):

            # Draw a brick wall if a "1" is detected
            # Increase the y
            if Maze[i][j] == 1:
                x = j * 50
                y = i * 50
                window.blit(image, (x,y))
            # Draw the treasure box if a "2" is detected
            elif Maze[i][j] == 2:
                x = (j * 50) + 10
                y = (i * 50) + 10
                window.blit(image2, (x,y))                
            j += 1
            
        # Increase i by 1 and reset j to first column
        i += 1
        j = 0

#
# Main Program
# Initialize the Maze screen
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Labyrinth Thief Game by Julie Tran - Press <ESC} to exit")

# Setup font for displaying texts 
font = pygame.font.SysFont(None, 48)

# Draw Maze background
background = pygame.Surface((800,600))
drawMaze(background)
screen.blit(background, (0,0))

# Check if a key is still pressed down every 100 milliseconds
# allows user to hold down the key to move
pygame.key.set_repeat(100, 100)

# Create the Treasure Thief and Guards at appropriate locations
guy = Person(0,0)

# Guard starting locations in Maze1
enemy1 = Guard(10,500)
enemy2 = Guard(410,160)
enemy3 = Guard(560,460)

# Guard starting locations in Maze2
# enemy1 = Guard(10,110)
# enemy2 = Guard(210,410)
# enemy3 = Guard(460,310)
# enemy4 = Guard(760,260)

# Moving speed of guards in Level 1
speed1 = 10
speed2 = 7
speed3 = 7

# Moving speed of guards in Level 2
speed4 = 10
speed5 = 10
speed6 = 7
speed7 = 8

# A list that keeps track of the areas of screen that have changed
changedRecs = []

# Draw the starting Maze screen
pygame.display.update()

# Main Program Loop
while True:
    # draw the Maze, Thief and Guards
    screen.blit(background, (0,0))    

    guy.draw(screen)
    enemy1.draw(screen)
    enemy2.draw(screen)
    enemy3.draw(screen)
    
    # Update the current positions of the Thief and Guards
    changedRecs.append(guy.getRec())
    changedRecs.append(enemy1.getRec())
    changedRecs.append(enemy2.getRec())
    changedRecs.append(enemy3.getRec())

    # There is an additional guard for Level 2
    if (Level > 1):
       enemy4.draw(screen)
       changedRecs.append(enemy4.getRec())

    # Update the changed areas of the screen
    pygame.display.update(changedRecs)

    # Check for a key press   
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYDOWN:
            
            # Update the position of the Thief to changedRecs
            changedRecs.append(guy.getRec())
            x = guy.x
            y = guy.y
            i = int(y/50)
            i2 = int((y+31)/50)
            if (i2 > row1):
                i2 = row1
            j = int(x/50)
            j2 = int((x+23)/50)
            if (j2 > col1):
                j2 = col1

            # Up Arrow key is pressed
            if event.key == K_UP: 
                guy.moveUp()
                i -= 1
                if (i >= 0):
                    if Maze[i][j] >= 1:
                        y = i*50
                        theWall = Wall(x,y)
                        if guy.collide(theWall):
                            if Maze[i][j] == 2:
                                drawText('You Win!', font, screen, 342, 280)
                                drawText('Press 2 for next Level', font, screen, 240, 314)
                                pygame.display.update()
                                waitForKeyPress()
                                Level = 2
                                Maze = Maze2
                                guy = Person(0,0)
                                enemy1 = Guard(10,110)
                                enemy2 = Guard(210,410)
                                enemy3 = Guard(460,310)
                                enemy4 = Guard(760,260)
                                background = pygame.Surface((800,600))
                                drawMaze(background)
                                screen.blit(background, (0,0))
                                pygame.display.update()
                            else:
                                guy.moveDown()                               
                    elif (j2 > j):
                        if Maze[i][j2] >= 1:
                            y = i*50
                            x = j2*50
                            theWall = Wall(x,y)
                            if guy.collide(theWall):
                                if Maze[i][j2] == 2:
                                    drawText('You Win!', font, screen, 342, 280)
                                    drawText('Press 2 for next Level', font, screen, 240, 314)         
                                    pygame.display.update()
                                    waitForKeyPress()
                                    Level = 2
                                    Maze = Maze2
                                    guy = Person(0,0)
                                    enemy1 = Guard(10,110)
                                    enemy2 = Guard(210,410)
                                    enemy3 = Guard(460,310)
                                    enemy4 = Guard(760,260)
                                    background = pygame.Surface((800,600))
                                    drawMaze(background)
                                    screen.blit(background, (0,0))
                                    pygame.display.update()                              
                                else:
                                    guy.moveDown()

            # Down Arrow key is pressed
            elif event.key==K_DOWN:
                guy.moveDown()
                i += 1
                if (i <= row1):
                    if Maze[i][j] >= 1:
                        y = i*50
                        theWall = Wall(x,y)
                        if guy.collide(theWall):
                            if Maze[i][j] == 2:
                                drawText('You Win!', font, screen, 342, 280)
                                drawText('Press 2 for next Level', font, screen, 240, 314)
                                pygame.display.update()
                                waitForKeyPress()
                                Level = 2
                                Maze = Maze2
                                guy = Person(0,0)
                                enemy1 = Guard(10,110)
                                enemy2 = Guard(210,410)
                                enemy3 = Guard(460,310)
                                enemy4 = Guard(760,260)
                                background = pygame.Surface((800,600))
                                drawMaze(background)
                                screen.blit(background, (0,0))
                                pygame.display.update()
                            else:
                                guy.moveUp()
                    elif (j2 > j):
                        if Maze[i][j2] >= 1:
                            y = i*50
                            x = j2*50
                            theWall = Wall(x,y)
                            if guy.collide(theWall):
                                if Maze[i][j2] == 2:
                                    drawText('You Win!', font, screen, 342, 280)
                                    drawText('Press 2 for next Level', font, screen, 240, 314)
                                    pygame.display.update()
                                    waitForKeyPress()
                                    Level = 2
                                    Maze = Maze2
                                    guy = Person(0,0)
                                    enemy1 = Guard(10,110)
                                    enemy2 = Guard(210,410)
                                    enemy3 = Guard(460,310)
                                    enemy4 = Guard(760,260)
                                    background = pygame.Surface((800,600))
                                    drawMaze(background)
                                    screen.blit(background, (0,0))
                                    pygame.display.update()
                                else:
                                    guy.moveUp()

            # Left Arrow key is pressed
            elif event.key==K_LEFT:
                guy.moveLeft()
                j -= 1
                if (j >= 0):
                    if Maze[i][j] >= 1:
                        x = j*50
                        theWall = Wall(x,y)
                        if guy.collide(theWall):
                            if Maze[i][j] == 2:
                                drawText('You Win!', font, screen, 342, 280)
                                drawText('Press 2 for next Level', font, screen, 240, 314)
                                pygame.display.update()
                                waitForKeyPress()
                                Level = 2
                                Maze = Maze2
                                guy = Person(0,0)
                                enemy1 = Guard(10,110)
                                enemy2 = Guard(210,410)
                                enemy3 = Guard(460,310)
                                enemy4 = Guard(760,260)
                                background = pygame.Surface((800,600))
                                drawMaze(background)
                                screen.blit(background, (0,0))
                                pygame.display.update()                               
                            else:
                                guy.moveRight()
                    elif (i2 > i):
                        if Maze[i2][j] >= 1:
                            x = j*50
                            y = i2*50
                            theWall = Wall(x,y)
                            if guy.collide(theWall):
                                if Maze[i2][j] == 2:
                                    drawText('You Win!', font, screen, 342, 280)
                                    drawText('Press 2 for next Level', font, screen, 240, 314)
                                    pygame.display.update()
                                    waitForKeyPress()
                                    Level = 2
                                    Maze = Maze2
                                    guy = Person(0,0)
                                    enemy1 = Guard(10,110)
                                    enemy2 = Guard(210,410)
                                    enemy3 = Guard(460,310)
                                    enemy4 = Guard(760,260)
                                    background = pygame.Surface((800,600))
                                    drawMaze(background)
                                    screen.blit(background, (0,0))
                                    pygame.display.update()                                        
                                else:
                                    guy.moveRight()

            # Right Arrow key is pressed
            elif event.key==K_RIGHT:
                guy.moveRight()
                j += 1
                if (j <= col1):
                    if Maze[i][j] >= 1:
                        x = j*50
                        theWall = Wall(x,y)
                        if guy.collide(theWall):
                            if Maze[i][j] == 2:
                                drawText('You Win!', font, screen, 342, 280)
                                drawText('Press 2 for next Level', font, screen, 240, 314)
                                pygame.display.update()
                                waitForKeyPress()
                                Level = 2
                                Maze = Maze2
                                guy = Person(0,0)
                                enemy1 = Guard(10,110)
                                enemy2 = Guard(210,410)
                                enemy3 = Guard(460,310)
                                enemy4 = Guard(760,260)
                                background = pygame.Surface((800,600))
                                drawMaze(background)
                                screen.blit(background, (0,0))
                                pygame.display.update()                               
                            else:
                                guy.moveLeft()
                    elif (i2 > i):
                        if Maze[i2][j] >= 1:
                            x = j*50
                            y = i2*50
                            theWall = Wall(x,y)
                            if guy.collide(theWall):
                                if Maze[i2][j] == 2:
                                    drawText('You Win!', font, screen, 342, 280)
                                    drawText('Press 2 for next Level', font, screen, 240, 314)
                                    pygame.display.update()
                                    waitForKeyPress()
                                    Level = 2
                                    Maze = Maze2
                                    guy = Person(0,0)
                                    enemy1 = Guard(10,110)
                                    enemy2 = Guard(210,410)
                                    enemy3 = Guard(460,310)
                                    enemy4 = Guard(760,260)
                                    background = pygame.Surface((800,600))
                                    drawMaze(background)
                                    screen.blit(background, (0,0))
                                    pygame.display.update()                                    
                                else:
                                    guy.moveLeft()

    if (Level < 2):
        enemy1.y += speed1
        y1 = enemy1.y
        if (y1 < 100) or (y1 > 500):
           speed1 = -speed1
        if guy.collide(enemy1):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,500)
           enemy2 = Guard(410,160)
           enemy3 = Guard(560,460)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()

        enemy2.x += speed2
        x2 = enemy2.x
        if (x2 < 410) or (x2 > 555):
           speed2 = -speed2
        if guy.collide(enemy2):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,500)
           enemy2 = Guard(410,160)
           enemy3 = Guard(560,460)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()
       
        enemy3.x += speed3
        x3 = enemy3.x
        if (x3 < 555) or (x3 > 655):
           speed3 = -speed3
        if guy.collide(enemy3):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,500)
           enemy2 = Guard(410,160)
           enemy3 = Guard(560,460)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()       
    else:
        enemy1.y += speed4
        y1 = enemy1.y
        if (y1 < 105) or (y1 > 460):
           speed4 = -speed4
        if guy.collide(enemy1):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,110)
           enemy2 = Guard(210,410)
           enemy3 = Guard(460,310)
           enemy4 = Guard(760,260)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()

        enemy2.y += speed5
        y2 = enemy2.y
        if (y2 < 105) or (y2 > 410):
           speed5 = -speed5
        if guy.collide(enemy2):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,110)
           enemy2 = Guard(210,410)
           enemy3 = Guard(460,310)
           enemy4 = Guard(760,260)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()
       
        enemy3.x += speed6
        x3 = enemy3.x
        if (x3 < 455) or (x3 > 660):
           speed6 = -speed6
        if guy.collide(enemy3):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,110)
           enemy2 = Guard(210,410)
           enemy3 = Guard(460,310)
           enemy4 = Guard(760,260)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()

        enemy4.y += speed7
        y4 = enemy4.y
        if (y4 < 255) or (y4 > 510):
           speed7 = -speed7
        if guy.collide(enemy4):
           drawText('You Lose!', font, screen, 341, 280)
           drawText('GAME OVER - Press n for New Game', font, screen, 124, 314)
           pygame.display.update()
           waitForKeyPress2()
           guy = Person(0,0)
           enemy1 = Guard(10,110)
           enemy2 = Guard(210,410)
           enemy3 = Guard(460,310)
           enemy4 = Guard(760,260)
           background = pygame.Surface((800,600))
           drawMaze(background)
           screen.blit(background, (0,0))
           pygame.display.update()
       
    pygame.time.wait(100)
