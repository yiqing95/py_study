__author__ = 'yiqing'

import pygame

class Game(object):
    def main(self,screen):
        clock = pygame.time.Clock()

        image = pygame.image.load('player.png')
        image_x = 320
        image_y = 240

        while 1:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                    return

            image_x += 1
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                image_x -= 10
            if key[pygame.K_RIGHT]:
                image_x += 10
            if key[pygame.K_UP]:
                image_y -= 10
            if key[pygame.K_DOWN]:
                image_y += 10

            screen.fill((200,200,200))
            screen.blit(image,(image_x,image_y))
            pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load('player.png')
        self.rect = pygame.rect.Rect((320,240),self.image.get_size())

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT]:
            self.rect.x += 10
        if key[pygame.K_UP]:
            self.rect.y -= 10
        if key[pygame.K_DOWN]:
            self.rect.y += 10


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    game = Game()
    game.main(screen)
