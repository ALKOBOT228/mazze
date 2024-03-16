from pygame import *


win = display.set_mode((888,555))
display.set_caption('dogon')


mixer.init()
mixer.music.load('dd.mp3')
mixer.music.play()

# damage = mixer.Sound('puk-v-ekho.mp3')
# winn = mixer.Sound('hhhhh.mp3')

# so = mixer.Sound("C://Users//Algoritmika//Desktop//pr3//MOR.mp3")

game = True
class GameSprite(sprite.Sprite):
    def __init__(self , p_img , p_x , p_y ,p_spe, p_s_x , p_s_y ):
        super().__init__()
        self.image = transform.scale(image.load(p_img) , (p_s_x , p_s_y ))
        self.speed = p_spe
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        win.blit(self.image,(self.rect.x , self.rect.y))

class wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3, wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width , self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x , self.rect.y))
    pass


clock = time.Clock()

bg = GameSprite('red.jpg', 0, 0, 0, 1000, 900)
hero = GameSprite('росс.jpg', 200, 100, 5, 85 , 85)
hero2 = GameSprite('навальный.jpg', 300, 150, 5, 85 , 85)
w1 = wall(255,5,222,100,20,450,10)
w2 = wall(1,5,222,100,444,333,10)
w3 = wall(255,5,3,100,20,11,333)
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
     

#    keys_pressed = key.get_pressed()
 #  if key_pressed[K_UP]:
  #      so.play()
    
    bg.reset()
    hero.reset()
    hero2.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()  
    display.update()
    clock.tick(60)
