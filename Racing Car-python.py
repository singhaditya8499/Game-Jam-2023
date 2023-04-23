#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pygame
import time
import random
import imutils
import numpy as np

bg = None
pygame.init()


# In[7]:


num = random.randrange(3)
num


# In[8]:


display_width=800
display_height=600
game_display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Earth Day 2023')
black=(0,0,0)
white=(255,255,255)
green=(0,150,0)
red=(150,0,0)
b_green=(0,255,0)
b_red=(255,0,0)
blue=(0,0,255)
earth_blue=(40,122,184)
clock=pygame.time.Clock()
carimg=pygame.image.load('./earth.png')
astroid=pygame.image.load('./astroid.png')


# In[9]:


def things_dodged(dodged):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged: "+str(dodged),True,white)
    game_display.blit(text,(0,0))
def car(x,y):
    game_display.blit(carimg,(x,y))
    
def things(tx,ty,tw,th,color):
    game_display.blit(astroid,(tx,ty))
    
def text_objects(text,fonts,color=black):
    text_surface=fonts.render(text,True,color)
    return text_surface,text_surface.get_rect()

def message_display(text):
    font=pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect=text_objects(text,font,white)
    textrect.center=((display_width/2,display_height/2))
    game_display.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
    intro()


# In[10]:


def intro():
    introo=True
    while introo:
        for event in pygame.event.get():
            #print event
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill((255,255,255))
        heading=pygame.font.Font('freesansbold.ttf',60)
        textsurf,textrec=text_objects("Earth goes wooshh..",heading)
        textrec.center=((display_width/2,display_height/2))
        game_display.blit(textsurf,textrec)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
#         print(click)
        if 150+100>mouse[0]>150 and 450+50>mouse[1]>450:
            pygame.draw.rect(game_display, green,(150,450,100,50))
            if click[0]==1:
                games()
        else:
            pygame.draw.rect(game_display, b_green,(150,450,100,50))
            
        if 550+100>mouse[0]>550 and 450+50>mouse[1]>450:
            pygame.draw.rect(game_display, red,(550,450,100,50))
            if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(game_display, b_red,(550,450,100,50))
            
        menu_text=pygame.font.Font('freesansbold.ttf',20)
        textsurf,textrec=text_objects("Go!!",menu_text)
        textrec.center=((150+100/2,450+50/2))
        game_display.blit(textsurf,textrec)
        textsurf,textrec=text_objects("Quit",menu_text)
        textrec.center=((550+100/2,450+50/2))
        game_display.blit(textsurf,textrec)
        pygame.display.update()
        clock.tick(15)


# In[11]:


def games():
    crashed=False
    dodged=0
    x=display_width*.45
    y=display_height*.80
    t_x=random.randrange(0,display_width)
    t_y=-100
    t_h=38
    t_w=60
    t_sp=4
    i=0
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    i=-9
                if event.key==pygame.K_RIGHT:
                    i=9
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    i=0
        game_display.fill(black)
        things(t_x,t_y,t_w,t_h,white)
        t_y=t_y+t_sp
        x=x+i
        car(x,y)
        things_dodged(dodged)
        if x>display_width-90 or x<0:
            message_display('Dont leave the space, literally!!')
            time.sleep(10)

        if t_y>display_height:
            t_y=-100
            t_x=random.randrange(0,display_width)
            t_sp+=0.8
            dodged+=1
            #t_w=t_w+(1.08*dodged)

        if y<t_y+t_h:
            if x>t_x and x<t_x+t_w or x+20<t_x+t_w and x+20>t_x:
                message_display('You crashed the earth, good that you can respawn :)')
                time.sleep(10)

        pygame.display.update()
        clock.tick(60)

intro()
games()
pygame.quit()
quit()


# In[1]:


pygame.quit()
quit()


# In[ ]:




