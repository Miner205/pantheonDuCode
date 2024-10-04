import pygame
import functions as fct


class Game:
    def __init__(self, size):
        self.map = []
        self.map_size = size   # nb of cells, like (100, 100).
        self.empty_map()
        self.iteration = 0

    def update(self, event):
        print('2')

    def print(self, screen, zoom, x_slide, y_slide):
        for row in range(self.map_size[0]):
            if len(self.map[row]) != 1:
                for col in range(self.map_size[1]):
                    if self.map[row][col] == '1':
                        pos = (1*(row+1)+int(15*zoom)*row+int(x_slide)-int(800*zoom), 1*(col+1)+int(15*zoom)*col+int(y_slide)-int(800*zoom))
                        fct.pygame_draw_square(screen, (0, 0, 200), pos, int(15*zoom))

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

    # def modify_map(self, cell_coords):


    # def next_iteration(self):
