from tkinter import*
from tkinter import ttk


def input_num(text):
    calc_entry.insert(END, text)
    return


def del_num():
    calc_entry.delete(0, END)
    return


def neg_num():
    calc_entry.insert(0, '-')


def res():
    c = calc_entry.get().split()
    try:
        if len(c) <= 3:
            if '+' in c:
                result = float(c[0]) + float(c[2])
                calc_entry.insert(END, f' = {round(result, 3)}')
            elif '-' in c:
                result = float(c[0]) - float(c[2])
                calc_entry.insert(END, f' = {round(result, 3)}')
            elif 'x' in c:
                result = float(c[0]) * float(c[2])
                calc_entry.insert(END, f' = {round(result, 3)}')
            elif '/' in c:
                result = float(c[0]) / float(c[2])
                calc_entry.insert(END, f' = {round(result, 3)}')
            elif '^' in c:
                result = float(c[0]) ** float(c[2])
                calc_entry.insert(END, f' = {round(result, 3)}')
            else:
                calc_entry.insert(END, f' = {round(float(c[0]), 3)}')
        else:
            calc_entry.delete(0, END)
    except ValueError:
        calc_entry.insert(END, f' ОШИБКА')


root = Tk()
root.geometry('430x342')
root.resizable(height=False, width=False)
root.title('Калькулятор')
root.iconphoto(True, PhotoImage(file='icon.png'))
frame_ent = Frame(root)
frame_ent.pack()
calc_entry = Entry(frame_ent, width=22, font=('Colibri', 25))
calc_entry.grid(row=0, column=0, ipadx=20, ipady=20)

frame_button = Frame(root)
frame_button.pack()
button_N1 = ttk.Button(frame_button, text='1', command=lambda: input_num(1))
button_N1.grid(row=0, column=0, ipadx=5, ipady=20)


button_N2 = ttk.Button(frame_button, text='2', command=lambda: input_num(2))
button_N2.grid(row=0, column=1, ipadx=5, ipady=20)

button_N3 = ttk.Button(frame_button, text='3', command=lambda: input_num(3))
button_N3.grid(row=0, column=2, ipadx=5, ipady=20)

button_del = ttk.Button(frame_button, text='AC', command=del_num)
button_del.grid(row=0, column=3, ipadx=5, ipady=20)

button_proc = ttk.Button(frame_button, text='^x', command=lambda: input_num(' ^ '))
button_proc.grid(row=0, column=4, ipadx=5, ipady=20)

frame_but2 = Frame(root)
frame_but2.pack()
button_N4 = ttk.Button(frame_but2, text='4', command=lambda: input_num(4))
button_N4.grid(row=0, column=0, ipadx=5, ipady=20)

button_N5 = ttk.Button(frame_but2, text='5', command=lambda: input_num(5))
button_N5.grid(row=0, column=1, ipadx=5, ipady=20)

button_N6 = ttk.Button(frame_but2, text='6', command=lambda: input_num(6))
button_N6.grid(row=0, column=2, ipadx=5, ipady=20)

button_sum = ttk.Button(frame_but2, text='+', command=lambda: input_num(' + '))
button_sum.grid(row=0, column=3, ipadx=5, ipady=20)

button_mult = ttk.Button(frame_but2, text='x', command=lambda: input_num(' x '))
button_mult.grid(row=0, column=4, ipadx=5, ipady=20)

frame_but3 = Frame(root)
frame_but3.pack()
button_N7 = ttk.Button(frame_but3, text='7', command=lambda: input_num(7))
button_N7.grid(row=0, column=0, ipadx=5, ipady=20)

button_N8 = ttk.Button(frame_but3, text='8', command=lambda: input_num(8))
button_N8.grid(row=0, column=1, ipadx=5, ipady=20)

button_N9 = ttk.Button(frame_but3, text='9', command=lambda: input_num(9))
button_N9.grid(row=0, column=2, ipadx=5, ipady=20)

button_min = ttk.Button(frame_but3, text='-', command=lambda: input_num(' - '))
button_min.grid(row=0, column=3, ipadx=5, ipady=20)

button_div = ttk.Button(frame_but3, text='/', command=lambda: input_num(' / '))
button_div.grid(row=0, column=4, ipadx=5, ipady=20)

frame_but4 = Frame(root)
frame_but4.pack()
button_N0 = ttk.Button(frame_but4, text='0', command=lambda: input_num(0))
button_N0.grid(row=0, column=0, ipadx=5, ipady=20)

button_N00 = ttk.Button(frame_but4, text='00', command=lambda: input_num('00'))
button_N00.grid(row=0, column=1, ipadx=5, ipady=20)

button_float = ttk.Button(frame_but4, text='.', command=lambda: input_num('.'))
button_float.grid(row=0, column=2, ipadx=5, ipady=20)

button_res = ttk.Button(frame_but4, text='=', command=res)
button_res.grid(row=0, column=3, ipadx=5, ipady=20)

button_neg = ttk.Button(frame_but4, text='+/-', command=neg_num)
button_neg.grid(row=0, column=4, ipadx=5, ipady=20)
root.mainloop()
