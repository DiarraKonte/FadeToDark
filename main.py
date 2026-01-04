import pygame

pygame.init()
screen = pygame.display.set_mode((384, 384))
SCALE = 2
screen = pygame.display.set_mode((384 * SCALE, 384 * SCALE))
clock = pygame.time.Clock()

player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (player_img.get_width() * SCALE, player_img.get_height() * SCALE))
room1 = pygame.image.load("assets/room1.png")
room1 = pygame.transform.scale(room1, (room1.get_width() * SCALE, room1.get_height() * SCALE))

player_x = 100
player_y = 100
player_width = player_img.get_width()
player_height = player_img.get_height()


vitesse = 4

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= vitesse
    if keys[pygame.K_RIGHT]:
        player_x += vitesse
    if keys[pygame.K_UP]:
        player_y -= vitesse
    if keys[pygame.K_DOWN]:
        player_y += vitesse
    
    clock.tick(60)

    screen.blit(room1, (0, 0))                    # Dessine le fond
    screen.blit(player_img, (player_x, player_y)) # Dessine le joueur
    pygame.display.update()   
