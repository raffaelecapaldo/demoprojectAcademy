import pygame
pygame.init()

clock = pygame.time.Clock()
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Gioco Demo')

running = True



while running:
    rgbColor = (255,255,255)
    screen.fill(rgbColor)
    pygame.draw.circle(screen, (0,0,0), (400,300), 5)
    pygame.draw.rect(screen, (127,0,255), (100,50, 40,20), 2)
    pygame.draw.line(screen, "black", (100,400), (700,400), 5)
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hai cliccato fra")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            print("Hai premuto tastiera fra")
    




