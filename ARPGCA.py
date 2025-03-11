from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import random
import pygame
import threading
import os
import sys
import datetime

class App:

    def __init__(self, master):


    #Global Variables
        aGreen = '#00FF00'
        aDGreen = '#009900'
        aBlack = '#1C1C1C'
        
        master.title('Alien RPG Companion App')
        master.geometry('640x480+100+100')
        master.minsize(640,480)
        master.config(bg = aBlack)

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        os.chdir(application_path)
    #region Global Styles
        self.style = ttk.Style()

        #Label Style
        self.style.configure('White.TLabel', font = ('Arial', 10), foreground = 'white', background = aBlack)
        self.style.configure('Alien.TLabel', font = ('Courier New', 12, 'bold'), background = aGreen, foreground = aBlack)
        self.style.configure('Inv.Alien.TLabel', font = ('Courier New', 12), background = aBlack, foreground = 'white')
        self.style.configure('Small.Alien.TLabel', font = ('Courier New', 8), background = aBlack, foreground = 'white')
        self.style.configure('NewChar.Alien.TLabel', font = ('Courier New', 14), background = aBlack, foreground = 'white')
        self.style.configure('Header.Alien.TLabel', font = ('Courier New', 20, 'bold'), foreground = 'white', background = aBlack)
        self.style.configure('SmHeader.Alien.TLabel', font = ('Courier New', 16, 'bold'), foreground = 'white', background = aBlack)
        self.style.configure('NPC.TLabel', font = ('Courier New', 8), background = aGreen)
        self.style.configure('Levels.TLabel', font = ('Calibri', 20), background = aBlack, foreground = aDGreen)


        #Button Style
        self.style.configure('Alien.TButton', font = ('Courier New', 14, 'bold'), foreground = aDGreen, background = aBlack, padding = 10, relief = 'raised')
        self.style.configure('Small.TButton', font = ('Courier New', 10), foreground = aDGreen, background = aBlack)
        self.style.configure('Smaller.TButton', font = ('Courier New', 8), foreground = aDGreen, background = aBlack)
        self.style.configure('SmDice.TButton', font = ('Courier New', 8), foreground = aDGreen, background = '#182318')
        self.style.configure('Green.Small.TButton', font = ('Courier New', 10), foreground = aBlack, background = aGreen)
        self.style.configure('NPC.TButton', background = aGreen, foreground = aBlack, justify = 'center', font = ('Courier New', 8))
        self.style.configure('Red.TButton', font = ('Courier New', 10), foreground = 'red', background = aBlack)

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

        #Radiobutton Style
        self.style.configure('Alien.TRadiobutton', background = aBlack)

        #Spinbox Style
        self.style.configure('Alien.TSpinbox', background = aBlack)

        #Checkbutton Style
        self.style.configure('Alien.TCheckbutton', background = aBlack)
    #endregion

    #Global Photos
        image_root = f'{os.getcwd()}\\images\\'

        self.top_menu_bg = PhotoImage(file = image_root + 'top_menu_bg.png')
        self.pm_bg_init = PhotoImage(file = image_root + 'pm_bg_init.png')
        self.pm_bg_new = PhotoImage(file = image_root + 'pm_bg_new.png')
        self.pm_bg_load = PhotoImage(file = image_root + 'pm_bg_load.png')
        self.cs_bg_init = PhotoImage(file = image_root + 'cs_bg_init.png')
        self.dr_bg_init = PhotoImage(file = image_root + 'dr_bg_init.png')

        self.sheet_bg_normal = PhotoImage(file = image_root + 'sheet_bg_normal.png')
        self.sheet_bg_panic = PhotoImage(file = image_root + 'sheet_bg_panic.png')
        self.sheet_bg_afflicted = PhotoImage(file = image_root + 'sheet_bg_afflicted.png')
        self.sheet_bg_broken = PhotoImage(file = image_root + 'sheet_bg_broken.png')
        self.sheet_bg_death = PhotoImage(file = image_root + 'sheet_bg_death.png')
    
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

        dicedict = {
            "1b":PhotoImage(file = image_root + 'dice_1b.png'),
            "1s":PhotoImage(file = image_root + 'dice_1s.png'),
            "2b":PhotoImage(file = image_root + 'dice_2b.png'),
            "2s":PhotoImage(file = image_root + 'dice_2s.png'),
            "3b":PhotoImage(file = image_root + 'dice_3b.png'),
            "3s":PhotoImage(file = image_root + 'dice_3s.png'),
            "4b":PhotoImage(file = image_root + 'dice_4b.png'),
            "4s":PhotoImage(file = image_root + 'dice_4s.png'),
            "5b":PhotoImage(file = image_root + 'dice_5b.png'),
            "5s":PhotoImage(file = image_root + 'dice_5s.png'),
            "6b":PhotoImage(file = image_root + 'dice_6b.png'),
            "6s":PhotoImage(file = image_root + 'dice_6s.png')
            }

        dice_base = PhotoImage(file = image_root + 'dice_base.png')
        dice_stress = PhotoImage(file = image_root + 'dice_stress.png')

        ch_skill_img = PhotoImage(file = image_root + 'ch_skill_img.png')

        death_bt_active = PhotoImage(file = image_root + 'death_bt_active2.png')
        death_bt_inactive = PhotoImage(file = image_root + 'death_bt_inactive2.png')
        panic_bt_active = PhotoImage(file = image_root + 'panic_bt_active2.png')
        panic_bt_inactive = PhotoImage(file = image_root + 'panic_bt_inactive2.png')
        end_panic_bt_active = PhotoImage(file = image_root + 'end_panic_bt_active2.png')
        end_panic_bt_inactive = PhotoImage(file = image_root + 'end_panic_bt_inactive2.png')
        push_bt_active = PhotoImage(file = image_root + 'push_bt_active2.png')
        push_bt_inactive = PhotoImage(file = image_root + 'push_bt_inactive2.png')
        resus_bt_active = PhotoImage(file = image_root + 'resus_bt_active2.png')
        resus_bt_inactive = PhotoImage(file = image_root + 'resus_bt_inactive2.png')
        trauma_bt_active = PhotoImage(file = image_root + 'trauma_bt_active2.png')
        trauma_bt_inactive = PhotoImage(file = image_root + 'trauma_bt_inactive2.png')
        inj_bt_active = PhotoImage(file = image_root + 'inj_bt_active2.png')
        inj_bt_inactive = PhotoImage(file = image_root + 'inj_bt_inactive2.png')




###---TOP MENU---###
#region Top Menu
        top_menu = ttk.Frame(master, width = 640, height = 480)
        top_menu.place(relx = 0.5, rely = 0.5, anchor = 'center')

            #Labels
        ttk.Label(top_menu, image = self.top_menu_bg, background = aBlack).place(x = 0, y = 0)
        ttk.Label(top_menu, style = 'Header.Alien.TLabel', text = 'Alien RPG Companion App', foreground= 'white', background= aBlack).place(relx = 0.5, rely = 0.25, anchor = 'center')
        ttk.Label(top_menu, text = 'Version 1.1.0', style = 'White.TLabel').place(relx = 0.5, rely = 0.35, anchor = 'center')

            # Buttons
        ttk.Button(top_menu, style = 'Alien.TButton', text = '  Party  Manager  ', command = lambda: pm_start()).place(relx = 0.3, rely = 0.58, anchor = 'center')    
        ttk.Button(top_menu, style = 'Alien.TButton', text = 'Initiative Tracker', command = lambda: cs_start()).place(relx = 0.7, rely = 0.58, anchor = 'center')
        ttk.Button(top_menu, style = 'Alien.TButton', text = '  Motion Tracker  ', command = lambda: mt_start()).place(relx = 0.3, rely = 0.69, anchor = 'center')
        ttk.Button(top_menu, style = 'Alien.TButton', text = '   Dice  Roller   ', command = lambda: dr_start()).place(relx = 0.7, rely = 0.69, anchor = 'center')
        ttk.Button(top_menu, style = 'Alien.TButton', text = ' Character Sheets ', command = lambda: ch_start()).place(relx = 0.5, rely = 0.8, anchor = "center")

#endregion

###---CHARACTER SHEETS---###

#region Character Sheets
    #region Character Sheet Start and Restart
    #Initialize Character Sheet
        def ch_start():
            pm_start()            
            self.pm_new.config(text = 'New Player', command = lambda: ch_new())
            self.pm_load.config(text = 'Load Player', command = lambda: ch_load())
            self.pm_title.config(text = 'Character Sheets')

    #Reset Character Sheet
        def ch_reset():
            self.pm_main.destroy()
            ch_start()
     #endregion   
         
##NEW CHARACTER##
    #region New Character
        def ch_new():
            self.pm_load.destroy()
            self.pm_new.destroy()
            self.pm_bg.config(image = self.top_menu_bg)

        #FUNCTIONS
            #Key Attribute Value    
            def keyatt_val(event):

            #Determine Key Attribute
                keyatt = keyatt_dict[job.get()]
                self.key.config(text = keyatt)
                att_dict.update({keyatt:[2,'Key']})
                        
            #Grid Attribute Frame and Race Details
                self.att_frame.grid(row = 3, column = 0, columnspan = 2, sticky = 'we')
                race_l.grid(row = 4, column = 0, sticky = 'w')
                race.grid(row = 4, column = 1, sticky = 'e')

                att_points_l = ttk.Label(self.att_frame, text = f'Attribute Points:', style = "SmHeader.Alien.TLabel")
                att_points_l.grid(row = 0, column = 0, sticky = 'w')
                self.att_pt_ct = ttk.Label(self.att_frame, text = f'{self.ap}/14', style = 'NewChar.Alien.TLabel')
                self.att_pt_ct.grid(row = 0, column = 1)

            #Pack Attributes
                for i, ATT in enumerate(att_keys):
                    att_place(att_keys[ATT][0], att_keys[ATT][1], att_keys[ATT][2], ATT, i+1)

            #Place Attribute Builder
            def att_place(frame, label, level, ATT, row):
                self.att_frame_on = True
                label = ttk.Label(self.att_frame, text = ATT, style = "SmHeader.Alien.TLabel")
                label.grid(row = row, column = 0, sticky = 'w')
                frame = ttk.Frame(self.att_frame, style = 'Alien.TFrame')
                frame.grid(row = row, column = 1, sticky = 'e')
                ttk.Button(frame, text = "+", width = 2, command = lambda: adjust(ATT, 1, level), style = 'Small.TButton').pack(side = RIGHT, anchor = 'center')
                level = ttk.Label(frame, text = "■"*att_dict[ATT][0], width = 8, style = "Levels.TLabel")
                level.pack(side = RIGHT, anchor = 'center')            
                ttk.Button(frame, text = "-", width = 2, command = lambda: adjust(ATT, -1, level), style = 'Small.TButton').pack(side = RIGHT, anchor = 'center')

            #Adjust Attribute Score
            def adjust(ATT, x, wgt):
                def assign():
                        self.ap -= x
                        self.att_pt_ct.config(text = f'{self.ap}/14', style = 'NewChar.Alien.TLabel')
                        if self.ap == 0:
                            self.att_pt_ct.config(foreground = 'red')
                        else:
                            self.att_pt_ct.config(foreground = 'white')
                        att_dict[ATT].pop(0)
                        att_dict[ATT].insert(0,y)
                        wgt.config(text = "■"*(y))

                y = att_dict[ATT][0]
                y += x
                if att_dict[ATT][1] == 'Key':
                    if y > 5:
                        y = 5
                        x = 0
                else:
                    if y > 4:
                        y = 4
                        x = 0
                if y < 2:
                    y = 2
                    x = 0

                if self.ap == 0:
                    if x == 1:
                        pass
                    else:
                        assign()

                else:
                    assign()

            #Identify Synth
            def id_synth(event):
                commit_bt.grid(row = 9, columnspan = 3, pady=5)

            #If Synth
                if race.get() == 'Synth':

                    def add_3():
                        for ATT in att_keys:
                            att_keys[ATT][4].config(state = ACTIVE)
                        att_keys[race_3.get()][4].config(state = DISABLED)

                    #Disallow +3 and +2 on same attribute
                        if race_2.get() == race_3.get():
                            if race_3.get() == 'Strength':
                                att_keys['Agility'][4].invoke()
                            else:
                                att_keys['Strength'][4].invoke()

                    race_2.set('null')
                    race_3.set('null')
                    
                    self.synth_on = True
                    self.race_add3 = ttk.Label(self.att_frame, text = "+3", style = 'NewChar.Alien.TLabel')
                    self.race_add2 = ttk.Label(self.att_frame, text = "+2", style = 'NewChar.Alien.TLabel')

                    self.race_add3.grid(row = 0, column = 2)
                    self.race_add2.grid(row = 0, column = 3)

                    for i, ATT in enumerate(att_keys):
                        att_keys[ATT][3] = ttk.Radiobutton(self.att_frame, variable=race_3, value = ATT, command = add_3, style= 'Alien.TRadiobutton')
                        att_keys[ATT][3].grid(row = i+1, column = 2, padx = 10)
                        att_keys[ATT][4] = ttk.Radiobutton(self.att_frame, variable = race_2, value = ATT, state = DISABLED, style = 'Alien.TRadiobutton')
                        att_keys[ATT][4].grid(row = i+1, column = 3, padx = 10)

            #If Human
                if race.get() == 'Human':
                    race_2.set('Human')
                    race_3.set('Human')
                    if self.synth_on == True:
                        for ATT in att_keys:
                            self.race_add3.destroy()
                            self.race_add2.destroy()
                            att_keys[ATT][3].destroy()
                            att_keys[ATT][4].destroy()

            #Verify all details are complete
            def commit_check():
                if self.ap == 0 and race_2.get() != 'null' and race_3.get() != 'null' and self.name.get() != '':
                    commit_att()
                else:
                    messagebox.showerror(title= 'Section Incomplete', message= 'Please verify all fields are completed\n\n(Name and Attributes)')

        #Commit Attributes to Character
            def commit_att():
                if race.get() == 'Synth':
                    att_dict[race_3.get()][0] += 3
                    att_dict[race_2.get()][0] += 2
                self.ch_name = self.name.get()
                self.char = {
                    self.ch_name:{
                        'Name': self.ch_name,
                        'Job': job.get(),
                        'Race': race.get(),
                        'Strength': att_dict['Strength'],
                        'Agility': att_dict['Agility'],
                        'Wits': att_dict['Wits'],
                        'Empathy': att_dict['Empathy']
                    }
                }
                ch_new_skills()

