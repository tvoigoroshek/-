from tkinter import *
tk = Tk()
btn=Button(tk,text="Количество: ")
btn.pack()
canvas= Canvas(tk, width=100,height=10)
canvas.pack()
i = 0 
def clicker(m):
    global i
    i = i + 1 
    label['text'] = str(i)
 
btn.bind_all('<Button-1>', clicker)
 
label = Label(tk, text=str(i))
label.pack()
