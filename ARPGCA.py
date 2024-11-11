from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import json
import random
import pygame
import threading
import os



class App:

    def __init__(self, master):
        
        master.title('Alien RPG Companion App')
        master.geometry('640x480+100+100')
        master.resizable(False,False)

    #Global Variables
        aGreen = '#00FF00'
        aDGreen = '#009900'
        aBlack = '#1C1C1C'

    #Global Styles
        self.style = ttk.Style()

        #Label Style
        self.style.configure('White.TLabel', font = ('Arial', 10), foreground = 'white', background = aBlack)
        self.style.configure('Alien.TLabel', font = ('OCR A Extended', 12, 'bold'), background = aGreen, foreground = aBlack)
        self.style.configure('Inv.Alien.TLabel', font = ('OCR A Extended', 12), background = aBlack, foreground = 'white')
        self.style.configure('Header.Alien.TLabel', font = ('OCR A Extended', 20, 'bold'), foreground = 'white', background = aBlack)
        self.style.configure('SmHeader.Alien.TLabel', font = ('OCR A Extended', 16, 'bold'), foreground = 'white', background = aBlack)
        self.style.configure('NPC.TLabel', font = ('OCR A Extended', 8), background = aGreen)

        #Button Style
        self.style.configure('Alien.TButton', font = ('OCR A Extended', 14, 'bold'), foreground = aDGreen, background = aBlack, padding = 10, relief = 'raised')
        self.style.configure('Small.TButton', font = ('OCR A Extended', 10), foreground = aDGreen, background = aBlack)
        self.style.configure('Green.Small.TButton', font = ('OCR A Extended', 10), foreground = aBlack, background = aGreen)
        self.style.configure('NPC.TButton', background = aGreen, foreground = aBlack, justify = 'center', font = ('OCR A Extended', 8))

        #Frame Style
        self.style.configure('Alien.TFrame', background = aBlack, relief = 'flat')
        self.style.configure('NPC.TFrame', background = aGreen, relief = 'flat')
        self.style.configure('Dice.TFrame', background = '#182318')
        self.style.configure('MT.TFrame', background = aBlack)

        #Scroll Style
        self.style.configure('Alien.Vertical.TScrollbar', background = aBlack)
        self.style.configure('Alien.TCanvas', background = aBlack, relief = 'flat')

        #Combobox Style
        self.style.configure('Alien.TCombobox', background = aBlack)

        #Entry Style
        self.style.configure('Alien.TEntry', background = aBlack)


    #Global Photos
        image_root = f'{os.getcwd()}\\images\\'

        self.top_menu_bg = PhotoImage(file = image_root + 'top_menu_bg.png')
        self.pm_bg_init = PhotoImage(file = image_root + 'pm_bg_init.png')
        self.pm_bg_new = PhotoImage(file = image_root + 'pm_bg_new.png')
        self.pm_bg_load = PhotoImage(file = image_root + 'pm_bg_load.png')
        self.cs_bg_init = PhotoImage(file = image_root + 'cs_bg_init.png')
        self.dr_bg_init = PhotoImage(file = image_root + 'dr_bg_init.png')
    
        frame_player = PhotoImage(file = image_root + 'frame_player.png')
        frame_player_small = PhotoImage(file = image_root + 'frame_player_small.png')
        frame_synth = PhotoImage(file = image_root + 'frame_synth.png')
        frame_synth_small = PhotoImage(file = image_root + 'frame_synth_small.png')
        frame_enemy = PhotoImage(file = image_root + 'frame_enemy.png')
        frame_enemy_small = PhotoImage(file = image_root + 'frame_enemy_small.png')
        frame_friendly = PhotoImage(file = image_root + 'frame_friendly.png')
        frame_friendly_small = PhotoImage(file = image_root + 'frame_friendly_small.png')

        mt_button_on = PhotoImage(file = image_root + 'mt_button_on.png')
        mt_button_off = PhotoImage(file = image_root + 'mt_button_off.png')
        mt_top_panel = PhotoImage(file = image_root + 'mt_top_panel.png')
        mt_bottom_panel = PhotoImage(file = image_root + 'mt_bottom_panel.png')

        dice_1b = PhotoImage(file = image_root + 'dice_1b.png')
        dice_1s = PhotoImage(file = image_root + 'dice_1s.png')
        dice_2b = PhotoImage(file = image_root + 'dice_2b.png')
        dice_2s = PhotoImage(file = image_root + 'dice_2s.png')
        dice_3b = PhotoImage(file = image_root + 'dice_3b.png')
        dice_3s = PhotoImage(file = image_root + 'dice_3s.png')
        dice_4b = PhotoImage(file = image_root + 'dice_4b.png')
        dice_4s = PhotoImage(file = image_root + 'dice_4s.png')
        dice_5b = PhotoImage(file = image_root + 'dice_5b.png')
        dice_5s = PhotoImage(file = image_root + 'dice_5s.png')
        dice_6b = PhotoImage(file = image_root + 'dice_6b.png')
        dice_6s = PhotoImage(file = image_root + 'dice_6s.png')

        dice_base = PhotoImage(file = image_root + 'dice_base.png')
        dice_stress = PhotoImage(file = image_root + 'dice_stress.png')


###---TOP MENU---###

        top_menu = ttk.Frame(master, width = 640, height = 480)
        top_menu.grid(sticky = 'nsew')

            #Labels
        ttk.Label(top_menu, image = self.top_menu_bg).place(x = 0, y = 0)
        ttk.Label(top_menu, style = 'Header.Alien.TLabel', text = 'Alien RPG Companion App', foreground= 'white', background= aBlack).place(relx = 0.5, rely = 0.25, anchor = 'center')
        ttk.Label(top_menu, text = 'Version 1.0.0', style = 'White.TLabel').place(relx = 0.5, rely = 0.35, anchor = 'center')

            # Buttons
        ttk.Button(top_menu, style = 'Alien.TButton', text = '  Party  Manager  ', command = lambda: pm_start()).place(relx = 0.3, rely = 0.645, anchor = 'center')    
        ttk.Button(top_menu, style = 'Alien.TButton', text = 'Initiative Tracker', command = lambda: cs_start()).place(relx = 0.7, rely = 0.645, anchor = 'center')
        ttk.Button(top_menu, style = 'Alien.TButton', text = '  Motion Tracker  ', command = lambda: mt_start()).place(relx = 0.3, rely = 0.75, anchor = 'center')
        ttk.Button(top_menu, style = 'Alien.TButton', text = '   Dice  Roller   ', command = lambda: dr_start()).place(relx = 0.7, rely = 0.75, anchor = 'center')


