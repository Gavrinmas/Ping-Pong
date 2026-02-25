from pygame import *

mixer.init()
w = 700
h = 500


clock = time.Clock()
font.init()
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
    
speed_x = 3
speed_y = 3


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
        
    def update_w(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed
finish = False        
p = Player('AND_THIS.png', 30, 200, 5, 50, 150)
p2 = Player('THGIS.png', 620, 200, 5, 50, 150)
b = GameSprite('ball.png', 200, 200, 7,  50, 50)
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        p.reset()
        p2.reset()
        b.reset()
        p.update()
        p2.update_w()
        b.rect.x += speed_x
        b.rect.y += speed_y
        if sprite.collide_rect(p, b) or sprite.collide_rect(p2, b):
            speed_x *= -1
        if b.rect.y < 0 or b.rect.y > 450:
            speed_y *= -1
        if b.rect.x < 0:
            qw = font.Font(None, 40).render('PLAYER1 LOSE!', True, (255, 0, 0))
            window.blit(qw, (200, 200))
            finish = True
        if b.rect.x > 650:
            q = font.Font(None, 40).render('PLAYER2 LOSE!', True, (255, 0, 0)) 
            window.blit(q, (200, 200))
            finish = True
    display.update()
    clock.tick(60)




    