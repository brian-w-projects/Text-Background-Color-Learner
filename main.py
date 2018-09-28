from tkinter import *
from random import randint
import numpy as np
from prediction import train_model
from pandas import DataFrame


def rgb():
    return "{:02x}".format(randint(0, 255))


def combo_painter():
    w.create_rectangle(0, 0, 400, 400, fill=f"#{''.join(list(choices[-1, 0:3]))}")
    w.create_rectangle(0, 0, 25, 25, fill='#ffffff')
    w.create_text((12, 12), text=f'{len(choices)}')
    w.create_text((200, 100), font=('Courier', 40), text="Number 1", fill=f'#{first_color}')
    w.create_text((200, 300), font=('Courier', 40), text="Number 2", fill=f'#{second_color}')


def results_display(model):
    colors = DataFrame(np.array([rgb() for _ in range(30)]).reshape(10, 3))
    results = model.predict(colors)
    print(results)
    for i in range(0, 10):
        w.create_rectangle(0, i*40, 400, i*40+40, fill=f"#{''.join(list(colors.iloc[i, :]))}")
        if results[i] == '0':
            w.create_text((100, i*40+20), font=('Courier', 16), text='Preference', fill=f'#{first_color}')
            w.create_text((300, i*40+20), font=('Courier', 16), text='Alternative', fill=f'#{second_color}')
        else:
            w.create_text((100, i*40+20), font=('Courier', 16), text='Preference', fill=f'#{second_color}')
            w.create_text((300, i*40+20), font=('Courier', 16), text='Alternative', fill=f'#{first_color}')


def action(selection):
    global choices

    choices[-1, -1] = selection
    if len(choices) == 100:
        w.create_rectangle(0, 0, 400, 400, fill="#000000")
        model = train_model(DataFrame(choices))
        results_display(model)
    elif len(choices) > 100:
        exit(0)
    else:
        choices = np.concatenate([choices, np.array([[rgb(), rgb(), rgb(), 'X']])])
        combo_painter()

if __name__ == '__main__':
    choices = np.array([[rgb(), rgb(), rgb(), 'X']])
    color_base = [rgb(), rgb(), rgb()]
    first_color = ''.join(color_base)
    second_color = ''.join(["{:02x}".format(255 - int(i, 16)) for i in color_base])

    master = Tk()
    w = Canvas(master, width=400, height=400)
    w.pack()
    b = Button(master, text='Number 1', command=lambda: action('0'))
    b2 = Button(master, text='Number 2', command=lambda: action('1'))
    b.pack(side='left')
    b2.pack(side='right')
    combo_painter()
    w.mainloop()