###---PARTY MANAGER---###

    #Initialize Party Manager
        def pm_start():

    #Party Top Menu Frames
            self.pm_main = ttk.Frame(master, width = 640, height = 480)
            self.pm_main.pack_propagate(False)
            self.pm_main.grid_propagate(False)
            self.pm_main.grid(row = 0, column = 0, sticky = 'nsew')

            self.pm_bg = ttk.Label(self.pm_main, image = self.pm_bg_init)
            self.pm_bg.place(x=0,y=0)

            self.pm_select = ttk.Frame(self.pm_main, style= 'Green.Alien.TFrame')
            self.pm_select.place(relx = 0.5, rely = 0.5, anchor = 'center')

    #Party Menu Buttons
            self.pm_new = ttk.Button(self.pm_main, style = 'Alien.TButton', text = 'New Party', command = lambda: new_party())
            self.pm_new.place(relx = 0.5, y = 204, anchor = 'center')

            self.pm_load = ttk.Button(self.pm_main, style = 'Alien.TButton', text = 'Load Party', command = lambda: load_party())
            self.pm_load.place(relx = 0.5, y = 279, anchor = 'center')

            self.pm_back = ttk.Button(self.pm_main, style = 'Small.TButton', text = 'Back', command = lambda: top_menu.lift())
            self.pm_back.place(relx = 0.5, y = 440, anchor = 'center')

            self.pm_main.lift()

    #Reset Party Manager back to Start
        def pm_reset():
            self.pm_main.destroy()
            pm_start()


##NEW PARTY##
        def new_party():
            self.pm_new.destroy()
            self.pm_load.destroy()
            self.pm_bg.config(image = self.pm_bg_new)
            self.pm_back.config(text = 'Cancel', command = lambda: new_cancel())

                #Variables
            self.party = []
            self.all_parties = {}
            self.i = 0

                #Add Party Frames
            ttk.Label(self.pm_main, text = 'New Party', style = 'Alien.TLabel').place(relx = 0.5, y = 30, anchor = 'center')

            self.pm_create = ttk.Frame(self.pm_main, height= 165, width = 480, padding= 5, style = 'Alien.TFrame')
            self.pm_create.grid_propagate(False)
            self.pm_create.place(relx = 0.5, y = 50, anchor = 'n')
                                       
            self.pm_info = ttk.Frame(self.pm_main, height = 150, width = 480, style = 'Alien.TFrame')
            self.pm_info.grid_propagate(False)
            self.pm_info.place(relx = 0.5, y = 270, anchor = 'n')

                #Party Create Widgets
            self.pm_name_label = ttk.Label(self.pm_create, text = "What is the name of your party?", style='Inv.Alien.TLabel')
            self.pm_name_label.grid(row = 0, column=0, pady = 9, padx = 5)

            self.party_name = ttk.Entry(self.pm_create, width = 20, style = 'Alien.TEntry')
            self.party_name.grid(row = 0, column = 1, pady = 9, padx = 5)

            self.count_label = ttk.Label(self.pm_create, text = 'How many party members?', style = 'Inv.Alien.TLabel')
            self.count_label.grid(row = 1, column = 0, padx = 5, pady = 9, sticky = 'w')

            self.party_max = ttk.Combobox(self.pm_create, values = (1,2,3,4,5,6,7,8,9,10,11,12), state= 'readonly', width = 2, style = 'Alien.TCombobox')
            self.party_max.set(1)
            self.party_max.grid(row = 1, column = 1, padx = 5, pady = 9, stick = 'w')
            
            self.add_member = ttk.Button(self.pm_create, text = 'Add Party Member(s)', command = lambda: add_title(), style = 'Small.TButton')
            self.add_member.place(relx = 0.5, y = 145, anchor = 'center')

    #Save Party Name, Initialize Adding Members
        def add_title():
            with open('json\\save_data.json', 'r+') as party_data:
                existing_party_data = json.load(party_data)
                if self.party_name.get() in existing_party_data:
                    name_check = messagebox.askyesno(title = 'Overwrite Existing Party', message = f'{self.party_name.get()} already exists as a party.\n\nDo you wish to overwrite the existing data?')
                    if name_check == True:
                        add_member()
                    else:
                        pass
                else:
                    add_member()

    #Input Member Data to the Active Party
        def add_member():
            self.party_name.config(state = 'readonly')
            self.count_label.destroy()

                #Adjust Widgets
            ttk.Label(self.pm_info, text = f'Party Name: {self.party_name.get()}', style = 'SmHeader.Alien.TLabel').grid(row = 0, column = 0, sticky = 'w', padx = 10)
            ttk.Label(self.pm_create, text = f'Player {self.i+1}/{self.party_max.get()} Name: ', style='Inv.Alien.TLabel').grid(row = 1, column= 0, sticky = 'w', pady = 9, padx = 5) 

            self.party_member = ttk.Entry(self.pm_create, width = 20, style = 'Alien.TEntry')
            self.party_member.grid(row = 1, column = 1, pady = 9, padx = 5)

            ttk.Label(self.pm_create, text = 'Species:', style='Inv.Alien.TLabel').grid(row = 2, column=0, sticky = 'w', pady = 9, padx = 5)

            self.party_spec = ttk.Combobox(self.pm_create, width = 17, values = ('Human', 'Synth'), state = 'readonly', style = 'Alien.TCombobox')
            self.party_spec.set('Human')
            self.party_spec.grid(row = 2, column = 1, pady = 9, padx = 5)

            self.party_init = 0
            self.i += 1

            if self.i < int(self.party_max.get()):
                self.add_member.config(text = 'Next Player', command = lambda: member_input())
            else:
                self.add_member.config(text = 'Save Party', command = lambda: save_party())

    #Save Member Info to Party            
        def member_input():
            self.party.append([f'{self.party_member.get()}', f'{self.party_spec.get()}', self.party_init])
            if self.i >= 7:
                self.x = self.i % 6
                self.y = 1
            else:
                self.x = self.i
                self.y = 0
            ttk.Label(self.pm_info, text = f'Party Member {self.i}: {self.party[self.i-1][0]}', style = 'Inv.Alien.TLabel').grid(row = self.x, column = self.y, sticky = 'w', padx = 20)
            add_member()

    #Save Party Info to All_Parties
        def save_party():
            self.party.append([f'{self.party_member.get()}', f'{self.party_spec.get()}', self.party_init])
            if self.i == 12:
                self.x = 5
                self.y = 1
            elif 12 < self.i >= 7 :
                self.x = self.i % 6
                self.y = 1
            else:
                self.x = self.i
                self.y = 0
            self.all_parties.update({self.party_name.get():self.party})
            ttk.Label(self.pm_info, text = f'Party Member {self.i}: {self.party[self.i-1][0]}', style = 'Inv.Alien.TLabel').grid(row=self.x+1, column = self.y, sticky = 'w', padx = 20)

                # JSON SAVE TO FILE
            with open('json\\save_data.json', 'r+') as self.old_savedata:
                self.party_list = json.load(self.old_savedata)
                self.party_list.update(self.all_parties)
                self.new_savedata = json.dumps(self.party_list)

            with open('json\\save_data.json', 'w') as self.old_savedata:
                self.old_savedata.write(self.new_savedata)
                
                #Save Confirmation
            messagebox.showinfo(title = 'Party Saved', message = 'Your party has been saved!')
            self.selected_party = self.party_name.get()
            set_activeparty()
            self.add_member.destroy()
            pm_reset()
        
    #Cancel Button
        def new_cancel():
            self.new_cancel_result = messagebox.askokcancel(title = 'Cancel Party Creation', message = 'New party data will not be saved.\n\n Do you wish to continue?')
            if self.new_cancel_result == True:
                pm_reset()


