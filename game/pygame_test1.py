__author__ = 'yiqing'

import pygame

'''
pygame.init()
screen = pygame.display.set_mode((640,480))

running = True
while running:
    "
    每个游戏框架 都会有事件队列，事件循环的实现
    然后注册事件处理器
    "
    # 从内存事件队列中不停取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN  and \
                event.key == pygame.K_ESCAPE :# and event.key
            running = False
'''

class Game(object):
    def main(self,scree):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                    return

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game.main(screen)
