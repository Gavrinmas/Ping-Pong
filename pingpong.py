from pygame import *

mixer.init()
w = 700
h = 500


clock = time.Clock()

window = display.set_mode((w, h))
background = (200, 255, 255)
window.fill(background)



game = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_w(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
p = Player('AND_THIS.png', 30, 200, 5, 50, 150)
p2 = Player('THGIS.png', 620, 200, 5, 50, 150)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    window.fill(background)
    p.reset()
    p2.reset()
    p.update()
    p2.update_w()

    display.update()
    clock.tick(60)