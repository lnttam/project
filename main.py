from tkinter import *
from game import create_game_win, create_result_win
from flashcard import create_fcard_win

def create_win():
    def play_button():
        win.destroy()
        create_game_win()

    def result_button():
        win.destroy()
        create_result_win()

    def flashcard_button():
        win.destroy()
        create_fcard_win()

    def quit_button():
        win.destroy()

    win = Tk()
    win.geometry("350x200")
    win.configure(bg = "light blue")

    left_frame = Frame(win, background="light blue")
    left_frame.pack(side=LEFT)

    right_frame = Frame(win, background="light blue")
    right_frame.pack(side=RIGHT)

    btn_play = Button(left_frame, text="Play Game",font=("Constantia",25,'bold'),bg="light pink",command=play_button)
    btn_play.pack()

    btn_result =  Button(right_frame,text="Result",font=("Constantia",25,'bold'),bg="light pink",command=result_button)
    btn_result.pack()

    btn_fcard = Button(left_frame,text="Flashcard",font=("Constantia",25,'bold'),bg="light pink",command=flashcard_button)
    btn_fcard.pack()

    btn_quit = Button(right_frame, text="Quit",font=("Constantia",25,'bold'),bg="light pink",command=quit_button)
    btn_quit.pack()

    win.mainloop()
create_win()