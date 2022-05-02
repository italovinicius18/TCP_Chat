from tkinter import *
from tkinter import messagebox
import socket
import threading

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
print(ADDRESS)
FORMAT = "utf-8"

# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
client.connect(ADDRESS)

WIDTH = 300
HEIGHT = 400

DARKCYAN = "#008B8B"
SALMON = "#FF7474"
DARK = "#464646"

class GUI:
    def __init__(self):
        self.login_name_nick = ""
        self.groups = []

        self.window = Tk()
        self.window.resizable(False, False)

        self.window.title("Grupos de chat")

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (WIDTH/2))
        self.y_cordinate = int((self.screen_height/2) - (HEIGHT/2))

        self.window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, self.x_cordinate, self.y_cordinate))

        self.frame_login = Frame(self.window,height=HEIGHT,width=WIDTH,bd=5,bg=DARKCYAN)

        self.frame_login.grid(column=1, row=0)

        self.disable_resize(self.frame_login)

        self.title_login = Label(self.frame_login, text="Grupos de chat",font=('Helvetica 15 bold'), bg=DARKCYAN, fg="white")

        self.title_login.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.description_login = Label(self.frame_login, text="Digite seu apelido:" ,font=('Helvetica 11'), bg=DARKCYAN, fg="white")

        self.description_login.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.login_name = Entry(self.frame_login,width=20)

        self.login_name.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.login_name.focus()

        self.btn_login = Button(self.frame_login,text="Login",width=5, bg=SALMON, fg="white", command= lambda: self.check_login(self.login_name.get(),self.window))

        self.btn_login.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.window.mainloop()

    def disable_resize(self,frame):
        frame.configure(height=frame["height"],width=frame["width"])
        frame.grid_propagate(0)

    def check_login(self,login_name,window):
        if len(login_name) > 5:
            print(f"Login valido {login_name}")
            window.destroy()
            self.login_name_nick = login_name
            self.build_groups()
        else:
            messagebox.showinfo('Alerta!', 'O apelido precisa ter tamanho maior que 5 caracteres')

    def check_group(self,group_name,window_groups, window):
        if len(group_name) <= 5:
            messagebox.showinfo('Alerta!', 'O nome do grupo precisa ter tamanho maior que 5 caracteres')
        elif group_name in self.groups:
            messagebox.showinfo('Alerta!', 'O grupo já existe')
        else:
            print("Grupo valido")
            self.groups.append(group_name)
            client.send(f"{self.login_name_nick}".encode(FORMAT))
            window_groups.destroy()
            window.destroy()
            
            self.build_groups()

    def access_group(self,window,group_name):
        print("Acessando grupo {}".format(group_name))
        self.go_ahead(window,group_name)

    def create_group(self,window_groups):
        HEIGHT = 200
        WIDTH = 300

        self.window = Tk()
        self.window.resizable(False, False)

        self.window.title("Grupos de chat")

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (WIDTH/2))
        self.y_cordinate = int((self.screen_height/2) - (HEIGHT/2))

        self.window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, self.x_cordinate, self.y_cordinate))

        self.frame_group = Frame(self.window,height=HEIGHT,width=WIDTH,bd=5, bg=DARKCYAN)

        self.frame_group.grid(column=1, row=0)

        self.disable_resize(self.frame_group)

        self.title_group = Label(self.frame_group, text="Criar grupo",font=('Helvetica 15 bold'), bg=DARKCYAN, fg="white")

        self.title_group.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.description_group = Label(self.frame_group, text="Digite o nome do grupo:" ,font=('Helvetica 11'), bg=DARKCYAN, fg="white")

        self.description_group.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.login_name = Entry(self.frame_group,width=20)

        self.login_name.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.login_name.focus()

        self.btn_group = Button(self.frame_group,text="Criar",width=5, bg=SALMON, fg="white", command= lambda: self.check_group(self.login_name.get(),window_groups, self.window))

        self.btn_group.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.window.mainloop()

    def build_groups(self):
        self.window = Tk()
        self.window.resizable(False, False)

        self.window.title("Grupos de chat")

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (WIDTH/2))
        self.y_cordinate = int((self.screen_height/2) - (HEIGHT/2))

        self.window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, self.x_cordinate, self.y_cordinate))

        self.frame_groups = Frame(self.window,height=HEIGHT,width=WIDTH,bd=5,bg=DARKCYAN)

        self.frame_groups.grid(column=2, row=0)

        for i,group in enumerate(self.groups):
            self.btn_group = Button(self.frame_groups,text=group,width=40, bg=SALMON, fg="white", command= lambda group=group : self.access_group(self.window,group))
            self.btn_group.place(relx=0.5, rely=0.04+i/12, anchor=CENTER)
        
        self.btn_create_group = Button(self.frame_groups,text="Criar novo grupo",width=30, bg=DARK, fg="white", command=lambda: self.create_group(self.window))
        self.btn_create_group.place(x=WIDTH//2, y=HEIGHT-20, anchor=CENTER)

        self.disable_resize(self.frame_groups)

        self.window.mainloop()

    def build_chat(self,group_name):
        self.window = Tk()
        self.window.resizable(False, False)

        self.window.title("Grupos de chat")

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (WIDTH/2))
        self.y_cordinate = int((self.screen_height/2) - (HEIGHT/2))

        self.window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, self.x_cordinate, self.y_cordinate))

        self.frame_chat = Frame(self.window,height=HEIGHT,width=WIDTH,bd=5,bg=DARKCYAN)

        self.frame_chat.grid(column=3, row=0)

        self.disable_resize(self.frame_chat)
            
        self.label_head = Label(self.frame_chat,bg = DARK,fg = "white",text = group_name ,font = "Helvetica 13 bold",pady = 5)
            
        self.label_head.place(relwidth = 1)
        self.line = Label(self.frame_chat,width = int(WIDTH/3),bg = DARK)
            
        self.line.place(relwidth = 1,rely = 0.07,relheight = 0.012)
            
        self.text_cons = Text(self.frame_chat,width = 20,height = 2,bg = DARKCYAN,fg = "#EAECEE",font = "Helvetica 14",padx = 5,pady = 5)
            
        self.text_cons.place(relheight = 0.745,relwidth = 1,rely = 0.08)
            
        self.label_bottom = Label(self.frame_chat,bg = DARKCYAN,height = 80)
            
        self.label_bottom.place(relwidth = 1,rely = 0.825)
            
        self.entry_msg = Entry(self.label_bottom,bg = DARKCYAN,fg = "#EAECEE",font = "Helvetica 13")
            
        # place the given widget
        # into the gui window
        self.entry_msg.place(relwidth = 0.74,relheight = 0.06,rely = 0.008,relx = 0.011)
            
        self.entry_msg.focus()
            
        # create a Send Button
        self.button_msg = Button(self.label_bottom,text = "Send",font = "Helvetica 10 bold",width = 20,bg = SALMON, fg="white",command = lambda : self.send_button(self.entry_msg.get()))
            
        self.button_msg.place(relx = 0.77,rely = 0.008,relheight = 0.06,relwidth = 0.22)
            
        self.text_cons.config(cursor = "arrow")
            
        # create a scroll bar
        self.scrollbar = Scrollbar(self.text_cons)
        
        # place the scroll bar
        # into the gui window
        self.scrollbar.place(relheight = 1,relx = 0.974)
            
        self.scrollbar.config(command = self.text_cons.yview)
            
        self.text_cons.config(state = DISABLED)

        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()

        self.window.mainloop()

    def go_ahead(self,window, group_name):
        window.destroy()
        self.build_chat(group_name)

    # function to basically start the thread for sending messages
    def send_button(self, msg):
        self.text_cons.config(state = DISABLED)
        self.msg=msg
        self.entry_msg.delete(0, END)
        snd= threading.Thread(target = self.send_message)
        snd.start()

    # function to receive messages
    def receive(self):
        print("Receiving messages...")
        while True:
            message = client.recv(1024).decode(FORMAT)
            print(message)
            # if the messages from the server is NAME send the client's name
            if message == 'NAME':
                print("Enviando nome...")
                client.send(self.login_name_nick.encode(FORMAT))
            else:
                # insert messages to text box
                self.text_cons.config(state = NORMAL)
                self.text_cons.insert(END,
                                        message+"\n\n")
                    
                self.text_cons.config(state = DISABLED)
                self.text_cons.see(END)
         
    # function to send messages
    def send_message(self):
        self.text_cons.config(state=DISABLED)
        while True:
            message = (f"{self.login_name_nick}: {self.msg}")
            client.send(message.encode(FORMAT))   
            break   

if __name__ == '__main__':
    init= threading.Thread(target = GUI())
    init.start()