#Calculator
from tkinter import *
from tkinter import messagebox


operator = ''
length = len(operator[:-1])

def btnClicked(numbers):
    try:
        global operator
        operator += str(numbers)
        text_var.set(operator)
    except:
        text_var.set('Math Error')

def equal():
    try:
        global operator
        equal = str(eval(operator))
        text_var.set(equal)
    except:
        text_var.set('Math Error')

def clear_all():
    global operator
    operator = ''
    text_var.set('')

def percentage_sign():
    global operator
    try:
        num = text_var.get()
        operator = int(num) / 100
        text_var.set(operator)
    except:
        return
    pass

if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    root.geometry('520x800+550+100')
    root.resizable(False,False)
    root.config(bg='#1A2030')

    icon = PhotoImage(file='icon.png')
    root.iconphoto(False,icon)
    
    Entry
    text_var = StringVar()
    text_field = Entry(root, bg='#1A2030', fg='white', font='Calculas 70', bd=0, textvariable=text_var, justify='right')
    text_field.place(x=0,y=0, width=525, height=300)

    Button(root, text='0', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(0), cursor='hand2').place(x=0, y=700, width=260, height=100)
    Button(root, text='.', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked('.'), cursor='hand2').place(x=260, y=700, width=130, height=100)
    Button(root, text='=', font=('digital-7', '70'), bg='darkcyan', fg='white', bd=1, command= equal, cursor='hand2').place(x=390, y=600, width=130, height=200)

    Button(root, text='1', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(1), cursor='hand2').place(x=0, y=600, width=130, height=100)
    Button(root, text='2', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(2), cursor='hand2').place(x=130, y=600, width=130, height=100)
    Button(root, text='3', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(3), cursor='hand2').place(x=260, y=600, width=130, height=100)
    Button(root, text='+', font=('digital-7', '70'), bg='#2D3245', fg='white', bd=1, command= lambda:btnClicked('+'), cursor='hand2').place(x=390, y=500, width=130, height=100)

    Button(root, text='4', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(4), cursor='hand2').place(x=0, y=500, width=130, height=100)
    Button(root, text='5', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(5), cursor='hand2').place(x=130, y=500, width=130, height=100)
    Button(root, text='6', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(6), cursor='hand2').place(x=260, y=500, width=130, height=100)
    Button(root, text='-', font=('digital-7', '70'), bg='#2D3245', fg='white', bd=1, command= lambda:btnClicked('-'), cursor='hand2').place(x=390, y=400, width=130, height=100)

    Button(root, text='7', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(7), cursor='hand2').place(x=0, y=400, width=130, height=100)
    Button(root, text='8', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(8), cursor='hand2').place(x=130, y=400, width=130, height=100)
    Button(root, text='9', font=('digital-7', '70'), bg='#353A4E', fg='white', bd=1, command= lambda:btnClicked(9), cursor='hand2').place(x=260, y=400, width=130, height=100)
    Button(root, text='x', font=('consolas', '60'), bg='#2D3245', fg='white', bd=1, command= lambda:btnClicked('*'), cursor='hand2').place(x=390, y=300, width=130, height=100)

    Button(root, text='C', font=('Footlight MT Light', '70'), bg='#2D3245', fg='white', bd=1, command=clear_all, cursor='hand2').place(x=0, y=300, width=130, height=100)
    Button(root, text='÷', font=('Footlight MT Light', '70'), bg='#2D3245', fg='white', bd=1, command=lambda:btnClicked('/'), cursor='hand2').place(x=130, y=300, width=130, height=100)
    Button(root, text='%', font=('Footlight MT Light', '70'), bg='#2D3245', fg='white', bd=1, command=percentage_sign, cursor='hand2').place(x=260, y=300, width=130, height=100)
    
    root.mainloop()