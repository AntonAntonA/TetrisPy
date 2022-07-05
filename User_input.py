from tkinter import *

class User_input:
    __RIGHT_RELEASED = 1
    __LEFT_RELEASED = 2
    __DOWN_PRESSED = 3
    __UP_RELEASED = 4
    __user_input = 0

    def __init__(self, key: int):
        self.user_input = key
        return

    def clear_user_input(self):
        self.__user_input = 0

    @property
    def user_input(self):
        return self.__user_input

    @user_input.setter
    def user_input(self, key: int):


    @property
    def RIGHT_RELEASED(self):
        return self.__RIGHT_RELEASED

    @property
    def LEFT_RELEASED(self):
        return self.__LEFT_RELEASED

    @property
    def DOWN_PRESSED(self):
        return self.__DOWN_PRESSED

    @property
    def UP_RELEASED(self):
        return self.__UP_RELEASED
