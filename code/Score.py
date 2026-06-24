import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import VIRTUAL_WIDTH, VIRTUAL_HEIGHT, C_YELLOW, SCORE_POS


class Score:
    def __init__(self, window):
        self.window = window
        image = pygame.image.load("./asset/City2.png").convert_alpha()
        window_width, window_height = self.window.get_size()

        self.surf = pygame.transform.smoothscale(image, (window_width, window_height))
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def save_score(self, menu_return: str, player_score: list[int]):
        print(f"Score {player_score[0]} save with sucess!")

    def show_score(self, player_score=None):
        pygame.mixer.music.load('./asset/ScoreMusic.ogg')
        pygame.mixer.music.play(-1)

        if player_score is None:
            player_score = [0]

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            if player_score[0] > 0:
                self.level_score(48, 'YOU LOSE !!', C_YELLOW, SCORE_POS['Title'])
                pontos = player_score[0]
                self.level_score(32, f'SCORE: {pontos}', C_YELLOW, SCORE_POS[0])
            else:
                self.level_score(48, 'SCOREBOARD', C_YELLOW, SCORE_POS['Title'])
                pontos = player_score[0]
                self.level_score(32, f'SCORE: {pontos}', C_YELLOW, SCORE_POS[0])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        return

    def level_score(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)