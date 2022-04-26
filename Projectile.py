import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, source, target, speed, lifetime, color):
        super().__init__()
        self.image = pg.Surface([4, 4])
        self.image.set_colorkey(pg.Color('red'))
        self.rect = self.image.get_rect(x=source[0], y=source[1])
        pg.draw.circle(self.image, color,
                           (self.rect.width // 2, self.rect.height // 2),
                           self.rect.width // 2)
        
        self.pos = [source[0], source[1]]
        self.movementVector = [target[0], target[1]]
        self.speed = speed
        self.lifetime = lifetime
        self.createdAt = pg.time.get_ticks()
        
    def move(self, surfaceSize, tDelta):
        if pg.time.get_ticks() > self.createdAt + self.lifetime:
            self.kill()
        self.pos[0] += self.movementVector[0] * self.speed * tDelta
        self.pos[1] += self.movementVector[1] * self.speed * tDelta
        self.rect.topleft = self.pos
        if self.pos[0] > surfaceSize[0] or self.pos[0] < 0  or \
           self.pos[1] > surfaceSize[1] or self.pos[1] < 0:
            self.kill()
    def render(self, surface):
        surface.blit(self.image, self.pos)