#region VARIABLES
        #Variables

            self.ap = 6
            self.att_frame_on = False
            self.synth_on = False
            str_ = ttk.Frame()
            str_l = ttk.Label()
            str_lv = ttk.Label()
            str_3 = ttk.Radiobutton()
            str_2 = ttk.Radiobutton()

            agl = ttk.Frame()
            agl_l = ttk.Label()
            agl_lv = ttk.Label()
            agl_3 = ttk.Radiobutton()
            agl_2 = ttk.Radiobutton()

            wit = ttk.Frame()
            wit_l = ttk.Label()
            wit_lv = ttk.Label()
            wit_3 = ttk.Radiobutton()
            wit_2 = ttk.Radiobutton()

            emp = ttk.Frame()
            emp_l = ttk.Label()
            emp_lv = ttk.Label()
            emp_3 = ttk.Radiobutton()
            emp_2 = ttk.Radiobutton()

            race_3 = StringVar()
            race_2 = StringVar()

            keyatt_dict = {
                'Colonial Marine':'Strength',
                'Colonial Marshal':'Wits', 
                'Company Agent':'Wits', 
                'Kid':'Agility', 
                'Medic':'Empathy', 
                'Officer':'Empathy', 
                'Pilot':'Agility', 
                'Roughneck':'Strength', 
                'Scientist':'Wits'
                    }
            
            att_dict = {
                'Strength':[2,''],
                'Agility':[2,''],
                'Wits':[2,''],
                'Empathy':[2,'']
            }

            att_keys = {
                'Strength':[str_, str_l, str_lv, str_3, str_2],
                'Agility':[agl, agl_l, agl_lv, agl_3, agl_2],
                'Wits':[wit, wit_l, wit_lv, wit_3, wit_2],
                'Empathy':[emp, emp_l, emp_lv, emp_3, emp_2]
            }
#endregion
    #WIDGETS

        #Name
            name_l = ttk.Label(self.pm_select, text = 'Name:', style = 'SmHeader.Alien.TLabel')
            name_l.grid(row = 0, column = 0, sticky = 'w')
            self.name = ttk.Entry(self.pm_select, width = 20, style = 'Alien.TEntry', font = ('Courier New', 14))
            self.name.grid(row = 0, column = 1, sticky = 'e', padx = 20)

        #Career
            job_l = ttk.Label(self.pm_select, text = 'Career:', style = 'SmHeader.Alien.TLabel')
            job_l.grid(row = 1, column = 0, sticky = 'w')
            job = ttk.Combobox(self.pm_select, width = 16, values = ['Colonial Marine', 'Colonial Marshal', 'Company Agent', 'Kid', 'Medic', 'Officer', 'Pilot', 'Roughneck', 'Scientist'], state = 'readonly', style = 'Alien.TCombobox', font = ('Courier New', 14), justify = CENTER)
            job.grid(row = 1, column = 1, sticky = "e", padx= 20)
            job.bind('<<ComboboxSelected>>', keyatt_val)

        #Key Attribute
            key_l = ttk.Label(self.pm_select, text = 'Key Attribute:', style = 'SmHeader.Alien.TLabel')
            key_l.grid(row = 2, column = 0, sticky = 'w')
            self.key = ttk.Label(self.pm_select, text = '', style = 'SmHeader.Alien.TLabel', font = ('Courier New', 14))
            self.key.grid(row = 2, column = 1)

        # #Attributes
            self.att_frame = ttk.Frame(self.pm_select, style = 'Alien.TFrame')

        #Race
            race_l = ttk.Label(self.pm_select, text = 'Race:', style = 'SmHeader.Alien.TLabel')
            race = ttk.Combobox(self.pm_select, width = 5, values = ['Human', 'Synth'],  style = 'Alien.TCombobox', font = ('Courier New', 14), justify = CENTER, state = 'readonly')
            race.bind('<<ComboboxSelected>>', id_synth)
            #Placements in key_att

        #Commit Button
            commit_bt = ttk.Button(self.pm_select, text = 'Commit', command = lambda: commit_check(), style = 'Small.TButton')

    #Assign Skill Points
        def ch_new_skills():
        #Update Combobox Values
            def skl_val(event, skl):
                score = skl_dict[skl][2].get()
                old_score = skl_dict[skl].pop(0)
                skl_dict[skl].insert(0, score)
                update_sp()

                if self.sp < 0:
                    messagebox.showerror(title='Not Enough Points', message= 'You do not have enough points to assign to this trait')
                    skl_dict[skl].pop(0)
                    skl_dict[skl].insert(0, old_score)
                    skl_dict[skl][2].set(old_score)
                    update_sp()

        #Updating Skill Points
            def update_sp():
                self.used_sp = 0
                for SKL in skl_dict:
                    self.used_sp += int(skl_dict[SKL][0])
                self.sp = 10 - self.used_sp
                skl_pts.config(text = f'{self.sp}/10')

        #Commit Skill Points
            def commit_skl():
                if self.sp != 0:
                    messagebox.showerror(title = 'Unfinished Skills', message = 'Not all Skill Points have been assigned')
                else:
                    self.char[self.ch_name].update({
                        'Close Combat':skl_dict['Close Combat'][0],
                        'Heavy Machinery':skl_dict['Heavy Machinery'][0],
                        'Stamina':skl_dict['Stamina'][0],
                        'Ranged Combat':skl_dict['Ranged Combat'][0],
                        'Mobility':skl_dict['Mobility'][0],
                        'Piloting':skl_dict['Piloting'][0],
                        'Observation':skl_dict['Observation'][0],
                        'Survival':skl_dict['Survival'][0],
                        'Comtech':skl_dict['Comtech'][0],
                        'Command':skl_dict['Command'][0],
                        'Manipulation':skl_dict['Manipulation'][0],
                        'Medical Aid':skl_dict['Medical Aid'][0]
                        })
                    ch_att_frame.destroy()
                    ch_skl_frame.destroy()
                    ch_new_gear()


            self.pm_select.destroy()
            self.pm_bg.config(image = self.pm_bg_load)
            ch_att_frame = ttk.Frame(self.pm_main, style = 'Alien.TFrame')
            ch_skl_frame = ttk.Frame(self.pm_main, style = 'Alien.TFrame')
            ch_att_frame.place(x = 50, y = 120)
            ch_skl_frame.place(x = 355, y = 60)

        #region Variables
            self.used_sp = 0
            self.sp = 10
            career = self.char[self.ch_name]['Job']

            cc = ttk.Combobox()
            hm = ttk.Combobox()
            st = ttk.Combobox()
            rc = ttk.Combobox()
            mb = ttk.Combobox()
            pl = ttk.Combobox()
            ob = ttk.Combobox()
            sv = ttk.Combobox()
            ct = ttk.Combobox()
            cm = ttk.Combobox()
            mn = ttk.Combobox()
            ma = ttk.Combobox()


            skl_dict = {
                'Close Combat':[0,'', cc, 'S'],
                'Heavy Machinery':[0,'', hm, 'S'],
                'Stamina':[0,'', st, 'S'],
                'Ranged Combat':[0,'',rc, 'A'],
                'Mobility':[0,'',mb, 'A'],
                'Piloting':[0,'',pl, 'A'],
                'Observation':[0,'',ob, 'W'],
                'Survival':[0,'',sv, 'W'],
                'Comtech':[0,'',ct, 'W'],
                'Command':[0,'',cm, 'E'],
                'Manipulation':[0,'',mn, 'E'],
                'Medical Aid':[0,'',ma, 'E']
            }

            job_skl = {
                'Colonial Marine':['Close Combat','Stamina','Ranged Combat'],
                'Colonial Marshal':['Observation','Ranged Combat','Manipulation'], 
                'Company Agent':['Comtech','Observation','Manipulation'], 
                'Kid':['Mobility','Survival','Observation'], 
                'Medic':['Mobility','Observation','Medical Aid'], 
                'Officer':['Ranged Combat','Command','Manipulation'], 
                'Pilot':['Piloting','Ranged Combat','Comtech'], 
                'Roughneck':['Heavy Machinery','Stamina','Close Combat'], 
                'Scientist':['Observation','Survival','Comtech']
            }
        #endregion

        #Widgets            
            for skl in job_skl[career]:
                skl_dict[skl].pop(1)
                skl_dict[skl].insert(1,'Key')

            #Pack Existing Data
            ttk.Label(ch_att_frame, text = f'Name: {self.char[self.ch_name]['Name']}\n\nCareer: {self.char[self.ch_name]['Job']}\n\nRace: {self.char[self.ch_name]['Race']}\n\nStrength: {"■"*self.char[self.ch_name]['Strength'][0]} ({self.char[self.ch_name]['Strength'][0]})\n\nAgility: {"■"*self.char[self.ch_name]['Agility'][0]} ({self.char[self.ch_name]['Agility'][0]})\n\nWits: {"■"*self.char[self.ch_name]['Wits'][0]} ({self.char[self.ch_name]['Wits'][0]})\n\nEmpathy: {"■"*self.char[self.ch_name]['Empathy'][0]} ({self.char[self.ch_name]['Empathy'][0]})', style = 'Inv.Alien.TLabel').pack(side = LEFT)

            #Create Widgets for Skill Assignment
            ttk.Label(ch_skl_frame, text = 'SKILLS', style = 'NewChar.Alien.TLabel').grid(row = 0, column = 0, columnspan= 2)
            skl_pts = ttk.Label(ch_skl_frame, text = f'{self.sp}/10', style = 'NewChar.Alien.TLabel')
            skl_pts.grid(row = 1, column = 0, columnspan = 2)

            #Create Each Skill Widget
            for i, skl in enumerate(skl_dict):
                skl_l = ttk.Label(ch_skl_frame, text = f'{skl} ({skl_dict[skl][3]})', style = 'Inv.Alien.TLabel')
                skl_l.grid(row = i+2, column = 0, sticky = 'w')
                skl_dict[skl][2] = ttk.Combobox(ch_skl_frame, values = [0,1], width = 1, state = 'readonly', style = 'Alien.TCombobox')
                if skl_dict[skl][1] == 'Key':
                    skl_dict[skl][2].config(values = [0,1,2,3])
                    skl_l.config(text = skl_l.cget('text').upper(), font = ('Courier New', 12, 'bold'), foreground = aDGreen)
                skl_dict[skl][2].grid(row = i+2, column = 1)
                skl_dict[skl][2].set(0)
                skl_dict[skl][2].bind('<<ComboboxSelected>>', lambda event, a= skl: skl_val(event, a))

            ttk.Button(ch_skl_frame, text = 'Commit', command = lambda: commit_skl(), style = 'Small.TButton').grid(row = 14, columnspan = 2, pady = 10)

    #Assign Starting Gear
        def ch_new_gear():
            ttk.Label(self.pm_main, text = f'{self.ch_name}', style = 'SmHeader.Alien.TLabel').place(relx = 0.5, rely = 0.15, anchor = 'center')
            self.pm_bg.config(image = self.top_menu_bg)
            ch_gearmenu = ttk.Frame(self.pm_main, style = 'Alien.TFrame')
            ch_gearmenu.place(relx = 0.5, rely = 0.5, anchor = 'center')

        #Identify Gear and Gatekeep if NOT 2 Picked
            def gear_val(event, i):
                gear_sel[i].pop(1)
                gear_sel[i].insert(1,gear_sel[i][0].get())
                g_ct = 0
                for sel in gear_sel:
                    if gear_sel[sel][1] != '-None-':
                        g_ct += 1
                if g_ct == 2:
                    self.gear_check = True
                    if self.tal_check == True:
                        g_commit_bt.config(state = ACTIVE)
                else:
                    self.gear_check = False
                    g_commit_bt.config(state = DISABLED)

        #Gatekeep for Talent Selection         
            def tal_val(event):
                if tal_sel.get() != '-Select One-':
                    self.tal_check = True
                    if self.gear_check == True:
                        g_commit_bt.config(state = ACTIVE)
                else:
                    self.tal_check = False
                    g_commit_bt.config(state = DISABLED)

        #Roll for Cash
            def roll_cash(num):
                results = []
                dice = 0
                total = 0

                while num > 0:
                    dice = random.randint(1,6)
                    results.append(dice)
                    num -= 1

                for num in results:
                    total += num
                    ttk.Label(self.dice_frame, image= dicedict[f'{num}b'], background = '#182318').pack(side = LEFT)

                self.cash = total*gear_dict[career][4][1]
                roll_bt.destroy()
                roll_result = ttk.Label(ch_gearmenu, text = f'Starting Cash: ${self.cash}', style = 'NewChar.Alien.TLabel')
                roll_result.pack()
                self.dice_frame.pack()
                g_commit_bt.pack()

        #Commit and Save Changes
            def commit_gear():
                if self.tal_check == True and self.gear_check == True:
                    gear = []
                    dict = self.char[self.ch_name]
                    for sel in gear_sel:
                        equip = gear_sel[sel][1]
                        if equip != '-None-':
                            gear.append([equip,'Set'])
                    while len(gear) != 10:
                        gear.append(["",0])
                    dict.update({'Strength':dict['Strength'][0], 
                                'Agility':dict['Agility'][0], 
                                'Wits':dict['Wits'][0],
                                'Empathy':dict['Empathy'][0],
                                'Gear':gear, 
                                'Cash':self.cash,
                                'Health':dict['Strength'][0],
                                'Max Health':dict['Strength'][0],
                                'Stress':0,
                                'Radiation':0,
                                "Permanent Radiation":0,
                                'Personal Agenda':'',
                                'Buddy':'',
                                'Rival':'',
                                'Critical Injuries':{},
                                'Conditions':{
                                    'Starving':False,
                                    'Dehydrated':False,
                                    'Exhausted':False,
                                    'Freezing':False,
                                    "Drowning": False,
                                    "Suffocating": False,
                                    "Sick": False
                                            },
                                'Consumables':{'Air':0,
                                                'Food':0,
                                                'Water':0,
                                                'Power':0
                                                },
                                'Armor':["", 0],
                                'Weapons':{
                                    0:['','','',''],
                                    1:['','','',''],
                                    2:['','','',''],
                                    3:['','','','']
                                },
                                'Encumbrance':(dict['Strength'][0])*2,
                                'Talents':[tal_sel.get()],
                                'Signature Item':'',
                                'Experience Points':0,
                                'Notes':'',
                                'Panic':0
                                })
                    with open('json\\character_sheets.json', 'r+') as loaded:
                        existing_data = json.load(loaded)
                        existing_data.update(self.char)
                        new_data = json.dumps(existing_data, indent = 4)
                    with open('json\\character_sheets.json','w') as loaded:
                        loaded.write(new_data)

                    messagebox.showinfo(title='Character Created!', message = f'Character Sheet for {dict['Name']} has been created!')
                    ch_gearmenu.destroy()
                    ch_start()

        #Variables
            career = self.char[self.ch_name]['Job']
            self.tal_check = False
            self.gear_check = False
            sel0 = ttk.Combobox()
            sel1 = None
            sel2 = None
            sel3 = None
            gear_sel = {
                0:[sel0, '-None-'], 
                1:[sel1, '-None-'], 
                2:[sel2, '-None-'], 
                3:[sel3, '-None-']
            }
            gear_dict = {
                'Colonial Marine':[['M41A Pulse Rifle', 'M56A2 Smart Gun'],['M314 Motion Tracker','2x G2 Electrock Grenades'],['IRC MK.35 Pressure Suit','M3 Personnel Armor'],['Signal Flare','Deck of Cards'],[1,100],'1D6 x $100'],
                'Colonial Marshal':[['.357 Magnum Revolver','Armat Model 37A2 12-Gauge Pump-Action'],['Binoculars','Hi-Beam Flashlight'],['Personal Medkit','Stun Baton'],['D6 Doses Neversleep','Hand Radio'],[1,100],'1D6 x $100'], 
                'Company Agent':[['Leather Briefcase','Chrome Briefcase'],['Gold-Plated Pen','Rolex Watch'],['Data Transmitter Card with Corporate Clearance Level','M4A3 Service Pistol'],['D6 Doses Neversleep','D6 Doses Naproleve'],[2,100], '2D6 x $100'], 
                'Kid':[['Fishing Line','Laser Pointer'],['Magnet', 'Radio-Controlled Car'],['Yo-yo','Electronic Handheld Game'],['Personal Locator Beacon','Coloring Pens'],[1,1], '1D6 x $1'], 
                'Medic':[['Surgical Kit','IRC Mk.50 Compression Suit'],['D6 Doses Neversleep','D6 Doses Naproleve'],['Personal Medkit','D6 Doses Experimental X-Drugs'],['Samani E-Series Watch','Hand Radio'],[1,100], '1D6 x $100'], 
                'Officer':[['M4A3 Service Pistol','Rexim RXF-M5 EVA Pistol'],['Samani E-Series Watch','Binoculars'],['M314 Motion Tracker','IRC Mk.50 Compression Suit'],['Seegson P-DAT','IFF Transponder'],[2,100], '2D6 x $100'],
                'Pilot':[['M4A3 Service Pistol','PR-PUT Uplink Terminal'],['Hand Radio','D6 Flares'],['Maintenance Jack','Seegson P-DAT'],['Seegson System Diagnostic Device', 'IRC Mk.50 Compression Suit'],[1,100], '1D6 x $100'], 
                'Roughneck':[['Cutting Torch','Watumi DV-303 Bolt Gun'],['D6 Hydr8tion','Maintenance Jack'],['Stash of Hard Liquor','IRC Mk.50 Compression Suit'],['Hi-Beam Flashlight','Seegson C-Series Magnetic Tape Recorder'],[1,100], '1D6 x $100'], 
                'Scientist':[['Digital Video Camera','Hand Radio'],['Seegson P-DAT','Neuro Visor'],['Seegson System Diagnostic Device','Personal Data Transmitter'],['M314 Motion Tracker','Personal Medkit'],[1,100], '1D6 x $100']
            }    
            tal_dict = {
                'Colonial Marine':['Banter','Overkill','Past the Limit'],
                'Colonial Marshal':['Authority','Investigator','Subdue'], 
                'Company Agent':['Cunning','Personal Safety','Take Control'], 
                'Kid':['Beneath Noise','Dodge','Nimble'], 
                'Medic':['Calming Presence','Compassion','Field Surgeon'], 
                'Officer':['Field Commander','Influence','Pull Rank'], 
                'Pilot':['Full Throttle','Like the Back of Your Hand','Reckless'], 
                'Roughneck':['Resilient','The Long Haul','True Grit'], 
                'Scientist':['Analysis','Breakthrough','Inquisitive']
                    }


        #Widgets

            tal_frame = ttk.Frame(ch_gearmenu, style = 'Alien.TFrame')
            tal_frame.pack(pady = 10)
            ttk.Label(tal_frame, text = 'Select ONE Talent', style = 'NewChar.Alien.TLabel').pack()
            tal_sel = ttk.Combobox(tal_frame, values = tal_dict[career], font = ('Courier New', 12), state = 'readonly', style = 'Alien.TCombobox')
            tal_sel.pack()
            tal_sel.set('-Select One-')
            tal_sel.bind('<<ComboboxSelected>>', tal_val)

            gear_frame = ttk.Frame(ch_gearmenu, style = 'Alien.TFrame')
            gear_frame.pack(pady = 10)
            ttk.Label(gear_frame, text = 'Select TWO Gear:', style = 'NewChar.Alien.TLabel').pack()
            i = 0
            while i < 4:
                gear_sel[i][0] = ttk.Combobox(gear_frame, values=('-None-',gear_dict[career][i][0],gear_dict[career][i][1]), state = 'readonly', style = 'Alien.TCombobox', font = ('Courier New', 12))
                gear_sel[i][0].pack()
                gear_sel[i][0].set('-None-')
                gear_sel[i][0].bind('<<ComboboxSelected>>', lambda event, a = i: gear_val(event, a))
                i +=1   

            roll_bt = ttk.Button(ch_gearmenu, text = f'Roll for Cash ({gear_dict[career][5]})', command = lambda: roll_cash(gear_dict[career][4][0]), style = 'Small.TButton')
            roll_bt.pack(pady = 10)

            self.dice_frame = ttk.Frame(ch_gearmenu, style = 'Dice.TFrame')
            g_commit_bt = ttk.Button(ch_gearmenu, text = 'Commit and Save', command = lambda: commit_gear(), state = DISABLED, style = 'Small.TButton')
    #endregion

