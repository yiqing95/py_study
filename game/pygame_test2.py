__author__ = 'yiqing'

import pygame

class Game(object):
    def main(self,screen):
        clock = pygame.time.Clock()

        image = pygame.image.load('player.png')
        image_x = 320
        image_y = 240

        while 1:
            # 歇息下！ less CPU used
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                    return

            image_x += 10

            screen.fill((200,200,200))
            # blit 是block image transfer 的缩写！
            screen.blit(image,(320,240))
            screen.blit(image,(image_x,image_y))
            # 双缓冲技术 交换display buffer跟drawing buffer的指针
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    game = Game()
    game.main(screen)
