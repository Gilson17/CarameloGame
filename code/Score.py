import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.DBProxy import DBProxy
from code.const import VIRTUAL_WIDTH, VIRTUAL_HEIGHT, C_YELLOW, C_WHITE, SCORE_POS



class Score:
    def __init__(self, window):
        self.window = window
        image = pygame.image.load("./asset/City2.png").convert_alpha()
        window_width, window_height = self.window.get_size()
        self.surf = pygame.transform.smoothscale(image, (window_width, window_height))
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.db_proxy = DBProxy('scores.db')

    def save_score(self, name: str, score: int):
        self.db_proxy.save_score(name, score)
        print(f"Score {score} save with sucess!")

    def input_name(self, status: str, score_value: int) -> str:
        name = ""
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            title_text = "YOU WIN !!" if status == "WIN" else "YOU LOSE !!"
            self.level_score(48, title_text, C_YELLOW, SCORE_POS['Title'])
            self.level_score(32, f'SCORE: {score_value}', C_YELLOW, (SCORE_POS['Title'][0], SCORE_POS['Title'][1] + 60))

            self.level_score(24, "ENTER NAME (MAX 6 LETTERS):", C_WHITE,
                             (SCORE_POS['Title'][0], SCORE_POS['Title'][1] + 130))
            self.level_score(36, name + "_", C_YELLOW, (SCORE_POS['Title'][0], SCORE_POS['Title'][1] + 180))
            self.level_score(16, "Press ENTER to confirm", C_WHITE,
                             (SCORE_POS['Title'][0], SCORE_POS['Title'][1] + 240))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) > 0:
                        return name.upper()
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 6 and event.unicode.isalpha():
                        name += event.unicode

    def show_score(self, current_game_data=None):
        pygame.mixer.music.load('./asset/ScoreMusic.ogg')
        pygame.mixer_music.play(-1)

        if current_game_data is not None:
            status, pontos = current_game_data
            player_name = self.input_name(status, pontos)
            self.save_score(player_name, pontos)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.level_score(48, 'SCOREBOARD', C_YELLOW, (SCORE_POS['Title'][0], 40))

            rows = self.db_proxy.get_top_10()

            for idx, row in enumerate(rows):
                pos_y = 110 + (idx * 25)
                text_row = f"{idx + 1}. {row[0]} ------ {row[1]}"
                self.level_score(24, text_row, C_WHITE, (SCORE_POS['Title'][0], pos_y))

            self.level_score(16, "Press SPACE or ESC to Return", C_YELLOW, (SCORE_POS['Title'][0], 420))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_SPACE):
                        return

    def level_score(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)