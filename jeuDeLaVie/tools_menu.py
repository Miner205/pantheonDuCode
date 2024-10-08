import pygame
from button import Button
from textezone import TextZone
from toggle import Toggle


class ToolsMenu:
    # menu ouvert avec click droit, où on choisit les actions possibles
    def __init__(self, game, screen, screen_width, screen_height, x=0, y=0):
        self.which_submenu = ['0']  # 1st char for the actual menu ; next char are for the previous menus
        # ; if num_submenu[0] == '0' : del/reset ToolsMenu
        self.width = 15*10
        self.height = 32
        self.nb_of_submenu = 4
        self.border_margin = 5
        self.rect = pygame.Rect(x, y, self.width+self.border_margin*2, self.height*self.nb_of_submenu+self.border_margin*2)
        self.all_button = {}
        self.all_textzone = {}
        self.all_toggle = {}
        self.all_toggle_state = {"1Detailed_color": False}
        self.button_to_del = []
        self.textzone_to_del = []
        self.toggle_to_del = []

        self.game = game
        self.screen = screen
        self.screen_width, self.screen_height = screen_width, screen_height

    def update(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # open menu    ;; pygame.mouse.get_pressed()[2]
            self.rect.x, self.rect.y = event.pos
            self.which_submenu = ['1', '0']
            self.all_button.clear()
            self.all_textzone.clear()
            self.all_toggle.clear()

        elif self.which_submenu[0] != '0' and event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
            self.exit_menu()

        for toggle in self.all_toggle.keys():
            self.all_toggle[toggle].use(event)
            self.all_toggle_state[toggle] = self.all_toggle[toggle].toggle_state

        for textzone in self.all_textzone.keys():
            self.all_textzone[textzone].use(event)

        for button in self.all_button.keys():
            if self.all_button[button].use(event):
                if button == "9PufferTwoCinq" or button == "9Rbreeder" or button == "9Vingt" or button == "9twoTruc":
                    nb_of_cells = 500
                    cell_size = 1
                    self.game.iteration = 0
                    self.game.play_pause_button_state = 0
                    self.game.mode_grille = 0
                    self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                    self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                    self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                    self.game.empty_map()
                elif button == "7R_pentomino" or button == "9aSmoker" or button == "9aTruc" or button == "9Max" or button == "9aRake" or button == "7Bunnies":  # change size of screen & map if needed
                    nb_of_cells = 200
                    cell_size = 4
                    self.game.iteration = 0
                    self.game.play_pause_button_state = 0
                    self.game.mode_grille = 0
                    self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                    self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                    self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                    self.game.empty_map()
                elif self.game.map_size != (100, 100) and button != "back" and (self.which_submenu[0] == "4" or self.which_submenu[0] == "5" or self.which_submenu[0] == "6"
                                                                          or self.which_submenu[0] == '7' or self.which_submenu[0] == '8' or self.which_submenu[0] == '9'):
                    nb_of_cells = 100
                    cell_size = 8
                    self.game.iteration = 0
                    self.game.play_pause_button_state = 0
                    self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                    self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                    self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                    self.game.empty_map()

                if button == "back":
                    self.which_submenu[0] = self.which_submenu.pop()
                    if self.which_submenu[0] == '0':
                        self.all_textzone.clear()
                        self.all_toggle.clear()
                else:
                    if button == "1Creation":
                        self.which_submenu[0] = '2'
                        self.which_submenu.append(button[0])
                    elif button == "1Save_Load":
                        self.which_submenu[0] = '3'
                        self.which_submenu.append(button[0])
                    elif button == "3Save":
                        if self.game.map_size == (100, 100):
                            self.game.save_map("vos_créations/"+self.all_textzone["3filename"].user_text+"_100x100")
                        elif self.game.map_size == (200, 200):
                            self.game.save_map("vos_créations/"+self.all_textzone["3filename"].user_text+"_200x200")
                        elif self.game.map_size == (500, 500):
                            self.game.save_map("vos_créations/"+self.all_textzone["3filename"].user_text+"_500x500")
                    elif button == "3Load":
                        if self.game.map_size == (100, 100):
                            self.game.load_map("vos_créations/"+self.all_textzone["3filename"].user_text+"_100x100")
                        elif self.game.map_size == (200, 200):
                            self.game.load_map("vos_créations/"+self.all_textzone["3filename"].user_text+"_200x200")
                        elif self.game.map_size == (500, 500):
                            self.game.load_map("vos_créations/"+self.all_textzone["3filename"].user_text+"_500x500")
                    elif button == "2Structure_stable":
                        self.which_submenu[0] = '4'
                        self.which_submenu.append(button[0])
                    elif button[0] == "4":
                        self.game.load_map("pré_concus/structures_stables/"+self.all_textzone[button].user_text)
                    elif button == "2Oscillateurs":
                        self.which_submenu[0] = '5'
                        self.which_submenu.append(button[0])
                    elif button[0] == "5":
                        self.game.load_map("pré_concus/oscillateurs/"+self.all_textzone[button].user_text)
                    elif button == "2Vaisseaux":
                        self.which_submenu[0] = '6'
                        self.which_submenu.append(button[0])
                    elif button[0] == "6":
                        self.game.load_map("pré_concus/vaisseaux/"+self.all_textzone[button].user_text)
                    elif button == "2Mathusalems":
                        self.which_submenu[0] = '7'
                        self.which_submenu.append(button[0])
                    elif button[0] == "7":
                        self.game.load_map("pré_concus/mathusalems/"+self.all_textzone[button].user_text)
                    elif button == "2Canons":
                        self.which_submenu[0] = '8'
                        self.which_submenu.append(button[0])
                    elif button[0] == "8":
                        self.game.load_map("pré_concus/canons/"+self.all_textzone[button].user_text)
                    elif button == "2Autres":
                        self.which_submenu[0] = '9'
                        self.which_submenu.append(button[0])
                    elif button[0] == "9":
                        self.game.load_map("pré_concus/autres/"+self.all_textzone[button].user_text)
                    elif button == "1CentCells":
                        nb_of_cells = 100
                        cell_size = 8
                        self.game.iteration = 0
                        self.game.play_pause_button_state = 0
                        self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                        self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                        self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                        self.game.empty_map()
                    elif button == "1DeuxCentCells":
                        nb_of_cells = 200
                        cell_size = 4
                        self.game.iteration = 0
                        self.game.play_pause_button_state = 0
                        self.game.mode_grille = 0
                        self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                        self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                        self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                        self.game.empty_map()
                    elif button == "1CinqCentCells":
                        nb_of_cells = 500
                        cell_size = 1
                        self.game.iteration = 0
                        self.game.play_pause_button_state = 0
                        self.game.mode_grille = 0
                        self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                        self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                        self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                        self.game.empty_map()

                if (self.game.map_size != (100, 100) and button != "7R_pentomino" and button != "9aSmoker" and button != "9aTruc" and button != "9Max"
                        and button != "9PufferTwoCinq" and button != "9Rbreeder" and button != "9Vingt" and button != "9twoTruc" and button != "9aRake"
                        and button != "7Bunnies" and (
                        self.which_submenu[0] == "4" or self.which_submenu[0] == "5" or self.which_submenu[0] == "6" or
                        self.which_submenu[0] == '7' or self.which_submenu[0] == '8' or self.which_submenu[0] == '9')):  # change size of screen & map if needed
                    nb_of_cells = 100
                    cell_size = 8
                    self.game.iteration = 0
                    self.game.play_pause_button_state = 0
                    self.screen_width, self.screen_height = nb_of_cells * (cell_size + 1), nb_of_cells * (cell_size + 1)
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                    self.game.map_size, self.game.cell_size = (nb_of_cells, nb_of_cells), cell_size
                    self.game.s_w, self.game.s_h = self.screen_width, self.screen_height
                    self.game.empty_map()

        for button in self.all_button.keys():
            if self.which_submenu[0] == '0' or (button != "back" and button[0] != self.which_submenu[0]):
                self.button_to_del.append(button)
        if self.button_to_del:
            for elt in self.button_to_del:
                del (self.all_button[elt])
            self.button_to_del.clear()

        for textzone in self.all_textzone.keys():
            if textzone != "back" and textzone[0] != self.which_submenu[0]:
                self.textzone_to_del.append(textzone)
        if self.textzone_to_del:
            for elt in self.textzone_to_del:
                del (self.all_textzone[elt])
            self.textzone_to_del.clear()

        for toggle in self.all_toggle.keys():
            if toggle != "back" and toggle[0] != self.which_submenu[0]:
                self.toggle_to_del.append(toggle)
        if self.toggle_to_del:
            for elt in self.toggle_to_del:
                del (self.all_toggle[elt])
            self.toggle_to_del.clear()

        if self.which_submenu[0] == '1' and "1Creation" not in self.all_button.keys():
            self.all_button["1Creation"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["1Creation"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "Pré-concus")
            self.all_button["1Save_Load"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["1Save_Load"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "Save&Load map")
            self.all_toggle["1Detailed_color"] = Toggle(self.rect.x + self.border_margin,
                                                           self.rect.y + self.border_margin+self.height*2,
                                                           "Detailed cell color",
                                                           self.all_toggle_state["1Detailed_color"], self.width,
                                                           self.height)
            self.all_button["1CentCells"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, self.height)
            self.all_textzone["1CentCells"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, False, "map = 100*100")
            self.all_button["1DeuxCentCells"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, self.height)
            self.all_textzone["1DeuxCentCells"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, False, "map = 200*200")
            self.all_button["1CinqCentCells"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, self.height)
            self.all_textzone["1CinqCentCells"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, False, "map = 500*500")
            self.nb_of_submenu = 7

        if self.which_submenu[0] == '2' and "2Structure_stable" not in self.all_button.keys():
            self.all_button["2Structure_stable"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["2Structure_stable"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "Structures stables/Still lifes")
            self.all_button["2Oscillateurs"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["2Oscillateurs"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "Oscillateurs/Oscillators")
            self.all_button["2Vaisseaux"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, self.height)
            self.all_textzone["2Vaisseaux"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, False, "Vaisseaux/Spaceships")
            self.all_button["2Mathusalems"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, self.height)
            self.all_textzone["2Mathusalems"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, False, "Mathusalems/Methuselahs")
            self.all_button["2Canons"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, self.height)
            self.all_textzone["2Canons"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, False, "Canons/Guns")
            self.all_button["2Autres"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, self.height)
            self.all_textzone["2Autres"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, False, "Autres")
            self.nb_of_submenu = 7

        if self.which_submenu[0] == '3' and "3filename" not in self.all_textzone.keys():
            self.all_textzone["3filename"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, True, "mymap", "txt name")
            self.all_button["3Save"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_button["3Load"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, self.height)
            self.all_textzone["3Save"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "Save map as txt")
            self.all_textzone["3Load"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, False, "Load a txt into map")
            self.nb_of_submenu = 4

        if self.which_submenu[0] == '4' and "4Block" not in self.all_button.keys():
            self.all_button["4Block"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["4Block"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "block")
            self.all_button["4Beehive"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["4Beehive"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "beehive")
            self.all_button["4Boat"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, self.height)
            self.all_textzone["4Boat"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, False, "boat")
            self.all_button["4Ship"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, self.height)
            self.all_textzone["4Ship"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, False, "ship")
            self.all_button["4Loaf"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, self.height)
            self.all_textzone["4Loaf"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, False, "loaf")
            self.all_button["4Pond"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, self.height)
            self.all_textzone["4Pond"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, False, "pond")
            self.all_button["4Cthulhu"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*6, self.width, self.height)
            self.all_textzone["4Cthulhu"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*6, self.width, False, "cthulhu")
            self.all_button["4Honey_farm"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*7, self.width, self.height)
            self.all_textzone["4Honey_farm"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*7, self.width, False, "honey farm (4 beehives)")
            self.all_button["4Blocks"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*8, self.width, self.height)
            self.all_textzone["4Blocks"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*8, self.width, False, "4 blocks")

            self.nb_of_submenu = 10

        if self.which_submenu[0] == '5' and "5Blinker" not in self.all_button.keys():
            self.all_button["5Blinker"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["5Blinker"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "blinker (period 2)")
            self.all_button["5Blinkers"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["5Blinkers"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "4 blinkers")
            self.all_button["5Beacon"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, self.height)
            self.all_textzone["5Beacon"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, False, "beacon (period 2)")
            self.all_button["5Toad"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, self.height)
            self.all_textzone["5Toad"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, False, "toad (period 2)")
            self.all_button["5Pulsar"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, self.height)
            self.all_textzone["5Pulsar"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, False, "pulsar (period 3)")
            self.all_button["5sept"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, self.height)
            self.all_textzone["5sept"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, False, "76 P7 (period 7)")
            self.all_button["5PentaD"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*6, self.width, self.height)
            self.all_textzone["5PentaD"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*6, self.width, False, "penta-decathlon (period 15)")
            self.all_button["5big_one"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*7, self.width, self.height)
            self.all_textzone["5big_one"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*7, self.width, False, "(period 177)")

            self.nb_of_submenu = 9

        if self.which_submenu[0] == '6' and "6Glider" not in self.all_button.keys():
            self.all_button["6Glider"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["6Glider"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "glider")
            self.all_button["6Weight_spaceship"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["6Weight_spaceship"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "light, middle and heavy weight_spaceships")
            self.all_button["6Canada_goose"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, self.height)
            self.all_textzone["6Canada_goose"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, False, "canada goose")
            self.all_button["6Papillon"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, self.height)
            self.all_textzone["6Papillon"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, False, "60P5H2V0")

            self.nb_of_submenu = 5

        if self.which_submenu[0] == '7' and "7R_pentomino" not in self.all_button.keys():
            self.all_button["7R_pentomino"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["7R_pentomino"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "the R-pentomino")
            self.all_button["7Bunnies"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["7Bunnies"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "Bunnies")

            self.nb_of_submenu = 3

        if self.which_submenu[0] == '8' and "9Gosper_glider_gun" not in self.all_button.keys():
            self.all_button["8Gosper_glider_gun"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["8Gosper_glider_gun"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "Gosper glider gun")

            self.nb_of_submenu = 2

        if self.which_submenu[0] == '9' and "9aSmoker" not in self.all_button.keys():
            self.all_button["9aSmoker"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_textzone["9aSmoker"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "a smoker; a puffer")
            self.all_button["9aTruc"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, self.height)
            self.all_textzone["9aTruc"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height, self.width, False, "a single block-laying switch engine")
            self.all_button["9PufferTwo"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, self.height)
            self.all_textzone["9PufferTwo"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*2, self.width, False, "Puffer 2")
            self.all_button["9aRake"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, self.height)
            self.all_textzone["9aRake"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*3, self.width, False, "the space rake")
            self.all_button["9twoTruc"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, self.height)
            self.all_textzone["9twoTruc"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*4, self.width, False, "two single block-layi truc (500x500)")
            self.all_button["9Max"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, self.height)
            self.all_textzone["9Max"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*5, self.width, False, "a spacefiller (Max)")
            self.all_button["9PufferTwoCinq"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*6, self.width, self.height)
            self.all_textzone["9PufferTwoCinq"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*6, self.width, False, "Puffer 2 (500x500)")
            self.all_button["9Rbreeder"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*7, self.width, self.height)
            self.all_textzone["9Rbreeder"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*7, self.width, False, "Riley's breeder (500x500)")
            self.all_button["9Vingt"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*8, self.width, self.height)
            self.all_textzone["9Vingt"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+self.height*8, self.width, False, "20-cell quadratic growth (500x500)")

            self.nb_of_submenu = 10

        if self.which_submenu[0] != '0':
            self.all_button["back"] = Button(self.rect.x + self.border_margin,
                                             self.rect.y + self.border_margin + self.height * (self.nb_of_submenu - 1),
                                             self.width, self.height)
            self.all_textzone["back"] = TextZone(self.rect.x + self.border_margin,
                                                 self.rect.y + self.border_margin + self.height * (
                                                             self.nb_of_submenu - 1), self.width, False, "back")
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width + self.border_margin * 2,
                                    self.height * self.nb_of_submenu + self.border_margin * 2)

            lens = []
            for textzone in self.all_textzone.keys():
                if textzone not in self.textzone_to_del:
                    if len(self.all_textzone[textzone].user_text) < 24:
                        lens.append(len(self.all_textzone[textzone].user_text)+len(self.all_textzone[textzone].name)-1)
                    else:
                        lens.append(len(self.all_textzone[textzone].user_text)-7)
            for toggle in self.all_toggle.keys():
                if toggle not in self.toggle_to_del:
                    lens.append(len(self.all_toggle[toggle].name)-3)
            if max(lens) * 15 != self.width:
                self.modify_width(max(lens) * 15)
            del lens

    def exit_menu(self):
        self.which_submenu = ['0']
        self.all_button.clear()
        self.all_textzone.clear()
        self.all_toggle.clear()

    def modify_width(self, new_width):
        self.width = new_width
        self.rect = pygame.Rect(self.rect.x, self.rect.y, new_width+self.border_margin*2, self.rect.height)
        for textzone in self.all_textzone.values():
            textzone.modify_width(new_width)
        for button in self.all_button.values():
            button.modify_width(new_width)
        for toggle in self.all_toggle.values():
            toggle.modify_width(new_width)

    def print(self, screen):
        if self.which_submenu[0] != '0':
            pygame.draw.rect(screen, (230, 230, 230), self.rect)

            for toggle in self.all_toggle.values():
                toggle.print(screen)

            for textzone in self.all_textzone.values():
                textzone.draw(screen)

            '''for button in self.all_button.values():  # for debugging
                button.print(screen)'''
