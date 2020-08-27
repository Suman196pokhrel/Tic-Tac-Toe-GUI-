from tkinter import *
from random import choice, choices
from functools import partial
import random

globals()['identifier'] = 'X'
globals()['user_positions'] = []
globals()['user_authentic'] = True
globals()['Start_status'] = True
globals()['user_status'] = True
globals()['random_list'] = [[1,0], [2, 0], [3, 0], [1, 1], [2, 1], [3, 1], [3, 2], [2, 2], [1, 2]]



class TicTacToe(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.x_text = StringVar()
        self.o_text = StringVar()
        # self.maxsize(320, 350)
        self.title("TIC TAC TOE")
        self.config(bg='#2C3539')
        self.btn_value = ' '
        # self.btn_value1 = None
        self.btn_height = 2
        self.btn_width = 5
        self.padx = 0
        self.pady = 0
        self.btn_font_size = 15
        self.btn = None
        self.btn_1 = None
        self.btn_2 = None
        self.btn_3 = None
        self.btn_4 = None
        self.btn_5 = None
        self.btn_6 = None
        self.btn_7 = None
        self.btn_8 = None
        self.btn_9 = None
        self.btn_value_modified = None
        self.machine_button = None


        # Functions


        self.frame_1 = Frame(self, borderwidth=2,relief="groove").grid(row=0,column=0,padx=10,pady=10)

        self.label_1 = Label(self.frame_1, text="TIC  TAC  TOE", borderwidth=2,relief="groove",
                             font=("comic sans ms", 15, "italic"),bg='#2C3539',fg='#FCDFFF').grid(row=0, column=0,sticky='n',columnspan=2,pady=10)

        # , command = partial(self.user_clicks, [self.i, self.j])
        # Button Construction
        if globals()['Start_status']:
            self.start = Button(self, text='START GAME', font=("comic sans ms", self.btn_font_size, "italic"),
                                height=1, width=15, command=self.generate_button)
            self.start.grid(row=1, column=0, padx=20, pady=30)

            self.quit_btn = Button(self, text='QUIT GAME', font=("comic sans ms", self.btn_font_size, "italic"),
                                  height=1, width=10,command=lambda : quit())
            self.quit_btn.grid(row=1, column=3, padx=20, pady=10)
            globals()['Start_status'] = False

    def generate_button(self):

        self.start.grid_forget()
        self.quit_btn.grid(row=3, column=4, padx=20, pady=10)

        self.frame_2 = Frame(self, borderwidth=2, relief="groove").grid(row=1, column=4, padx=10, pady=10)

        self.label_2 = Label(self.frame_2, text="WHOSE TURN ?", borderwidth=2, relief="groove",
                             font=("comic sans ms", 15, "italic"), bg='#2C3539', fg='#FCDFFF').grid(row=0, column=4,
                                                                                                    sticky='n',
                                                                                                    columnspan=2)
        self.turn_board_text = Text(self.frame_2, width=20, height=4,font=("comic sans ms", 8, "italic"))
        self.turn_board_text.grid(row=1, column=4, pady=10,rowspan=1)
        self.turn_board_text.insert(INSERT,'Its Your Turn.\nClick NEXT Button to pass\n the turn to Computer')

        self.machine_button = Button(self, text='Next', font=("comic sans ms", self.btn_font_size, "italic"),
                                  height=1, width=10,command=lambda : self.helper([False]))
        self.machine_button.grid(row=2, column=4, padx=20, pady=10)

        self.replay = Button(self, text='REPLAY', font=("comic sans ms", self.btn_font_size, "italic"),
                                  height=1, width=10,command=self.replay_btn)
        self.replay.grid(row=4, column=4,padx=20)

        # self.quit_btn.grid_forget()
        # Button Creation

        self.btn_1 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([1, 0]))
        self.btn_1.grid(row=1, column=0,padx = self.padx,pady=self.pady)


        self.btn_2 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([1, 1]))
        self.btn_2.grid(row=1, column=1, padx=self.padx, pady=self.pady)


        self.btn_3 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([1, 2]))
        self.btn_3.grid(row=1, column=2, padx=self.padx, pady=self.pady)

        self.btn_4 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([2, 0]))
        self.btn_4.grid(row=2, column=0, padx=self.padx, pady=self.pady)

        self.btn_5 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([2, 1]))
        self.btn_5.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        self.btn_6 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([2, 2]))
        self.btn_6.grid(row=2, column=2, padx=self.padx, pady=self.pady)

        self.btn_7 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([3, 0]))
        self.btn_7.grid(row=3, column=0, padx=self.padx, pady=self.pady)

        self.btn_8 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([3, 1]))
        self.btn_8.grid(row=3, column=1, padx=self.padx, pady=self.pady)

        self.btn_9 = Button(self, text=self.btn_value, font=("comic sans ms", self.btn_font_size, "italic"),
                            height=self.btn_height, width=self.btn_width, command=lambda :self.helper([3, 2]))
        self.btn_9.grid(row=3, column=2, padx=self.padx, pady=self.pady)

        # print('Buttons Generated')
        # print((self.grid_slaves()))

    def click_response_user(self, btn_index_list):
        # print('Button Command Called')
        # btn_var = 9

        self.check_authenticity_user_input(btn_index_list)

        if globals()['user_authentic']:
            if btn_index_list[0] == 1 and btn_index_list[1] == 0:
                self.btn_1['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 1 and btn_index_list[1] == 1:
                self.btn_2['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 1 and btn_index_list[1] == 2:
                self.btn_3['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 2 and btn_index_list[1] == 0:
                self.btn_4['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 2 and btn_index_list[1] == 1:
                self.btn_5['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 2 and btn_index_list[1] == 2:
                self.btn_6['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 3 and btn_index_list[1] == 0:
                self.btn_7['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 3 and btn_index_list[1] == 1:
                self.btn_8['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)

            if btn_index_list[0] == 3 and btn_index_list[1] == 2:
                self.btn_9['text'] = 'X'
                globals()['user_positions'].append(btn_index_list)
                globals()['random_list'].remove(btn_index_list)
                # globals()['user_status'] = False
                # globals()['user_status'] = False


        else:
            print("Space Already Accoupied")
        # print(globals()['user_positions'])
        # globals()['user_status'] = False
        # print('Exiting the button Command')
        # print(globals()['user_status'])

    def click_response_machine(self, btn_index_list):
        # print('Button Command Called inside machine')
        # btn_var = 9

        # self.check_authenticity_user_input(btn_index_list)

        # if globals()['user_authentic']:
        if btn_index_list[0] == 1 and btn_index_list[1] == 0:
            self.grid_slaves()[0] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 1 and btn_index_list[1] == 1:
            self.btn_2['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 1 and btn_index_list[1] == 2:
            self.btn_3['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 2 and btn_index_list[1] == 0:
            self.btn_4['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 2 and btn_index_list[1] == 1:
            self.btn_5['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 2 and btn_index_list[1] == 2:
            self.btn_6['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 3 and btn_index_list[1] == 0:
            self.btn_7['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 3 and btn_index_list[1] == 1:
            self.btn_8['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)

        if btn_index_list[0] == 3 and btn_index_list[1] == 2:
            self.btn_9['text'] = '0'
            globals()['user_positions'].append(btn_index_list)
            globals()['random_list'].remove(btn_index_list)
            # globals()['user_status'] = False
            # globals()['user_status'] = False


        # else:
        #     print("Space Already Accoupied")
        # # print(globals()['user_positions'])
        # # globals()['user_status'] = False
        # print('Exiting the button Command')
        # # print(globals()['user_status'])

    def check_authenticity_user_input(self,inpp):
        # print("inside the Checking Fucntion")
        for i in globals()['user_positions']:
            if i == inpp:
                globals()['user_authentic'] = False
                break
            else:
                globals()['user_authentic'] = True

                # print("Sorry Position already taken\n")
        # print('Outside the Checking Function')

    def machine(self):
        # print('Inside the machine block')
        # self.turn_board_text.insert(INSERT, "It's Machine's Turn")
        ran = choice(globals()['random_list'])
        # self.check_authenticity_user_input(ran)
        self.click_response_machine(ran)
        # globals()['user_positions'].append(ran)
        # globals()['random_list'].remove(ran)
        # print('Outside the machine Block')

    def helper(self, btn_index):
        if btn_index[0]:
            self.click_response_user(btn_index)
            self.check_game_win_cndth('USER')


        else:
            # self.turn_board_text.delete('1.0', 'end')
            # self.turn_board_text.insert(INSERT,'->Your Turn, Select a block and pass the turn to Computer by pressing the NEXT button')
            self.machine()
            self.check_game_win_cndth('COMPUTER')

    def check_game_win_cndth(self, identifier):
        print('Inside the game WIn Checking Funciton')
        print(self.btn_1['text'],self.btn_2['text'],self.btn_3['text'])
        # Diagonal Possibilities
        self.turn_board_text.delete('1.0','end')
        # print(f'{identifier} won the game')

        if self.btn_1['text'] == 'X' and self.btn_5['text'] == 'X' and self.btn_9['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT,f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_1['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_9['text'] = f'{identifier}'

        elif self.btn_1['text'] == '0' and self.btn_5['text']=='0' and self.btn_9['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT,f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_1['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_9['text'] = f'{identifier}'

        elif self.btn_3['text'] == 'X' and self.btn_5['text'] == 'X' and self.btn_7['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_3['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_7['text'] = f'{identifier}'

        elif self.btn_3['text'] == '0' and self.btn_5['text'] == '0' and self.btn_7['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_3['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_7['text'] = f'{identifier}'

        # elif self.btn_3['text'] == 'X' and self.btn_5['text'] == 'X' and self.btn_7['text'] == 'X':
        #     self.turn_board_text.delete('1.0', 'end')
        #     self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
        #     self.btn_3['text'] = f'{identifier}'
        #     self.btn_5['text'] = f'{identifier}'
        #     self.btn_7['text'] = f'{identifier}'
        #
        # elif self.btn_3['text'] == '0' and self.btn_5['text'] == '0' and self.btn_7['text'] == '0':
        #     self.turn_board_text.delete('1.0', 'end')
        #     self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')

        # Linear  horizontal Possibilities

        elif self.btn_1['text'] == 'X' and self.btn_2['text'] == 'X' and self.btn_3['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_1['text'] = f'{identifier}'
            self.btn_2['text'] = f'{identifier}'
            self.btn_3['text'] = f'{identifier}'

        elif self.btn_1['text'] == '0' and self.btn_2['text'] == '0' and self.btn_3['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_1['text'] = f'{identifier}'
            self.btn_2['text'] = f'{identifier}'
            self.btn_3['text'] = f'{identifier}'

        elif self.btn_4['text'] == 'X' and self.btn_5['text'] == 'X' and self.btn_6['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_4['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_6['text'] = f'{identifier}'

        elif self.btn_4['text'] == '0' and self.btn_5['text'] == '0' and self.btn_6['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_4['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_6['text'] = f'{identifier}'

        elif self.btn_7['text'] == 'X' and self.btn_8['text'] == 'X' and self.btn_9['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_7['text'] = f'{identifier}'
            self.btn_8['text'] = f'{identifier}'
            self.btn_9['text'] = f'{identifier}'

        elif self.btn_7['text'] == '0' and self.btn_8['text'] == '0' and self.btn_9['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_7['text'] = f'{identifier}'
            self.btn_8['text'] = f'{identifier}'
            self.btn_9['text'] = f'{identifier}'

        # Linear Vertical Possibilities

        elif self.btn_1['text'] == 'X' and self.btn_4['text'] == 'X' and self.btn_7['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_1['text'] = f'{identifier}'
            self.btn_4['text'] = f'{identifier}'
            self.btn_7['text'] = f'{identifier}'

        elif self.btn_1['text'] == '0' and self.btn_4['text'] == '0' and self.btn_7['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_1['text'] = f'{identifier}'
            self.btn_4['text'] = f'{identifier}'
            self.btn_7['text'] = f'{identifier}'


        elif self.btn_2['text'] == 'X' and self.btn_5['text'] == 'X' and self.btn_8['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_2['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_8['text'] = f'{identifier}'

        elif self.btn_2['text'] == '0' and self.btn_5['text'] == '0' and self.btn_8['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_2['text'] = f'{identifier}'
            self.btn_5['text'] = f'{identifier}'
            self.btn_8['text'] = f'{identifier}'

        elif self.btn_3['text'] == 'X' and self.btn_6['text'] == 'X' and self.btn_9['text'] == 'X':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_3['text'] = f'{identifier}'
            self.btn_6['text'] = f'{identifier}'
            self.btn_9['text'] = f'{identifier}'

        elif self.btn_3['text'] == '0' and self.btn_6['text'] == '0' and self.btn_5['text'] == '0':
            self.turn_board_text.delete('1.0', 'end')
            self.turn_board_text.insert(INSERT, f'GAME OVER {identifier} \nWON THE GAME')
            self.btn_3['text'] = f'{identifier}'
            self.btn_6['text'] = f'{identifier}'
            self.btn_9['text'] = f'{identifier}'

        else:
            print("none of the Condition matches")

    def replay_btn(self):
        globals()['user_positions'] = []
        globals()['random_list'] = [[1, 0], [2, 0], [3, 0], [1, 1], [2, 1], [3, 1], [3, 2], [2, 2], [1, 2]]

        self.btn_1['text'] = ''
        self.btn_2['text'] = ''
        self.btn_3['text'] = ''
        self.btn_4['text'] = ''
        self.btn_5['text'] = ''
        self.btn_6['text'] = ''
        self.btn_7['text'] = ''
        self.btn_8['text'] = ''
        self.btn_9['text'] = ''


if __name__ == '__main__':
    tiktik = TicTacToe()
    # if not(globals()['user_status']):
    #     tiktik.machine()
    # globals()['user_status'] = True
    # print(globals()['user_status'])
    tiktik.mainloop()
