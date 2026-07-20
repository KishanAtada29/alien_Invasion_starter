import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Button:

    def __init__(self, game: 'AlienInvasion', msg):
        self.gmae = self.gmae
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w,self.settings.button_h)
        self.rect.center = self.boundaries.center
    

    def _prep_msg(self,msg):
        self.msg_img = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def  draw(self):
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

    def check_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)