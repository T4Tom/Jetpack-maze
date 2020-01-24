import pygame, time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


red = (255, 0, 0)
green = (0, 255, 0)


characterImg = pygame.image.load('character.png')
characterImg = pygame.transform.scale(characterImg, (120, 140))
characterw = 120
characterh = 120

startfont = pygame.font.SysFont(None, 90)
starttext = startfont.render('Maze Game!', True, (0, 0, 0))
starttextRect = starttext.get_rect()
starttextRect.center = (400, 300)

startfont2 = pygame.font.SysFont(None, 50)
starttext2 = startfont2.render('Avoid the red, get to the green!', True, (0, 0, 0))
starttextRect2 = starttext2.get_rect()
starttextRect2.center = (400, 400)

wintext = startfont.render('YOU WIN!', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (400, 300)


levelfont = pygame.font.SysFont(None, 50)


screen.fill((0, 0, 255))
screen.blit(starttext, starttextRect)
screen.blit(starttext2, starttextRect2)
pygame.display.flip()
time.sleep(2)

def dead():
  screen.fill(red)
  pygame.display.flip()
  time.sleep(2)
  game_loop()

def win():
  screen.fill(green)
  screen.blit(wintext, (wintextRect))
  pygame.display.flip()
  time.sleep(2)
  exit()
 
def border():
  pygame.draw.rect(screen, (red), pygame.Rect(0, 0, 800, 50))
  pygame.draw.rect(screen, (red), pygame.Rect(0, 550, 800, 50))

def game_loop():

  level1 = True
  level2 = False
  level3 = False

  x = 20
  y = 400

  levelNum = 1



  done = False
  while not done:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
      y -= 3
    if pressed[pygame.K_DOWN]:
      y += 3
    if pressed[pygame.K_RIGHT] and x + characterw <= 800:
      x += 3
    if pressed[pygame.K_LEFT] and x >= 0:
      x -= 3

    leveltext = levelfont.render('Level: {0}'.format(levelNum), True, (0, 0, 0))
    leveltextRect = leveltext.get_rect()
    leveltextRect.center = (80, 30)


    if y < 50 or y + characterh > 550:
      dead()


    if level1:
      levelNum = 1
      border()

      pygame.draw.rect(screen, (red), pygame.Rect(150, 220, 50, 400))
      pygame.draw.rect(screen, (red), pygame.Rect(350, 0, 50, 380))
      pygame.draw.rect(screen, (red), pygame.Rect(550, 220, 50, 400))

      pygame.draw.rect(screen, (green), pygame.Rect(600, 350, 200, 200))

      if y + characterh >= 220 and x <= 180 and x + characterw >= 170:
        dead()
      if y <= 380 and x <= 380 and x + characterw >= 370:
        dead()
      if y + characterh >= 220 and x <= 580 and x + characterw >= 570:
        dead()

      if x > 550 and y >= 350:
        time.sleep(2)
        x = 30
        y = 80
        level1 = False
        level2 = True

    
    if level2:
      levelNum = 2
      border()

      pygame.draw.rect(screen, (red), pygame.Rect(180, 0, 50, 380))
      pygame.draw.rect(screen, (red), pygame.Rect(180, 350, 400, 50))
      pygame.draw.rect(screen, (red), pygame.Rect(530, 200, 50, 150))

      pygame.draw.rect(screen, (green), pygame.Rect(230, 200, 300, 150))

      if y <= 380 and x <= 220 and x + characterw >= 210:
        dead()
      if y + characterh >= 350 and y <= 400 and x + characterw >= 210 and x <= 570:
        dead()
      if y + characterh >= 200 and y <= 350 and x + characterw >= 560 and x <= 570:
        dead()
   
      if y > 200 and x > 230 and y + characterh < 350 and x + characterw < 530:
        time.sleep(2)
        x = 650
        y = 100
        level2 = False
        level3 = True
    
    if level3:
      win()

    screen.blit(characterImg, (x, y))
    screen.blit(leveltext, leveltextRect)

    pygame.display.flip()
    clock.tick(70)

game_loop()
