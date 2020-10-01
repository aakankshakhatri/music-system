import pygame
import os
os.getcwd()

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
x=pygame.mixer.Sound("/home/aakankshakhatri/Facial-Expression-Detection-master(2)/nick jonas - jealous.mp3")
clock=pygame.time,Clock()
x.play()
while True:
	clock.tick(60)
pygame.quit()
 



