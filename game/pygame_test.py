__author__ = 'yiqing'

import pygame

class Game(object):
    def main(self,screen):
        clock = pygame.time.Clock()

        image = pygame.image.load('player.png')
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        while 1:
            clock.tick(30)
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                    return

            sprites.update()
            # t = dt / 1000
            # sprites.update( 0.033 )
            screen.fill((200,200,200))
            # screen.blit(image,(320,240))
            sprites.draw(screen)
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