##LOAD CHARACTER##
    #region Load Character
        def ch_load():
            self.load_char_on = False
            load_party('character_sheets.json', load_char)

        #Load Character Buttons
        def load_char(num):
            #These VARs pulled from JSON
            name = self.names_list[num]
            dict = self.load_dict[name]

            stats = ['Health','Stress','Strength','Agility','Wits','Empathy']

            if self.load_char_on == False:
                self.load_char_on = True
                self.load_name = 'none'
                ttk.Label(self.pm_info, text =  dict['Name'].upper(), background = aBlack, font = ('Courier New', 16, 'bold'), foreground = 'white').pack(anchor = 'w')
                ttk.Label(self.pm_info, text = dict['Job'], background = aBlack, font = ('Courier New', 13, 'bold italic'), foreground = 'white').pack(anchor = 'w')
                ttk.Label(self.pm_info, background = aBlack).pack(anchor = 'w')
                for stat in stats:
                    ttk.Label(self.pm_info, text = f'{stat}:{dict[stat]}', background = aBlack, font = ('Courier New', 12), foreground = 'white').pack(anchor = 'w')

                select_party(num)
                self.del_bt.config(command = lambda: delete_char(num))
                self.sel_bt.config(text = 'Open', command = lambda: open_char(num))
            
            elif self.load_char_on == True:
                self.load_char_on = False
                self.pm_info.destroy()
                self.pm_info = ttk.Frame(self.pm_main, height = 330, width = 230, style = 'Alien.TFrame')
                self.pm_info.pack_propagate(False)
                self.pm_info.place(x = 355, y = 75)
                load_char(num) 

        #Delete Character
        def delete_char(num):
            del_confirm = messagebox.askyesno(title = 'Delete', message = f'Delete {self.names_list[num]}?')
            if del_confirm == True:
                with open('json\\character_sheets.json', 'r') as load_char:
                    char_dict = json.load(load_char)
                    char_dict.pop(self.names_list[num])
                with open('json\\character_sheets.json', 'w') as load_char:
                    overwrite_dict = json.dumps(char_dict, indent = 4)
                    load_char.write(overwrite_dict)
                ch_load()
            else:
                pass
    #endregion

