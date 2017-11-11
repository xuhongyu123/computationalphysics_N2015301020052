import win32api, win32gui  
ct = win32api.GetConsoleTitle()  
hd = win32gui.FindWindow(0,ct)  
win32gui.ShowWindow(hd,0)  

import pygame, sys
from pygame.locals import *
from random import randint

class ETK(object):
    def __init__(self):
        self.pos_x = 800
        self.pos_y = 318
        self.speed = 5
        self.active = False
        self.blood = randint(100,200)
        self.oblood = self.blood
    def move(self):
        self.speed = randint(10,15)
        if self.active and self.pos_x > 0:
            self.pos_x -= self.speed
        else:
            self.pos_x = 0
            self.active = False
    def reset(self):
        self.active = True
        self.pos_x = 800
        self.blood = 100
    def attack(self):
        self.blood -= 50 - randint(0,30)
        
class Bomb(object):
    def __init__(self,x,y):
        self.pos_x = x+100
        self.pos_y = y+20
    def move(self):
        self.pos_x += 20
        if self.pos_x > 800:
            self.pos_x = 800


pygame.init()

main = pygame.display.set_mode((800,460))
pygame.display.set_caption('PyTank v0.1')

bg = pygame.image.load('bg.jpg').convert_alpha()
tk = pygame.image.load('tk.png').convert_alpha()
etk = pygame.image.load('etk.png').convert_alpha()
pygame.display.set_icon(tk)
grass = pygame.image.load('grass.png').convert_alpha()
bomb = pygame.image.load('bomb.png').convert_alpha()
boom = pygame.image.load('boom.png').convert_alpha()
text = pygame.font.SysFont("arial", 36)


running = True
FPS = 50
x,y = 107,316
etks = []
bombs = []
miss = 0
score  = 0
r = 0
while running:
    r += 1
    if r%100 == 0:
        FPS -= 1
    main.blit(bg,(0,0))
    main.blit(text.render('Welcome to play tank game! Your score: %d!' % score, True, (248, 0, 248)), (10,20))
    main.blit(text.render('You missed %d tanks' % miss, True, (248, 248, 0)), (10,50))
    if miss >= 5:
        running = False
        FPS = 50
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                x += 5
            if event.key == K_a:
                x -= 5
            if event.key == K_j:
                bb = Bomb(x,y)
                bombs.append(bb)
    if len(etks) == 0:
        enemy = ETK()
        enemy.reset()
        etks.append(enemy)
    elif len(etks) < 5 and etks[-1].pos_x < 600:
        enemy = ETK()
        enemy.reset()
        etks.append(enemy)
    for e in etks:
        e.move()
        if e.pos_x <= 0 or e.blood <= 0:
            if e.pos_x <= 0:
                miss += 1
            if e.blood <= 0:
                score += e.oblood
            etks.remove(e)
        main.blit(etk,(e.pos_x,e.pos_y))
    for b in bombs:
        b.move()
        if b.pos_x >= 800:
            bombs.remove(b)
        for e in etks:
            if e.pos_x < b.pos_x < e.pos_x + 100:
                main.blit(boom,(b.pos_x,b.pos_y))
                bombs.remove(b)
                e.attack()
        main.blit(bomb,(b.pos_x,b.pos_y))
    main.blit(tk,(x,y))
    for i in range(0,800,65):
        main.blit(grass,(i,406))
    pygame.display.update()
    pygame.time.delay(FPS)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main.blit(bg,(0,0))
    main.blit(text.render('Your score: %d!' % score, True, (248, 0, 248)), (350,20))
    main.blit(text.render('You Lose!', True, (248, 0, 0)), (380,100))
    pygame.display.update()
    pygame.time.delay(FPS)
