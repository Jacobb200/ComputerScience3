"""Final Project #1 Jacob B."""

"""
External Links:
https://stackoverflow.com/questions/8874276/trouble-with-making-background-of-image-transparent-in-python-using-pygame
https://stackoverflow.com/questions/16551009/gravity-in-pygame
https://pythonspot.com/jump-and-run-in-pygame/
https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
https://www.pygame.org/docs/tut/MakeGames.html
http://programarcadegames.com/index.php?chapter=example_code
https://realpython.com/pygame-a-primer/
https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
http://pygametutorials.wikidot.com/book-time
https://github.com/f-prime/DoodleJump
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame
https://gamedev.stackexchange.com/questions/129688/how-to-make-an-object-move-outside-the-map-and-appear-on-the-other-side-with-a-t
Lima Sky(Developer of Doodle Jump)
Older Graphics Assignments

PNG Images:
https://raw.githubusercontent.com/f-prime/DoodleJump/master/assets/blue.png
(Shrunk and rotated the player and saved)
https://d14nx13ylsx7x8.cloudfront.net/lesson_images/images/000/001/428/original/temp1406587188.png
https://raw.githubusercontent.com/f-prime/DoodleJump/master/assets/green.png
https://raw.githubusercontent.com/f-prime/DoodleJump/master/assets/red.png
https://raw.githubusercontent.com/f-prime/DoodleJump/master/assets/red_1.png
mean-monster-clipart-free-clipart-images.png

Description:
SO I used the github doodle jump that was made and from there I used various links and
websites in order to be able to understand and make slight modifications onto the code
From there I tried to implment moving enemies using similar code to the moving platforms
however I wasn't able to randomly generate the character since it would always spawn under
the screen for some reason. However if it is touched it should restart the game



"""

import pygame
import sys
import random

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    QUIT,
)


class DoodleJumpGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.green = pygame.image.load("green.png").convert_alpha()
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 25)
        self.blue = pygame.image.load("blue.png").convert_alpha()
        self.red = pygame.image.load("red.png").convert_alpha()
        self.red_1 = pygame.image.load("red_1.png").convert_alpha()
        self.playerRight_1 = pygame.image.load("right_1.png").convert_alpha()
        self.playerLeft_1 = pygame.image.load("left_1.png").convert_alpha()
        self.enemy = pygame.image.load("enemy.png").convert_alpha()
        self.direction = 0
        self.playerx = 400
        self.playery = 400
        self.platforms = [[400, 500, 0, 0]]
        self.enemies = [[400, 500, 0, 0]]
        self.cameray = 0
        self.jump = 0
        self.gravity = 0
        self.xmovement = 0

    def update_player(self):
        """Updates the player and allows it to move and to jump"""
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1
        key = pygame.key.get_pressed()
        # Turn right
        if key[K_RIGHT]:
            if self.xmovement < 10:
                self.xmovement += 1
            self.direction = 0
        # Turn left
        elif key[K_LEFT]:
            if self.xmovement > -10:
                self.xmovement -= 1
            self.direction = 1
        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            elif self.xmovement < 0:
                self.xmovement += 1
        if self.playerx > 850:
            self.playerx = -50
        elif self.playerx < -50:
            self.playerx = 850
        self.playerx += self.xmovement
        if self.playery - self.cameray <= 200:
            self.cameray -= 10
        if not self.direction:
            self.screen.blit(self.playerRight_1, (self.playerx, self.playery - self.cameray))
        else:
            self.screen.blit(self.playerLeft_1, (self.playerx, self.playery - self.cameray))

    def draw_enemies(self):
        """Draws the platforms the player will jump on"""
        for e in self.enemies:
            check = self.enemies[0][1] - self.cameray
            if check > 600:
                enemy = random.randint(0, 1000)
                if enemy < 800:
                    enemy = 0
                elif enemy < 900:
                    enemy = 1
                else:
                    enemy = 2
                self.enemies.append([random.randint(0, 700), self.enemies[-1][1] - 50, enemy, 0])
                self.platforms.pop(0)
            if e[2] == 1:
                self.screen.blit(self.enemy, (e[0], e[1] - self.cameray))


    def update_enemies(self):
        """ Allows for player to make contact with the player"""
        for e in self.enemies:
            if e[2] == 1:
                if e[-1] == 1:
                    e[0] += 5
                    if e[0] > 550:
                        e[-1] = 0
                else:
                    e[0] -= 5
                    if e[0] <= 0:
                        e[-1] = 1

    def update_platforms(self):
        """ Allows for player to make contact with the player"""
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.green.get_width() - 10, self.green.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.playerRight_1.get_width() - 10,
                                 self.playerRight_1.get_height())
            if rect.colliderect(player) and self.gravity and self.playery < (p[1] - self.cameray):
                if p[2] != 2:
                    self.jump = 15
                    self.gravity = 0
                else:
                    p[-1] = 1
            if p[2] == 1:
                if p[-1] == 1:
                    p[0] += 5
                    if p[0] > 550:
                        p[-1] = 0
                else:
                    p[0] -= 5
                    if p[0] <= 0:
                        p[-1] = 1

    def draw_platforms(self):
        """Draws the platforms the player will jump on"""
        for p in self.platforms:
            check = self.platforms[1][1] - self.cameray
            if check > 600:
                platform = random.randint(0, 1000)
                if platform < 800:
                    platform = 0
                elif platform < 900:
                    platform = 1
                else:
                    platform = 2
                self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, platform, 0])
                self.platforms.pop(0)
                self.score += 1
            if p[2] == 0:
                self.screen.blit(self.green, (p[0], p[1] - self.cameray))
            elif p[2] == 1:
                self.screen.blit(self.blue, (p[0], p[1] - self.cameray))
            elif p[2] == 2:
                if not p[3]:
                    self.screen.blit(self.red, (p[0], p[1] - self.cameray))
                else:
                    self.screen.blit(self.red_1, (p[0], p[1] - self.cameray))

    def background(self):
        """Draws the background"""
        for x in range(80):
            pygame.draw.line(self.screen, (222, 222, 222), (x * 12, 0), (x * 12, 600))
            pygame.draw.line(self.screen, (222, 222, 222), (0, x * 12), (800, x * 12))

    def generate_platforms(self):
        """Helps draw in the platforms"""
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            platform = random.randint(0, 1000)
            if platform < 800:
                platform = 0
            elif platform < 900:
                platform = 1
            else:
                platform = 2
            self.platforms.append([x, on, platform, 0])
            on -= 50

    def run(self):
        clock = pygame.time.Clock()
        self.generate_platforms()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            if self.playery - self.cameray > 700:
                self.cameray = 0
                self.score = 0
                self.platforms = [[400, 500, 0, 0]]
                self.enemies = [[400, 500, 0, 0]]
                self.generate_platforms()
                self.playerx = 400
                self.playery = 400
            # If player touches the villain it should restart
            """
            villain = pygame.Rect(self.enemies[0][1], self.enemies[0][1], self.enemy.get_width() - 10, self.enemy.get_height())
            player1 = pygame.Rect(self.playerx, self.playery, self.playerRight_1.get_width() - 10,
                                    self.playerRight_1.get_height())
            if villain.colliderect(player1) and self.gravity and self.playery < (p[1] - self.cameray):
                self.cameray = 0
                self.score = 0
                self.platforms = [[400, 500, 0, 0]]
                self.enemies = [[400, 500, 0, 0]]
                self.generate_platforms()
                self.playerx = 400
                self.playery = 400
            """
            self.background()
            self.draw_platforms()
            self.draw_enemies()
            self.update_player()
            self.update_platforms()
            self.update_enemies()
            self.screen.blit(self.font.render(str(self.score), -1, (0, 0, 0)), (25, 25))
            pygame.display.flip()


DoodleJumpGame().run()
