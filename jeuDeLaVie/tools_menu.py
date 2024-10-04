import pygame
from button import Button
from textezone import TextZone


class ToolsMenu:
    # menu ouvert avec click droit, où on choisit les actions possibles
    def __init__(self, x=0, y=0):
        self.which_submenu = ['0']  # 1st char for the actual menu ; next char are for the previous menus
        # ; if num_submenu[0] == '0' : del/reset ToolsMenu
        self.width = 15*10
        self.height = 32
        self.nb_of_submenu = 4
        self.border_margin = 5
        self.rect = pygame.Rect(x, y, self.width+self.border_margin*2, self.height*self.nb_of_submenu+self.border_margin*2)
        self.all_button = {}
        self.all_textzone = {}
        self.button_to_del = []
        self.textzone_to_del = []

    def update(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # open menu    ;; pygame.mouse.get_pressed()[2]
            self.rect.x, self.rect.y = event.pos
            self.which_submenu = ['1', '0']
            self.all_button.clear()
            self.all_textzone.clear()

        elif self.which_submenu[0] != '0' and event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
            self.exit_menu()

        for button in self.all_button.keys():
            if self.all_button[button].use(event):
                if button == "back":
                    self.which_submenu[0] = self.which_submenu.pop()
                    if self.which_submenu[0] == '0':
                        self.all_textzone.clear()
                else:
                    if button == "1Creation":
                        self.which_submenu[0] = '2'
                        self.which_submenu.append(button[0])
                    elif button == "1Save_Load":
                        self.which_submenu[0] = '3'
                        self.which_submenu.append(button[0])

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

        if self.which_submenu[0] == '1' and "1Erase" not in self.all_button.keys():
            self.all_button["1Erase"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, self.height)
            self.all_button["1Creation"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+32, self.width, self.height)
            self.all_button["1Save_Load"] = Button(self.rect.x+self.border_margin, self.rect.y+self.border_margin+32*2, self.width, self.height)
            self.all_textzone["1Erase"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.width, False, "Delete all cells")
            self.all_textzone["1Creation"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+32, self.width, False, "pré-concu")
            self.all_textzone["1Save_Load"] = TextZone(self.rect.x+self.border_margin, self.rect.y+self.border_margin+32*2, self.width, False, "Save&Load map")
            self.nb_of_submenu = 4

        if self.which_submenu[0] == '2' and "2Overlays" not in self.all_button.keys():

            self.nb_of_submenu = 3


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
                    lens.append(len(self.all_textzone[textzone].user_text))
            if max(lens) * 15 != self.width:
                self.modify_width(max(lens) * 15)
            del lens

    def exit_menu(self):
        self.which_submenu = ['0']
        self.all_button.clear()
        self.all_textzone.clear()

    def modify_width(self, new_width):
        self.width = new_width
        self.rect = pygame.Rect(self.rect.x, self.rect.y, new_width+self.border_margin*2, self.rect.height)
        for textzone in self.all_textzone.values():
            textzone.modify_width(new_width)
        for button in self.all_button.values():
            button.modify_width(new_width)

    def print(self, screen):
        if self.which_submenu[0] != '0':
            pygame.draw.rect(screen, (230, 230, 230), self.rect)

            for textzone in self.all_textzone.values():
                textzone.draw(screen)

            '''for button in self.all_button.values():  # for debugging
                button.print(screen)'''