##LOAD PARTY##
        def load_party():
            self.pm_new.destroy()
            self.pm_load.destroy()
            self.pm_bg.config(image = self.pm_bg_load)

                #Variables
            self.load_partyname = 'null'
            self.partynames_list = [] 

                #Read Saved Data from JSON
            with open('json\\save_data.json', 'r') as load_data:
                self.party_dict = json.load(load_data)

                #Update party_dict With Saved Parties
            for name in self.party_dict:
                self.partynames_list.append(name)   
            length = len(self.partynames_list)                   

                #Load Party Frames
            self.pm_canvas = Canvas(self.pm_main, height = 330, width = 205, scrollregion=(0,0,300,length*63), highlightthickness= 0, background = aBlack)
            self.pm_canvas.place(x = 55, y = 75)

            self.pm_scroll_frame = ttk.Frame(self.pm_main, height = 330, width = 15, style = 'Alien.TFrame')
            self.pm_scroll_frame.pack_propagate(False)
            self.pm_scroll_frame.place(x = 265, y = 75)
            
            self.pm_info = ttk.Frame(self.pm_main, height = 330, width = 230, style = 'Alien.TFrame')
            self.pm_info.pack_propagate(False)
            self.pm_info.place(x = 355, y = 75)

                #Load Party Widgets
            ttk.Label(self.pm_main, text = 'Load Party', style = 'Alien.TLabel').place(relx = 0.5, y = 30, anchor = 'center')
            
            self.pm_scroll = ttk.Scrollbar(self.pm_scroll_frame, orient= VERTICAL, command = self.pm_canvas.yview, style = 'Alien.Vertical.TScrollbar')
            self.pm_scroll.pack(side = LEFT, fill = Y)
            
            self.pm_buttons = ttk.Frame(self.pm_canvas, height = length*63, width = 205, borderwidth = 0, style = 'Alien.TFrame')
            self.pm_buttons.pack_propagate(False)
            self.pm_buttons.pack(anchor = 'nw', side = LEFT)

                #Load Party Configs
            self.pm_canvas.config(yscrollcommand=self.pm_scroll.set)
            self.pm_canvas.create_window(0, 0, anchor = 'nw', window = self.pm_buttons)
            
            self.pm_back.config(text = 'Cancel', command = lambda: pm_reset())

            if length <= 6:
                self.pm_scroll.forget()
                self.pm_canvas.place(x = 70, y = 75)
                self.pm_scroll_frame.place(x= 280, y = 75)

            

        #Pack Buttons Into party_load
            def button_pack(num):
                ttk.Button(self.pm_buttons, text = self.partynames_list[num], command = lambda: load_data(), style = 'Small.TButton').pack(ipady = 20, fill = X)
                def load_data():
                    if self.load_partyname == 'null':
                        self.load_partyname = ttk.Label(self.pm_info, text = f'{self.partynames_list[num]}\n', background = aBlack, font = ('OCR A Extended', 14, 'bold'), foreground = 'white')
                        self.load_partyname.pack(anchor = 'w')
                        n = 1
                        for mem in (self.party_dict[self.partynames_list[num]]):
                            self.load_partymember = ttk.Label(self.pm_info, text = f'Player {n}: {mem[0]}', background = aBlack, font = ('OCR A Extended', 10), foreground = 'white')
                            self.load_partymember.pack(anchor = 'w')
                            n += 1
                        self.selected_party = self.partynames_list[num]
                        select_party()
                    else:
                        self.load_partyname = 'null'
                        self.pm_info.destroy()
                        self.pm_info = ttk.Frame(self.pm_main, height = 330, width = 230, style = 'Alien.TFrame')
                        self.pm_info.pack_propagate(False)
                        self.pm_info.place(x = 355, y = 75)
                        load_data()
                if num < (length-1):
                    button_pack(num+1)
                else:
                    pass       
            button_pack(1)

    #Select Party Buttons Appear
        def select_party():
            ttk.Button(self.pm_info, text = 'Delete', command = lambda: delete_party(), style = 'Small.TButton').pack(anchor='s', side = BOTTOM, pady = 10)
            ttk.Button(self.pm_info, text = 'Select', command = lambda: set_activeparty(), style = 'Small.TButton').pack(anchor='s', side = BOTTOM)

    #Delete Selected Party
        def delete_party():

            def delete_data():
                with open('json\\save_data.json', 'r') as self.global_party:
                    self.deleting_dict = json.load(self.global_party)
                    self.deleting_dict.pop(self.selected_party)
                with open('json\\save_data.json', 'w') as self.global_party:
                    overwrite_dict = json.dumps(self.deleting_dict)
                    self.global_party.write(overwrite_dict) 

            with open('json\\active_party.json', 'r') as matching:
                matched_party = json.load(matching)
                matched_name = matched_party["active_party"]
                if matched_name == self.selected_party:
                    delete_party_result = messagebox.askyesno(title = 'Delete Active Party', message = f'{self.selected_party} is the active party.  Would you still like to delete {self.selected_party}?')
                    if delete_party_result == True:
                        delete_data()
                        self.selected_party = 'null'
                        overwrite_activeparty()
                        messagebox.showinfo(title = 'No Active Party', message = 'Party Deleted! \n\nNo active party is set.  Please select another party.')
                        pm_reset()
                        load_party()
                    else:
                        pass
                else:
                    delete_party_result = messagebox.askyesno(title = 'Delete Party', message = f'Are you sure you would like to delete {self.selected_party}?')
                    if delete_party_result == True:
                        delete_data()
                        pm_reset()
                        load_party()
                    else:
                        pass

    #Set Active Party
        def set_activeparty():
            set_active_result = messagebox.askyesno(title = 'Select Party', message = f'Would you like to set {self.selected_party} as the Active Party?')
            if set_active_result == True:
                overwrite_activeparty()
                messagebox.showinfo(title = 'Active Party Set', message = f'{self.selected_party} is now the active party!')
                pm_reset()
            else:
                pass

    #JSON Active Party Overwrite
        def overwrite_activeparty():
            with open('json\\active_party.json', 'w') as self.global_party:
                active_dict = {"active_party": self.selected_party}
                active_json = json.dumps(active_dict)
                self.global_party.write(active_json)




