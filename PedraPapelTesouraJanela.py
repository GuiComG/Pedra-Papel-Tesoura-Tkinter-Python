from tkinter import *
import random
from tkinter.font import *


root = Tk()
root.configure(bg="lightblue")
root.title("Pedra Papel Tesoura")
val = IntVar()
ready = Font(family="Press Start 2P", size=12, weight="bold", slant="roman")
readytext = Font(family="Press Start 2P", size=8, weight="normal", slant="roman")
readybutton = Font(family="Press Start 2P", size=6, weight="normal", slant="roman")
label = Label(root, text = "Escolha Pedra, Papel ou Tesoura!", bg="lightblue", font=readytext)
rock = Radiobutton(root, text = "Pedra", variable=val, value=1, bg="lightblue", font=readybutton)
paper = Radiobutton(root, text = "Papel", variable=val, value=2, bg="lightblue", font=readybutton)
scissors = Radiobutton(root, text = "Tesoura", variable=val, value=3, bg="lightblue", font=readybutton)
def Inserir():
    v = val.get()
    rand = random.randint(1, 3)
    botchoice = ""
    if rand == 1:
        botchoice = "Pedra"
    if rand == 2:
        botchoice = "Papel"
    if rand == 3:
        botchoice = "Tesoura"
    if v == rand:
        label.config(text=("Escolhi... %s, Empate!" %(botchoice)))
    if v == 1 and rand == 2 or v == 2 and rand == 3 or v == 3 and rand == 1:
        label.config(text=("Escolhi... %s, Ganhei!" %(botchoice)))
    if rand == 1 and v == 2 or rand == 2 and v == 3 or rand == 3 and v == 1:
        label.config(text=("Escolhi... %s, Você ganhou!" %(botchoice)))
        

root.minsize(353, 125)
root.maxsize(353, 125)
root.resizable(False, False)
btn = Button(root, text ="Inserir", command=Inserir, activebackground="red", activeforeground="white", overrelief=RIDGE, highlightcolor="black", bg="blue", fg="white", font=ready)
label.grid(row=1, column=0)
rock.grid(row=2, column=0)
paper.grid(row=3, column=0)
scissors.grid(row=4, column=0)
btn.grid(row=5, column=0)


root.mainloop()
