from tkinter import *
from tkinter import messagebox

WIDTH = 300
HEIGHT = 400

DARKCYAN = "#008B8B"
SALMON = "#FF7474"
DARK = "#464646"

GROUPS = []

def disable_resize(frame):
    frame.configure(height=frame["height"],width=frame["width"])
    frame.grid_propagate(0)

def check_login(login_name,window):
    if len(login_name) > 5:
        print("Login valido")
        window.destroy()
        build_groups()
    else:
        messagebox.showinfo('Alerta!', 'O apelido precisa ter tamanho maior que 5 caracteres')

def check_group(group_name,window_groups, window):
    if len(group_name) <= 5:
        messagebox.showinfo('Alerta!', 'O nome do grupo precisa ter tamanho maior que 5 caracteres')
    elif group_name in GROUPS:
        messagebox.showinfo('Alerta!', 'O grupo já existe')
    else:
        print("Grupo valido")
        GROUPS.append(group_name)
        window_groups.destroy()
        window.destroy()
        build_groups()

def access_group(window,group_name):
    print("Acessando grupo {}".format(group_name))
    window.destroy()

    build_chat(group_name)

def create_group(window_groups):
    HEIGHT = 200
    WIDTH = 300

    window = Tk()
    window.resizable(False, False)

    window.title("Grupos de chat")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (WIDTH/2))
    y_cordinate = int((screen_height/2) - (HEIGHT/2))

    window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))

    frame_group = Frame(window,height=HEIGHT,width=WIDTH,bd=5, bg=DARKCYAN)

    frame_group.grid(column=1, row=0)

    disable_resize(frame_group)

    title_group = Label(frame_group, text="Criar grupo",font=('Helvetica 15 bold'), bg=DARKCYAN, fg="white")

    title_group.place(relx=0.5, rely=0.3, anchor=CENTER)

    description_group = Label(frame_group, text="Digite o nome do grupo:" ,font=('Helvetica 11'), bg=DARKCYAN, fg="white")

    description_group.place(relx=0.5, rely=0.5, anchor=CENTER)

    login_name = Entry(frame_group,width=20)

    login_name.place(relx=0.5, rely=0.7, anchor=CENTER)

    login_name.focus()

    btn_group = Button(frame_group,text="Criar",width=5, bg=SALMON, fg="white", command= lambda: check_group(login_name.get(),window_groups, window))

    btn_group.place(relx=0.5, rely=0.9, anchor=CENTER)

    window.mainloop()

def build_login():
    window = Tk()
    window.resizable(False, False)

    window.title("Grupos de chat")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (WIDTH/2))
    y_cordinate = int((screen_height/2) - (HEIGHT/2))

    window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))

    frame_login = Frame(window,height=HEIGHT,width=WIDTH,bd=5,bg=DARKCYAN)

    frame_login.grid(column=1, row=0)

    disable_resize(frame_login)

    title_login = Label(frame_login, text="Grupos de chat",font=('Helvetica 15 bold'), bg=DARKCYAN, fg="white")

    title_login.place(relx=0.5, rely=0.3, anchor=CENTER)

    description_login = Label(frame_login, text="Digite seu apelido:" ,font=('Helvetica 11'), bg=DARKCYAN, fg="white")

    description_login.place(relx=0.5, rely=0.4, anchor=CENTER)

    login_name = Entry(frame_login,width=20)

    login_name.place(relx=0.5, rely=0.5, anchor=CENTER)

    login_name.focus()

    btn_login = Button(frame_login,text="Login",width=5, bg=SALMON, fg="white", command= lambda: check_login(login_name.get(),window))

    btn_login.place(relx=0.5, rely=0.6, anchor=CENTER)

    window.mainloop()

def build_groups():
    window = Tk()
    window.resizable(False, False)

    window.title("Grupos de chat")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (WIDTH/2))
    y_cordinate = int((screen_height/2) - (HEIGHT/2))

    window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))

    frame_groups = Frame(window,height=HEIGHT,width=WIDTH,bd=5,bg=DARKCYAN)

    frame_groups.grid(column=2, row=0)

    for i,group in enumerate(GROUPS):
        btn_group = Button(frame_groups,text=group,width=40, bg=SALMON, fg="white", command= lambda group=group : access_group(window,group))
        btn_group.place(relx=0.5, rely=0.04+i/12, anchor=CENTER)
    
    btn_create_group = Button(frame_groups,text="Criar novo grupo",width=30, bg=DARK, fg="white", command=lambda: create_group(window))
    btn_create_group.place(x=WIDTH//2, y=HEIGHT-20, anchor=CENTER)

    disable_resize(frame_groups)

    window.mainloop()

def build_chat(group_name):
    window = Tk()
    window.resizable(False, False)

    window.title("Grupos de chat")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (WIDTH/2))
    y_cordinate = int((screen_height/2) - (HEIGHT/2))

    window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))

    frame_chat = Frame(window,height=HEIGHT,width=WIDTH,bd=5,bg=DARKCYAN)

    frame_chat.grid(column=3, row=0)

    disable_resize(frame_chat)
        
    labelHead = Label(frame_chat,bg = DARK,fg = "white",text = group_name ,font = "Helvetica 13 bold",pady = 5)
         
    labelHead.place(relwidth = 1)
    line = Label(frame_chat,width = int(WIDTH/3),bg = DARK)
         
    line.place(relwidth = 1,rely = 0.07,relheight = 0.012)
         
    textCons = Text(frame_chat,width = 20,height = 2,bg = DARKCYAN,fg = "#EAECEE",font = "Helvetica 14",padx = 5,pady = 5)
         
    textCons.place(relheight = 0.745,relwidth = 1,rely = 0.08)
         
    labelBottom = Label(frame_chat,bg = DARKCYAN,height = 80)
         
    labelBottom.place(relwidth = 1,rely = 0.825)
         
    entryMsg = Entry(labelBottom,bg = DARKCYAN,fg = "#EAECEE",font = "Helvetica 13")
         
    # place the given widget
    # into the gui window
    entryMsg.place(relwidth = 0.74,relheight = 0.06,rely = 0.008,relx = 0.011)
         
    entryMsg.focus()
         
    # create a Send Button
    buttonMsg = Button(labelBottom,text = "Send",font = "Helvetica 10 bold",width = 20,bg = DARKCYAN,command = lambda : sendButton(entryMsg.get()))
         
    buttonMsg.place(relx = 0.77,rely = 0.008,relheight = 0.06,relwidth = 0.22)
         
    textCons.config(cursor = "arrow")
         
    # create a scroll bar
    scrollbar = Scrollbar(textCons)
     
    # place the scroll bar
    # into the gui window
    scrollbar.place(relheight = 1,relx = 0.974)
         
    scrollbar.config(command = textCons.yview)
         
    textCons.config(state = DISABLED)

def main():

    build_login()


if __name__ == '__main__':
    main()