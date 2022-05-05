import pygame
import random
import math

pygame.init()
 
screen = pygame.display.set_mode((800,600))

#background
background=pygame.image.load('bk.png')

#title and icon
pygame.display.set_caption("Game made by NPS")
icon = pygame.image.load('anh1.png')
pygame.display.set_icon(icon)

# player
objectImg = pygame.image.load('phi thuyen.png')
objectX=370
objectY=480
objectX_change=0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

number_enemies = 10
for i in range (number_enemies):
    enemyImg.append(pygame.image.load('monster.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint (0,0))
    enemyX_change.append(2)
    enemyY_change.append(25)



#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY= 480
bulletX_change=0
bulletY_change=5
bullet_state="ready"

#crossbar
crbImg = []
crbX = []
crbY = []
number_cross = 34
for i in range (number_cross):
    crbImg.append(pygame.image.load('minus.png'))
    crbX.append(0)
    crbY.append(400)


score = 0
font = pygame.font.Font('freesansbold.ttf',20)

over_font = pygame.font.Font('freesansbold.ttf',64)

textX = 10
textY = 10

def show_crb (x,y):
    screen.blit(crbImg[i],(x,y))

def show_score (x,y):
    score_value = font.render("Score: "+ str(score),True,(0,255,0))
    screen.blit(score_value,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(0,255,0))
    screen.blit(over_text,(200,250))

def object( x,y):
    screen.blit(objectImg,(x,y))

def enemy (x,y,i):
    screen.blit(enemyImg[i],(x,y))

def bullet (x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision (objectX, objectY, bulletX, bulletY):
    distance = math.sqrt(math.pow(objectX-bulletX,2)+math.pow(objectY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False


running  = True
while running:

    #background
    screen.fill((24,10,10))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #handling obj
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                objectX_change = -0.8
                
            if event.key==pygame.K_RIGHT:
                objectX_change = 0.8

            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX=objectX
                    bullet(bulletX, bulletY)
               
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                objectX_change = 0
        
       

    
    # boundary of objects
    #space  
    objectX +=objectX_change

    if objectX <= 0:
        objectX=0
    elif objectX >=736:
        objectX = 736

    for i in range (number_enemies):

        #game over 
          #game over
        if enemyY[i]>350:
            for j in range (number_enemies):
                enemyY[j]=2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i]=2
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i]=-2
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score+=1
            #print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i]= random.randint (0,0)
        enemy(enemyX[i],enemyY[i],i)
    
    for i in range (number_cross):
        crbX[i] =400
        crbY[i] = 400
        show_crb(crbX[i], crbY[i])

    #bullet handling
    if bulletY <=0:
        bulletY=480
        bullet_state = "ready"
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    object(objectX, objectY)

    show_score(textX,textY)


    pygame.display.update() 