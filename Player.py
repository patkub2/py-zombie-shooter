import pygame as pg
from pygame.math import Vector2
import Weapon

class Player(pg.sprite.Sprite):
    projectiles = pg.sprite.Group()
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load('player.png')
        # A reference to the original image to preserve the quality.
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)  # The original center position/pivot point.
        self.offset = Vector2(0,0)  # We shift the sprite 50 px to the right.
        self.angle = 0
        self.movementSpeed = 5
        self.availableWeapons = [Weapon.Pistol()]


        
        self.equippedWeapon = self.availableWeapons[0]

    def update(self):
        self.rotate()

    def rotate(self):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pg.transform.rotozoom(self.orig_image, -self.angle, 1)
        
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos)
        
        direction = pg.mouse.get_pos() - self.pos
        # .as_polar gives you the polar coordinates of the vector,
        # i.e. the radius (distance to the target) and the angle.
        radius, angle = direction.as_polar()
        # Rotate the image by the negative angle (y-axis in pygame is flipped).
        self.image = pg.transform.rotate(self.orig_image, -angle)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def shoot(self, mousePos):
        self.equippedWeapon.shoot(self, mousePos)
        
    def render(self, surface):
        surface.blit(self.image, self.rect)        
