import pygame
pygame.init()

clock = pygame.time.Clock()
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Faccia esercizio')

gatto = pygame.image.load('images/gatto.jpg')
gattoRidimensionato = pygame.transform.scale(gatto, (200,200))

running = True



while running:
    rgbColor = (255,255,255)
    screen.fill(rgbColor)
    pygame.draw.circle(screen, (0,0,0), (400,300), 120, 2) # Contorno faccione
   # pygame.draw.rect(screen, (127,0,255), (100,50, 40,20), 2) 
   # pygame.draw.line(screen, "black", (100,400), (700,400), 5)
    pygame.draw.circle(screen, (0,0,0), (340,250), 28, 2) # occhio sinistro
    pygame.draw.circle(screen, (0,0,0), (460,250), 28, 2) # occhio destro
    pygame.draw.line(screen, (0,0,0), (400,270), (400,330), 2)  # naso
    pygame.draw.rect(screen, (0,0,0), (350,360, 100, 20), 2)   # bocca
    screen.blit(gattoRidimensionato, (10,10))
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
    




