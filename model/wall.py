import pygame

class Wall:
    def __init__(self, left_top, right_bot):
        self.left = left_top[0]*60
        self.top = left_top[1]*60
        self.right = (right_bot[0] + 1)*60
        self.bot = (right_bot[1] + 1)*60

    def draw(self, screen):
        # For now...
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (self.left, self.top, self.right, self.bot))

        # Actually...
        # screen.blit
