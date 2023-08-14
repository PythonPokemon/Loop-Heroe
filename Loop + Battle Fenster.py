import pygame
import math
import random
import subprocess
import sys

# Pygame initialisieren
pygame.init()

# Fenstergröße
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Erstellen des Spielfensters
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Loop Hero")

# Klassen für Spielobjekte
class Hero(pygame.sprite.Sprite):
    def __init__(self, radius):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.radius = radius
        self.angle = 0
        self.speed = 1

    def update(self):
        # Bewegung des Quadrats im Kreis
        self.angle += self.speed
        self.rect.centerx = WINDOW_WIDTH // 2 + self.radius * math.cos(math.radians(self.angle))
        self.rect.centery = WINDOW_HEIGHT // 2 + self.radius * math.sin(math.radians(self.angle))

class RedSquare(pygame.sprite.Sprite):
    def __init__(self, radius):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.radius = radius
        self.angle = 180  # Startwinkel, um sich entgegen der Bewegung des grünen Quadrats zu bewegen
        self.speed = 1

    def update(self):
        # Bewegung des Quadrats im Kreis in entgegengesetzter Richtung zum grünen Quadrat
        self.angle -= self.speed
        self.rect.centerx = WINDOW_WIDTH // 2 + self.radius * math.cos(math.radians(self.angle))
        self.rect.centery = WINDOW_HEIGHT // 2 + self.radius * math.sin(math.radians(self.angle))

# Funktion zum Überprüfen der Kollision
def check_collision(sprite1, sprite2):
    return sprite1.rect.colliderect(sprite2.rect)

# Spielobjekte erstellen
all_sprites = pygame.sprite.Group()
radius = 400  # Radius des Kreises, in dem sich das Quadrat bewegen soll
hero = Hero(radius)
red_square = RedSquare(radius)
all_sprites.add(hero, red_square)
window.fill(WHITE)


# Spiel-Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bildschirm aktualisieren
    window.fill(WHITE)

    # Kreis zeichnen
    pygame.draw.circle(window, RED, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), radius, 2)

    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()

    # Kollisionsprüfung und Aufrufen der main.py im neuen Fenster bei Kollision
    if check_collision(red_square, hero):
        subprocess.Popen([sys.executable, "battle.py"])
        running = False

pygame.quit()
