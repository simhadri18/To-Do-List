import tkinter
from tkinter import*
def date():
    task=date1.get()
    listbox.insert(END,task)
    date1.delete(0,END)



def add():
    task=entry.get()
    if task:
        listbox.insert(END,entry.get())
        entry.delete(0,END)
        
def remove():
    listbox.delete(ANCHOR)


def mark():
    try:
        result=listbox.curselection()[0]
        listbox.itemconfig(result,bg="sky blue")
    except IndexError:
        pass

root=Tk()

root.title("TO-DO-LIST-APP")
root.geometry("410x650+400+100")
root.resizable(False,False)


text=Label(root,text="📓  ADD LIST",width=30,font=("Arial",25,"bold"),bg="gray",relief=SUNKEN,fg="white")
text.pack()
label=Label(root,text="Enter Today Date:",font=("arial",10,"bold"))
label.place(x=5,y=50)

date1=Entry(root)
date1.place(x=130,y=50)

button=Button(root,text="Add Date",command=date,width=8)
button.place(x=270,y=50)

entry=Entry(root,font=("arial",15),width=28,bd=5,bg="#93ff75",relief=SUNKEN)
entry.place(x=0,y=80)

button=Button(text="ADD",font=("arial",10,"bold"),command=add,width=10,bd=6,bg="#de9bce")
button.place(x=320,y=80)


frame1=LabelFrame(root,text="this is my text",bd=3,width=700,height=280,bg="#fff875")
frame1.pack(pady=(95,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg='white')
listbox.pack(side=LEFT,fill=BOTH)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


button1=Button(text="❎  Clear The File",bg="#6970c2",command=remove,bd=5,relief=RAISED,width=27,font=("arial",12,"bold"))
button1.place(x=60,y=490)

button1=Button(text="☑️  Mark As Read",bg="sky blue",command=mark,bd=5,relief=RAISED,width=27,font=("arial",12,"bold"))
button1.place(x=60,y=540)


label=Label(text="Thank you...🥰",bd=5,width=27,font=("arial",18,"bold"))
label.place(x=10,y=590)

root.mainloop()