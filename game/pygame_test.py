__author__ = 'yiqing'

import pygame

class Game(object):
    def main(self,screen):
        clock = pygame.time.Clock()

        backgroud = pygame.image.load('backgroud.jpg')
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        self.walls = pygame.sprite.Group()
        block = pygame.image.load('block.gif')
        for x in range(0,640,32):
            for y in range(0,480,32):
                if x in(0,640-32) or y in (0,480-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x,y))

        sprites.add(self.walls)

        while 1:
            clock.tick(30)
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                    return

            # sprites.update()
            sprites.update(self)
            # t = dt / 1000
            # sprites.update( 0.033 )
            # screen.fill((200,200,200))
            screen.blit(backgroud,(0,0))
            sprites.draw(screen)
            pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load('player.png')
        self.rect = pygame.rect.Rect((320,240),self.image.get_size())
        self.resting = False
        self.dy = 0

    def update(self,dt=0.03,game=None):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT]:
            self.rect.x += 10

        # if key[pygame.K_UP]:
        #     self.rect.y -= 10
        # if key[pygame.K_DOWN]:
        #     self.rect.y += 10
        if self.resting and key[pygame.K_SPACE]:
            self.dy = -500
        self.dy = min(400,self.dy+40)

        self.rect.y += self.dy * dt

        # collisions conform
        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self,game.walls,False):
            self.rect = last
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left <cell.right:
                new.left = cell.right
            if last.botton <= cell.top and new.bottom >cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.botton and new.top <cell.bottom:
                new.top = cell.bottom
                self.dy = 0

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    game = Game()
    game.main(screen)
