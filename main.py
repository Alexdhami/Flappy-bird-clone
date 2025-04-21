import pygame
from random import randint
pygame.init()
CLOCK = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
SCORE = 0
SEC = pygame.time.get_ticks()

class Flappy(pygame.sprite.Sprite):
    def __init__(self,screen,width,height):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.x = 80
        self.y = self.height/2

        self.birds = []
        
        for i in range(1,4):
            self.birds.append(pygame.image.load(f'bird{i}.png').convert_alpha())
        self.current_bird = 0
        self.image = self.birds[int(self.current_bird)]
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.mask = pygame.mask.from_surface(self.image)

        self.bird_gravity = -10
        self.velocity = 0.4

    def update(self):
        self.current_bird += 0.15
        if self.current_bird >2:
            self.current_bird = 0
        self.x +=2                                
        if self.x >=self.width/2:
            self.x =self.width/2

        self.image = self.birds[int(self.current_bird)]
        self.rect = self.image.get_rect(center = (self.x,self.y))

        #we are updating the mask because we are animating the bird each bird has different mask, if we don't update the mask then it will use only first image's mask 
        self.mask = pygame.mask.from_surface(self.image)

    def gravity(self):
        self.bird_gravity += self.velocity
        self.y += self.bird_gravity
        self.rect = self.image.get_rect(center = (self.x,self.y))
    
    def jump(self):
        self.bird_gravity = -7
        # self.rect = self.image.get_rect(center = (self.x,self.y))

    def ground_collision(self):
        global game_running
        if self.rect.y >= self.width - 550  or self.rect.y <= 0:
            game_running = False

    

class Pillars(pygame.sprite.Sprite):
    def __init__(self,screen,width,height):
        super().__init__()
        self.x = 1300
        self.y = randint(150,500)
        self.speed = 6
        self.images = []

        self.images.append(pygame.image.load('green_pillar.png'))
        self.images.append(pygame.image.load('red_pillar.png'))
        
        self.current_image = randint(0,1)
        
        self.image = self.images[self.current_image]
        self.wid,self.hei = self.image.get_size()
        
        self.image = pygame.transform.scale(self.image,(self.wid//2,self.hei//2)).convert_alpha()
        self.rect = self.image.get_rect(center =(self.x,self.y))
        self.mask = pygame.mask.from_surface(self.image)


    def collision(self,bird_rect,bird_mask):
        offset = (self.rect.x - bird_rect.x,self.rect.y - bird_rect.y)
        collisionpoint = bird_mask.overlap(self.mask,offset)
        return collisionpoint

    def update(self):
        self.rect.x -= self.speed

        # we didn't update the mask because we are not animating the pillars
        # self.mask = pygame.mask.from_surface(self.image)

        
pygame.mouse.set_visible(False)
flappy = Flappy(SCREEN,WIDTH,HEIGHT)
flappy_group = pygame.sprite.Group()
flappy_group.add(flappy)
    
pillar_group = pygame.sprite.Group()
last_time = pygame.time.get_ticks()
spawn_interval = 1000

bg_image = pygame.transform.scale(pygame.image.load('background.jpg'),(WIDTH,HEIGHT+65))
ground_image = pygame.transform.scale(pygame.image.load('ground.png'),(WIDTH+WIDTH,HEIGHT))
ground_image_rect = ground_image.get_rect()

main_menu_mage = pygame.transform.scale(pygame.image.load('main_menu.png'),(WIDTH,HEIGHT))

ground_speed = 6
def update_ground():
    global ground_image_rect
    ground_image_rect.x -= ground_speed
    
    if ground_image_rect.x <= -WIDTH:
        ground_image_rect.x = 0
def font_work():
    pillar_passed = False
    global SCORE,SEC,secc
    font = pygame.font.Font('Pixeltype.ttf',50)
    
    SCORE = (pygame.time.get_ticks() - SEC)//1000

    font_surf = font.render(f'Score: {SCORE}',False,'blue')
    font_rect = font_surf.get_rect(center = (WIDTH//2,30))
    SCREEN.blit(font_surf,font_rect)

game_running = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


        if game_running == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                    flappy.x = 80
                    flappy.y = HEIGHT/2
                    flappy.bird_gravity = -10
                    SCORE = 0
                    SEC = pygame.time.get_ticks()

                    pillar_group.empty()

                    # for pillar in pillar_group:
                    #     pillar_group.remove(pillar)

                    
                    

        if game_running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flappy.jump()

    if game_running:
            SCREEN.blit(bg_image,(0,0))
        
            new_time = pygame.time.get_ticks()
        

            if new_time - last_time > spawn_interval:
                pillar = Pillars(SCREEN,WIDTH,HEIGHT)
                pillar_group.add(pillar)
                last_time = new_time
        
            flappy.gravity()
        
            flappy_group.update()
            flappy_group.draw(SCREEN)
        
            pillar_group.update()
            pillar_group.draw(SCREEN)
            SCREEN.blit(ground_image,ground_image_rect)
            update_ground()
        
        
            for pillar in pillar_group:
                if pillar.collision(flappy.rect,flappy.mask):
                    print('colliusion')
                    game_running = False
            font_work()
            flappy.ground_collision()
            
    else:
        SCREEN.blit(main_menu_mage,(0,0))
        
    pygame.display.update()
    CLOCK.tick(60)