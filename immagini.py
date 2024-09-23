# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption('Esercizio immagini')
sfondo = pygame.image.load("images/icona.jpg")
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
background = pygame.image.load("images/persona5sfondo.jpg") #carico sfondo
hero = pygame.image.load("images/p5hero.png")

pygame.display.set_icon(sfondo)

clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hai cliccato fra")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            print("Hai premuto tastiera fra")

    screen.blit(background, (0,0)) #inserisco background
    screen.blit(hero, (300, 100)) #inserisco personaggio
    pygame.display.update()


    clock.tick(60)  

pygame.quit()
