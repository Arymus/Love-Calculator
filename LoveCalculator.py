import tkinter
import random

root = tkinter.Tk()
root.title("Love Calculator ♡")
root.geometry("600x600")
root.configure(bg = "pink")
def calulate_love():
    st = "0123456789"
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.configure(text = temp)
heading = tkinter.Label(root, text = "Love Calculator ♡", bg = "pink")
heading.pack()
slot_1 = tkinter.Label(root, text = "Enter your name here:", bg = "pink")
slot_1.pack()
name_1 = tkinter.Entry(root, border = 5)
name_1.pack()
slot_2 = tkinter.Label(root, text = "Enter your partner's name here:", bg = "pink")
slot_2.pack()
name_2 = tkinter.Entry(root, border = 5)
name_2.pack()
button = tkinter.Button(root, bg = "white", text = "Calculate!", command = calulate_love)
button.pack()
result = tkinter.Label(root, text = "Your love percentage:", bg = "pink")
result.pack()
root.mainloop()