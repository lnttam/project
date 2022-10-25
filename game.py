from tkinter import *
import csv
from tkinter import messagebox
from tkinter.ttk import Style, Treeview

ques_no = -1
score = 0

# Đọc file câu hỏi
ques_lst = list()
ans_lst = list()
with open("ques_file.csv","r") as ques_file:
    ques_reader = csv.reader(ques_file, delimiter=',')
    for row in ques_reader:
       ques_lst.append(row[0])
       ans_lst.append(row[1])
    ques_dict = {k : v for k, v in zip(ques_lst,ans_lst)}

# Đọc file score
def readList():
    name_lst = list()
    score_lst = list()
    with open("result_file.csv","r") as result_file:
        result_reader = csv.reader(result_file, delimiter=',')
        for row in result_reader:
            name_lst.append(row[0])
            score_lst.append(row[1])
        # score_lst.sort(reverse=True)
    global result_dict
    global result_dict_sort
    result_dict = {k : v for k, v in zip(name_lst,score_lst)}
    result_dict_sort = dict(sorted(result_dict.items(), key=lambda x:x[1],reverse=True))
#     print(result_dict_sort)
# readList()

def create_result_win():
    result_win = Tk()
    result_win.geometry("350x200")
    result_win.configure(bg = "light blue")
    frame1 = Frame(result_win,bg = "light blue")
    frame1.pack(side=LEFT)
    frame2 = Frame(result_win,bg = "light blue")
    frame2.pack(side=BOTTOM)
        # Hiển thị ở frame1
    # danh sach treeview
    readList()
    result_view_style = Style()
    result_view_style.configure("Trstyle.Treeview.Heading", foreground='#f38755',font=("Constantia", 15,'bold'))
    result_view = Treeview(frame1, columns=("player","score"),show='headings', style="Trstyle.Treeview")
    result_view.heading("player", text="Player")
    result_view.column("player",width=88,anchor=CENTER)
    result_view.heading("score",text="Score")
    result_view.column("score",width=87,anchor=CENTER)
    for key,value in result_dict_sort.items():
        result_view.insert('', END, values=(key,value))
    result_view.pack()

        # Hiển thị ở frame2
    # Them nut xoa
    def playgame_button():
        global ques_no
        global score
        ques_no = -1
        score = 0
        result_win.destroy()
        create_game_win()
    
    def quit_button():
        result_win.destroy()

    btn_playgame = Button(frame2,
                text="Play game",
                font=("Constantia",15,"bold"),
                bg = "gray",
                fg = "white",
                command=playgame_button
                )
    btn_playgame.pack()

    btn_quit = Button(frame2,
                text="Quit",
                font=("Constantia",15,"bold"),
                bg = "gray",
                fg = "white",
                command=quit_button
                )
    btn_quit.pack()


def create_game_win():
    def write_result():
        with open("result_file.csv","a",newline="") as result_file:
            result_write = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result_write.writerow([name, score])
    def next_button(): #hàm event cho cái nút next
        global ques_no
        global score
        global name
        if ques_no == -1:
            name = en_ans.get()
            # name_lst.append(name)
            if name.strip()=="":
                messagebox.showwarning(title="Warning",message="Hãy nhập tên của bạn")
            else:
                en_ans.delete(0,END)
                ques_no +=1
                lbl_ques.config(text=f'{ques_lst[ques_no]}', font=("Constantia",40,'bold'))
        elif ques_no <= len(ques_lst) - 2:
            if en_ans.get().lower() == ans_lst[ques_no]:
                score += 1
                en_ans.delete(0,END)
                ques_no += 1
                lbl_ques.config(text=f'{ques_lst[ques_no]}', font=("Constantia",40,'bold'))         
            else:
                messagebox.showinfo(title= "Score" ,message= f'Điểm của bạn: {score}')
                write_result()
                game_win.destroy()
                create_result_win()
        else :
            if en_ans.get() == ans_lst[ques_no]:
                score += 1
                messagebox.showinfo(title= "Score" ,message= f'Bạn đã thắng: {score}')
                write_result()
                game_win.destroy()
                create_result_win()

    # Tạo màn hình game
    game_win = Tk()
    game_win.geometry("350x200")
    game_win.configure(bg = "light blue") # màu background

    #Chạy mấy cái widget này trước trong game_win
    lbl_ques = Label(game_win, # label câu hỏi
                    text="XIN CHÀO!\nBẠN TÊN GÌ?.",
                    bg="light blue",
                    font=("Constantia",20,'bold'),
                    fg = "red",
                    )
    lbl_ques.pack()
    en_ans = Entry(game_win, # Ô nhập
                    font=("Constantia",20),
                    justify= CENTER
                )
    en_ans.pack()
    btn_next = Button(game_win, # Nút next
                    text="Next",
                    font=("Constantia",15,"bold"),
                    bg = "gray",
                    fg = "white",
                    command=next_button
                    )
    btn_next.pack()
    # game_win.mainloop()
