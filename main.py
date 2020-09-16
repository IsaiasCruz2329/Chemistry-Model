from tkinter import *
import tkinter.font as tkFont
from main_screen import MainScreen


def main():
    root = Tk()
    app = MainScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
