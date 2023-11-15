import pygame
from random import shuffle

class gui():
    def __init__(self, weight, height, tick):
        self.height = height
        self.weight = weight
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = tick

    def createArrayOfRects(self, number):
        rects = []
        #estudar
        positions = list(range(1, number + 1))  
        shuffle(positions)  
        for i, pos in enumerate(positions):
            rects.append(pygame.Rect(pos*10-7, 10, 8, i*6.8))
        return rects

    def drawRects(self, screen, rects):
        colorRect = (255,255,255)
        for rect in rects: 
            print(rect)         
            pygame.draw.rect(screen, colorRect, rect)

    def start(self):
        pygame.init()
        rects = self.createArrayOfRects(72)
        self.screen = pygame.display.set_mode((self.weight, self.height))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("black")
            self.drawRects(self.screen, rects)
            pygame.display.flip()
            self.clock.tick(self.tick)
        pygame.quit()


