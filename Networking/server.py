import   socket
from tkinter import *

root = Tk()
root.title("Server")
root.minsize(400, 400)

def send(listbox, entry):
    message = entry.get()
    listbox.insert("end", "Server: "+message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))

def receive(listbox):
    message_rec = client.recv(50)
    # print("Client: ", message_rec.decode("utf-8"))
    listbox.insert("end", "Client: "+message_rec.decode("utf-8"))

label1 = Label(root,text="Vikas-Chatbox", font=("Arial", 12))
label1.pack()

listbox = Listbox(root)
listbox.pack()

label2 = Label(root,text="Type Message", font=("Arial", 10))
label2.pack()

entry = Entry()
entry.pack()

button = Button(root,text="SEND", command=lambda :send(listbox, entry))
button.pack()

rbutton = Button(root,text="RECEIVE", command=lambda :receive(listbox))
rbutton.pack()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
port = 8010
s.bind((HOST, port))

s.listen(4) # Number of connection to be accepted before refused.
client, addr = s.accept()

root.mainloop()


