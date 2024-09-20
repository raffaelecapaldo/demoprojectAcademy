# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption('Gioco Raffa')
sfondo = pygame.image.load("icona.jpg")
screen = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()