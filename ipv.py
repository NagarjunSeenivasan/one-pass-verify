import math
import random
import array
from random import sample
import tkinter as tk
import messagebox
import winsound


num = ['0','1','2','4','5','6','7','8','9']

symbols = ['+', '-', '*', '/','*','&']

s_l =['a','b','c','d','e','f','g','h','i','j','k','l','m']

A_l =['A','B','C','D','E','F','G','H','I','J','K','L','M']

length = 10

random_num =random.choice(num)
random_symbols = random.choice(symbols)
random_s_l = random.choice(s_l)
random_A_l= random.choice(A_l)

add_all = num + symbols + s_l + A_l
add_random = random_num + random_symbols + random_s_l + random_A_l

for i in range(length - 4):
    add_random += random.choice(add_all)
    

print(add_random)    

win = tk.Tk()
win.geometry('600x400')

user_var = tk.StringVar()
pass_var = tk.StringVar()

def click():
    username = user_var.get()
    password = pass_var.get()
    frequency = 2000
    duration = 1500

    print('username:'+ username)
    print('paaswd:'+ password)

    if username == 'arjun':
        if password == add_random:
            messagebox.showinfo('login','login successfully')
        else:
            messagebox.showerror('error',"wrong password")
            for i in range (10):
                winsound.Beep(frequency,duration)
    else:
        messagebox.showerror("Error", "User not found.")
        for i in range (10):
             winsound.Beep(frequency,duration)

la1 = tk.Label(win,text='username:',padx=20,pady=20)
la1.grid(row=1,column=2)

el1 = tk.Entry(win,width=20,textvariable = user_var)
el1.grid(row=1,column=3)

la2 = tk.Label(win,text='password:',padx=20,pady=20)
la2.grid(row=2,column=2)

el2 = tk.Entry(win,width=20,textvariable=pass_var,show='*')
el2.grid(row=2,column=3)

sub = tk.Button(win,text='submit',command=click)
sub.grid(row=3,column=2)

win.mainloop()