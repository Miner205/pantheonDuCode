import pygame


class Piece:
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color  # w or k for white and black
        self.pos = pos  # in chess board like a matrix ; so in function of row & col
        self.initial_pos = self.pos
        self.state = 1  # 0 for dead & 1 for alive
        self.have_ever_moved = 0  # pour les coups du roque et du en passant(to verif rules)

        self.screen_size = pygame.display.get_window_size()  # screen w and h
        self.image =
        self.rect = pygame.Rect()

        self.selected = False

    def get_allowed_mouvements_matrix(self, board_matrix):
        # suppose that self.state==1 and piece have been clicked / self.selected==1
        allowed_mouvements_matrix = [[0 for _ in range(8)] for _ in range(8)]
        self.pos
        if self.name == "rook":

        elif self.name == "bishop":

        elif self.name == "queen":

        elif self.name == "king":

        elif self.name == "knight":

        elif self.name == "pawn":

        else:
            print("impossible name error ! : a piece is named incorrectly")

        return allowed_mouvements_matrix

    def update(self, event, board_matrix):
        # suppose that self.state==1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.selected and not self.rect.collidepoint(event.pos):
                row = event.pos[1]//(self.screen_size[1]//8)
                col = event.pos[0]//(self.screen_size[0]//8)
                if self.get_allowed_mouvements_matrix(board_matrix)[row][col]:
                    self.pos = (row, col)
                    self.have_ever_moved = 1

            self.selected = self.rect.collidepoint(event.pos)

            if self.rect.collidepoint(event.pos) and not self.selected:
                self.state = 0
                self.selected = False

    def print(self, screen, board_matrix):
        # suppose that self.state==1
        if self.selected:
            m = self.get_allowed_mouvements_matrix(board_matrix)
            for row in range(8):
                for col in range(8):
                    if m[row][col]:
                        pygame.draw.rect(screen, "green",  (row*(self.screen_size[1]//8), col*(self.screen_size[0]//8),
                                                            self.screen_size[0]//8, self.screen_size[1]//8))

        self.image.print~~
