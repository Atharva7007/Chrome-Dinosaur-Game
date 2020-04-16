import random
import pygame
from pygame.locals import *

pygame.init()

class Dino():
    def __init__(self):
        self.Img = pygame.image.load("dino_.png")
        self.WIDTH, self.HEIGHT = 44, 48
        self.Img = pygame.transform.scale(self.Img, (self.WIDTH, self.HEIGHT))
        self.image = self.Img
        self.x = 20
        self.y = 170
        self.g = -0.25 # Gravity
        self.up = 7 # Initial upward velocity
        self.t = 0 # time
        self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5)

        self.runImg1 = pygame.image.load("dino_1.png")
        self.runImg2 = pygame.image.load("dino_2.png")
        self.runImg1 = pygame.transform.scale(self.runImg1, (self.WIDTH, self.HEIGHT))
        self.runImg2 = pygame.transform.scale(self.runImg2, (self.WIDTH, self.HEIGHT))

        self.duck1 = pygame.image.load("dino_ducking1.png")
        self.duck2 = pygame.image.load("dino_ducking2.png")
        self.duck1 = pygame.transform.scale(self.duck1, (self.WIDTH + 15, self.HEIGHT))
        self.duck2 = pygame.transform.scale(self.duck2, (self.WIDTH + 15, self.HEIGHT))
        self.ducking = False

        self.duckImgs = [self.duck1, self.duck2]

        self.runImgs = [self.runImg1, self.runImg2]

        self.jump_sound = pygame.mixer.Sound("jump.wav")
        self.count = 0
        self.jumping = False


    def jump(self):
        self.y -= self.up # Start jumping
        self.jumping = True
        self.jump_sound.play()

    def update(self):
        if self.y < 170: # check if jumping
            self.up = self.up + self.g * self.t # v = u + at
            self.y -= self.up
            self.t += 0.15 #  incrementing time

        if self.y > 170: # check if the jump is complete and resetting all variables
            self.y = 170
            self.t = 0
            self.up = 7
            self.jumping = False

        if self.ducking:
            self.hitbox = pygame.Rect(self.x + 5, self.y + 20, self.WIDTH + 12, self.HEIGHT - 20)
            self.image = self.duckImgs[int(self.count) % 2]
            self.count += 0.2
        elif self.jumping:
            self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5)
            self.image = self.Img
        else:
            self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5)
            self.image = self.runImgs[int(self.count) % 2]
            self.count += 0.2

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) In case you want to see the hitbox

class Ptera():
    def __init__(self):
        self.WIDTH, self.HEIGHT = 50, 40
        self.im1 = pygame.image.load("ptera1.png")
        self.im2 = pygame.image.load("ptera2.png")

        self.im1 = pygame.transform.scale(self.im1, (self.WIDTH, self.HEIGHT))
        self.im2 = pygame.transform.scale(self.im2, (self.WIDTH, self.HEIGHT))

        self.flaps = [self.im1, self.im2]

        self.image = None
        self.allowed = False

        self.x = 20000
        self.y = 175
        self.altitudes = [175, 150, 110]
        self.speed = 5
        self.count = 0

        self.hitbox = (self.x, self.y + 10, self.WIDTH, self.HEIGHT - 12)

    def create(self):
        self.x = random.randint(100, 200) * 10 # generate a random position for ptera
        self.y = random.choice(self.altitudes)

    def update(self):
        if self.allowed:
            self.create()
            self.allowed = False

        self.image = self.flaps[int(self.count) % 2] # Flapping mechanism
        self.count += 0.1

        self.x -= self.speed

        if self.x < 50:
            self.allowed = True

        self.hitbox = pygame.Rect(self.x, self.y + 10, self.WIDTH, self.HEIGHT - 12)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) In case you want to see the hitbox

class Cactus():
    def __init__(self):
        self.image0 = pygame.image.load("cacti-small.png")
        self.image1 = pygame.image.load("cacti-big.png")
        self.width0 = 45
        self.height = 44
        self.width1 = 50
        self.image0 = pygame.transform.scale(self.image0, (self.width0, self.height))
        self.image1 = pygame.transform.scale(self.image1, (self.width1, self.height))
        self.cacti_dist = 450
        self.x0 = 1350
        self.y = 175
        self.x1 = self.x0 + self.cacti_dist
        self.x2 = self.x1 + self.cacti_dist - 100
        self.speed = 4

        self.hitbox0 = pygame.Rect(self.x0, self.y, self.width0, self.height)
        self.hitbox1 = pygame.Rect(self.x1, self.y, self.width1, self.height)
        self.hitbox2 = pygame.Rect(self.x2, self.y, self.width0, self.height)
        self.hitboxes = [self.hitbox0, self.hitbox1, self.hitbox2]

    def update(self):
        self.x0 -= self.speed
        self.x1 -= self.speed
        self.x2 -= self.speed

        self.hitbox0 = pygame.Rect(self.x0, self.y, self.width0, self.height)
        self.hitbox1 = pygame.Rect(self.x1, self.y, self.width1, self.height)
        self.hitbox2 = pygame.Rect(self.x2, self.y, self.width0, self.height)
        self.hitboxes = [self.hitbox0, self.hitbox1, self.hitbox2]

        if self.x0 < -30:
            #self.x0 = 1500
            self.x0 = 1400
        elif self.x1 < -30:
            #self.x1 = 1500
            self.x1 = self.x0 + random.randint(300, 700)
        elif self.x2 < -30:
            #self.x2 = 1500
            self.x2 = self.x1 + random.randint(300, 700)

    def draw(self, screen):
        screen.blit(self.image0, (self.x0, self.y))
        screen.blit(self.image1, (self.x1, self.y))
        screen.blit(self.image0, (self.x2, self.y))