##--OPEN CHARACTER SHEET--##
        def open_char(num):

        #region VAR PULLED FROM JSON AND TOP LEVEL
        
            name = self.names_list[num]
            self.name = name

            with open('json\\character_sheets.json','r') as load_dict:
                dict = json.load(load_dict)[name]

            cs_top = Toplevel(background=aBlack)
            cs_top.title(name)
            cs_top.geometry('1354x754+350+150')
            cs_top.resizable(True, True)
            cs_top.minsize(width = 1354, height = 754)

            sheet = ttk.Frame(cs_top, style = 'Alien.TFrame')
            sheet.place(relx = 0.5, rely = 0.5, relheight=1, relwidth=1, anchor = 'center')
            

            sheet_bg = ttk.Label(sheet, image = self.sheet_bg_normal)
            sheet_bg.place(x = 0, y = 0)
        #endregion

    #Functions

        #Edit Health Bar
            def edit_hp(act):
                if act == '-':
                    self.hp -= 1
                    if self.hp < 0:
                        self.hp = 0
                    hp_ct.config(text = f'Health {self.hp}/{dict['Max Health']}')
                    hp_bar.config(value = self.hp)

                elif act == '+':
                    #Status Effect Stops Health
                    if self.starv.get() or self.dehyd.get() or self.freez.get() or self.sick.get() == True:
                        pass

                    else:
                        self.hp += 1
                        if self.hp > dict['Max Health']:
                            self.hp = dict['Max Health']
                        hp_ct.config(text = f'Health {self.hp}/{dict['Max Health']}')
                        hp_bar.config(value = self.hp)

                elif act == 0:
                    self.hp = 0
                    hp_ct.config(text = f'Health {self.hp}/{dict['Max Health']}')
                    hp_bar.config(value = self.hp)

                if self.hp == 0:
                    self.crit = True
                    crit_on()
                
                if self.hp == 1 and self.crit == True:
                    self.crit = False
                    crit_on()
                
                update_sheet()

        #Make Stat Boxes
            def stat_box(key, type):
                Stats[key][0] = ttk.Frame(sheet, style = 'Alien.TFrame')
                ttk.Label(sheet, text = f'{key}', style = 'Inv.Alien.TLabel', font = ('Courier New', 10)).place(x = Stats[key][2], y = Stats[key][3]-45, anchor = 'n')
                Stats[key][1] = ttk.Label(Stats[key][0], text = f'{dict[key]}', font = ('Courier New', 30, 'bold'), foreground = 'white', image=ch_skill_img, compound = 'center', background = aBlack)
                if key not in ['Strength', 'Agility', 'Wits', 'Empathy']: 
                    ttk.Label(sheet, text = f'{dict[key]}', font = ('Courier New', 12), background = aBlack, foreground= 'white').place(x = Stats[key][2]-46, y = Stats[key][3]+14, anchor = 'center')
                    Stats[key][1].config(text = f'{dict[Stats[key][4]]+int(dict[key])}')
                Stats[key][1].pack(side = LEFT)
                ttk.Button(Stats[key][0], text = 'Roll', width = 4, command = lambda: rollqueue(type, key), style = 'Small.TButton').pack(side = LEFT)
                Stats[key][0].place(x = Stats[key][2], y = Stats[key][3], anchor = 'center')

        #Edit Cash
            def edit_cash(num):
                if num == '':
                    num = 0
                result = int(num)
                self.cash += result
                cash.config(text = f'${self.cash}')
                math.delete(0, END)
                update_sheet()

        #Edit Gear
            def edit_gear(act):
                if act == 'Edit':
                    for g in GEAR:
                        GEAR[g][0].config(state = ACTIVE)
                        GEAR[g][1].config(state = 'readonly')
                    gear_edit.config(text = 'Save', command = lambda: edit_gear('Save'))
                    self.sigitem.config(state = ACTIVE)

                if act == 'Save':                       
                    self.gear = []
                    for g in GEAR:
                        GEAR[g][0].config(state = 'readonly')
                        GEAR[g][1].config(state = DISABLED)
                        self.gear.append([GEAR[g][0].get(), GEAR[g][1].get()])
                    self.sigitem.config(state = 'readonly')
                    gear_edit.config(text = 'Edit Inventory', command = lambda: edit_gear('Edit'))
                    add_weight()
                    update_sheet()

        #Edit Notes
            def edit_notes():
                if self.notes.cget('state') == 'disabled':
                    self.notes.config(state = 'normal')
                    notes_edit.config(text = 'Lock Notes')
                elif self.notes.cget('state') == 'normal':
                    self.notes.config(state = 'disabled')
                    notes_edit.config(text = 'Unlock Notes')
                    update_sheet()

        #Edit Stress and Radiation
            def edit_strsrad(var,type):
                if type == 'Stress':
                    if var == -1 and (self.starv.get() == True or self.dehyd.get() == True or self.exhst.get() == True or self.freez.get() == True):
                        pass
                    else:
                        self.stress += var
                        if self.stress > 10:
                            self.stress = 10
                        elif self.stress < 0:
                            self.stress = 0
                        else:
                            STRSRAD['Stress'][1].config(text = f'{'■'*self.stress}')
                            update_sheet()

                elif type == 'Radiation':
                    old_rad = self.rad
                    self.rad += var

                    if self.rad > 10:
                        self.rad = 10
                    elif self.rad < self.permrad:
                        self.rad = self.permrad

                    if var == 1:
                        rollqueue('Radiation', 'Gain')

                    elif var == -1 and old_rad > self.permrad:
                        rollqueue('Radiation', 'Heal')

                    STRSRAD['Radiation'][1].config(text = f'{'■'*self.rad}')         
                    update_sheet()

        #Edit Conditions       
            def edit_cond(cond):
                if COND[cond][1].get() == True:

                    COND[cond][2].config(state = ACTIVE)                
                    status.config(text = 'Status: AFFLICTED')
                    sheet_bg.config(image = self.sheet_bg_afflicted)
                elif COND[cond][1].get() == False:
                    self.suffocate = 0
                    self.exhaust = 0
                    COND[cond][2].config(state = DISABLED)
                    if self.starv.get() == False and self.dehyd.get() == False and self.exhst.get() == False and self.freez.get() == False:
                        status.config(text = 'Status: STABLE')
                        sheet_bg.config(image = self.sheet_bg_normal)

                update_sheet()

        #Reset XP to 0 after spending
            def reset_spend():
                self.xp -= 5
                if self.xp < 0:
                    self.xp = 0
                self.xp_l.config(text = f'{'■'*self.xp}')
                if self.xp >= 5:
                    self.spend.config(state = ACTIVE)
                else:
                    self.spend.config(state = DISABLED)

        #Edit Experience Points
            def edit_xp(num):
                if num == -5:
                    add_stat_win()
                else:
                    self.xp += num
                    if self.xp > 10:
                        self.xp = 10
                    elif self.xp < 0:
                        self.xp = 0
                    else:            
                        self.xp_l.config(text = f'{'■'*self.xp}')
                        update_sheet()

                if self.xp >= 5:
                    self.spend.config(state = ACTIVE)
                else:
                    self.spend.config(state = DISABLED)

        #Add to Stats
            def add_stat_win():
                stat_win = Toplevel(background=aBlack)

            #Function
                def commit():

                    #Add Talent Func
                    def commit_add_tal(choice):
                        if tal_ent.get() != '':
                            self.add_tal = tal_ent.get()
                            tal_win.destroy()
                            rollqueue('TalWits', choice)
                        else:
                            messagebox.showerror(title='Enter Text', message = 'Please enter a talent in the text field')

                    stat_win.destroy()
                    if selected.get() == 'Talent':
                        tal_win = Toplevel(background=aBlack)
                        ttk.Label(tal_win, text = 'Add a Talent', style = 'Inv.Alien.TLabel').pack(pady = 10)
                        tal_ent = ttk.Entry(tal_win, style = 'Alien.TEntry')
                        tal_ent.pack(pady = 10)
                        ttk.Button(tal_win, text = 'Wits Roll', command= lambda: commit_add_tal('Roll'), style = 'Small.TButton').pack(pady = 5)
                        ttk.Button(tal_win, text = 'Add Without Roll', command= lambda: commit_add_tal('No Roll'), style = 'Small.TButton').pack()

                    else:
                        self.add_skl = selected.get()
                        update_sheet()
                        Stats[self.add_skl][1].config(text = (int(dict[Stats[self.add_skl][4]]) + int(dict[self.add_skl])))
                        self.add_skl = None


            #Variables
                cc = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                hm = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                st = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                rc = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                mb = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                pl = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                ob = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                sv = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                ct = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                cm = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                mn = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')
                ma = ttk.Radiobutton(stat_win, style = 'Alien.TRadiobutton')

                selected = StringVar()

                SKILL = {
                    'Close Combat':[dict['Close Combat'], cc],
                    'Heavy Machinery':[dict['Heavy Machinery'], hm],
                    'Stamina':[dict['Stamina'], st],
                    'Ranged Combat':[dict['Ranged Combat'], rc],
                    'Mobility':[dict['Mobility'], mb],
                    'Piloting':[dict['Piloting'], pl],
                    'Observation':[dict['Observation'], ob],
                    'Survival':[dict['Survival'], sv],
                    'Comtech':[dict['Comtech'], ct],
                    'Command':[dict['Command'], cm],
                    'Manipulation':[dict['Manipulation'], mn],
                    'Medical Aid':[dict['Medical Aid'], ma]
                    }
                
            #Widgets    
                ttk.Label(stat_win, text = 'Add +1 to a Skill', style = 'Inv.Alien.TLabel').grid(row = 0, columnspan = 3, pady = 10)

                for i, s in enumerate(SKILL):
                    ttk.Label(stat_win, text = s, style = 'Inv.Alien.TLabel').grid(row = i+1, column = 0)
                    ttk.Label(stat_win, text = SKILL[s][0], style = 'Inv.Alien.TLabel').grid(row = i+1, column = 1)
                    SKILL[s][1].config(value = s, variable = selected, command = lambda: commit_bt.config(state = ACTIVE))
                    SKILL[s][1].grid(row = i+1, column = 2)

                ttk.Label(stat_win, text = 'Add a Talent', style = 'Inv.Alien.TLabel').grid(row = 13, column = 0)
                ttk.Radiobutton(stat_win, value =  'Talent', variable = selected, command = lambda: commit_bt.config(state = ACTIVE), style = 'Alien.TRadiobutton').grid(row = 13, column = 2)
                
                commit_bt = ttk.Button(stat_win, text = 'Commit', state = DISABLED, command = commit, style = 'Small.TButton')
                commit_bt.grid(row = 14, columnspan = 3, pady = 10)
   
        #Add Weight
            def add_weight():
                self.weight = 0
                for w in GEAR:
                    if GEAR[w][1].get() == 'Set':
                        pass
                    else:
                        self.weight += float(GEAR[w][1].get())

                for c in CONSUME:
                    self.weight += ((CONSUME[c][2] - 1)//4) +1

                ncom.config(text = f'{self.weight}/{dict['Encumbrance']}')
                if self.weight >= dict['Encumbrance']*2:
                    overncom.config(text = '-IMMOBILE-')
                elif self.weight > dict['Encumbrance']:
                    overncom.config(text = '-OVER ENCUMBERED-')
                else:
                    overncom.config(text = '')

        #Edit Consumables
            def edit_consume(num, c):
                    if num == -1 and CONSUME[c][2] == 0:
                        pass
                    else:
                        CONSUME[c][3].config(state = ACTIVE)
                        CONSUME[c][2] += num
                        CONSUME[c][1].config(text = CONSUME[c][2])
                        if CONSUME[c][2] == 0:
                            CONSUME[c][3].config(state = DISABLED)
                        add_weight()
                        update_sheet()

        #Edit Equipment
            def edit_equip(act):
                if act == 'Edit':
                    armor.config(state = ACTIVE)
                    ar_val.config(state = ACTIVE)
                    for w in dict['Weapons']:
                        for n in WEAPONS:
                            WEAPONS[int(w)][n].config(state = ACTIVE)
                    equip_bt.config(text = 'Save Equipment', command = lambda: edit_equip('Save'))
                elif act == 'Save':
                    armor.config(state = DISABLED)
                    ar_val.config(state = DISABLED)
                    for w in dict['Weapons']:
                        for n in WEAPONS:
                            WEAPONS[int(w)][n].config(state = DISABLED)
                    equip_bt.config(text = 'Edit Equipment', command = lambda: edit_equip('Edit'))
                    update_sheet()

        #Affect Health and Stress
            def affect_hp_strs():
                edit_hp('-')
                edit_strsrad(1, 'Stress')
                update_sheet()

        #Critical Injury Button Appears
            def crit_on():
                if self.crit == True:
                    crit_bt.config(image = inj_bt_active)
                    crit_bt.bind('<ButtonPress>', lambda event: rollqueue('Critical Injury', 'Critical Injury'))
                    sheet_bg.config(image = self.sheet_bg_broken)
                else:
                    crit_bt.config(image = inj_bt_inactive)
                    crit_bt.unbind('<ButtonPress>')
                    sheet_bg.config(image = self.sheet_bg_normal)

        #Death Button Appears
            def death_on(death, time = '', mod = 0):
                if death == True:
                    death_bt.config(image = death_bt_active)
                    death_bt.bind('<ButtonPress>', lambda event: rollqueue('Death', 'Death', mod = mod))
                    
                    sheet_bg.config(image = self.sheet_bg_death)

                    death_time.config(text = time)
                    death_freq.config(foreground='white')
                    resus_bt.config(image = resus_bt_active)
                    resus_bt.bind('<ButtonPress>', lambda event: deactivate_death())
                    
                else:
                    pass

        #Edit Personal Info
            def edit_persinfo():
                if self.agenda.cget('state') == 'disabled':
                    self.agenda.config(state = 'normal')
                    self.buddy.config(state = ACTIVE)
                    self.rival.config(state = ACTIVE)
                    pers_bt.config(text = 'Save Personal Info')
                    
                elif self.agenda.cget('state') == 'normal':
                    self.agenda.config(state = 'disabled')
                    self.buddy.config(state = DISABLED)
                    self.rival.config(state = DISABLED)
                    pers_bt.config(text = 'Edit Personal Info')
                update_sheet()
      
        #Pack Critical Injuries into Frame
            def pack_injuries():
                for i, j in enumerate(self.injs):
                    INJS[i][0] = j
                    INJS[i][1] = ttk.Entry(crit_frame, width = 20, style = 'Alien.TEntry', font = ('Courier New', 11))
                    INJS[i][1].insert(0, self.injs[j][0])
                    INJS[i][1].config(state = DISABLED)
                    INJS[i][1].grid(row = i+1, column = 0, padx = 5)

                    if dict['Race'] == 'Human':
                        recov_num = self.injs[j][5]
                        INJS[i][2] = ttk.Button(crit_frame, width = 8, style = 'Smaller.TButton')
                        INJS[i][2].grid(row = i+1, column = 1)

                    #No recovery needed
                        if recov_num == 'null':
                            INJS[i][2].config(text = 'Recover', command = lambda index = i: heal_inj(index))

                    #Permanent injuries have no recovery
                        elif recov_num == 'Permanent':
                            INJS[i][2].destroy()

                    #Start New Countdown
                        elif recov_num == '1D6' or recov_num == '2D6' or recov_num == '3D6':
                            INJS[i][2].config(text = f'Roll {recov_num[0]}D6', command = lambda num = int(recov_num[0]), inj_num = j, index = i: recovery_roll(num, index, inj_num))

                    #pick up existing countdown
                        else:            
                            if recov_num == 1:
                                INJS[i][2].config(text = f'{recov_num} Day', command = lambda index = i, inj = j, days = recov_num: heal_countdown(days, index, inj))
                            elif recov_num > 0:
                                INJS[i][2].config(text = f'{recov_num} Days', command = lambda index = i, inj = j, days = recov_num: heal_countdown(days, index, inj))
                            elif recov_num <= 0:
                                INJS[i][2].config(text = 'Recover', command = lambda: heal_inj(i))

                    elif dict['Race'] == 'Synth':
                        INJS[i][2] = ttk.Button(crit_frame, text = 'Repair', command = lambda index = i: heal_inj(index))
                        INJS[i][2].grid(row = i+1, column = 1)

        #Roll Initial Recovery Dice
            def recovery_roll(dice, index, inj_num):
                roll(dice, INJS[index][3], 'b')
                total = 0
                for n in INJS[index][3]:
                    total += int(n[0])
                INJS[index][3] = total
                INJS[index][2].config(text = f'{INJS[index][3]} Days', command = lambda: heal_countdown(INJS[index][3], index, inj_num))
                self.injs[inj_num][5] = INJS[index][3]
                update_sheet()

        #Tick on Healing Countdown
            def heal_countdown(days, index, inj_num):
                days -= 1
                if days == 1:
                    INJS[index][2].config(text = f'{days} Day', command = lambda: heal_countdown(days, index, inj_num))
                elif days > 0:
                    INJS[index][2].config(text = f'{days} Days', command = lambda: heal_countdown(days, index, inj_num))
                elif days <= 0:
                    INJS[index][2].config(text = 'Recover', command = lambda i = index: heal_inj(i))
                self.injs[inj_num][5] = days
                update_sheet()

        #Fully Heal
            def heal_inj(index):
                print(index)
                print(INJS[index][0])
                self.injs.pop(INJS[index][0])
                INJS[index][1].destroy()
                INJS[index][2].destroy()
                update_sheet()
            
        #UPDATE CHARACTER SHEET
            def update_sheet():
                #add Consumables
                self.consume = {}
                for c in CONSUME:
                    self.consume.update({c: CONSUME[c][2]})

                #add Weapons
                self.weapons = {}
                for w in dict['Weapons']:
                    weap = []
                    for n in WEAPONS:
                        weap.append(WEAPONS[int(w)][n].get())
                    self.weapons.update({w:weap})

                #adding Skill Points
                if self.add_skl != None:
                    dict.update({self.add_skl:int(dict[self.add_skl])+1})
                    reset_spend()

                #add a Talent
                elif self.add_tal != None:
                    dict['Talents'].append(self.add_tal)
                    tal.config(state = 'normal')
                    tal.insert('1.0', f'{self.add_tal}\n')
                    tal.config(state = 'disabled')
                  
                #add armor
                self.armor = [armor.get(), ar_val.get()]
                
                print('Saved!')
                new_data = {dict['Name']:
                    {
                        "Name": dict['Name'],
                        "Job": dict['Job'],
                        "Race": dict['Race'],
                        "Strength": dict['Strength'],
                        "Agility": dict['Agility'],
                        "Wits": dict['Wits'],
                        "Empathy": dict['Empathy'],
                        "Close Combat": dict['Close Combat'],
                        "Heavy Machinery": dict['Heavy Machinery'],
                        "Stamina": dict['Stamina'],
                        "Ranged Combat": dict['Ranged Combat'],
                        "Mobility": dict['Mobility'],
                        "Piloting": dict['Piloting'],
                        "Observation": dict['Observation'],
                        "Survival": dict['Survival'],
                        "Comtech": dict['Comtech'],
                        "Command": dict['Command'],
                        "Manipulation": dict['Manipulation'],
                        "Medical Aid": dict['Medical Aid'],
                        "Talents": dict['Talents'],
                        "Health": self.hp,
                        'Max Health':dict['Max Health'],
                        "Stress": self.stress,
                        "Gear": self.gear,
                        "Encumbrance": dict['Encumbrance'],
                        "Armor": self.armor,
                        "Weapons": self.weapons,
                        "Cash": self.cash,
                        "Consumables": self.consume,
                        "Radiation": self.rad,
                        "Permanent Radiation":self.permrad,
                        "Critical Injuries": self.injs,
                        "Conditions": {
                            "Starving": self.starv.get(),
                            "Dehydrated": self.dehyd.get(),
                            "Exhausted": self.exhst.get(),
                            "Freezing": self.freez.get(),
                            "Drowning": self.drown.get(),
                            "Suffocating": self.sfct.get(),
                            "Sick": self.sick.get()
                        },
                        "Personal Agenda": self.agenda.get("1.0",END),
                        "Buddy": self.buddy.get(),
                        "Rival": self.rival.get(),
                        "Signature Item": self.sigitem.get(),
                        "Experience Points": self.xp,
                        'Notes':self.notes.get("1.0",END),
                        'Panic':self.panic
                    },
                }              

                with open('json\\character_sheets.json', 'r') as load_char:
                    char_sheet = json.load(load_char)
                    char_sheet.update(new_data)
                    dumped_sheet = json.dumps(char_sheet, indent = 4)
                
                with open('json\\character_sheets.json', 'w') as load_char:
                    load_char.write(dumped_sheet)

        #Panic Button Appears
            def panic():
                panic_bt.config(image=panic_bt_active)
                panic_bt.bind('<ButtonPress>', lambda event: rollqueue('Panic', 'Panic'))

                sheet_bg.config(image = self.sheet_bg_panic)
                
        #End Panic State
            def panic_end():
                self.panic = 0
                # panic_off.config(state = DISABLED)
                end_panic_bt.config(image = end_panic_bt_inactive)
                end_panic_bt.unbind('<ButtonPress>')

                panic_bt.config(image=panic_bt_inactive)
                panic_bt.unbind('<ButtonPress>')

                sheet_bg.config(image = self.sheet_bg_normal)
                update_sheet()
                
        #ROLL DICE UNIVERSAL
            def rollqueue(type, key, keylist = [], mod = 0):
                self.roll_info.destroy()
                self.dice_frame.destroy()
                self.dice_label.destroy()
                self.roll_info = ttk.Frame(self.roll_frame, style = 'Dice.TFrame')
                self.roll_info.pack()
                self.roll_nm = ttk.Label(self.roll_info, text = f'{key.upper()} ROLL', style = 'NewChar.Alien.TLabel', background = '#182318')
                self.roll_nm.pack()

            #ROLL TYPES
                if type == 'Skill':

                #Variables                
                    skls = {
                        'Close Combat':'Strength',
                        'Heavy Machinery':'Strength',
                        'Stamina':'Strength',
                        'Ranged Combat':'Agility',
                        'Mobility':'Agility',
                        'Piloting':'Agility',
                        'Observation':'Wits',
                        'Survival':'Wits',
                        'Comtech':'Wits',
                        'Command':'Empathy',
                        'Manipulation':'Empathy',
                        'Medical Aid':'Empathy'
                        }
                    
                    if key in skls:
                        base = int(dict[key]) + int(dict[skls[key]])
                    else: 
                        base = int(dict[key])

                #Widgets
                    add_mod = ttk.Frame(self.roll_info, style = 'Dice.TFrame')
                    add_mod.pack()

                    ttk.Label(add_mod, text = 'Gear Modifier\n(Weapons Excluded)', style = 'NewChar.Alien.TLabel',background = '#182318').grid(row = 0, column = 0)
                    equip_mod = ttk.Combobox(add_mod, values = ['+4','+3','+2','+1','0','-1','-2','-3','-4'], font = ('Courier New', 12), width = 3, style = 'Alien.TCombobox')
                    equip_mod.set('0')
                    equip_mod.grid(row = 1, column = 0)

                    ttk.Label(add_mod, text = 'Difficulty Modifier', style = 'NewChar.Alien.TLabel',background = '#182318').grid(row= 0, column = 1)
                    dfcty_mod = ttk.Combobox(add_mod, values = ['+2','+1','0','-1','-2'], font = ('Courier New', 12), width = 3, style = 'Alien.TCombobox')
                    dfcty_mod.set('0')
                    dfcty_mod.grid(row = 1, column = 1)

                    ttk.Button(self.roll_info, text = 'ROLL', command = lambda: rolldice(type, key, base = base, frame = self.roll_frame, stress = self.stress, mod= int(equip_mod.get()) + int(dfcty_mod.get()), push = True), style = 'SmDice.TButton').pack()

                elif type == 'Armor':
                    rolldice('Armor', 'Armor', frame = self.roll_frame, base = int(key))

                elif type == 'Weapon':
                    base = 0
                    mod = keylist[1]
                    if keylist[3] == 'Engaged':
                        base += int(dict['Close Combat']) + int(dict['Strength'])
                    else: 
                        base += int(dict['Ranged Combat']) + int(dict['Agility'])

                    rolldice('Skill', keylist[0], base = base, stress = self.stress, frame = self.roll_frame, mod = int(mod), push = True)

                elif type == 'Radiation':
                    if key == 'Gain':
                        rolldice('Radiation', 'Gain', frame = self.roll_frame, base = self.rad), 
                    elif key == 'Heal':
                        rolldice('Radiation','Heal', frame = self.roll_frame, stress = self.rad+1)                  

                elif type == 'Consumable':
                    if CONSUME[key][2] == 0:
                        pass
                    else:
                        rolldice('Consumable', key, frame = self.roll_frame, stress = CONSUME[key][2], push = True)

                elif type == 'Condition':
                    base = dict['Stamina']+ dict['Strength']
                    rolldice('Skill', key, frame = self.roll_frame, base = base, stress = self.stress, push = True)

                elif type == 'TalWits':
                    if key == 'Roll':
                        rolldice('TalWits', 'Roll', frame = self.roll_frame, base = dict['Wits'])
                    elif key == 'No Roll':
                        self.roll_info.destroy()
                        self.roll_nm.destroy()
                        reset_spend()
                        update_sheet()
                        self.add_tal = None

                elif type == 'Critical Injury':
                    rolldice('Critical Injury','Critical Injury', frame = self.roll_frame, base = 2)

                elif type == 'Death':
                    rolldice('Death', 'Death', frame = self.roll_frame, base = int(dict['Stamina']) + int(dict['Strength']), mod = mod)

                elif type == 'Panic':
                    push_bt.config(image = push_bt_inactive)
                    push_bt.unbind('<ButtonPress>')
                    rolldice('Panic', 'Panic', frame = self.roll_frame)

                elif type == 'Trauma':
                    rolldice('Trauma', 'Trauma', frame = self.roll_frame)   

        #Decide How to Roll
            def rolldice(type, key, frame, base = 0, stress = 0, mod = 0, push = False):

                #Set Up
                self.roll_info.destroy()
                self.roll_nm.destroy()
                self.dice_frame = ttk.Frame(frame, style = 'Dice.TFrame')
                self.dice_frame.pack()
                self.dice_label = ttk.Label(self.dice_frame, text = f'{key.upper()} ROLL', style =  'NewChar.Alien.TLabel', background = '#182318')
                self.dice_label.grid(row = 0, columnspan=12)

                #Gatekeep: Synths can't push
                if dict['Race'] == 'Synth':
                    push = False

                #Roll Skill Check And Weapon Rolls AND Conditions
                if type == 'Skill':
                    #Check for Injury Modifiers
                    if dict['Race'] == 'Human':
                        for j in self.injs:
                            if key in self.injs[j][4][0]:
                                mod += self.injs[j][4][1]

                    #Compound Negative Condition Modifiers
                    if key == 'Suffocating':
                        base -= self.suffocate
                    elif key == 'Exhausted':
                        base -= self.exhaust
                    if base < 0: base = 0

                    #Skill Roll
                    total_b = base + mod
                    b_rolls = []
                    s_rolls = []
                    roll(total_b, b_rolls, 'b')
                    roll(stress, s_rolls, 's')
                    self.all_dice = b_rolls + s_rolls
                    random.shuffle(self.all_dice)
                    display_dice(self.all_dice)

                    if key == 'Suffocating':
                        self.suffocate += 1
                    elif key == 'Exhausted':
                        self.exhaust += 1

                    if '6b' not in self.all_dice and '6s' not in self.all_dice:
                        
                        if key == 'Starving' or key == 'Freezing':
                            affect_hp_strs()
                            if key == 'Starving' and self.hp == 0:
                                death_on(True, 'One Day')
                            elif key == 'Freezing':
                                death_on(True, '(Ask GM)')
                        elif key == 'Drowning' or key == 'Sick':
                            edit_hp('-')
                            if key == 'Drowning':
                                death_on(True, 'One Round')
                            if key == 'Sick':
                                death_on(True, 'One Shift')
                        elif key == 'Suffocating':
                            edit_hp(0)
                            death_on(True, 'One Round')

                        elif key == 'Exhausted':
                            ttk.Label(self.dice_frame, text = 'Asleep for 1 shift', style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 5, columnspan = 12)

                #Roll Armor
                elif type == 'Armor':
                    armor = []
                    roll(base, armor, 'b')
                    display_dice(armor)

                #Roll for Raditation
                elif type == 'Radiation':
                    self.dice_label.config( text = 'RADIATION ROLL')
                    if key == 'Gain':
                        gains = []
                        roll(base, gains, 'b')
                        display_dice(gains)
                        for d in gains:
                            if d == '6b':
                                edit_hp('-')
                    elif key == 'Heal':
                        heals = []
                        roll(stress, heals, 's')
                        display_dice(heals)
                        for d in heals:
                            if d == '1s':
                                self.permrad += 1
                        permrad_l.config(text = f"Permanent Radiation: {self.permrad}")
                        if self.rad < self.permrad:
                            self.rad = self.permrad
                        STRSRAD['Radiation'][1].config(text = f'{'■'*STRSRAD['Radiation'][2]}')

                #Roll for Consumable
                elif type == 'Consumable':
                    self.all_dice = []
                    roll(stress, self.all_dice, 's')
                    display_dice(self.all_dice)
                    for d in self.all_dice:
                        if d == '1s':
                            edit_consume(-1, key)
                            sheet_bg.config(image = self.sheet_bg_normal)

                #Roll for Talent
                elif type == 'TalWits':
                    if key == 'Roll':
                        self.dice_label.config(text = 'WITS ROLL')
                        wits = []
                        roll(base, wits, 'b')
                        display_dice(wits)
                        if '6b' in wits:
                            reset_spend()
                            update_sheet()
                        else:
                            pass
                        self.add_tal = None

                #Roll for Critical Injury
                elif type == 'Critical Injury':
                    inj = []
                    #Injuries for Humans
                    if dict['Race'] == 'Human':
                        roll(base, inj, 'b')
                        display_dice(inj)
                        inj_num = inj[0][0] + inj[1][0]

                        with open('json\\tables.json', 'r') as load_table:
                            inj_table = json.load(load_table)['Critical Injuries']
                            self.injs.update({inj_num:inj_table[inj_num]})

                        #Adding Injury Description to Notes
                            self.notes.config(state = 'normal')
                            self.notes.insert("1.0", f'{self.injs[inj_num][0]}: ({self.injs[inj_num][1][0]}){self.injs[inj_num][3]}\n')
                            self.notes.config(state = 'disabled')
                            update_sheet()
                            self.injs = dict['Critical Injuries']

                        #Refresh the Critical Injuries Table
                            for i, j in enumerate(self.injs):
                                INJS[i][1].destroy()
                                INJS[i][2].destroy()
                            pack_injuries()

                            ttk.Label(self.dice_frame, text = self.injs[inj_num][0], style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 2, columnspan= 12)
                            ttk.Label(self.dice_frame, text = self.injs[inj_num][3], style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 3, columnspan= 12)

                            #Adding Stress
                            if self.injs[inj_num][4][0][0] == 'Stress':
                                edit_strsrad(1, 'Stress')

                            #Fatal Injuries
                            if self.injs[inj_num][1][0] == 'Fatal':
                                if self.injs[inj_num][2] != 'null':
                                    death_on(True, self.injs[inj_num][2], mod = self.injs[inj_num][1][1])
                                else:
                                    hp_ct.config(text = 'Deceased')
                                    hp_bar.config(value = 0)
                            else:
                                pass

                    #Injuries for Synthetics
                    elif dict['Race'] == 'Synth':
                        roll(1, inj, 'b')
                        display_dice(inj)
                        inj_num = inj[0][0]
                        with open('json\\tables.json', 'r') as load_table:
                            synth_inj = json.load(load_table)['Synth Injuries']
                            self.injs.update({inj_num:synth_inj[inj_num]})

                        #Adding Injury Description to Notes
                            self.notes.config(state = 'normal')
                            self.notes.insert("1.0", f'{self.injs[inj_num][0]}: ({self.injs[inj_num][1][0]}){self.injs[inj_num][1]}\n')
                            self.notes.config(state = 'disabled')
                            update_sheet()

                        #Refresh the Critical Injuries Table
                            for i, j in enumerate(self.injs):
                                INJS[i][1].destroy()
                                INJS[i][2].destroy()
                            pack_injuries()

                            ttk.Label(self.dice_frame, text = synth_inj[inj_num][0], style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 2, columnspan= 12)
                            ttk.Label(self.dice_frame, text = synth_inj[inj_num][1], style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 3, columnspan= 12)

                #Roll for Death
                elif type == 'Death':
                    death = []
                    death_b = base + mod
                    roll(death_b, death, 'b')
                    display_dice(death)
                    if '6b' not in death:
                        hp_ct.config(text = 'Deceased')
                        hp_bar.config(value = 0)
                        self.name += ' (deceased)'
                        namelabel.config(text = self.name)
                        update_sheet()
                    else:
                        death_on(False)

                #Roll for Panic
                elif type == 'Panic':
                    panic = []
                    roll(1, panic, 'b')
                    display_dice(panic)
                    total = int(panic[0][0]) + self.stress
                    prev_panic = self.panic
                    
                    panic_bt.config(image=panic_bt_inactive)
                    panic_bt.unbind('<ButtonPress>')

                #Setting global panic
                    if total > 6:
                        end_panic_bt.config(image = end_panic_bt_active)
                        end_panic_bt.bind('<ButtonPress>', lambda event: panic_end())
                        if total <= prev_panic:
                            total = prev_panic + 1
                        self.panic = total

                #Add or Less Stress
                    if total < 6:
                        total = 6
                        sheet_bg.config(image = self.sheet_bg_normal)
                    elif  7 <= total <= 10:
                        edit_strsrad(1, 'Stress')
                    elif 11 <= total <= 13:
                        edit_strsrad(-1, 'Stress')
                    elif total > 15:
                        total = 15
                        self.panic = 15

                #Add Mental Trauma
                    if total >= 13:
                        trauma_bt.config(image = trauma_bt_active)
                        trauma_bt.bind('<ButtonPress>', lambda event: rollqueue('Trauma', 'Trauma'))

                    with open('json\\tables.json', 'r') as load_tables:
                        panic_tb = json.load(load_tables)['Panic Roll']
                    ttk.Label(self.dice_frame, text = f'{panic_tb[str(total)][0]}', style = 'NewChar.Alien.TLabel', background = '#182318').grid(row = 90, columnspan = 12)
                    ttk.Label(self.dice_frame, text = f'{panic_tb[str(total)][1]}', style = 'Small.Alien.TLabel', background = '#182318').grid(row = 91, columnspan = 12)
                    update_sheet()

                #Roll for Trauma
                elif type == 'Trauma':
                    trauma = []
                    roll(1, trauma, 'b')
                    display_dice(trauma)
                    result = trauma[0][0]
                    with open('json\\tables.json', 'r') as load_table:
                        trauma_tb = json.load(load_table)['Mental Trauma']

                    ttk.Label(self.dice_frame, text = f'{trauma_tb[str(result)][0]}', style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 90, columnspan = 12)
                    ttk.Label(self.dice_frame, text = 'Added to Notes', style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 91, columnspan = 12)
                    #Add trauma to notes
                    self.notes.config(state = 'normal')
                    self.notes.insert("1.0", f'{trauma_tb[str(result)][0]}: {trauma_tb[str(result)][1]}\n')
                    self.notes.config(state = 'disabled')
                    trauma_bt.config(image = trauma_bt_inactive)
                    trauma_bt.unbind('<ButtonPress>')
                    update_sheet()

                #Push a roll
                elif type == 'Push':
                    self.push_ct += 1
                    self.dice_label.config(text = f'PUSHED {key.upper()} ROLL')
                    self.stress += 1
                    self.all_dice.append('2s')
                    if self.stress > 10:
                        self.stress = 10
                    STRSRAD['Stress'][1].config(text = f'{'■'*self.stress}')

                    for i, d in enumerate(self.all_dice):
                        if d[0] != '6':
                            self.all_dice.pop(i)
                            new = random.randint(1,6)
                            newnew = f'{new}{d[1]}'
                            self.all_dice.insert(i, newnew)
                    
                    if "1s" in self.all_dice:
                        panic_bt.config(image=panic_bt_active)
                        panic_bt.bind('<ButtonPress>', lambda event: rollqueue('Panic', 'Panic'))
                        #Reset Push Ct
                        self.push_ct = 0
                        push_bt.config(image = push_bt_inactive)
                        push_bt.unbind('<ButtonPress>')
                        sheet_bg.config(image = self.sheet_bg_panic)
                    
                    elif self.push_ct == 2:
                        self.push_ct = 0
                        push_bt.config(image = push_bt_inactive)
                        push_bt.unbind('<ButtonPress>')

                    display_dice(self.all_dice)

                #Initiate a Push
                if push == True:
                    if '1s' not in self.all_dice:
                        push_bt.config(image = push_bt_active)
                        push_bt.bind('<ButtonPress>', lambda event: (self.dice_frame.destroy(), rolldice('Push', key, frame, base, stress, mod, push = False)))

                    else:
                        pass

        #The actual Roll
            def roll(dice, list, letter):
                while dice > 0:
                    roll = str(random.randint(1,6)) + letter
                    list.append(roll)
                    dice -= 1

                if "1s" in list:
                    panic()

        #Display the Dice
            def display_dice(list):
                for i, dice in enumerate(list):
                    ttk.Label(self.dice_frame, image = dicedict[dice], background = '#182318').grid(row = (i // 13)+1, column = i % 13)

                now = datetime.datetime.now()
                time = now.strftime("Rolled on %m/%d/%Y, at %H:%M:%S")
                stamp = ttk.Label(sheet, text = time, style = 'White.TLabel', background = '#182318')
                stamp.place(x = 320, y = 550, anchor = 'nw')

        #Deactivate Death Roll Button
            def deactivate_death():
                death_bt.config(image = death_bt_inactive)
                death_bt.unbind('<ButtonPress>')

                resus_bt.config(image = resus_bt_inactive)
                resus_bt.unbind('<ButtonPress>')

                death_time.config(text = '')
                death_freq.config(foreground='#555555')

                
                sheet_bg.config(image = self.sheet_bg_normal)

    #Variables
        #region HEALTH BAR
            self.hp = dict['Health']

        #endregion

        #region STAT VARIABLES
            STR = ttk.Frame()
            AGL = ttk.Frame()
            WIT = ttk.Frame()
            EMP = ttk.Frame()
            CC = ttk.Frame()
            HM = ttk.Frame()
            ST = ttk.Frame()
            RC = ttk.Frame()
            MB = ttk.Frame()
            PL = ttk.Frame()
            OB = ttk.Frame()
            SV = ttk.Frame()
            CT = ttk.Frame()
            CM = ttk.Frame()
            MN = ttk.Frame()
            MA = ttk.Frame()

            STR_l = ttk.Label()
            AGL_l = ttk.Label()
            WIT_l = ttk.Label()
            EMP_l = ttk.Label()
            CC_l = ttk.Label()
            HM_l = ttk.Label()
            ST_l = ttk.Label()
            RC_l = ttk.Label()
            MB_l = ttk.Label()
            PL_l = ttk.Label()
            OB_l = ttk.Label()
            SV_l = ttk.Label()
            CT_l = ttk.Label()
            CM_l = ttk.Label()
            MN_l = ttk.Label()
            MA_l = ttk.Label()

            Stats = {
                'Strength':[STR, STR_l, 370, 220],
                'Agility':[AGL, AGL_l, 370, 300],
                'Wits':[WIT, WIT_l, 500, 220],
                'Empathy':[EMP, EMP_l, 500, 300],
                'Close Combat':[CC, CC_l, 680, 220, 'Strength'],
                'Heavy Machinery':[HM, HM_l, 830, 220, 'Strength'],
                'Stamina':[ST, ST_l, 980, 220, 'Strength'],
                'Ranged Combat':[RC, RC_l, 680, 300, 'Agility'],
                'Mobility':[MB, MB_l, 830, 300, 'Agility'],
                'Piloting':[PL, PL_l, 980, 300, 'Agility'],
                'Observation':[OB, OB_l, 680, 380, 'Wits'],
                'Survival':[SV, SV_l, 830, 380, 'Wits'],
                'Comtech':[CT, CT_l, 980, 380, 'Wits'],
                'Command':[CM, CM_l, 680, 460, 'Empathy'],
                'Manipulation':[MN, MN_l, 830, 460, 'Empathy'],
                'Medical Aid':[MA, MA_l, 980, 460, 'Empathy']
            }        
#endregion

        #region GEAR VARIABLES
            self.cash = dict['Cash']
            self.gear = dict['Gear']
            self.notes = dict['Notes']
            gear0 = ttk.Entry()
            gear1 = ttk.Entry()
            gear2 = ttk.Entry()
            gear3 = ttk.Entry()
            gear4 = ttk.Entry()
            gear5 = ttk.Entry()
            gear6 = ttk.Entry()
            gear7 = ttk.Entry()
            gear8 = ttk.Entry()
            gear9 = ttk.Entry()
            gw0 = ttk.Spinbox()
            gw1 = ttk.Spinbox()
            gw2 = ttk.Spinbox()
            gw3 = ttk.Spinbox()
            gw4 = ttk.Spinbox()
            gw5 = ttk.Spinbox()
            gw6 = ttk.Spinbox()
            gw7 = ttk.Spinbox()
            gw8 = ttk.Spinbox()
            gw9 = ttk.Spinbox()
            GEAR = {
                0:[gear0, gw0],
                1:[gear1, gw1],
                2:[gear2, gw2],
                3:[gear3, gw3],
                4:[gear4, gw4],
                5:[gear5, gw5],
                6:[gear6, gw6],
                7:[gear7, gw7],
                8:[gear8, gw8],
                9:[gear9, gw9]
            }
#endregion

        #region STRSRAD VARIABLES
            self.stress = dict['Stress']
            self.rad = dict['Radiation']
            self.permrad = dict['Permanent Radiation']
            
            stress_frame = ttk.Frame()
            rad_frame = ttk.Frame()
            stress = ttk.Label()
            rad = ttk.Label()
 
            STRSRAD = {'Stress':[stress_frame, stress, self.stress],
                    'Radiation':[rad_frame, rad, self.rad]}
        #endregion

        #region COND VARIABLES

            self.suffocate = 0
            starv = ttk.Checkbutton()
            dehyd = ttk.Checkbutton()
            exhst = ttk.Checkbutton()
            freez = ttk.Checkbutton()
            drown = ttk.Checkbutton()
            sfct = ttk.Checkbutton()
            sick = ttk.Checkbutton()
            self.starv = BooleanVar(value = dict['Conditions']['Starving'])
            self.dehyd = BooleanVar(value = dict['Conditions']['Dehydrated'])
            self.exhst = BooleanVar(value = dict['Conditions']['Exhausted'])
            self.freez = BooleanVar(value = dict['Conditions']['Freezing'])
            self.drown = BooleanVar(value = dict['Conditions']['Drowning'])
            self.sfct = BooleanVar(value = dict['Conditions']['Suffocating'])
            self.sick = BooleanVar(value = dict['Conditions']['Sick'])
            starv_bt = ttk.Button()
            dehyd_bt = ttk.Button()
            exhst_bt = ttk.Button()
            freez_bt = ttk.Button()
            drown_bt = ttk.Button()
            sfct_bt = ttk.Button()
            sick_bt = ttk.Button()

            COND = {
                'Starving':[starv, self.starv, starv_bt],
                'Dehydrated':[dehyd, self.dehyd, dehyd_bt],
                'Exhausted':[exhst, self.exhst, exhst_bt],
                'Freezing':[freez, self.freez, freez_bt],
                'Drowning':[drown, self.drown, drown_bt],
                'Suffocating':[sfct, self.sfct, sfct_bt],
                'Sick':[sick, self.sick, sick_bt]
            }
        #endregion

        #region XP and WEIGHT VARIABLES
            self.xp = dict['Experience Points']
            self.add_skl = None
            self.add_tal = None

            self.weight = 0
        #endregion

        #region CONSUME VARIABLES
            air = ttk.Frame()
            food = ttk.Frame()
            water = ttk.Frame()
            power = ttk.Frame()
            arnum = ttk.Label()
            fdnum = ttk.Label()
            wtnum = ttk.Label()
            pwnum = ttk.Label()
            self.air = dict['Consumables']['Air']
            self.food = dict['Consumables']['Food']
            self.water = dict['Consumables']['Water']
            self.power = dict['Consumables']['Power']
            arbt = ttk.Button()
            fdbt = ttk.Button()
            wtbt = ttk.Button()
            pwbt = ttk.Button()  

            CONSUME = {
                'Air':[air, arnum, self.air, arbt],
                "Food":[food, fdnum, self.food, fdbt],
                "Water":[water, wtnum,  self.water, wtbt],
                "Power":[power, pwnum, self.power, pwbt]
            }
        #endregion

        #region EQUIP VARIABLES
        
            #Variables located with Widgets because of Master/Slave requirements

        #endregion

        #region TALENT VARIABLES

            self.tal = dict['Talents']

        #endregion

        #region PANIC AND DEATH VARIABLES
            self.death = False
            self.panic = dict['Panic']
            self.push_ct = 0

        #endregion 
               
        #region CRITICAL INJURIES VARIABLES
            self.crit = False

            self.injs = dict['Critical Injuries']

            injnum0 = StringVar()
            injnum1 = StringVar()
            injnum2 = StringVar()
            injnum3 = StringVar()
            injnum4 = StringVar()
            injnum5 = StringVar()
            injnum6 = StringVar()
            injnum7 = StringVar()
            injnum8 = StringVar()
            injnum9 = StringVar()
            inj0 = ttk.Entry()
            inj1 = ttk.Entry()
            inj2 = ttk.Entry()
            inj3 = ttk.Entry()
            inj4 = ttk.Entry()
            inj5 = ttk.Entry()
            inj6 = ttk.Entry()
            inj7 = ttk.Entry()
            inj8 = ttk.Entry()
            inj9 = ttk.Entry()
            ib0 = ttk.Button()
            ib1 = ttk.Button()
            ib2 = ttk.Button()
            ib3 = ttk.Button()
            ib4 = ttk.Button()
            ib5 = ttk.Button()
            ib6 = ttk.Button()
            ib7 = ttk.Button()
            ib8 = ttk.Button()
            ib9 = ttk.Button()
            recov_ct0 = []
            recov_ct1 = []
            recov_ct2 = []
            recov_ct3 = []
            recov_ct4 = []
            recov_ct5 = []
            recov_ct6 = []
            recov_ct7 = []
            recov_ct8 = []
            recov_ct9 = []

            INJS = {0:[injnum0, inj0, ib0, recov_ct0],
                    1:[injnum1, inj1, ib1, recov_ct1],
                    2:[injnum2, inj2, ib2, recov_ct2],
                    3:[injnum3, inj3, ib3, recov_ct3],
                    4:[injnum4, inj4, ib4, recov_ct4],
                    5:[injnum5, inj5, ib5, recov_ct5],
                    6:[injnum6, inj6, ib6, recov_ct6],
                    7:[injnum7, inj7, ib7, recov_ct7],
                    8:[injnum8, inj8, ib8, recov_ct8],
                    9:[injnum9, inj9, ib9, recov_ct9]
                    }

        #endregion
        
        
    #Widgets
        #region SHEET FRAMES
            self.roll_frame = ttk.Frame(sheet, style = 'Dice.TFrame')
            self.roll_frame.place(x = 305, y = 545, width = 740, height = 150, anchor = 'nw')

            self.dice_frame = ttk.Frame(self.roll_frame, style = 'Dice.TFrame')
            self.dice_label = ttk.Label(self.dice_frame, style = 'Dice.TFrame')
            self.roll_info = ttk.Frame(self.roll_frame, style = 'Dice.TFrame')

        #endregion

        #region NAME, CAREER, RACE AND HEALTH
            namelabel = ttk.Label(sheet, text = dict['Name'].upper(), style = 'Header.Alien.TLabel', font = ('Courier New', 24))
            namelabel.place(relx = 0.5, y = 32, anchor='center')

            job = ttk.Label(sheet, text = f'{dict['Race']} {dict['Job']}', style = 'SmHeader.Alien.TLabel')
            job.place(relx = 0.5, y = 70, anchor = 'n')

            status = ttk.Label(sheet, text = 'Status: AFFLICTED', style = 'NewChar.Alien.TLabel')
            status.place(x = 510, y = 100, anchor = 'nw')

            hp_ct = ttk.Label(sheet, text = f'Health {self.hp}/{dict['Max Health']}', style = 'NewChar.Alien.TLabel')
            hp_ct.place(x = 840, y = 110, anchor = 'ne')


        #Health Bar
            hp_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            hp_frame.place(relx = 0.5, y = 151, anchor = 'center')

            hp_lose = ttk.Button(hp_frame, text = '-', width = 2, command = lambda: edit_hp('-'), style = 'Small.TButton')
            hp_lose.grid(row = 1, column = 0)
            hp_bar = ttk.Progressbar(hp_frame, maximum= dict['Max Health'], value = self.hp, length = 400)
            hp_bar.grid(row = 1, column = 1)
            hp_gain = ttk.Button(hp_frame, text = '+', width = 2, command = lambda: edit_hp('+'), style = 'Small.TButton')
            hp_gain.grid(row = 1, column = 2)

            if self.starv.get() == True or self.dehyd.get() == True or self.exhst.get() == True or self.freez.get() == True or self.drown.get() == True or self.sfct.get() == True or self.sick.get() == True:                
                status.config(text = 'Status: AFFLICTED')
                sheet_bg.config(image = self.sheet_bg_afflicted)
            else:
                status.config(text = 'Status: STABLE')
                sheet_bg.config(image = self.sheet_bg_normal)



        #endregion

        #region STAT BOXES
            for key in Stats:
                stat_box(key, 'Skill')
        #endregion

        #region CASH and SIGNATURE ITEM
        #Cash
            cash_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            cash_frame.place(x = 1200, y = 10, anchor = 'n')

            math_frame = ttk.Frame(cash_frame, style = 'Alien.TFrame')
            math_frame.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

            ttk.Label(cash_frame, text = 'Cash:', style = 'Inv.Alien.TLabel').grid(row = 0, column = 0)
            cash = ttk.Label(cash_frame, text = f'${self.cash}', style = 'Inv.Alien.TLabel')
            cash.grid(row = 0, column = 1)

            add = ttk.Button(math_frame, text = "+", width = 2, command = lambda: edit_cash(math.get()), style = 'Small.TButton')
            add.pack(side = RIGHT)
            math = ttk.Entry(math_frame, width = 21, justify = RIGHT, style = 'Alien.TEntry', font = ('Courier New', 12))
            math.pack(side = RIGHT)
            minus = ttk.Button(math_frame, text = '-', width = 2, command = lambda: edit_cash(-int(math.get())), style = 'Small.TButton')
            minus.pack(side = RIGHT)

        #Signature Item
            sigsheet = ttk.Frame(sheet, style = 'Alien.TFrame')
            sigsheet.place(x = 1200, y = 95, anchor = 'center')

            ttk.Label(sigsheet, text = 'Signature Item', style = 'Inv.Alien.TLabel').pack()
            self.sigitem = ttk.Entry(sigsheet, width = 26, style = 'Alien.TEntry', font = ('Courier New', 12))
            self.sigitem.insert(0, dict['Signature Item'])
            self.sigitem.config(state = DISABLED)
            self.sigitem.pack(padx = 5, pady = 5)
#endregion

        #region GEAR INFO
            gear_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            gear_frame.place(x = 1200, y = 125, anchor = 'n')

            ttk.Label(gear_frame, text = 'Gear', style = 'Inv.Alien.TLabel').grid(row = 0, sticky = 'w')
            ttk.Label(gear_frame, text = 'Weight', style = 'Inv.Alien.TLabel').grid(row = 0, column = 1)
            for g in GEAR:
                GEAR[g][0] = ttk.Entry(gear_frame, foreground = 'Black', style = 'Alien.TEntry', font = ('Courier New', 11))
                GEAR[g][0].grid(row = g+1, column = 0, padx = 2, pady = 2)
                GEAR[g][0].insert(0,dict['Gear'][g][0])
                GEAR[g][0].config(state = DISABLED)

                GEAR[g][1] = ttk.Spinbox(gear_frame, width = 3, foreground = 'Black', increment = 0.5, from_ = 0, to = 9.5, state = DISABLED, style = 'Alien.TSpinbox', font = ('Courier New', 12))
                GEAR[g][1].grid(row = g+1, column = 1)
                if dict['Gear'][g][0] == '':
                    GEAR[g][1].set(0)
                else: 
                    if GEAR[g][1].get() != 'Set':
                        GEAR[g][1].set(dict['Gear'][g][1])
                    else:
                        GEAR[g][1].set('Set')
            gear_edit = ttk.Button(gear_frame, text = 'Edit Inventory', command = lambda: edit_gear('Edit'), style = 'Small.TButton')
            gear_edit.grid(row = 13, column = 0, columnspan= 2, pady = 5)
        #endregion

        #region ENCUMBRANCE
            ttk.Label(gear_frame, text = 'ENCUMBRANCE', style = 'Inv.Alien.TLabel').grid(row = 11, column = 0, sticky = 'w', padx = 5)
            ncom = ttk.Label(gear_frame, text = f'{self.weight}/{dict['Encumbrance']}', style = 'Inv.Alien.TLabel')
            ncom.grid(row = 11, column = 1, sticky = 'w', padx = 5)
            overncom = ttk.Label(gear_frame, text = '', style = 'Inv.Alien.TLabel', font = ('Courier New', 12, 'bold'))
            overncom.grid(row = 12, column = 0, columnspan = 2)
            add_weight()
        #endregion

        #region NOTES
            notes_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            # notes_frame.place(x = 1200, y = 510, anchor = 'n')

            ttk.Label(notes_frame, text = 'Notes', style = 'Inv.Alien.TLabel').grid(row = 14, column = 0, sticky = 'w')
            self.notes = Text(notes_frame, width = 34, height = 11, wrap='word')
            self.notes.grid(row = 15, column = 0, columnspan= 2)
            self.notes.insert("1.0", dict['Notes'])
            self.notes.config(state = 'disabled')

            notes_edit = ttk.Button(notes_frame, text = 'Unlock Notes', command = lambda: edit_notes(), style = 'Small.TButton')
            notes_edit.grid(row = 16, column = 0, columnspan = 2, pady = 5)




        #endregion

        #region PERSONAL AGENDA, BUDDY, RIVAL
            pers_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            pers_frame.place(x = 150, y = 10, anchor = 'n')

            #Personal Agenda
            ttk.Label(pers_frame, text = 'Personal Agenda', style = 'Inv.Alien.TLabel').grid(row = 0, column = 0 , columnspan= 2)
            self.agenda = Text(pers_frame, width = 34, height = 3, wrap = 'word')
            self.agenda.insert("1.0", dict['Personal Agenda'])
            self.agenda.config(state = 'disabled')
            self.agenda.grid(row = 1, column = 0 , columnspan= 2)

            #Buddy
            ttk.Label(pers_frame, text = 'Buddy', style = 'Inv.Alien.TLabel').grid(row = 2, column = 0)
            self.buddy = ttk.Entry(pers_frame, width = 20)
            self.buddy.insert(0, dict['Buddy'])
            self.buddy.config(state = DISABLED)
            self.buddy.grid(row = 3, column = 0)

            #Rival
            ttk.Label(pers_frame, text = 'Rival', style = 'Inv.Alien.TLabel').grid(row = 2, column = 1)
            self.rival = ttk.Entry(pers_frame, width = 20)
            self.rival.insert(0, dict['Rival'])
            self.rival.config(state = DISABLED)
            self.rival.grid(row = 3, column = 1)
            
            #Button
            pers_bt = ttk.Button(pers_frame, text = 'Edit Personal Info', command = edit_persinfo, style = 'Small.TButton')
            pers_bt.grid(row = 4, column = 0, columnspan = 2, pady = 5)

        #endregion

        #region EXPERIENCE POINTS
            xp_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            xp_frame.place(x = 300, y = 10, anchor = 'nw')

            ttk.Label(xp_frame, text = 'Experience', style = 'Inv.Alien.TLabel').grid(row = 0, column = 0, columnspan = 3, padx = 5)

            self.xp_l = ttk.Label(xp_frame, width = 16, text = f'{'■'*self.xp}', style = 'Levels.TLabel', font = ('Calibri', 15))
            self.xp_l.grid(row = 1, column = 0, columnspan = 3, padx = 5)

            self.spend = ttk.Button(xp_frame, text = 'Spend XP', width = 8, command = lambda: edit_xp(-5), style = 'Small.TButton')
            self.spend.grid(row = 2, column = 0, pady = 5)
            ttk.Button(xp_frame, text = '-', width = 2, command = lambda: edit_xp(-1), style = 'Small.TButton').grid(row = 2, column = 1, pady = 5)
            ttk.Button(xp_frame, text = '+', width = 2, command = lambda: edit_xp(1)).grid(row = 2, column = 2, pady = 5)

            if self.xp >= 5:
                self.spend.config(state = ACTIVE)
            else:
                self.spend.config(state = DISABLED)
        #endregion

        #region STRESS AND RADIATION AND PANIC
            strsrad_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            strsrad_frame.place(x = 150, y = 250, anchor = 'center')

            for c in STRSRAD:
                if c == 'Stress' and dict['Race'] == 'Synth':
                    pass
                else:
                    STRSRAD[c][0] = ttk.Frame(strsrad_frame, style = 'Alien.TFrame')
                    STRSRAD[c][0].pack(pady = 6)
                    ttk.Label(STRSRAD[c][0], text = c, style = 'Inv.Alien.TLabel').grid(row = 0, columnspan = 2, sticky = 'w')
                    ttk.Button(STRSRAD[c][0], text = '-', width = 2, command = lambda type = c: edit_strsrad(-1,type), style = 'Small.TButton').grid(row = 1, column = 0)
                    STRSRAD[c][1] = ttk.Label(STRSRAD[c][0], text = f'{'■'*STRSRAD[c][2]}', width = 15, justify = LEFT, style = 'Levels.TLabel')
                    STRSRAD[c][1].grid(row = 1, column = 1, sticky = 'n')
                    ttk.Button(STRSRAD[c][0], text = '+', width = 2, command = lambda type = c: edit_strsrad(1,type), style = 'Small.TButton').grid(row = 1, column = 2)

            permrad_l = ttk.Label(strsrad_frame, text = f"Permanent Radiation: {self.permrad}", style = 'Small.Alien.TLabel')
            permrad_l.pack()

        #endregion

        #region CONDITIONS
            stseff_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            stseff_frame.place(x = 10, y = 340)


            for i, c in enumerate(COND):
                
                COND[c][1].set(dict['Conditions'][c])
                ttk.Label(stseff_frame, text = c, style = 'Inv.Alien.TLabel').grid(row = i, column = 0)
                COND[c][0] = ttk.Checkbutton(stseff_frame, onvalue= True, offvalue = False, variable= COND[c][1], command = lambda cond = c: edit_cond(cond), style = 'Alien.TCheckbutton')
                COND[c][0].grid(row = i, column = 1)
                COND[c][2] = ttk.Button(stseff_frame, text = 'Roll', width = 6, command = lambda x = c: rollqueue('Condition', x), state = DISABLED, style = 'Small.TButton')
                COND[c][2].grid(row = i, column = 2)
                if COND[c][1].get() == True:
                    COND[c][2].config(state = ACTIVE)

                if c == 'Dehydrated':
                    COND[c][2].config(text = 'Apply', width = 6, command = apply_dehyd)
                    
                
                def apply_dehyd():
                    affect_hp_strs()
                    if self.hp == 0:
                        death_on(True,'One Shift')


        #endregion

        #region CRITICAL INJURIES

            crit_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            crit_frame.place(x = 1200, y = 510, anchor = 'n')
            
            # notes_frame.place(x = 5, y = 720)

            ttk.Label(crit_frame, text = 'Critical Injuries', style = 'Inv.Alien.TLabel').grid(row = 0, column = 0)

        #endregion

        #region ARMOR AND WEAPONS
            equip_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            equip_frame.place(x = 210, y = 340, anchor = 'nw')

        #Variables ---Have to be here due to master and slave variables---
            wnam0,wnam1,wnam2,wnam3 = [ttk.Entry(equip_frame, width = 15, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 15, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 15, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 15, style = 'Alien.TEntry', font = ('Courier New', 12))]
            wbns0,wbns1,wbns2,wbns3 = [ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12))]
            wdmg0,wdmg1,wdmg2,wdmg3 = [ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 3, style = 'Alien.TEntry', font = ('Courier New', 12))]
            wrng0,wrng1,wrng2,wrng3 = [ttk.Entry(equip_frame, width = 8, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 8, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 8, style = 'Alien.TEntry', font = ('Courier New', 12)),
                                       ttk.Entry(equip_frame, width = 8, style = 'Alien.TEntry', font = ('Courier New', 12))]

            WEAPONS = {
                0:[wnam0, wbns0, wdmg0, wrng0],
                1:[wnam1, wbns1, wdmg1, wrng1],
                2:[wnam2, wbns2, wdmg2, wrng2],
                3:[wnam3, wbns3, wdmg3, wrng3]
            }

        #Armor
            ttk.Label(equip_frame, text = 'Armor', style = 'Inv.Alien.TLabel').grid(row = 0, column = 0)
            armor = ttk.Entry(equip_frame, width = 15, style = 'Alien.TEntry', font = ('Courier New', 12))
            armor.insert(0, dict['Armor'][0])
            armor.config(state = DISABLED)
            armor.grid(row = 1, column = 0)

            ar_val = ttk.Spinbox(equip_frame, from_= 1, to = 10, width = 2, style = 'Alien.TSpinbox', font = ('Courier New', 12))
            ar_val.set(dict['Armor'][1])
            ar_val.config( state = DISABLED)
            ar_val.grid(row = 1, column = 1)

            ttk.Button(equip_frame, text = 'Roll', width = 4, command = lambda: rollqueue('Armor', ar_val.get()), style = 'Small.TButton').grid(row = 1, column = 2)

        #Weapons
            ttk.Label(equip_frame, text = 'Weapons', style = 'Inv.Alien.TLabel').grid(row = 2, column = 0)
            ttk.Label(equip_frame, text = 'Bonus', style = 'Small.Alien.TLabel').grid(row = 2, column = 1, sticky = 'w')
            ttk.Label(equip_frame, text = 'Damage', style = 'Small.Alien.TLabel').grid(row = 2, column = 2, sticky = 'w')
            ttk.Label(equip_frame, text = 'Range', style = 'Small.Alien.TLabel').grid(row = 2, column = 3, sticky = 'w')

            for w in dict['Weapons']:
                for n in WEAPONS:
                    WEAPONS[int(w)][n].insert(0, dict['Weapons'][w][n])
                    WEAPONS[int(w)][n].config(state = DISABLED)
                    WEAPONS[int(w)][n].grid(row = int(w)+3, column = n, padx = 5, pady = 2)
                ttk.Button(equip_frame, text = 'Roll', width = 4, command = lambda name = WEAPONS[int(w)][0], bonus = WEAPONS[int(w)][1], damage = WEAPONS[int(w)][2], range = WEAPONS[int(w)][3]: rollqueue('Weapon', name.get(), [name.get(), bonus.get(), damage.get(), range.get()]), style = 'Small.TButton').grid(row = int(w)+3, column = 4)
           
            equip_bt = ttk.Button(equip_frame, text = 'EDIT EQUIPMENT', command = lambda: edit_equip('Edit'), style = 'Small.TButton')
            equip_bt.grid(row = 1, column = 3, columnspan = 5, pady = 5)
        #endregion
      
        #region CONSUMABLES

            cnsm_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            cnsm_frame.place(x = 10, y = 535)

            for i, c in enumerate(CONSUME):
                ttk.Label(cnsm_frame, text = f'{c}:', style = 'Inv.Alien.TLabel', justify = LEFT).grid(row = i, column = 0)

                ttk.Button(cnsm_frame, text = '-', width = 1, command= lambda x = c: edit_consume(-1, x), style = 'Small.TButton').grid(row = i, column = 1, pady = 5)

                CONSUME[c][1] = ttk.Label(cnsm_frame, text = CONSUME[c][2], image = ch_skill_img, compound = 'center', style = 'Inv.Alien.TLabel', font = ('Courier New', 24, 'bold'))
                CONSUME[c][1].grid(row = i, column = 2)

                ttk.Button(cnsm_frame, text = '+', width = 1, command= lambda x = c: edit_consume(1, x), style = 'Small.TButton').grid(row = i, column = 3)

                CONSUME[c][3] = ttk.Button(cnsm_frame, width = 6, text = 'Roll', command = lambda x = c: rollqueue('Consumable', x), style = 'Small.TButton')
                CONSUME[c][3].grid(row = i, column = 4, padx = 14)

                if CONSUME[c][2] == 0:
                    CONSUME[c][3].config(state = DISABLED)

        #endregion

        #region TALENTS
            tal_frame = ttk.Frame(sheet, style = 'Alien.TFrame')
            tal_frame.place(x = 910, y = 10)

            ttk.Label(tal_frame, text = 'Talents', style = 'Inv.Alien.TLabel').pack(padx = 5, anchor = 'w')
            tal = Text(tal_frame, width = 16, height = 7)
            tal.pack(padx = 5, pady = 5)
            for t in dict['Talents']:
                i = dict['Talents'].index(t)
                tal.insert(f'{i+1}.0', f'{t}\n')
            tal.config(state = 'disabled')

        #endregion

        #region DICE BUTTONS
            panic_bt = ttk.Label(sheet, image = panic_bt_inactive, background = aBlack)
            panic_bt.place(x = 303, y = 679)

            push_bt = ttk.Label(sheet, image = push_bt_inactive, background = aBlack)
            push_bt.place(relx = 0.5,y = 679, anchor = 'n')

            crit_bt = ttk.Label(sheet, image = inj_bt_inactive, background = aBlack)
            crit_bt.place(x = 1048, y = 679, anchor = 'ne')

            end_panic_bt = ttk.Label(sheet, image = end_panic_bt_inactive, background = aBlack)
            end_panic_bt.place(x = 303, y = 715)
            if self.panic > 0:
                end_panic_bt.config(image = end_panic_bt_active)
                end_panic_bt.bind('<ButtonPress>', lambda event: panic_end())

            death_bt = ttk.Label(sheet, image = death_bt_inactive, background= aBlack)
            death_bt.place(x = 430, y = 715)

            death_freq = ttk.Label(sheet, text = 'Frequency', foreground = '#555555', style = 'Inv.Alien.TLabel', font = ('Courier New', 10))
            death_freq.place(x = 685, y = 715)
            death_time = ttk.Label(sheet, style = 'Inv.Alien.TLabel', font = ('Courier New', 10))
            death_time.place(x = 685, y = 732)

            resus_bt = ttk.Label(sheet, image = resus_bt_inactive, background = aBlack)
            resus_bt.place(x = 923, y = 715, anchor = 'ne')

            trauma_bt = ttk.Label(sheet, image = trauma_bt_inactive, background = aBlack)
            trauma_bt.place(x = 1050, y = 715, anchor = 'ne')

    #Called Functions
            pack_injuries()
        #endregion
