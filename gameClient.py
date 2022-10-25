import socket
import pygame
import random
import math
from pygame.locals import *
host = "192.168.1.106"
port = 1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Weird Game")
move = 0
red = ((255,0,0))
x=0
y=0
black = (0,0,0)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
class Player():
    def __init__(self,color):
        self.x=WIDTH//2-30
        self.y=HEIGHT//2
        self.color = color
        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0
        self.lives = 3
        self.bullet_list = []
    def draw(self):
        pygame.draw.rect(window,self.color,(self.x,self.y,20,20))
        if self.right==1 and self.x<480:
            self.x=self.x+2
        if self.left==1 and self.x>0:
            self.x=self.x-2
        if self.up==1 and self.y>0:
            self.y=self.y-2
        if self.down == 1 and self.y<480:
            self.y = self.y+2

        for bullet in self.bullet_list:
            pygame.draw.rect(window,red,bullet + [5,10])
            bullet[1] -= 10
            if bullet[1]==0:
                self.bullet_list.remove(bullet)
            if bullet[0] in range(x,x+100) and bullet[1] in range(y,y+70):
                self.bullet_list.remove(bullet)
                
    def move(self,event):
        if event.type==KEYDOWN:
            if event.key==K_RIGHT or event.key==K_d:
                self.right=1
            if event.key==K_LEFT or event.key==K_a:
                self.left=1
            if event.key==K_UP or event.key==K_w:
                self.up=1
            if event.key==K_DOWN or event.key==K_s:
                self.down=1
            if event.key==K_SPACE:
               self.bullet_list.append([self.x+40, self.y])
               
        elif event.type==KEYUP:
            if event.key==K_RIGHT or event.key==K_d:
                self.right=0
            if event.key==K_LEFT or event.key==K_a:
                self.left=0
            if event.key==K_UP or event.key==K_w:
                self.up=0
            if event.key==K_DOWN or event.key==K_s:
                self.down=0
            if event.key==K_SPACE:
                bullet=False

player1=Player((255,0,0))
player2=Player((0,255,255))
circles = []
food = []
xypos = s.recv(1024).decode('utf-8')   
xypos = s.recv(1024).decode('utf-8')   
xypos = xypos.split()
for i in range(0,30,2):
    cx,cy = int(xypos[i]),int(xypos[i+1])
    circles.append([cx,cy])

#COLLISION TESTING CODE
    #rectangle & circle
kx = -5
ky = -5 
def checkeat(co):
    testx = co[0]
    testy = co[1]
    if co[0]<player2.x:
        testx = player2.x
    elif co[0]>player2.x+20:
        testx = player2.x+20
    if co[1]<player2.y:
        testy = player2.y
    elif co[1]>player2.y+20:
        testy = player2.y+20
    distx = co[0]-testx
    disty = co[1]-testy
    dist = math.sqrt((distx*distx)+(disty*disty))
    if dist<=7:
        return True
    else:
        return False
while True:
    window.fill((255,255,255))
    s.sendall(bytes("{} {}\n".format(player2.x,player2.y),"utf-8"))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        player2.move(event)
    data = s.recv(1024).decode('utf-8')
    data=data.split()
    player1.x , player1.y =int(data[0]),int(data[1])
    player1.draw()
    player2.draw()
    for co in circles:
        pygame.draw.circle(window,black,co,7)
        if checkeat(co)==True:
            circles.remove(co)
            kx,ky = co[0],co[1]
    if kx!=5 and ky!=5:
        s.send(bytes("{} {}\n".format(kx,ky),"utf-8"))
    eaten = (s.recv(1024).decode('utf-8')).split()
    bx,by= int(eaten[0]),int(eaten[1])
    if [bx,by] in circles:
        circles.remove([bx,by])
    pygame.display.update()
s.close()

