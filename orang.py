import pygame

window = pygame.display.set_mode((1280, 720))
running = True
orange = pygame.transform.scale(pygame.image.load('AMOGUS.png'),(300,300))

x = 0
y = 0

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    window.fill((0,0,0))
    window.blit(orange,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

if pygame.key.get_pressed()[pygame.K_LEFT]:
    x -= 2
if pygame.key.get_pressed()[pygame.K_RIGHT]:
    x += 2
if pygame.key.get_pressed()[pygame.K_UP]:
    y -= 2
if pygame.key.get_pressed()[pygame.K_DOWN]:
    y += 2
pygame.display.update()