#endregion



###---PARTY MANAGER---###

    #Initialize Party Manager
        def pm_start():

    #Party Top Menu Frames
            self.pm_main = ttk.Frame(master, width = 640, height = 480)
            self.pm_main.pack_propagate(False)
            self.pm_main.grid_propagate(False)
            self.pm_main.place(relx = 0.5, rely = 0.5, anchor = 'center')

            self.pm_bg = ttk.Label(self.pm_main, image = self.pm_bg_init, background = aBlack)
            self.pm_bg.place(x=0,y=0)

            self.pm_select = ttk.Frame(self.pm_main, style= 'Green.Alien.TFrame')
            self.pm_select.place(relx = 0.5, rely = 0.5, anchor = 'center')

    #Party Menu Buttons

            self.pm_title = ttk.Label(self.pm_main, text = 'Party Manager', style = 'Inv.Alien.TLabel', padding = 5)
            self.pm_title.place(relx = 0.5, y = 40, anchor = 'center')

            self.pm_new = ttk.Button(self.pm_main, style = 'Alien.TButton', text = 'New Party', command = lambda: new_party())
            self.pm_new.place(relx = 0.5, y = 204, anchor = 'center')

            self.pm_load = ttk.Button(self.pm_main, style = 'Alien.TButton', text = 'Load Party', command = lambda: load_party('save_data.json',load_data))
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
                self.new_savedata = json.dumps(self.party_list, indent=4)

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
        def load_party(link, func):
            self.pm_new.destroy()
            self.pm_load.destroy()
            self.pm_bg.config(image = self.pm_bg_load)

        #Variables
            self.load_name = 'null'
            self.names_list = []

                #Read Saved Data from JSON
            with open(f'json\\{link}', 'r') as load_data:
                self.load_dict = json.load(load_data) 

                #Update self.load_dict With Saved Names
            for name in self.load_dict:
                self.names_list.append(name)   
            self.length = len(self.names_list)
            if len(self.names_list) == 1:
                messagebox.showerror(title='No Character Sheets Available', message='Please create a character')
                ch_start()
                self.pm_back.config(text = 'Back', command = lambda: top_menu.lift())
            else:            

        #Frames
                load_canvas = Canvas(self.pm_main, height = 330, width = 205, scrollregion=(0,0,300,self.length*63), highlightthickness= 0, background = aBlack)
                load_canvas.place(x = 55, y = 75)

                scroll_frame = ttk.Frame(self.pm_main, height = 330, width = 15, style = 'Alien.TFrame')
                scroll_frame.pack_propagate(False)
                scroll_frame.place(x = 265, y = 75)
                
                self.pm_info = ttk.Frame(self.pm_main, height = 330, width = 230, style = 'Alien.TFrame')
                self.pm_info.pack_propagate(False)
                self.pm_info.place(x = 355, y = 75)

            #Widgets          
                name_scroll = ttk.Scrollbar(scroll_frame, orient= VERTICAL, command = load_canvas.yview, style = 'Alien.Vertical.TScrollbar')
                name_scroll.pack(side = LEFT, fill = Y)
                
                self.load_buttons = ttk.Frame(load_canvas, height = self.length*63, width = 205, borderwidth = 0, style = 'Alien.TFrame')
                self.load_buttons.pack_propagate(False)
                self.load_buttons.pack(anchor = 'nw', side = LEFT)

                    #Load Party Configs
                load_canvas.config(yscrollcommand=name_scroll.set)
                load_canvas.create_window(0, 0, anchor = 'nw', window = self.load_buttons)
                
                if link == 'save_data.json':
                    self.pm_back.config(text = 'Cancel', command = lambda: pm_reset())
                
                elif link == 'character_sheets.json':
                    self.pm_back.config(text = 'Cancel', command = lambda: ch_reset())
                

                if self.length <= 6:
                    name_scroll.forget()
                    load_canvas.place(x = 70, y = 75)
                    scroll_frame.place(x= 280, y = 75)

                button_pack(func, 1)

    #Pack Buttons
        def button_pack(func, num):
            ttk.Button(self.load_buttons, text = self.names_list[num], command = lambda: func(num), style = 'Small.TButton').pack(ipady = 20, fill = X)
            if num < (self.length-1):
                button_pack(func, num+1)
            else:
                pass   

    #Load Button Data
        def load_data(num):
            if self.load_name == 'null':
                self.load_name = ttk.Label(self.pm_info, text = f'{self.names_list[num]}\n'.upper(), background = aBlack, font = ('Courier New', 16, 'bold'), foreground = 'white')
                self.load_name.pack(anchor = 'w')
                n = 1
                for mem in (self.load_dict[self.names_list[num]]):
                    self.load_partymember = ttk.Label(self.pm_info, text = f'Player {n}: {mem[0]}', background = aBlack, font = ('Courier New', 10), foreground = 'white')
                    self.load_partymember.pack(anchor = 'w')
                    n += 1
                self.selected_party = self.names_list[num]
                select_party(num)
            else:
                self.load_name = 'null'
                self.pm_info.destroy()
                self.pm_info = ttk.Frame(self.pm_main, height = 330, width = 230, style = 'Alien.TFrame')
                self.pm_info.pack_propagate(False)
                self.pm_info.place(x = 355, y = 75)
                load_data(num)

    #Select Party Buttons Appear
        def select_party(num):
            self.del_bt = ttk.Button(self.pm_info, text = 'Delete', command = lambda: delete_party(), style = 'Small.TButton')
            self.del_bt.pack(anchor='s', side = BOTTOM, pady = 10)

            self.sel_bt = ttk.Button(self.pm_info, text = 'Select', command = lambda: set_activeparty(), style = 'Small.TButton')
            self.sel_bt.pack(anchor='s', side = BOTTOM)

    #Delete Selected Party
        def delete_party():

            def delete_data():
                with open('json\\save_data.json', 'r') as self.global_party:
                    self.deleting_dict = json.load(self.global_party)
                    self.deleting_dict.pop(self.selected_party)
                with open('json\\save_data.json', 'w') as self.global_party:
                    overwrite_dict = json.dumps(self.deleting_dict, indent = 4)
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
                active_json = json.dumps(active_dict, indent = 4)
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
                self.cs_main.place(relx = 0.5, rely = 0.5, anchor = 'center')

                self.cs_bg = ttk.Label(self.cs_main, image = self.cs_bg_init, background = aBlack)
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
                ttk.Label(self.cs_intro, text = 'No active party selected,\nPlease select a party.',font = ('Courier New', 16, 'bold'), style = 'Header.Alien.TLabel', justify = 'center').grid(row=0, column = 0, pady = 20)
                ttk.Button(self.cs_intro, text = 'Choose Party', command = lambda: (pm_start(), cs_restart()), style = 'Small.TButton').grid(row = 1, column = 0)
            else:

                ttk.Label(self.cs_intro, text = f'Start a new Combat with\n\n{self.active_name}?',font = ('Courier New', 16, 'bold'), style = 'Header.Alien.TLabel', justify = 'center').grid(row = 0, column=0, columnspan=2, pady = 20)
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

            npc_name = Entry(cs_frame, width = 12, background = aBlack, foreground = aGreen, font = ('Courier New', 10), insertbackground= aGreen)
            npc_checkbox = Checkbutton(cs_frame, variable = npc_checkbox_value, onvalue = 'Friendly', offvalue = 'Enemy', background = aGreen, relief= 'flat')
            npc_name.grid(row = 0, column = 1, sticky = 'w', padx = 5, pady = 3)
            npc_checkbox.grid(row = 1, column = 1, sticky = 'w', padx = 5)

            npc_addbutton = Button(cs_frame, text = 'Add to Party', background = aDGreen, foreground = aBlack, font = ('Courier New', 8), width = 12, command = lambda: cs_updateparty(npc_name.get(), npc_checkbox_value.get()))
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
            cs_player_tracker = ttk.Label(self.cs_intro, text = f'Draw for Initiative!\n{self.active_party[0][0]}, pick a card! (1/{len(self.active_party)})', justify= CENTER, style = 'Inv.Alien.TLabel', font = ('Courier New', 10))
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
                        ttk.Label(self.cs_intro, text = f'{self.active_party[self.pnum-1][0]} chose {var}!  Shall we begin?', background = aBlack, font = ('Courier New', 12, 'bold'), foreground = 'white').grid(row = 0)
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
            self.cs_gamemother = ttk.Label(self.cs_readoutframe, text = f"It's your turn, {self.sorted_party[0][0]}!", font = ('Courier New', 18), background = aBlack, foreground = 'white')
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

            char_label = ttk.Label(char_frame, text = f'{self.active_party[num][0]}', compound = 'center', image = icon_p, font = ('Courier New', 10, 'bold'), foreground = aBlack, background = aBlack)
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
                self.dr_main.place(relx = 0.5, rely = 0.5, anchor = 'center')

                ttk.Label(self.dr_main, image = self.dr_bg_init, background = aBlack).place(x = 0, y = 0)
                    
                #Options
                self.dr_options = ttk.Frame(self.dr_main, width = 550, height = 200, style = 'Alien.TFrame')
                self.dr_options.pack_propagate(False)
                self.dr_options.pack(side = TOP, padx = 45, pady = 35)
                    #Options Menu
                self.dr_opt_menu = ttk.Frame(self.dr_options, style = 'Alien.TFrame')
                self.dr_opt_menu.pack()

                #Readout Frame
                self.dr_readout = ttk.Frame(self.dr_main, width = 606, height = 180, style = 'Dice.TFrame')
                self.dr_readout.grid_propagate(False)
                self.dr_readout.pack_propagate(False)
                self.dr_readout.pack(side = BOTTOM, padx = 18, pady = 18)

                self.dr_results = ttk.Frame(self.dr_readout, style = 'Dice.TFrame')
                self.dr_results.pack(padx = 5, pady = 0)

            #DR Options Widgets
                ttk.Label(self.dr_opt_menu, text = "Options Menu", style="Inv.Alien.TLabel").pack()

                gen_btn = ttk.Button(self.dr_opt_menu, text = 'General Roll', style = "Alien.TButton", command = lambda: gen_opts())
                gen_btn.pack()

                inj_btn = ttk.Button(self.dr_opt_menu, text = 'D66 Rolls', style = 'Alien.TButton', command = lambda: inj_opts())
                inj_btn.pack(pady = 30)


                self.dr_main.lift()
    
    #MENU OPTIONS
        #General Roll
        def gen_opts():
            def back():
                self.dr_opt_gen.destroy()
                self.dr_opt_menu.pack()

            self.dr_opt_menu.forget()

            #Frames
            self.dr_opt_gen = ttk.Frame(self.dr_options, width = 550, height = 200, style = 'Alien.TFrame')
            self.dr_opt_gen.pack_propagate(False)
            self.dr_opt_gen.pack(side = TOP)

            #Widgets
            ttk.Label(self.dr_opt_gen, text = "General Rolls", style="Inv.Alien.TLabel").pack()

                #Base Dice
            ttk.Label(self.dr_opt_gen, text = 'Base Dice', font = ('Courier New', 18), image = dice_base, compound= 'bottom', background = aBlack, foreground = 'white').place(relx = 0.2, y = 80, anchor = 'center')
            self.dr_bdice_amt = Spinbox(self.dr_opt_gen, from_ = 1, to = 20, font = ('Courier New', 24), width = 2, state = 'readonly')
            self.dr_bdice_amt.place(relx = 0.4, y = 100, anchor = 'center')

                #Stress Dice
            ttk.Label(self.dr_opt_gen, text = 'Stress Dice', font = ('Courier New', 18), image = dice_stress, compound = 'bottom', background = aBlack, foreground = 'white').place(relx = 0.8, y=80, anchor = 'center')
            self.dr_sdice_amt = Spinbox(self.dr_opt_gen, from_ = 0, to = 10, font = ('Courier New', 24), width = 2, state = 'readonly')
            self.dr_sdice_amt.place(relx = 0.6, y = 100, anchor = 'center')

                #Buttons
            ttk.Button(self.dr_opt_gen, text = 'Roll', command = lambda: gen_roll(), style = 'Small.TButton').place(relx = 0.5, rely = 0.75, anchor = 'center')
            ttk.Button(self.dr_opt_gen, text = 'Options Menu', command = lambda: (back()), style = 'Small.TButton').place(relx = 0.1, rely = 0.95, anchor = 'center')
            ttk.Button(self.dr_opt_gen, text = 'Top Menu', command = lambda: (top_menu.lift()), style = 'Small.TButton').place(relx = 0.9, rely = 0.95, anchor = 'center')
            self.dr_clear = ttk.Button(self.dr_opt_gen, text = 'Clear', command = lambda: dice_clear(), state = 'disabled', style = 'Small.TButton')
            self.dr_clear.place(relx = 0.5, rely = 0.95, anchor = 'center')

        #Injury Roll
        def inj_opts():

            def back():
                self.dr_opt_inj.destroy()
                self.dr_opt_menu.pack()
            
            self.dr_opt_menu.forget()

            #Frames
            self.dr_opt_inj = ttk.Frame(self.dr_options, width = 550, height = 200, style = 'Alien.TFrame')
            self.dr_opt_inj.pack_propagate(False)
            self.dr_opt_inj.pack(side = TOP)

            #Widgets
            ttk.Label(self.dr_opt_inj, text = 'Injury Table', style = 'Inv.Alien.TLabel').pack(side = TOP)

                #Injury Dice
            roll = ttk.Button(self.dr_opt_inj, text = 'Roll A D66', style = 'Alien.TButton', command = lambda: inj_roll())
            roll.place(relx = 0.5, rely = 0.5, anchor = 'center')

            ttk.Button(self.dr_opt_inj, text = 'Options Menu', command = lambda: (back()), style = 'Small.TButton').place(relx = 0.1, rely = 0.95, anchor = 'center')
            ttk.Button(self.dr_opt_inj, text = 'Top Menu', command = lambda: (top_menu.lift()), style = 'Small.TButton').place(relx = 0.9, rely = 0.95, anchor = 'center')
            self.dr_clear = ttk.Button(self.dr_opt_inj, text = 'Clear', command = lambda: dice_clear(), state = 'disabled', style = 'Small.TButton')
            self.dr_clear.place(relx = 0.5, rely = 0.95, anchor = 'center')

    #Roll for Injury!
        def inj_roll():
            results_reset()
            self.dr_clear.config(state = ACTIVE)
            tens = random.randint(1,6)
            ones = random.randint(1,6)

            ttk.Label(self.dr_results, image = dicedict[f'{tens}b'], style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 0, column = 0)
            ttk.Label(self.dr_results, image = dicedict[f'{ones}b'], style = 'Inv.Alien.TLabel', background = '#182318').grid(row = 0, column = 1)

            inj_num = (tens*10 + ones)
            ttk.Label(self.dr_results, text = inj_num, style = 'Header.Alien.TLabel', background = '#182318').grid(row = 1, column = 0, columnspan = 2, pady = 20)


    #Roll the Dice!        
        def gen_roll():
            results_reset()

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
                        self.dice_img = dicedict[sorted_rolls.pop(0)]
                    ttk.Label(self.dr_results, image = self.dice_img, background = '#182318').grid(row = i // 10, column = i % 10, padx = 3, pady = 2)
                    i += 1
                    h += 1

            #Display Base Dice
                j = 0
                limit = len(base_results)
                while j < limit:
                    if base_results != []:
                        self.dice_img = dicedict[base_results.pop(0)]
                    ttk.Label(self.dr_results, image = self.dice_img, background = '#182318').grid(row = i // 10, column = i % 10, padx = 3, pady = 2)
                    i += 1
                    j += 1

            #Display Stress Dice
                k = 0
                limit = len(stress_results)
                while k < limit:
                    if stress_results != []:
                        self.dice_img = dicedict[stress_results.pop(0)]
                    ttk.Label(self.dr_results, image = self.dice_img, background = '#182318').grid(row = i // 10, column = i % 10, padx = 3, pady = 2)
                    i += 1
                    k += 1

        #Variables
        
            base_results = []
            stress_results = []
            important_rolls = []
            bdice = int(self.dr_bdice_amt.get())
            sdice = -int(self.dr_sdice_amt.get())

        #Call Dice Functions    
            roll(sdice)
            roll(bdice)
            print_roll()
   
    #Clear the Dice Box
        def dice_clear():
            self.dr_results.destroy()

    #Reset Readout
        def results_reset():
            self.dr_results.destroy()
            self.dr_results = ttk.Frame(self.dr_readout, style = 'Dice.TFrame')
            self.dr_results.pack(padx = 5, pady = 0)




###---MOTION TRACKER---###

        def mt_start():
        #Frames
            self.mt_main = ttk.Frame(master, height = 480, width = 640, style = 'MT.TFrame')
            self.mt_main.pack_propagate(False)
            self.mt_main.place(relx = 0.5, rely = 0.5, anchor = 'center')

            self.mt_trackerframe = ttk.Frame(self.mt_main, height = 400, width = 620, style = 'MT.TFrame',)
            self.mt_trackerframe.place(relx = 0.5, y = 215, anchor = 'n')

        #Variables

            self.mt_val = IntVar()
            self.mt_val.set(0)
            self.mt_toggle_value = False

        #Credits
            ttk.Label(self.mt_main, text = 'Credits:', style = 'Header.Alien.TLabel', font = ('Courier New', 16)).place(x = 10, y = 10)
            ttk.Label(self.mt_main, style = 'Inv.Alien.TLabel', font = ('Courier New', 10), text = 'Programming and Graphic Design - Micah Popp \n\nMotion Tracker SFX - Alien vs Predator (2010) \n\nFor use with the Alien RPG by Free League').place(x = 20, y = 50)

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
                                          font = ('Courier New', 10),
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