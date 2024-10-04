import pygame
import functions as fct


class Game:
    def __init__(self, map_size, cell_size, screen_w, screen_h):
        self.map = []
        self.map_size = map_size   # nb of cells, like (100, 100).
        self.cell_size = cell_size
        self.empty_map()
        self.iteration = 0

        self.s_w = screen_w
        self.s_h = screen_h
        self.keys_pressed = {}
        self.x_slide = 0
        self.y_slide = 0

        self.mode_grille = 1

    def run(self, zoom, k=0):
        if self.keys_pressed.get(pygame.K_DOWN):
            self.y_slide -= (self.cell_size+1) * zoom
        if self.keys_pressed.get(pygame.K_UP):
            self.y_slide += (self.cell_size+1) * zoom
        if self.keys_pressed.get(pygame.K_RIGHT):
            self.x_slide -= (self.cell_size+1) * zoom
        if self.keys_pressed.get(pygame.K_LEFT):
            self.x_slide += (self.cell_size+1) * zoom

        if True in self.keys_pressed.values() or k == 1:
            if self.x_slide > (self.s_w//2-self.s_w//2/zoom)*zoom:
                self.x_slide = (self.s_w//2-self.s_w//2/zoom)*zoom
            if self.x_slide < -(self.s_w//2-self.s_w//2/zoom)*zoom:
                self.x_slide = -(self.s_w//2-self.s_w//2/zoom)*zoom
            if self. y_slide > (self.s_h//2-self.s_h//2/zoom)*zoom:
                self.y_slide = (self.s_h//2-self.s_h//2/zoom)*zoom
            if self.y_slide < -(self.s_h//2-self.s_h//2/zoom)*zoom:
                self.y_slide = -(self.s_h//2-self.s_h//2/zoom)*zoom

    def update(self, event, zoom):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for row in range(self.map_size[0]):
                for col in range(self.map_size[1]):
                    pos_x = (int((self.cell_size + 1) * zoom) * row + int(self.x_slide) - int(
                                (self.s_w // 2 - self.s_w // 2 / zoom) * zoom))
                    pos_y = (int((self.cell_size + 1) * zoom) * col + int(self.y_slide) - int(
                                (self.s_h // 2 - self.s_h // 2 / zoom) * zoom))
                    rect_s = fct.pygame_rect_square((pos_x, pos_y), int((self.cell_size + 1) * zoom))
                    if rect_s.collidepoint(event.pos):
                        if len(self.map[row]) == 1:
                            self.map[row] = ['0']*self.map_size[1]
                        if self.map[row][col] == '0':
                            self.map[row][col] = '1'
                        else:
                            self.map[row][col] = '0'
                        if '1' not in self.map[row]:
                            self.map[row] = ['0']

    def print(self, screen, zoom):

        # print grille/quadrillage
        for x in range(self.s_w//2+int(self.x_slide), -1, int(-(self.cell_size+1)*zoom)):
            if self.mode_grille == 1:
                pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, self.s_h), int(1*zoom))
            for y in range(self.s_h//2+int(self.y_slide), -1, int(-(self.cell_size+1)*zoom)):
                if self.mode_grille == 1:
                    pygame.draw.line(screen, (0, 0, 0), (0, y), (self.s_w, y), int(1*zoom))
                else:
                    pygame.draw.circle(screen, (0, 0, 0), (x, y), int(1*zoom))
            for y in range(self.s_h//2+int(self.y_slide), self.s_h+1, int((self.cell_size+1)*zoom)):
                if self.mode_grille == 1:
                    pygame.draw.line(screen, (0, 0, 0), (0, y), (self.s_w, y), int(1*zoom))
                else:
                    pygame.draw.circle(screen, (0, 0, 0), (x, y), int(1*zoom))
        for x in range(self.s_w//2+int(self.x_slide), self.s_w+1, int((self.cell_size+1)*zoom)):
            if self.mode_grille == 1:
                pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, self.s_h), int(1*zoom))
            for y in range(self.s_h//2+int(self.y_slide), -1, int(-(self.cell_size+1)*zoom)):
                if self.mode_grille == 1:
                    pygame.draw.line(screen, (0, 0, 0), (0, y), (self.s_w, y), int(1*zoom))
                else:
                    pygame.draw.circle(screen, (0, 0, 0), (x, y), int(1*zoom))
            for y in range(self.s_h//2+int(self.y_slide), self.s_h+1, int((self.cell_size+1)*zoom)):
                if self.mode_grille == 1:
                    pygame.draw.line(screen, (0, 0, 0), (0, y), (self.s_w, y), int(1*zoom))
                else:
                    pygame.draw.circle(screen, (0, 0, 0), (x, y), int(1*zoom))

        # to show numbers
        font = pygame.font.SysFont("ArialBlack", int(4 * zoom))
        for i in range(self.map_size[0]):
            pos_x = (int((self.cell_size+1)*zoom)*i + int(self.x_slide) - int((self.s_w//2-self.s_w//2/zoom)*zoom))
            # middle
            text = font.render('{}'.format(i), True, (0, 250, 0))
            screen.blit(text, (2+pos_x, self.s_h//2+1+self.y_slide))
            # topleft
            text = font.render('{}'.format(i), True, (250, 0, 0))
            screen.blit(text, (2+pos_x, self.s_h//4-int((self.s_h//4-self.s_h//4/zoom)*zoom)+1+self.y_slide))
            # bottomright
            text = font.render('{}'.format(i), True, (0, 0, 250))
            screen.blit(text, (2+pos_x, 3*self.s_h//4+int((self.s_h//4-self.s_h//4/zoom)*zoom)+1+self.y_slide))
        for j in range(self.map_size[1]):
            pos_y = (int((self.cell_size+1)*zoom)*j + int(self.y_slide) - int((self.s_h//2-self.s_h//2/zoom)*zoom))
            # middle
            text = font.render('{}'.format(j), True, (0, 250, 0))
            screen.blit(text, (self.s_w//2+2+self.x_slide, 1+pos_y))
            # topleft
            text = font.render('{}'.format(j), True, (250, 0, 0))
            screen.blit(text, (self.s_w//4-int((self.s_w//4-self.s_w//4/zoom)*zoom)+2+self.x_slide, 1+pos_y))
            # bottomright
            text = font.render('{}'.format(j), True, (0, 0, 250))
            screen.blit(text, (3*self.s_w//4+int((self.s_w//4-self.s_w//4/zoom)*zoom)+2+self.x_slide, 1+pos_y))

        # to visualize the center
        pygame.draw.circle(screen, "green", (self.s_w//2+self.x_slide, self.s_h//2+self.y_slide), 4*zoom)

        # print alive cells
        for row in range(self.map_size[0]):
            if len(self.map[row]) != 1:
                for col in range(self.map_size[1]):
                    if self.map[row][col] == '1':
                        pos_x = (int((self.cell_size+1)*zoom)*row + int(self.x_slide) - int((self.s_w//2-self.s_w//2/zoom)*zoom))
                        pos_y = (int((self.cell_size+1)*zoom)*col + int(self.y_slide) - int((self.s_h//2-self.s_h//2/zoom)*zoom))
                        fct.pygame_draw_square(screen, (0, 0, 200), (pos_x, pos_y), int((self.cell_size+1)*zoom), zoom)

    def empty_map(self):
        self.map = []
        for i in range(self.map_size[0]):
            self.map.append(['0'])

    def save_map(self):
        with open("map.txt", 'w') as f:
            for row in range(self.map_size[0]):
                if '1' in self.map[row]:
                    f.write(";".join(self.map[row]))
                else:
                    f.write('0')
                f.write('\n')

    def load_map(self):
        self.map = []
        with open("map.txt", 'r') as f:
            line = f.readline()
            while line != "":
                self.map.append(line.strip('\n').split(';'))
                line = f.readline()

    # def next_iteration(self):
