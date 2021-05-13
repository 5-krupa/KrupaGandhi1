# Mother's day special project
import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('xxx.mp3')
pygame.mixer.music.play()
sleep(10)
image = pygame.image.load("xxx.png")
window.blit(image, (0, 0))
pygame.mixer.music.load('xxx.mp3')
pygame.mixer.music.play()
pygame.display.update()
sleep(11)
