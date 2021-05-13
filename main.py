# Mother's day special project
import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# sleep(5)
pygame.mixer.init()
pygame.mixer.music.load('AISA KYUN MAA Lyrical NEERJA Sonam Kapoor Prasoon Joshi T-Series.mp3')
pygame.mixer.music.play()
sleep(10)
image = pygame.image.load("modern-happy-mother-s-day-floral-background_1361-1241.png")
window.blit(image, (0, 0))
pygame.mixer.music.load('Meri Pyaari Ammi - Secret Superstar Zaira Wasim Aamir Khan Amit Trivedi Kausar Meghna.mp3')
pygame.mixer.music.play()
pygame.display.update()
sleep(11)