###---INITIATIVE TRACKER---###

    #CS Global Variables
        self.cs_on = False

    #Combat Sequencer Frames
        def cs_start():
            if self.cs_on == True:
                self.cs_main.lift()
            else:
                self.cs_on = True
                self.cs_main = ttk.Frame(master, width=640, height = 480, style = 'Alien.TFrame')
                self.cs_main.grid_propagate(False)
                self.cs_main.grid(row=0, column=0, sticky = 'nsew')

                self.cs_bg = ttk.Label(self.cs_main, image = self.cs_bg_init)
                self.cs_bg.place(x=0, y=0)

                self.cs_labelframe = ttk.Frame(self.cs_main, height = 25, width = 290, style = 'Alien.TFrame')
                self.cs_labelframe.pack_propagate(False)
                self.cs_labelframe.place(x = 95, y = 17)

                self.cs_orderframe = ttk.Frame(self.cs_main, height = 385, width = 87, style = 'Alien.TFrame')
                self.cs_orderframe.grid_propagate(False)
                self.cs_orderframe.place(x = 30, y = 75)

                self.cs_readoutframe = ttk.Frame(self.cs_main, height = 310, width = 445, style = 'Alien.TFrame')
                self.cs_readoutframe.pack_propagate(False)
                self.cs_readoutframe.grid_propagate(False)
                self.cs_readoutframe.place(x=155, y=75)

                self.cs_buttonframe = ttk.Frame(self.cs_main, height = 50, width = 445, style = 'Alien.TFrame')
                self.cs_buttonframe.pack_propagate(False)
                self.cs_buttonframe.place(x = 155, y = 410)

            #Load Active Party

                with open('json\\active_party.json', 'r') as global_party:
                    self.active_json = json.load(global_party)
                    self.active_name = self.active_json["active_party"]

                with open('json\\save_data.json', 'r') as save_data:
                    self.save_data = json.load(save_data)
                    self.active_party = (self.save_data[self.active_name])

                self.cs_new = ttk.Button(self.cs_buttonframe, text = 'New', command = lambda: cs_newcom(), style = 'Small.TButton')
                self.cs_new.place(relx = 0.15, rely = 0.5, anchor=CENTER)
                ttk.Button(self.cs_buttonframe, text = 'Back', command = lambda: cs_back(), style = 'Small.TButton').place(relx = 0.85, rely = 0.5, anchor = CENTER)

                self.start_initiative = ttk.Button(self.cs_buttonframe, text = 'Draw For Initiative', width = 21, command = lambda: cs_init_draw(), style = 'Small.TButton') #self.start_initiative doesn't place until draw_init()

                self.cs_main.lift()

    #Resets cs_main so that it can be pulled back up
        def cs_restart():
            self.cs_main.destroy()
            self.cs_on = False

    #Begin Combat
        def cs_newcom():
            self.cs_new.config(text = 'Start Over', command = lambda: (cs_restart(), cs_start()))

            self.cs_intro = ttk.Frame(self.cs_readoutframe, style = 'Alien.TFrame')
            self.cs_intro.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            self.cs_intro.pack_propagate(False)

            if self.active_name == 'null':
                ttk.Label(self.cs_intro, text = 'No active party selected,\nPlease select a party.',font = ('OCR A Extended', 16, 'bold'), style = 'Header.Alien.TLabel', justify = 'center').grid(row=0, column = 0, pady = 20)
                ttk.Button(self.cs_intro, text = 'Choose Party', command = lambda: (pm_start(), cs_restart()), style = 'Small.TButton').grid(row = 1, column = 0)
            else:

                ttk.Label(self.cs_intro, text = f'Start a new Combat with\n\n{self.active_name}?',font = ('OCR A Extended', 16, 'bold'), style = 'Header.Alien.TLabel', justify = 'center').grid(row = 0, column=0, columnspan=2, pady = 20)
                ttk.Button(self.cs_intro, text = 'Yes', command = lambda: begin_com(), style = 'Small.TButton').grid(row = 1, column = 1, pady = 20)
                ttk.Button(self.cs_intro, text = 'Choose Another Party', command = lambda: (pm_start(), cs_restart()), style = 'Small.TButton').grid(row = 1, column = 0)

    #Begin to Add NPCs
        def begin_com():
            ttk.Label(self.cs_labelframe, text = f'{self.active_name}', justify= 'center', style = 'SmHeader.Alien.TLabel').pack(side = TOP)
            cs_intro_recreate()
            ttk.Label(self.cs_intro, text = 'Number of Enemies', style = 'Inv.Alien.TLabel').grid(row = 0, column = 0, padx = 5)
            self.cs_combobox = ttk.Combobox(self.cs_intro, values = (1,2,3,4,5,6,7,8), state = 'readonly', width = 1, style = 'Alien.TCombobox')
            self.cs_combobox.set(1)
            self.cs_combobox.grid(row = 0, column = 1, padx = 5)
            ttk.Button(self.cs_intro, text = 'Add', command = lambda: cs_add_npc(self.cs_combobox.get()), style = 'Small.TButton').grid(row = 0, column = 2, padx = 5)

    #Iterate through Combobox
        def cs_add_npc(num):
            cs_intro_recreate()
            x = 0
            while x < int(num):
                cs_add_npctable(x)
                x += 1

    #Building ADD NPC Tables
        def cs_add_npctable(x):
            if x % 2 == 0:
                y = int(x/2)
                z = 0
            elif x % 2 == 1:
                y = int((x-1)/2) 
                z = 1

            cs_frame = ttk.Frame(self.cs_intro, style = 'NPC.TFrame')
            cs_frame.grid(row = y, column = z, ipady = 2, ipadx = 5, padx = 2, pady = 2)

            npc_checkbox_value = StringVar()
            npc_checkbox_value.set('Enemy')
            ttk.Label(cs_frame, text = 'Enemy Name:', style = 'NPC.TLabel').grid(row = 0, column = 0, padx = 5)
            ttk.Label(cs_frame, text = 'Friendly?', style = 'NPC.TLabel').grid(row = 1, column = 0, padx = 5)

            npc_name = Entry(cs_frame, width = 12, background = aBlack, foreground = aGreen, font = ('OCR A Extended', 10), insertbackground= aGreen)
            npc_checkbox = Checkbutton(cs_frame, variable = npc_checkbox_value, onvalue = 'Friendly', offvalue = 'Enemy', background = aGreen, relief= 'flat')
            npc_name.grid(row = 0, column = 1, sticky = 'w', padx = 5, pady = 3)
            npc_checkbox.grid(row = 1, column = 1, sticky = 'w', padx = 5)

            npc_addbutton = Button(cs_frame, text = 'Add to Party', background = aDGreen, foreground = aBlack, font = ('OCR A Extended', 8), width = 12, command = lambda: cs_updateparty(npc_name.get(), npc_checkbox_value.get()))
            npc_addbutton.grid(row = 2, column = 0, columnspan = 2)

            def cs_updateparty(name, type):
                npc_add_list = [name, type, 0]
                self.active_party.append(npc_add_list)
                npc_addbutton.config(state = 'disabled', text = 'Added!', disabledforeground= aBlack)
                npc_checkbox.config(state = 'disabled')
                npc_name.config(state = 'disabled', disabledforeground = aBlack)
                self.start_initiative.place(relx = 0.5, rely = 0.5, anchor = 'center')

    #Draw Initiative
        def cs_init_draw():
            cs_intro_recreate()
            self.start_initiative.destroy()
            cs_player_tracker = ttk.Label(self.cs_intro, text = f'Draw for Initiative!\n{self.active_party[0][0]}, pick a card! (1/{len(self.active_party)})', justify= CENTER, style = 'Inv.Alien.TLabel', font = ('OCR A Extended', 10))
            cs_player_tracker.grid(row = 0, column = 0, columnspan = 5)
            self.cs_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            self.rangevar = len(self.cs_range) - 1
            self.pnum = 0

            def cs_button_builder(num):
                self.rangevar -= 1
                y = num // 5
                z = num % 5
                cs_button = Button(self.cs_intro, text = '?', command = lambda: assign_int(), width = 8, foreground = aBlack, background = aDGreen, disabledforeground= aBlack, font = ('Arial', 10, 'bold'))
                cs_button.grid(row = y+1, column = z, ipady = 15, padx = 5, pady = 5)

                if self.rangevar == -1:
                    pass
                else:
                    cs_button_builder(self.rangevar)

                def assign_int():
                    random.shuffle(self.cs_range)
                    var = self.cs_range.pop()
                    cs_button.config(text = var, state = 'disabled', background = aGreen)
                    self.cs_range.sort()

                    if self.pnum == (len(self.active_party)-2):
                        cs_player_tracker.config(text = f'{self.active_party[self.pnum][0]} chose {var}!\nLastly {self.active_party[self.pnum+1][0]}, select a card... ({self.pnum+2}/{len(self.active_party)})')  


                    elif self.pnum < (len(self.active_party) - 1):
                        cs_player_tracker.config(text = f'{self.active_party[self.pnum][0]} chose {var}!\n{self.active_party[self.pnum+1][0]}, select a card... ({self.pnum+2}/{len(self.active_party)})')

                    else:

                        cs_intro_recreate()
                        ttk.Label(self.cs_intro, text = f'{self.active_party[self.pnum-1][0]} chose {var}!  Shall we begin?', background = aBlack, font = ('OCR A Extended', 12, 'bold'), foreground = 'white').grid(row = 0)
                        ttk.Button(self.cs_intro, text = 'Begin', command = lambda: stack_init(), style = 'Small.TButton').grid(row = 1, pady = 10)

                    self.active_party[self.pnum].pop()
                    self.active_party[self.pnum].append(var)
                    self.pnum += 1

            cs_button_builder(self.rangevar)

    #Build Initiative Order          
        def stack_init():
            self.cs_intro.destroy()
            label_stack(0)

            self.sorted_party = sorted(self.active_party, key = lambda mem: mem[2])
            self.cs_turn_count = 1
            self.cs_round_count = 1
            self.cs_init_count = len(self.sorted_party) - 1
            self.active_player = self.sorted_party[0][0]
            self.active_player_data = self.sorted_party[0]

            self.cs_counter = ttk.Label(self.cs_readoutframe, text = f'Round {self.cs_round_count} - Turn {self.cs_turn_count}', style = 'Inv.Alien.TLabel')
            self.cs_counter.place(x=20, y = 20)
            self.cs_gamemother = ttk.Label(self.cs_readoutframe, text = f"It's your turn, {self.sorted_party[0][0]}!", font = ('OCR A Extended', 18), background = aBlack, foreground = 'white')
            self.cs_gamemother.place(relx = 0.5, rely = 0.4, anchor = 'center')

            self.cs_swap_frame = ttk.Frame(self.cs_readoutframe, height = 30, width = 200, style = 'Alien.TFrame')
            self.cs_swap_frame.place(relx = 0.1, rely = 0.9, anchor = 'w')

            self.init_swap = ttk.Button(self.cs_swap_frame, text = 'Swap Initiative', command = lambda: init_swap(), style = 'Small.TButton')
            self.init_swap.pack(anchor = 'w', side = LEFT)

            self.end_turn = ttk.Button(self.cs_readoutframe, text = 'End Turn', command = lambda: begin_order(1),style = 'Small.TButton')
            self.end_turn.place(relx = 0.9, rely = 0.9, anchor = 'e')

    #Stack/Restack Initiative Frames
        def label_stack(num):
            char_frame = ttk.Frame(self.cs_orderframe)
            char_frame.grid(row = self.active_party[num][2])

            length = len(self.active_party)

            if length <= 10:
                icon_p = frame_player
                icon_s = frame_synth
                icon_e = frame_enemy
                icon_f = frame_friendly            
            else:
                icon_p= frame_player_small
                icon_s = frame_synth_small
                icon_e = frame_enemy_small
                icon_f = frame_friendly_small

            char_label = ttk.Label(char_frame, text = f'{self.active_party[num][0]}', compound = 'center', image = icon_p, font = ('OCR A Extended', 10, 'bold'), foreground = aBlack, background = aBlack)
            char_label.pack()

            if self.active_party[num][1] == 'Enemy':
                char_label.config(image = icon_e)
            elif self.active_party[num][1] == 'Synth':
                char_label.config(image = icon_s)
            elif self.active_party[num][1] == 'Friendly':
                char_label.config(image = icon_f)
            else:
                pass

        # If/Then to repeat the call
            if num == len(self.active_party) - 1:
                pass
            else:
                label_stack(num+1)

    #Combat Begins
        def begin_order(num):

            self.cs_turn_count += 1
            self.cs_counter.config(text = f'Round {self.cs_round_count} - Turn {self.cs_turn_count}')

            self.active_player = self.sorted_party[num][0]

            self.cs_gamemother.config(text = f"It's your turn, {self.active_player}!")
            self.end_turn.config(command = lambda: next_order(num))

    #Call next in line
        def next_order(num):
            if num == self.cs_init_count:
                begin_order(0)
                self.cs_round_count += 1
                self.cs_counter.config(text = f'Round {self.cs_round_count} - Turn {self.cs_turn_count}')
            if num < self.cs_init_count:
                begin_order(num+1)

    #Function to swap initiative
        def init_swap():
            pnum = (self.cs_turn_count % len(self.sorted_party)) - 1
            self.active_player_data = self.sorted_party[pnum]

            self.end_turn.config(text = 'Cancel Swap', command = lambda: canc_swap())

            sorted_names = []
            sorted_dict = {}

            for name in self.sorted_party:
                sorted_names.append(name[0])
                sorted_dict.update({name[0]: name})


            self.pop_up = ttk.Combobox(self.cs_swap_frame, values = sorted(sorted_names), width = 17, style = 'Alien.TCombobox')
            self.pop_up.set('Choose Character')
            self.pop_up.pack(anchor = 's', padx = 16)

            self.init_swap.config(text = 'Confirm', command = lambda: swap_choose())

            def swap_choose():
                if self.pop_up.get() == 'Choose Character':
                    pass
                else:
                    new_active_init = [self.active_player_data[0], self.active_player_data[1], sorted_dict[self.pop_up.get()][2]]
                    new_swapped_init = [sorted_dict[self.pop_up.get()][0], sorted_dict[self.pop_up.get()][1], self.active_player_data[2]]

                    new_sorted = []

                    for name in self.sorted_party:
                        if name[0] == new_active_init[0]:
                            new_sorted.append(new_active_init)
                        elif name[0] == new_swapped_init[0]:
                            new_sorted.append(new_swapped_init)
                        else:
                            new_sorted.append(name)

                    self.active_party = new_sorted
                    self.sorted_party = sorted(new_sorted, key = lambda mem: mem[2])

                    self.cs_orderframe.destroy()
                    self.cs_orderframe = ttk.Frame(self.cs_main, height = 385, width = 87, style = 'Alien.TFrame')
                    self.cs_orderframe.grid_propagate(False)
                    self.cs_orderframe.place(x = 30, y = 75)

                    self.pop_up.destroy()

                    self.init_swap.config(text = 'Swap Initiative', command = lambda: init_swap())
                    self.end_turn.config(text = 'End Turn', command = lambda: next_order(pnum))

                    label_stack(0)

    #Destroy and Create cs_intro
        def cs_intro_recreate():
            self.cs_intro.destroy()
            self.cs_intro = ttk.Frame(self.cs_readoutframe, style = 'Alien.TFrame')
            self.cs_intro.pack_propagate(False)
            self.cs_intro.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    #Cancel Swap
        def canc_swap():
            pnum = (self.cs_turn_count % len(self.sorted_party)) - 1
            self.pop_up.destroy()
            self.init_swap.config(text = 'Swap Initiative', command = lambda: init_swap())
            self.end_turn.config(text = 'End Turn', command = lambda: next_order(pnum))

    #Go back without deleting combat
        def cs_back():
            top_menu.lift()





