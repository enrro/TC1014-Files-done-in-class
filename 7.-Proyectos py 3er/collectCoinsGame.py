'''
Created on 11/11/2014
pygame
Proven and tested on python 2.7
@author: A01221672
'''
import pygame
import random
import sys
# functions
def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # pressing escape quits
                    terminate()
                return

def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def playSong(song,volume,loop):
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(float(volume))
    pygame.mixer.music.play(loop)
#poniendo en starting the game
pygame.init()
clock = pygame.time.Clock()

#creating a new window for the game
ancho = 640
alto = 480
lienzo = pygame.display.set_mode((ancho,alto)) #Aqui es el tamano de la pantalla
pygame.display.set_caption("Circle Runner")

# creating the player
player = pygame.Rect(30, 150, 50, 50)

# score
score = 0
# creating enemies
enemyCounter = 0
enemy = []
enemySize = 20

#choosing the color palet
colorSugar = [[254,67,101],[252,157,154],[249,205,173],[200,200,169],[131,175,155]] #paleta de colores calidos
colorDreamMagnet = [[52,56,56],[0,95,107],[0,140,158],[0,180,204],[0,223,252]]

#adding music
musiclist = ["leaving the past behind.mp3","This Is The End.mp3","21. TechnoMan.mp3","sky_idgaf.mp3"]

#adding sound
sound = pygame.mixer.Sound('smb_coin.wav')
sound.set_volume(.4)
#creating a font constant for the game
FONT = pygame.font.SysFont('monospace!!!',20) #SysFont creates a font object from available pygame fonts


#Seting up the movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

drawText('Collector', FONT, lienzo, (ancho / 2), (190),colorSugar[1])
drawText('Press a key to start.', FONT, lienzo, (ancho / 2), (230),colorSugar[1])
pygame.display.update()
waitForPlayerToPressKey()


#running the game
topScore = 0
while True:
    score = 0
    gameLoop = True
    playSong(musiclist[0],.4,-1)
    moveLeft = moveRight = moveUp = moveDown = False
    for i in range(20):
        enemy.append(pygame.Rect(random.randint(30, ancho - enemySize), random.randint(0, alto - enemySize), enemySize, enemySize))
    while gameLoop:
        score+=1
        # check every event before continuing with the game
        for event in pygame.event.get():
            keysPress = pygame.key.get_pressed()
            # game exit conditions
            if event.type == pygame.QUIT:
                gameLoop = False
            if keysPress[pygame.K_ESCAPE]:
                gameLoop = False
            if keysPress[pygame.K_LALT] and keysPress[pygame.K_F4]:
                gameLoop = False
            # mouse feedback to use maybe for latter
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse")

            # Keyboard variables
            if event.type == pygame.KEYDOWN:
                #print(event.key)
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    moveLeft = True
                    moveRight = False
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    moveLeft = False
                    moveRight = True
                if event.key == pygame.K_UP or event.key == ord("w"):
                    moveUp = True
                    moveDown = False
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    moveUp = False
                    moveDown = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    moveLeft = False
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    moveRight = False
                if event.key == pygame.K_UP or event.key == ord("w"):
                    moveUp = False
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    moveDown = False
        #Creationg more enemies
        '''
        trabajo pendiente
        '''

        # creating the background
        pygame.draw.rect(lienzo,(colorSugar[4]),(0, 0, ancho, alto))#fondo
        pygame.draw.rect(lienzo,(colorSugar[0]),(0,0,30,alto))#Piso

        # move the player
        if moveDown and player.bottom < alto:
            player.top += MOVESPEED
        if moveUp and player.top > 0:
            player.top -= MOVESPEED
        if moveRight and player.right < ancho:
            player.right += MOVESPEED
        if moveLeft and player.left > 30:
            player.left -= MOVESPEED


        # creating the player inside the surface
        pygame.draw.rect(lienzo,(colorSugar[1]),player)

        #interection if collision
        for en in enemy[:]:
            if player.colliderect(en):
                sound.play()
                enemy.remove(en)

        # draw the enemies
        for i in range(len(enemy)):
            pygame.draw.rect(lienzo, colorSugar[3], enemy[i])


        # score system
        drawText('BEST GAME EVER!!',FONT,lienzo,ancho/2,20,(0,0,0))
        drawText('CURRENT SCORE: ' + str(20-len(enemy)),FONT,lienzo,ancho/2, 40,(0,0,0))
        drawText('Best time: '+ str(topScore),FONT,lienzo,110,20,(0,0,0))
        drawText('Time: '+ str(score),FONT,lienzo,90,40,(0,0,0))

        # victory condition
        if len(enemy) <= 0:
            if score > topScore:
                topScore = score
            gameLoop = False

        #updating the screen
        pygame.display.update()
        clock.tick(60)

    # gameover screen
    pygame.mixer.music.stop()
    playSong(musiclist[-1],.4,0)
    drawText('GAME OVER!!',FONT,lienzo,ancho/2,150,(0,0,0))
    drawText('PRESS ANY KEY TO RESTART',FONT,lienzo,ancho/2,200,(0,0,0))
    pygame.display.update()
    waitForPlayerToPressKey()
    pygame.mixer.music.stop()

