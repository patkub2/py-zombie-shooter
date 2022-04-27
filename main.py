import pygame as pg
from Player import Player
import random
import math

pg.init()
size    = (800, 600)
BGCOLOR = (0, 0, 0)
screen = pg.display.set_mode(size)
scoreFont = pg.font.Font("fonts/UpheavalPro.ttf", 30)
healthFont = pg.font.Font("fonts/OmnicSans.ttf", 50)
healthRender = healthFont.render('z', True, pg.Color('red'))
pg.display.set_caption("Top Down")

def process_keys(keys, player):
    if keys[pg.K_w]:
        player.pos.y -= player.movementSpeed
    if keys[pg.K_a]:
        player.pos.x -= player.movementSpeed
    if keys[pg.K_s]:
        player.pos.y += player.movementSpeed
    if keys[pg.K_d]:
        player.pos.x += player.movementSpeed
        
def process_mouse(mouse, hero):
    if mouse[0]:
        hero.shoot(pg.mouse.get_pos())

def render_entities(hero):
    hero.render(screen)
    for proj in Player.projectiles:
        proj.render(screen)
   
    
def main():
    screen = pg.display.set_mode((800, 800))
    clock = pg.time.Clock()
    player = Player((400, 400))
    hero = pg.sprite.Group(player)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        keys = pg.key.get_pressed()
        mouse = pg.mouse.get_pressed()
        currentTime = pg.time.get_ticks()


        
        process_mouse(mouse, player)
        process_keys(keys, player)
        hero.update()
        screen.fill((30, 30, 30))
        hero.draw(screen)
        pg.draw.circle(screen, (255, 128, 0), [int(i) for i in player.pos], 3)
        pg.draw.rect(screen, (255, 128, 0), player.rect, 2)
        render_entities(player)
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()