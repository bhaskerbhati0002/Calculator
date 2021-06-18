from tkinter import *

root = Tk()


root.title('BHASKER calculator')
root.iconbitmap('calculator.ico')
root.geometry('278x285')
root.configure(bg='black')


e=Entry(root,fg='black',font='lucida 20 bold',bg='grey',width=17,borderwidth=10)
e.grid(row=0,column=0,columnspan=4)


def mybutton(n):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(n))
global operation
operation='null'

def percentage():
    global first_num
    first_num=float(e.get())
    e.delete(0,END)
    global operation
    operation = 'percentage'

def addition():
    global first_num
    first_num=float(e.get())
    e.delete(0,END)
    global operation
    operation = 'addition'

def subtraction():
    global first_num
    first_num=float(e.get())
    e.delete(0,END)
    global operation
    operation = 'subtraction'

def multiplication():
    global first_num
    first_num=float(e.get())
    e.delete(0,END)
    global operation
    operation = 'multiplication'

def division():
    global first_num
    first_num=float(e.get())
    e.delete(0,END)
    global operation
    operation='division'

def equal():
    second_num=float(e.get())
    e.delete(0,END)
    if (operation=='addition'):
        e.insert(0,first_num+second_num)
    elif(operation=='subtraction'):
        e.insert(0, first_num - second_num)
    elif(operation=='multiplication'):
        e.insert(0, first_num * second_num)
    elif(operation=='percentage'):
        prcnt=(first_num * (second_num/100))
        e.insert(0,prcnt)
    else:
        e.insert(0, first_num / second_num)


def clearbutton():
    e.delete(0,END)


button_clear=Button(root,padx=25,pady=10,borderwidth=3,text='C',command=clearbutton,bg='red',font='lucida 9 bold italic',fg='white')
button_percentage=Button(root,padx=25,pady=10,borderwidth=3,text='%',command=percentage,font='lucida 9',fg='white',bg='blue')
button_division=Button(root,padx=25,pady=10,borderwidth=3,text='/',command=division,font='lucida 9 bold italic',fg='white',bg='blue')
button_equal=Button(root,padx=57,pady=10,borderwidth=3,text='=',command=equal,font='lucida 9 bold italic',fg='white',bg='dark violet')
button_7=Button(root,padx=25,pady=10,borderwidth=3,text='7',command=lambda: mybutton(7),font='lucida 9 bold italic',fg='white',bg='black')
button_8=Button(root,padx=25,pady=10,borderwidth=3,text='8',command=lambda: mybutton(8),font='lucida 9 bold italic',fg='white',bg='black')
button_9=Button(root,padx=25,pady=10,borderwidth=3,text='9',command=lambda: mybutton(9),font='lucida 9 bold italic',fg='white',bg='black')
button_multiply=Button(root,padx=24,pady=10,borderwidth=3,text='*',command=multiplication,font='lucida 9 bold italic',fg='white',bg='blue')
button_4=Button(root,padx=25,pady=10,borderwidth=3,text='4',command=lambda: mybutton(4),font='lucida 9 bold italic',fg='white',bg='black')
button_5=Button(root,padx=25,pady=10,borderwidth=3,text='5',command=lambda: mybutton(5),font='lucida 9 bold italic',fg='white',bg='black')
button_6=Button(root,padx=25,pady=10,borderwidth=3,text='6',command=lambda: mybutton(6),font='lucida 9 bold italic',fg='white',bg='black')
button_subtract=Button(root,padx=24,pady=10,borderwidth=3,text='-',command=subtraction,font='lucida 9 bold italic',fg='white',bg='blue')
button_1=Button(root,padx=25,pady=10,borderwidth=3,text='1',command=lambda: mybutton(1),font='lucida 9 bold italic',fg='white',bg='black')
button_2=Button(root,padx=25,pady=10,borderwidth=3,text='2',command=lambda: mybutton(2),font='lucida 9 bold italic',fg='white',bg='black')
button_3=Button(root,padx=25,pady=10,borderwidth=3,text='3',command=lambda: mybutton(3),font='lucida 9 bold italic',fg='white',bg='black')
button_addition=Button(root,padx=23,pady=10,borderwidth=3,text='+',command=addition,font='lucida 9 bold italic',fg='white',bg='blue')
button_0=Button(root,padx=60,pady=10,borderwidth=3,text='0',command=lambda: mybutton(0),font='lucida 9 bold italic',fg='white',bg='black')
button_exit=Button(root,padx=25,pady=10,borderwidth=3,text='E',command=root.quit,bg='red',font='lucida 9 bold italic',fg='white')


button_clear.grid(row=1,column=0)
button_percentage.grid(row=1,column=2)
button_equal.grid(row=5,column=2,columnspan=2)
button_division.grid(row=1,column=3)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_multiply.grid(row=2,column=3)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_subtract.grid(row=3,column=3)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_addition.grid(row=4,column=3)
button_0.grid(row=5,column=0,columnspan=2)
button_exit.grid(row=1,column=1)

root.mainloop()
