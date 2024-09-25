import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Esercizio Sprites')

counter = 0
TOCCATO_BORDO = pygame.USEREVENT + 1
counter = counter +1




class Personaggio(pygame.sprite.Sprite):

    # Constructor.
    def __init__(self, width, height, immagine):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
        #carico immagine
       self.image = pygame.image.load(immagine)
       self.image = pygame.transform.scale(self.image, (100,100))
       self.image = self.image.convert_alpha()
       #Rettangolo di posizione e collisione
       self.rect =  self.image.get_rect()

       self.rect.topleft = (width,height)
       self.vel_x = 0
       self.vel_y = 0

       self.mask = pygame.mask.from_surface(self.image)


       #aggiornamento Sprite

    def cambia_vel(self, x, y):
        self.vel_x += x
        self.vel_y += y


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.left  < 0 :
            self.rect.left = 0
            pygame.event.post(pygame.event.Event(TOCCATO_BORDO))
        if self.rect.right > 800:
            self.rect.right = 800
            pygame.event.post(pygame.event.Event(TOCCATO_BORDO))
        if self.rect.top < 0:
            self.rect.top = 0
            pygame.event.post(pygame.event.Event(TOCCATO_BORDO))
        if self.rect.bottom > 600:
            pygame.event.post(pygame.event.Event(TOCCATO_BORDO))
            self.rect.bottom = 600
            
        


#Istanzia mioPg, gruppo, e aggiungi PG al gruppo
mioPg = Personaggio(100,100, "images/man.png")
mioPg2 = Personaggio(500,500, "images/man.png")

gruppoPg = pygame.sprite.Group()
gruppoPg.add(mioPg, mioPg2)


running = True
FILL = "blue"
while running:
    screen.fill(FILL)

    if pygame.sprite.collide_mask(mioPg, mioPg2):
        screen.fill("red")

    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == TOCCATO_BORDO:
            if FILL == "blue":
                FILL = "black"
            elif FILL == "black":
                FILL = "blue"
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hai cliccato fra")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                mioPg.cambia_vel(-5, 0)
            if event.key == pygame.K_RIGHT:
                mioPg.cambia_vel(5, 0)
            if event.key == pygame.K_UP:
                mioPg.cambia_vel(0, -5)
            if event.key == pygame.K_DOWN:
                mioPg.cambia_vel(0, 5)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mioPg.cambia_vel(5, 0)
            if event.key == pygame.K_RIGHT:
                mioPg.cambia_vel(-5, 0)
            if event.key == pygame.K_UP:
                mioPg.cambia_vel(0, 5)
            if event.key == pygame.K_DOWN:
                mioPg.cambia_vel(0, -5)


            print("Hai premuto tastiera fra")


    gruppoPg.update()
    gruppoPg.draw(screen)
    clock.tick(60)  


    pygame.display.update()




pygame.quit()
    