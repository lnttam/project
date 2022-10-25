from tkinter import *
import csv

ques_lst = list()
ans_lst = list()
with open("ques_file.csv","r") as ques_file:
    ques_reader = csv.reader(ques_file, delimiter=',')
    for row in ques_reader:
       ques_lst.append(row[0])
       ans_lst.append(row[1])
    ques_dict = {k : v for k, v in zip(ques_lst,ans_lst)}

no = 0
def create_fcard_win():
    def next_button():
        global no
        if no == len(ques_lst)-1:
            no = 0
        else:
            no += 1
        lbl_ques.config(text=ques_lst[no])
        lbl_ans.config(text=ans_lst[no])
    def quit_button():
        fcard_win.destroy()

    fcard_win = Tk()
    fcard_win.geometry("350x200")
    fcard_win.configure(bg = "light blue")
    bottom_frame = Frame(fcard_win,background="light blue")
    bottom_frame.pack(side=BOTTOM)

    lbl_ques = Label(text=ques_lst[no],
                    bg="light blue",
                    font=("Constantia",40,'bold'),
                    fg="red"
                    )
    lbl_ques.pack()
    lbl_ans = Label(text=ans_lst[no],
                    bg="light blue",
                    font=("Constantia",40,'bold')
                    )
    lbl_ans.pack()

    btn_next = Button(bottom_frame,text="Next",
                    font=("Constantia",15,'bold'),
                    bg = "gray",
                    fg = "white",
                    command=next_button
                    )
    btn_next.pack(side=RIGHT)

    btn_quit = Button(bottom_frame,text="Quit",
                    font=("Constantia",15,'bold'),
                    bg = "gray",
                    fg = "white",
                    command=quit_button
                    )
    btn_quit.pack(side=LEFT)
