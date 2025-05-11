from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    
    def updater(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    
playerr = Player('', 620, 200, 5, 50, 200)
playerl = Player('', 30, 200, 5, 50, 200)

win_width, win_height = 700, 500 # создаем окно приложения
window = display.set_mode((win_width, win_height))

display.set_caption('PingPong')
background = transform.scale(image.load(''), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
fps = 60

ball = GameSprite('', 200, 200, 5, 50, 50)

speed_x = ball.speed
speed_y = ball.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:  
        window.blit(background, (0, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        playerr.updater()
        playerl.updatel()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(playerl, ball) or sprite.collide_rect(playerr, ball):
            speed_x *= -1
        
        playerr.reset()
        playerl.reset()
        ball.reset() 

    display.update()
    clock.tick(fps)

    
