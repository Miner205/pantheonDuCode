import pygame


class Piece:
    def __init__(self, game, name, color, pos):
        self.name = name
        self.color = color  # w or k for white and black
        self.pos = pos  # in chess board like a matrix ; so in function of row & col
        self.initial_pos = self.pos
        self.state = 1  # 0 for dead & 1 for alive
        self.have_ever_moved = 0  # pour les coups du roque et du en passant(to verif rules)

        self.screen_size = pygame.display.get_window_size()  # screen w and h
        self.image = pygame.image.load("./images/"+self.name+"_"+self.color+".png")
        self.rect = pygame.Rect(self.pos[1]*(self.screen_size[1]//8), self.pos[0]*(self.screen_size[0]//8), self.image.get_width(), self.image.get_height())

        self.selected = False

        self.game = game

    def get_allowed_mouvements_matrix(self):
        # suppose that self.state==1 and self.selected==1 (=piece have been clicked)
        allowed_mouvements_matrix = [[0 for _ in range(8)] for _ in range(8)]
        row = self.pos[0]
        col = self.pos[1]
        if self.name == "rook" or self.name == "queen":
            row-=1
            while row >= 0 and not self.game.board_matrix[row][col]:
                allowed_mouvements_matrix[row][col]=1
                row-=1
            if row >= 0 and self.game.board_matrix[row][col]==-1:
                allowed_mouvements_matrix[row][col]=1
            row = self.pos[0]+1
            while row < 8 and not self.game.board_matrix[row][col]:
                allowed_mouvements_matrix[row][col]=1
                row+=1
            if row < 8 and self.game.board_matrix[row][col]==-1:
                allowed_mouvements_matrix[row][col]=1
            row = self.pos[0]
            col-=1
            while col >= 0 and not self.game.board_matrix[row][col]:
                allowed_mouvements_matrix[row][col]=1
                col-=1
            if col >= 0 and self.game.board_matrix[row][col]==-1:
                allowed_mouvements_matrix[row][col]=1
            col = self.pos[1]+1
            while col < 8 and not self.game.board_matrix[row][col]:
                allowed_mouvements_matrix[row][col]=1
                col+=1
            if col < 8 and self.game.board_matrix[row][col]==-1:
                allowed_mouvements_matrix[row][col]=1

        if self.name != "rook":
            if self.name == "bishop" or self.name == "queen":
                row = self.pos[0]-1
                col = self.pos[1]-1
                while row >= 0 and col >= 0 and not self.game.board_matrix[row][col]:
                    allowed_mouvements_matrix[row][col]=1
                    row-=1
                    col-=1
                if row >= 0 and col >= 0 and self.game.board_matrix[row][col]==-1:
                    allowed_mouvements_matrix[row][col]=1
                row = self.pos[0]+1
                col = self.pos[1]+1
                while row < 8 and col < 8 and not self.game.board_matrix[row][col]:
                    allowed_mouvements_matrix[row][col]=1
                    row+=1
                    col+=1
                if row < 8 and col < 8 and self.game.board_matrix[row][col]==-1:
                    allowed_mouvements_matrix[row][col]=1
                row = self.pos[0]+1
                col = self.pos[1]-1
                while col >= 0 and row < 8 and not self.game.board_matrix[row][col]:
                    allowed_mouvements_matrix[row][col]=1
                    col-=1
                    row+=1
                if col >= 0 and row < 8 and self.game.board_matrix[row][col]==-1:
                    allowed_mouvements_matrix[row][col]=1
                col = self.pos[1]+1
                row = self.pos[0]-1
                while col < 8 and row >= 0 and not self.game.board_matrix[row][col]:
                    allowed_mouvements_matrix[row][col]=1
                    col+=1
                    row-=1
                if col < 8 and row >= 0 and self.game.board_matrix[row][col]==-1:
                    allowed_mouvements_matrix[row][col]=1

            elif self.name == "king":
                if row-1>=0 and (0==self.game.board_matrix[row-1][col] or self.game.board_matrix[row-1][col]==-1):
                    allowed_mouvements_matrix[row-1][col] = 1
                if row+1<8 and (0==self.game.board_matrix[row+1][col] or self.game.board_matrix[row+1][col]==-1):
                    allowed_mouvements_matrix[row+1][col] = 1
                if col-1>=0 and (0==self.game.board_matrix[row][col-1] or self.game.board_matrix[row][col-1]==-1):
                    allowed_mouvements_matrix[row][col-1] = 1
                if col+1<8 and (0==self.game.board_matrix[row][col+1] or self.game.board_matrix[row][col+1]==-1):
                    allowed_mouvements_matrix[row][col+1] = 1
                if row-1>=0 and col-1>=0 and (0==self.game.board_matrix[row-1][col-1] or self.game.board_matrix[row-1][col-1]==-1):
                    allowed_mouvements_matrix[row-1][col-1] = 1
                if row+1<8 and col+1<8 and (0==self.game.board_matrix[row+1][col+1] or self.game.board_matrix[row+1][col+1]==-1):
                    allowed_mouvements_matrix[row+1][col+1] = 1
                if row+1<8 and col-1>=0 and (0==self.game.board_matrix[row+1][col-1] or self.game.board_matrix[row+1][col-1]==-1):
                    allowed_mouvements_matrix[row+1][col-1] = 1
                if row-1>=0 and col+1<8 and (0==self.game.board_matrix[row-1][col+1] or self.game.board_matrix[row-1][col+1]==-1):
                    allowed_mouvements_matrix[row-1][col+1] = 1

            elif self.name == "knight":
                if row-2>=0 and col-1>=0 and (0==self.game.board_matrix[row-2][col-1] or self.game.board_matrix[row-2][col-1]==-1):
                    allowed_mouvements_matrix[row-2][col-1] = 1
                if row-2>=0 and col+1<8 and (0==self.game.board_matrix[row-2][col+1] or self.game.board_matrix[row-2][col+1]==-1):
                    allowed_mouvements_matrix[row-2][col+1] = 1
                if row+2<8 and col-1>=0 and (0==self.game.board_matrix[row+2][col-1] or self.game.board_matrix[row+2][col-1]==-1):
                    allowed_mouvements_matrix[row+2][col-1] = 1
                if row+2<8 and col+1<8 and (0==self.game.board_matrix[row+2][col+1] or self.game.board_matrix[row+2][col+1]==-1):
                    allowed_mouvements_matrix[row+2][col+1] = 1

                if row-1>=0 and col-2>=0 and (0==self.game.board_matrix[row-1][col-2] or self.game.board_matrix[row-1][col-2]==-1):
                    allowed_mouvements_matrix[row-1][col-2] = 1
                if row+1<8 and col-2>=0 and (0==self.game.board_matrix[row+1][col-2] or self.game.board_matrix[row+1][col-2]==-1):
                    allowed_mouvements_matrix[row+1][col-2] = 1
                if row-1>=0 and col+2<8 and (0==self.game.board_matrix[row-1][col+2] or self.game.board_matrix[row-1][col+2]==-1):
                    allowed_mouvements_matrix[row-1][col+2] = 1
                if row+1<8 and col+2<8 and (0==self.game.board_matrix[row+1][col+2] or self.game.board_matrix[row+1][col+2]==-1):
                    allowed_mouvements_matrix[row+1][col+2] = 1

            elif self.name == "pawn":
                if self.color == "w":
                    if self.game.board_matrix[row-1][col]==0:  # row-1>=0 and
                        allowed_mouvements_matrix[row-1][col] = 1
                    if self.have_ever_moved == 0 and self.game.board_matrix[row-1][col]==0 and self.game.board_matrix[row-2][col]==0:
                        allowed_mouvements_matrix[row-2][col] = 1
                    if col-1>=0 and self.game.board_matrix[row-1][col-1]==-1:
                        allowed_mouvements_matrix[row-1][col-1] = 1
                    if col+1<8 and self.game.board_matrix[row-1][col+1]==-1:
                        allowed_mouvements_matrix[row-1][col+1] = 1
                else:
                    if self.game.board_matrix[row+1][col]==0:
                        allowed_mouvements_matrix[row+1][col] = 1
                    if self.have_ever_moved == 0 and self.game.board_matrix[row+1][col]==0 and self.game.board_matrix[row+2][col]==0:
                        allowed_mouvements_matrix[row+2][col] = 1
                    if col-1>=0 and self.game.board_matrix[row+1][col-1]==-1:
                        allowed_mouvements_matrix[row+1][col-1] = 1
                    if col+1<8 and self.game.board_matrix[row+1][col+1]==-1:
                        allowed_mouvements_matrix[row+1][col+1] = 1

            else:
                print("impossible name error ! : a piece is named incorrectly")

        return allowed_mouvements_matrix

    def special_moves(self):
        # king echec & echec&mat ; roque ; en passant
        print("WIP")

    def update(self, event):
        # suppose that self.state==1
        if event.type == pygame.MOUSEBUTTONDOWN:
            row = event.pos[1] // (self.screen_size[1] // 8)
            col = event.pos[0] // (self.screen_size[0] // 8)

            if self.selected and not self.rect.collidepoint(event.pos) and self.get_allowed_mouvements_matrix()[row][col] and ((not self.game.king_is_check) or self.name == "king"):

                # move & capture sound
                if self.game.board_matrix[row][col] == 0:
                    sound_move = pygame.mixer.Sound("./sounds/move.mp3")
                    sound_move.play()
                elif self.game.board_matrix[row][col] == -1:
                    sound_capture = pygame.mixer.Sound("./sounds/capture.mp3")
                    sound_capture.play()
                #

                if self.game.turn == "w":
                    self.game.turn = "k"
                else:
                    self.game.turn = "w"

                for piece in self.game.chess_board:
                    if piece.rect.collidepoint(event.pos):  # and not self.selected:
                        piece.state = 0
                        piece.selected = False

                self.game.en_passant_is_possible = 0
                if self.name == "pawn":
                    if self.pos[0]-row == 2 or self.pos[0]-row == -2:
                        self.game.en_passant_is_possible = 1
                self.pos = (row, col)
                self.rect = pygame.Rect(self.pos[1]*(self.screen_size[1]//8), self.pos[0]*(self.screen_size[0]//8), self.image.get_width(), self.image.get_height())
                self.have_ever_moved = 1
                self.selected = False
                if self.name == "pawn" and (self.pos[0] == 0 or self.pos[0] == 7):
                    self.game.pawn_promotion_is_occurring = self

            else:
                self.selected = self.rect.collidepoint(event.pos)

    def print(self, screen):
        # suppose that self.state==1
        screen.blit(self.image, self.rect)

    def to_get_all_enemies_mouvements_matrix(self):  # for king check
        # suppose that self.state==1
        matrix = [[0 for _ in range(8)] for _ in range(8)]
        row = self.pos[0]
        col = self.pos[1]
        if self.name == "rook" or self.name == "queen":
            row-=1
            while row >= 0 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):  # consider the king(2) 'transparent'/ignore it
                matrix[row][col]=1
                row-=1
            if row >= 0 and self.game.board_matrix[row][col]==1:
                matrix[row][col]=1
            row = self.pos[0]+1
            while row < 8 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                matrix[row][col]=1
                row+=1
            if row < 8 and self.game.board_matrix[row][col]==1:
                matrix[row][col]=1
            row = self.pos[0]
            col-=1
            while col >= 0 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                matrix[row][col]=1
                col-=1
            if col >= 0 and self.game.board_matrix[row][col]==1:
                matrix[row][col]=1
            col = self.pos[1]+1
            while col < 8 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                matrix[row][col]=1
                col+=1
            if col < 8 and self.game.board_matrix[row][col]==1:
                matrix[row][col]=1

        if self.name != "rook":
            if self.name == "bishop" or self.name == "queen":
                row = self.pos[0]-1
                col = self.pos[1]-1
                while row >= 0 and col >= 0 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                    matrix[row][col]=1
                    row-=1
                    col-=1
                if row >= 0 and col >= 0 and self.game.board_matrix[row][col]==1:
                    matrix[row][col]=1
                row = self.pos[0]+1
                col = self.pos[1]+1
                while row < 8 and col < 8 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                    matrix[row][col]=1
                    row+=1
                    col+=1
                if row < 8 and col < 8 and self.game.board_matrix[row][col]==1:
                    matrix[row][col]=1
                row = self.pos[0]+1
                col = self.pos[1]-1
                while col >= 0 and row < 8 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                    matrix[row][col]=1
                    col-=1
                    row+=1
                if col >= 0 and row < 8 and self.game.board_matrix[row][col]==1:
                    matrix[row][col]=1
                col = self.pos[1]+1
                row = self.pos[0]-1
                while col < 8 and row >= 0 and (0==self.game.board_matrix[row][col] or self.game.board_matrix[row][col]==2):
                    matrix[row][col]=1
                    col+=1
                    row-=1
                if col < 8 and row >= 0 and self.game.board_matrix[row][col]==1:
                    matrix[row][col]=1

            elif self.name == "king":
                if row-1>=0 and self.game.board_matrix[row-1][col]>=0:
                    matrix[row-1][col] = 1
                if row+1<8 and self.game.board_matrix[row+1][col]>=0:
                    matrix[row+1][col] = 1
                if col-1>=0 and self.game.board_matrix[row][col-1]>=0:
                    matrix[row][col-1] = 1
                if col+1<8 and self.game.board_matrix[row][col+1]>=0:
                    matrix[row][col+1] = 1
                if row-1>=0 and col-1>=0 and self.game.board_matrix[row-1][col-1]>=0:
                    matrix[row-1][col-1] = 1
                if row+1<8 and col+1<8 and self.game.board_matrix[row+1][col+1]>=0:
                    matrix[row+1][col+1] = 1
                if row+1<8 and col-1>=0 and self.game.board_matrix[row+1][col-1]>=0:
                    matrix[row+1][col-1] = 1
                if row-1>=0 and col+1<8 and self.game.board_matrix[row-1][col+1]>=0:
                    matrix[row-1][col+1] = 1

            elif self.name == "knight":
                if row-2>=0 and col-1>=0 and self.game.board_matrix[row-2][col-1]>=0:
                    matrix[row-2][col-1] = 1
                if row-2>=0 and col+1<8 and self.game.board_matrix[row-2][col+1]>=0:
                    matrix[row-2][col+1] = 1
                if row+2<8 and col-1>=0 and self.game.board_matrix[row+2][col-1]>=0:
                    matrix[row+2][col-1] = 1
                if row+2<8 and col+1<8 and self.game.board_matrix[row+2][col+1]>=0:
                    matrix[row+2][col+1] = 1

                if row-1>=0 and col-2>=0 and self.game.board_matrix[row-1][col-2]>=0:
                    matrix[row-1][col-2] = 1
                if row+1<8 and col-2>=0 and self.game.board_matrix[row+1][col-2]>=0:
                    matrix[row+1][col-2] = 1
                if row-1>=0 and col+2<8 and self.game.board_matrix[row-1][col+2]>=0:
                    matrix[row-1][col+2] = 1
                if row+1<8 and col+2<8 and self.game.board_matrix[row+1][col+2]>=0:
                    matrix[row+1][col+2] = 1

            elif self.name == "pawn":
                if self.color == "w":
                    '''if self.game.board_matrix[row-1][col]==0:  # row-1>=0 and
                        matrix[row-1][col] = 1
                    if self.have_ever_moved == 0 and self.game.board_matrix[row-1][col]==0 and self.game.board_matrix[row-2][col]==0:
                        matrix[row-2][col] = 1'''
                    if col-1>=0 and self.game.board_matrix[row-1][col-1]>0:
                        matrix[row-1][col-1] = 1
                    if col+1<8 and self.game.board_matrix[row-1][col+1]>0:
                        matrix[row-1][col+1] = 1
                else:
                    '''if self.game.board_matrix[row+1][col]==0:
                        matrix[row+1][col] = 1
                    if self.have_ever_moved == 0 and self.game.board_matrix[row+1][col]==0 and self.game.board_matrix[row+2][col]==0:
                        matrix[row+2][col] = 1'''
                    if col-1>=0 and self.game.board_matrix[row+1][col-1]>0:
                        matrix[row+1][col-1] = 1
                    if col+1<8 and self.game.board_matrix[row+1][col+1]>0:
                        matrix[row+1][col+1] = 1

            else:
                print("impossible name error ! ;;; to get all enemies mouvement matrix")

        for i in range(8):
            for j in range(8):
                if matrix[i][j]:
                    self.game.all_enemies_mouvements_matrix[i][j] = matrix[i][j]
