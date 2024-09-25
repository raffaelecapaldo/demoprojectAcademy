# Example file showing a basic pygame "game loop"
import pygame
import sys

# pygame setup
pygame.init()
pygame.display.set_caption('Esercizio immagini')
sfondo = pygame.image.load("images/icona.jpg")
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
background = pygame.image.load("images/persona5sfondo.jpg") #carico sfondo
hero = pygame.image.load("images/p5hero.png")

font = pygame.font.Font("fonts/Roboto-Light.ttf", 90)
myText = font.render("BENVENUTO IN PERSONA5", True, "red")

pygame.display.set_icon(sfondo)

clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hai cliccato fra")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            print("Hai premuto tastiera fra")

    screen.blit(background, (0,0)) #inserisco background
    screen.blit(hero, (300, 100)) #inserisco personaggio


    screen.blit(myText, (400,800))


    clock.tick(60)  
    pygame.display.update()

pygame.quit()