class Ground():
    def __init__(self):
        self.ground_length = 1202
        self.image1 = pygame.image.load("ground.png")
        self.image1_x = 0
        self.image1_y = 200
        self.image2 = pygame.image.load("ground.png")
        self.image2_x = self.image1_x + self.ground_length
        self.image2_y = self.image1_y
        self.speed = 4


    def draw(self, screen):
        screen.blit(self.image1, (self.image1_x, self.image1_y))
        screen.blit(self.image2, (self.image2_x, self.image2_y))

    def update(self):
        self.image1_x -= self.speed
        self.image2_x -= self.speed

        if self.image1_x + self.ground_length < 0:
            self.image1_x = self.image2_x + self.ground_length
        elif self.image2_x + self.ground_length < 0:
            self.image2_x = self.image1_x + self.ground_length

class Cloud():

    def __init__(self):
        self.image = pygame.image.load("cloud.png")
        self.WIDTH, self.HEIGHT = 70, 40
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.speed = 1
        self.x = 600
        self.y = 50

    def update(self):
        self.x -= self.speed

        if self.x < -self.WIDTH:
            self.x = 600
            self.y = random.randint(10, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


def game():
    screen = pygame.display.set_mode((800, 230))
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf", 20)
    check_point = pygame.mixer.Sound("checkPoint.wav")
    death_sound = pygame.mixer.Sound("die.wav")
    pygame.display.set_caption("Dino Run")
    dino_icon = pygame.image.load("dino.png")

    pygame.display.set_icon(dino_icon)

    game_over = pygame.image.load("game_over.png")
    replay_button = pygame.image.load("replay_button.png")
    logo = pygame.image.load("logo.png")
    GREY = (240, 240, 240)
    WHITE = (255, 255, 255)

    ground = Ground()
    dino = Dino()
    cactus = Cactus()
    cloud = Cloud()
    ptera = Ptera()

    running = False
    play_game = True
    dead = False
    high_score_value = 0
    FPS = 60

    while play_game:
        if not dead:
            screen.fill(GREY)
            ground.draw(screen)
            screen.blit(dino.image, (dino.x, dino.y))
            screen.blit(logo, (200, 70))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                play_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    ground = Ground()
                    dino = Dino()
                    cactus = Cactus()
                    ptera = Ptera()
                    dead = False
                    running = True
                    score_value = 0


        while running:
            clock.tick(FPS) # Controlling Frames Per Second

            score = font.render("Score: " + str(int(score_value)), True, (200, 200, 200))
            score_value += 0.25
            high_score_value = max(high_score_value, score_value)
            high_score = font.render("High Score: " + str(int(high_score_value)), True, (200, 200, 200))
            screen.fill(GREY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino.jump()
                    elif event.key == pygame.K_DOWN:
                        dino.ducking = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        dino.ducking = False

            ground.update()
            ground.draw(screen)

            cloud.update()
            cloud.draw(screen)

            dino.update()
            dino.draw(screen)

            cactus.update()
            cactus.draw(screen)

            ptera.update()
            ptera.draw(screen)

            screen.blit(score, (650, 30))
            screen.blit(high_score, (450, 30))

            if int(score_value) % 100 == 0 and int(score_value) % 3 == 0: # Increase game speed after score crosses a multiple of 300
                cactus.speed += 0.25
                ground.speed += 0.25

            if score_value == 500.0: # ptera is allowed to spawn after score crosses 500
                ptera.allowed = True

            if score_value > 1 and score_value % 100 == 0: # Checkpoint sound after score crosses a multiple of 100
                check_point.play()

            closest_hitbox = min(cactus.hitbox0, cactus.hitbox1, cactus.hitbox2) # Hitbox of closest cactus

            if dino.hitbox.colliderect(closest_hitbox): # Collision detection with closest cactus
                death_sound.play()
                dead = True
                screen.blit(game_over, (200, 70))
                screen.blit(replay_button, (360, 100))

            if dino.hitbox.colliderect(ptera.hitbox): # Collision detection with ptera
                death_sound.play()
                dead = True
                screen.blit(game_over, (200, 70))
                screen.blit(replay_button, (360, 100))


            pygame.display.update()

            if dead:
                del dino
                del ground
                del cactus
                del ptera
                running = False

game()