###---DICE ROLLER---##

    #DR Global Variables
        self.dr_on = False

    #Begin Dice Roller
        def dr_start():
            if self.dr_on == True:
                self.dr_main.lift()
            else:

            #Dice Roller Frames
                self.dr_on = True
                self.dr_main = ttk.Frame(master, width=640, height = 480)
                self.dr_main.grid_propagate(False)
                self.dr_main.grid(row = 0, column = 0)

                ttk.Label(self.dr_main, image = self.dr_bg_init).place(x = 0, y = 0)

                self.dr_options = ttk.Frame(self.dr_main, width = 550, height = 200, style = 'Alien.TFrame')
                self.dr_options.pack_propagate(False)
                self.dr_options.pack(side = TOP, padx = 45, pady = 35)

                self.dr_readout = ttk.Frame(self.dr_main, width = 606, height = 180, style = 'Dice.TFrame')
                self.dr_readout.grid_propagate(False)
                self.dr_readout.pack_propagate(False)
                self.dr_readout.pack(side = BOTTOM, padx = 18, pady = 18)

                self.dr_results = ttk.Frame(self.dr_readout, style = 'Dice.TFrame')
                self.dr_results.pack(padx = 5, pady = 0)

            #Create Dice Roller Widgets
                ttk.Label(self.dr_options, text = 'Base Dice', font = ('OCR A Extended', 18), image = dice_base, compound= 'bottom', background = aBlack, foreground = 'white').place(relx = 0.2, y = 80, anchor = 'center')

                ttk.Label(self.dr_options, text = 'Stress Dice', font = ('OCR A Extended', 18), image = dice_stress, compound = 'bottom', background = aBlack, foreground = 'white').place(relx = 0.8, y=80, anchor = 'center')

                self.dr_bdice_amt = Spinbox(self.dr_options, from_ = 1, to = 20, font = ('OCR A Extended', 24), width = 2, state = 'readonly')
                self.dr_bdice_amt.place(relx = 0.4, y = 100, anchor = 'center')

                self.dr_sdice_amt = Spinbox(self.dr_options, from_ = 0, to = 10, font = ('OCR A Extended', 24), width = 2, state = 'readonly')
                self.dr_sdice_amt.place(relx = 0.6, y = 100, anchor = 'center')

                ttk.Button(self.dr_options, text = 'Roll', command = lambda: dice_roll(), style = 'Small.TButton').place(relx = 0.5, rely = 0.75, anchor = 'center')

                ttk.Button(self.dr_options, text = 'Back', command = lambda: top_menu.lift(),style = 'Small.TButton').place(relx = 0.9, rely = 0.95, anchor = 'center')

                self.dr_clear = ttk.Button(self.dr_options, text = 'Clear', command = lambda: dice_clear(), state = 'disabled', style = 'Small.TButton')
                self.dr_clear.place(relx = 0.5, rely = 0.95, anchor = 'center')

                self.dr_main.lift()

    #Roll the Dice!        
        def dice_roll():
            self.dr_results.destroy()
            self.dr_results = ttk.Frame(self.dr_readout, style = 'Dice.TFrame')
            self.dr_results.pack(padx = 5, pady = 0)
        #Variables
            base_results = []
            stress_results = []
            important_rolls = []
            bdice = int(self.dr_bdice_amt.get())
            sdice = -int(self.dr_sdice_amt.get())

        #Roll both sets of dice
            def roll(d):
                x = 0
                while x != d:
                    dice_roll = random.randint(1,6)

                #Assign Base Dice
                    if d == bdice:
                        if dice_roll == 6:
                            important_rolls.append('6b')
                        else:
                            base_results.append(str(dice_roll) + 'b')
                        x += 1
                        if x == bdice + 1:
                            break

                #Assign Stress Dice
                    elif d == sdice:
                        if dice_roll == 1:
                            important_rolls.append('1s')
                        elif dice_roll == 6:
                            important_rolls.append('6s')
                        else:
                            stress_results.append(str(dice_roll) + 's')
                        x -= 1
                        if x == sdice - 1:
                            break
        
        #Dice Appear in Readout
            def print_roll():
                self.dr_clear.config(state = 'enabled')

            #Display Important Dice First
                i = 0
                h = 0
                limit = len(important_rolls)
                sorted_rolls = sorted(important_rolls)
                while h < limit:
                    if important_rolls != []:
                        dice_choice(sorted_rolls.pop(0))
                    ttk.Label(self.dr_results, image = self.dice_img, background = '#182318').grid(row = i // 10, column = i % 10, padx = 3, pady = 2)
                    i += 1
                    h += 1

            #Display Base Dice
                j = 0
                limit = len(base_results)
                while j < limit:
                    if base_results != []:
                        dice_choice(base_results.pop(0))
                    ttk.Label(self.dr_results, image = self.dice_img, background = '#182318').grid(row = i // 10, column = i % 10, padx = 3, pady = 2)
                    i += 1
                    j += 1

            #Display Stress Dice
                k = 0
                limit = len(stress_results)
                while k < limit:
                    if stress_results != []: 
                        dice_choice(stress_results.pop(0))
                    ttk.Label(self.dr_results, image = self.dice_img, background = '#182318').grid(row = i // 10, column = i % 10, padx = 3, pady = 2)
                    i += 1
                    k += 1

        #Dice Image Assignment
            def dice_choice(r):

                if r == '1b':
                    self.dice_img = dice_1b

                elif r == '1s':
                    self.dice_img = dice_1s

                elif r == '2b':
                    self.dice_img = dice_2b

                elif r == '2s':
                    self.dice_img = dice_2s 

                elif r == '3b':
                    self.dice_img = dice_3b

                elif r == '3s':
                    self.dice_img = dice_3s 

                elif r == '4b':
                    self.dice_img = dice_4b
                      
                elif r == '4s':
                    self.dice_img = dice_4s
                      
                elif r == '5b':
                    self.dice_img = dice_5b

                elif r == '5s':
                    self.dice_img = dice_5s

                elif r == '6b':
                    self.dice_img = dice_6b

                elif r == '6s': 
                    self.dice_img = dice_6s

        #Call Dice Functions    
            roll(sdice)
            roll(bdice)
            print_roll()
   
    #Clear the Dice Box
        def dice_clear():
            self.dr_results.destroy()
            self.dr_clear.config(state = 'disabled')




###---MOTION TRACKER---###

        def mt_start():
        #Frames
            self.mt_main = ttk.Frame(master, height = 480, width = 640, style = 'MT.TFrame')
            self.mt_main.pack_propagate(False)
            self.mt_main.grid(row = 0, column = 0)

            self.mt_trackerframe = ttk.Frame(self.mt_main, height = 400, width = 620, style = 'MT.TFrame',)
            self.mt_trackerframe.place(relx = 0.5, y = 215, anchor = 'n')

        #Variables

            self.mt_val = IntVar()
            self.mt_val.set(0)
            self.mt_toggle_value = False

        #Credits
            ttk.Label(self.mt_main, text = 'Credits:', style = 'Header.Alien.TLabel', font = ('OCR A Extended', 16)).place(x = 10, y = 10)
            ttk.Label(self.mt_main, style = 'Inv.Alien.TLabel', font = ('OCR A Extended', 10), text = 'Programming and Graphic Design - Micah Popp \n\nMotion Tracker SFX - Alien vs Predator (2010) \n\nFor use with the Alien RPG by Free League').place(x = 20, y = 50)

        #Widgets
            ttk.Label(self.mt_trackerframe, image = mt_top_panel,background = aBlack).place(x= 0,y =0)
            
            self.mt_button = ttk.Label(self.mt_trackerframe, image = mt_button_off, background = '#564937')
            self.mt_button.place(x = 78, y = 20)
            self.mt_button.bind('<ButtonPress>', lambda x: mt_toggle(True))

            ttk.Label(self.mt_trackerframe, image = mt_bottom_panel, background = aBlack).place(x= 0, y = 130)

            self.mt_motiontracker = Scale(self.mt_trackerframe, length = 600,
                                          from_= 0, to = 10,
                                          orient = HORIZONTAL,
                                          variable = self.mt_val,
                                          showvalue= False,
                                          tickinterval= 1,
                                          state = 'disabled',
                                          troughcolor= 'grey',
                                          foreground= 'grey',
                                          background = aBlack,
                                          font = ('OCR A Extended', 10),
                                          activebackground= 'red',
                                          highlightthickness=0
                                          )
            self.mt_motiontracker.config(command = lambda x: update_pulse(x))
            self.mt_motiontracker.place(relx = 0.5, y = 115, anchor = 'center')

            pygame.mixer.init()
            self.mt_ch_1 = pygame.mixer.Channel(1)
            self.mt_blip = pygame.mixer.Sound('audio\\mt_blip.wav')
            self.mt_ch_2 = pygame.mixer.Channel(2)
            self.t = threading.Timer(1.0, update_pulse, args=[self.mt_motiontracker.get()])

            ttk.Button(self.mt_main, text = 'Back', style = 'Small.TButton', command = lambda: mt_back()).place(relx = 0.9, rely = 0.95, anchor = 'e')

        def mt_back():
            pygame.mixer.quit()
            self.mt_main.destroy()

# Turn on Tracker 1
        def mt_toggle(state):
            if state == False:
                self.mt_toggle_value = False
                self.mt_motiontracker.config(state = 'disabled', foreground = 'grey', troughcolor = 'grey')
                self.mt_button.config(image = mt_button_off)
                self.mt_button.bind('<ButtonPress>', lambda x: mt_toggle(True))
                if pygame.mixer.get_busy() == True:
                    pygame.mixer.stop()
                self.mt_val.set(0)
  
            if state == True:
                self.mt_toggle_value = True
                self.mt_motiontracker.config(state = 'active', foreground = aGreen, troughcolor = aGreen)
                self.mt_button.config(image = mt_button_on)
                self.mt_button.bind('<ButtonPress>', lambda x: mt_toggle(False))
                self.mt_ch_1.play(self.mt_blip, loops = -1)

        def update_pulse(x):
            self.t.cancel()
            self.t = threading.Timer(1.0, update_pulse, args=[self.mt_motiontracker.get()])

            if self.mt_toggle_value == True:
                if pygame.mixer.get_busy() == False:
                    self.mt_ch_2.play(pygame.mixer.Sound(f'audio\\mt_pulse_{x}.wav'))
                    self.t.start()
                else:
                    self.mt_ch_2.queue(pygame.mixer.Sound(f'audio\\mt_pulse_{x}.wav'))
                    self.t.start()
            else:
                pass

        top_menu.lift()

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':main()