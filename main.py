import pygame as pg
from pygame.math import Vector2
from Player import Player

def process_keys(keys, player):
    if keys[pg.K_w]:
        player.pos.y -= player.movementSpeed
    if keys[pg.K_a]:
        player.pos.x -= player.movementSpeed
    if keys[pg.K_s]:
        player.pos.y += player.movementSpeed
    if keys[pg.K_d]:
        player.pos.x += player.movementSpeed
        
def process_mouse(mouse, player):
    if mouse[0]:
        player.shoot(pg.mouse.get_pos())


def main():
    screen = pg.display.set_mode((800, 800))
    clock = pg.time.Clock()
    player = Player((400, 400))
    all_sprites = pg.sprite.Group(player)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        keys = pg.key.get_pressed()
        mouse = pg.mouse.get_pressed()
        currentTime = pg.time.get_ticks()


        
        process_mouse(mouse, player)
        process_keys(keys, player)
        all_sprites.update()
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pg.draw.circle(screen, (255, 128, 0), [int(i) for i in player.pos], 3)
        pg.draw.rect(screen, (255, 128, 0), player.rect, 2)
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()