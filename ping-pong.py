from pygame import *

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

font.init()
font1 = font.SysFont('Arial', 80)
lose1 = font1.render('PLAYER1 WIN!',True,(255,255,255))
lose2 = font1.render('PLAYER2 LOSE!',True,(255,255,255))

back = (100, 255, 255) #цвет фона
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

racket1 = Player('racket.png',30,200,4,50,150)
racket2 = Player('racket.png',520,200,4,50,150)
ball = GameSprite('tenis_ball.png',200,200,4,50,50)

game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)

        racket1.update_r()
        racket2.update_l()

        racket1.reset()
        racket2.reset()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1
                
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1

    if ball.rect.x > win_width:
        window.blit(lose1,(90,10))
    elif ball.rect.x < 0:
        window.blit(lose2,(80,10))

    display.update()
    time.delay(20)