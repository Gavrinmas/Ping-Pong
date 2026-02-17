from pygame import *

mixer.init()
w = 700
h = 500


clock = time.Clock()

window = display.set_mode((w, h))

window.fill((200, 255, 255))



game = True


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False




    display.update()
    clock.tick(60)