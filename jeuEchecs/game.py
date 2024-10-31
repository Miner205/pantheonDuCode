import pygame
from piece import Piece
from button import Button
import os
import functions as fct
from popups import PawnPromotion


class Game:
    def __init__(self, screen_w, screen_h):
        self.game_mode = 0  # 1 for local solo ; 0 for local multi ; 2 for online multi
        self.game_state = 0  # 1 = white win ; 2 for black win ; 3 for nul
        self.chess_board = (Piece(self, "rook", "k", (0, 0)), Piece(self, "knight", "k", (0, 1)),
                            Piece(self, "bishop", "k", (0, 2)), Piece(self, "queen", "k", (0, 3)),
                            Piece(self, "king", "k", (0, 4)), Piece(self, "bishop", "k", (0, 5)),
                            Piece(self, "knight", "k", (0, 6)), Piece(self, "rook", "k", (0, 7)),
                            Piece(self, "pawn", "k", (1, 0)), Piece(self, "pawn", "k", (1, 1)),
                            Piece(self, "pawn", "k", (1, 2)), Piece(self, "pawn", "k", (1, 3)),
                            Piece(self, "pawn", "k", (1, 4)), Piece(self, "pawn", "k", (1, 5)),
                            Piece(self, "pawn", "k", (1, 6)), Piece(self, "pawn", "k", (1, 7)),
                            Piece(self, "pawn", "w", (6, 0)), Piece(self, "pawn", "w", (6, 1)),
                            Piece(self, "pawn", "w", (6, 2)), Piece(self, "pawn", "w", (6, 3)),
                            Piece(self, "pawn", "w", (6, 4)), Piece(self, "pawn", "w", (6, 5)),
                            Piece(self, "pawn", "w", (6, 6)), Piece(self, "pawn", "w", (6, 7)),
                            Piece(self, "rook", "w", (7, 0)), Piece(self, "knight", "w", (7, 1)),
                            Piece(self, "bishop", "w", (7, 2)), Piece(self, "queen", "w", (7, 3)),
                            Piece(self, "king", "w", (7, 4)), Piece(self, "bishop", "w", (7, 5)),
                            Piece(self, "knight", "w", (7, 6)), Piece(self, "rook", "w", (7, 7)))
        self.turn = "w"

        self.s_w = screen_w
        self.s_h = screen_h

        self.x_slide = 0
        self.y_slide = 0

        self.board_matrix = []
        self.update_board_representation_matrix()
        self.en_passant_is_possible = 0
        self.pawn_promotion_is_occurring = None
        self.pawn_promotion_popup = None

        self.menu_button = Button(screen_w-5-27, 5, 27, 27)

    def update(self, event, zoom):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pawn_promotion_is_occurring is None:
                for piece in self.chess_board:
                    if piece.state and piece.color == self.turn:
                        piece.update(event)
                self.update_board_representation_matrix()
            if self.pawn_promotion_is_occurring is not None:
                if self.pawn_promotion_popup is None:
                    self.pawn_promotion_popup = PawnPromotion(self.pawn_promotion_is_occurring.rect.topleft[0], self.pawn_promotion_is_occurring.rect.topleft[1],
                                                          self.pawn_promotion_is_occurring.color)
                    self.pawn_promotion_popup.active = 1
                else:
                    temp = self.pawn_promotion_popup.update(event)
                    if temp:
                        self.pawn_promotion_is_occurring.name = temp
                        self.pawn_promotion_is_occurring.image = pygame.image.load("./images/"+temp+"_"+self.pawn_promotion_is_occurring.color+".png")
                        self.pawn_promotion_popup = None
                        self.pawn_promotion_is_occurring = None
                        self.update_board_representation_matrix()


    def print(self, screen, zoom):
        k = 1
        # chess board
        for y in range(0, self.s_h, self.s_h//8):
            k = 1-k
            for x in range(0+k*self.s_w//8, self.s_w, 2*self.s_h//8):
                pygame.draw.rect(screen, "#eeeed2", (x, y, self.s_w//8, self.s_h//8))
            for x in range(0+(1-k)*self.s_w//8, self.s_w, 2*self.s_h//8):
                pygame.draw.rect(screen, "#769656", (x, y, self.s_w//8, self.s_h//8))

        # to visualize the center
        pygame.draw.circle(screen, "green", (self.s_w//2+self.x_slide, self.s_h//2+self.y_slide), min(4*zoom, 4*5))

        # print pieces
        for piece in self.chess_board:
            if piece.state and piece.selected:
                m = piece.get_allowed_mouvements_matrix()
                for row in range(8):
                    for col in range(8):
                        if m[row][col]:
                            pygame.draw.rect(screen, "green",
                                             (col*(piece.screen_size[1]//8)+(piece.screen_size[1]//8)//30, row*(piece.screen_size[0]//8)+(piece.screen_size[0]//8)//30,
                                              piece.screen_size[0]//8-2*(piece.screen_size[0]//8)//30, piece.screen_size[1]//8-2*(piece.screen_size[1]//8)//30))
        for piece in self.chess_board:
            if piece.state:
                piece.print(screen)

        if self.pawn_promotion_is_occurring is not None:
            if self.pawn_promotion_popup is not None:
                self.pawn_promotion_popup.print(screen)

        # print game menu_button
        self.menu_button.print(screen)
        fct.pygame_draw_hashtag(screen, (130, 0, 0), self.menu_button.rect.center, self.menu_button.rect.w - 10, 3)
        pygame.draw.circle(screen, (130, 0, 0), self.menu_button.rect.center, 7)

        # turn/action rect
        t = self.turn
        if self.pawn_promotion_is_occurring is not None:
            if t == 'w':
                t = 'k'
            else:
                t = 'w'
        if t == 'w':
            pygame.draw.rect(screen, "#FFFFFF", (5, 35, 20, 20))
        else:
            pygame.draw.rect(screen, "#363636", (5, 35, 20, 20))
        pygame.draw.rect(screen, "black", (5, 35, 20, 20), 3)
        if self.pawn_promotion_is_occurring is not None:
            pygame.draw.rect(screen, "red", (5, 35+20, 20, 20))
            pygame.draw.rect(screen, "black", (5, 35+20, 20, 20), 3)

    def reset_chess_board(self):
        for piece in self.chess_board:
            piece.pos = piece.initial_pos
            piece.state = 1
            piece.have_ever_moved = 0
            # + update rect.x .y

    def save_game(self):
        with open("./save.txt", 'w') as f:
            for piece in self.chess_board:
                f.write(piece.pos[0]+';'+piece.pos[1]+';'+piece.state+';'+piece.have_ever_moved)
                f.write('\n')

    def load_game(self):
        if os.path.exists("./save.txt"):
            with open("./save.txt", 'r') as f:
                line = f.readline()
                piece = 0
                while line != "":
                    temp = line.strip('\n').split(';')
                    self.chess_board[piece].pos = temp[0], temp[1]
                    self.chess_board[piece].state = temp[2]
                    self.chess_board[piece].have_ever_moved = temp[3]
                    line = f.readline()
                    piece += 0

    def update_board_representation_matrix(self):
        self.board_matrix = [[0 for _ in range(8)] for _ in range(8)]
        for piece in self.chess_board:
            if piece.state:
                if self.turn == "w":
                    if piece.color == "w":
                        self.board_matrix[piece.pos[0]][piece.pos[1]] = 1  # 1 like allies & -1 like enemies
                    else:
                        if piece.name != "king":
                            self.board_matrix[piece.pos[0]][piece.pos[1]] = -1
                        else:
                            self.board_matrix[piece.pos[0]][piece.pos[1]] = -2
                else:
                    if piece.color == "k":
                        self.board_matrix[piece.pos[0]][piece.pos[1]] = 1
                    else:
                        if piece.name != "king":
                            self.board_matrix[piece.pos[0]][piece.pos[1]] = -1
                        else:
                            self.board_matrix[piece.pos[0]][piece.pos[1]] = -2
