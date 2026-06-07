import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
PLAYER_SIZE = 30
PLAYER_SPEED = 5
PLAYER_ROT_SPEED = 4
PLAYER_IMG = pygame.image.load('spaceship.png')
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_SIZE, PLAYER_SIZE))
PLAYER_IMG_THRUST = pygame.image.load('spaceship_thrust.png')
PLAYER_IMG_THRUST = pygame.transform.scale(PLAYER_IMG_THRUST, (PLAYER_SIZE, PLAYER_SIZE))

# Bullet settings
BULLET_SPEED = 7
BULLET_IMG = pygame.image.load('bullet.png')
BULLET_IMG = pygame.transform.scale(BULLET_IMG, (10, 10))

# Asteroid settings
ASTEROID_IMG = pygame.image.load('asteroid.png')
ASTEROID_IMG = pygame.transform.scale(ASTEROID_IMG, (50, 50))
ASTEROID_SPEED = 2
ASTEROID_SIZES = [50, 30, 20]  # Sizes of asteroids

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids Game")

clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.angle = 0
        self.speedx = 0
        self.speedy = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += PLAYER_ROT_SPEED
        if keys[pygame.K_RIGHT]:
            self.angle -= PLAYER_ROT_SPEED
        if keys[pygame.K_UP]:
            self.speedx += PLAYER_SPEED * math.cos(math.radians(self.angle))
            self.speedy -= PLAYER_SPEED * math.sin(math.radians(self.angle))
            self.image = PLAYER_IMG_THRUST
        else:
            self.image = PLAYER_IMG

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Screen wrapping
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0

    def shoot(self):
        bullet = Bullet(self.rect.center, self.angle)
        bullets.add(bullet)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        super().__init__()
        self.image = BULLET_IMG
        self.rect = self.image.get_rect(center=pos)
        self.angle = angle
        self.speedx = BULLET_SPEED * math.cos(math.radians(self.angle))
        self.speedy = -BULLET_SPEED * math.sin(math.radians(self.angle))

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

# Asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ASTEROID_IMG
        self.rect = self.image.get_rect()

        # Random initial position and velocity
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = -self.rect.height
            self.speedx = random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
            self.speedy = random.uniform(1, ASTEROID_SPEED)
        elif side == 'bottom':
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = HEIGHT
            self.speedx = random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
            self.speedy = random.uniform(-ASTEROID_SPEED, -1)
        elif side == 'left':
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(0, HEIGHT)
            self.speedx = random.uniform(1, ASTEROID_SPEED)
            self.speedy = random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
        elif side == 'right':
            self.rect.x = WIDTH
            self.rect.y = random.randint(0, HEIGHT)
            self.speedx = random.uniform(-ASTEROID_SPEED, -1)
            self.speedy = random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()

# Sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Add player to sprite group
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # Spawn asteroids
    if len(asteroids) < 10:
        asteroid = Asteroid()
        asteroids.add(asteroid)
        all_sprites.add(asteroid)

    # Collision detection: bullets vs asteroids
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    for hit in hits:
        score += 1
        asteroid = Asteroid()
        asteroids.add(asteroid)
        all_sprites.add(asteroid)

    # Collision detection: player vs asteroids
    hits = pygame.sprite.spritecollide(player, asteroids, False)
    if hits:
        print("Game Over!")
        running = False

    # Drawing
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
