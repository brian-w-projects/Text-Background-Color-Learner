from tkinter import *
from random import randint
import numpy as np
from prediction import train_model
from pandas import DataFrame
import argparse


def rgb():
    """Returns pseudo-random hex digit

    Returns:
        str: The psuedo-random
    """

    return "{:02x}".format(randint(0, 255))


def combo_painter():
    """Paints the canvas w with the next round of information.

    Returns:
         Nothing
    """

    w.create_rectangle(0, 0, 400, 400, fill=f"#{''.join(list(choices[-1, 0:3]))}")
    w.create_rectangle(0, 0, 40, 25, fill='#ffffff')
    w.create_text((20, 12), text=f'{len(choices)}/{results.iterations}')
    w.create_text((200, 100), font=('Courier', 40), text="Number 1", fill=f'#{results.colors[0]}')
    w.create_text((200, 300), font=('Courier', 40), text="Number 2", fill=f'#{results.colors[1]}')


def waiting_painter():
    """Paints the canvas with the splash screen while the ML algorithm runs.

    Returns:
        Nothing
    """

    w.create_rectangle(0, 0, 400, 400, fill="#000000")
    w.create_text((200, 100), font=('Courier', 40), text="Thank You", fill='#ffffff')
    w.create_text((200, 300), font=('Courier', 40), text="Processing", fill='#ffffff')
    w.update()


def results_display():
    """Trains the ML algorithm, predicts on 10 new colors and displays the results

    Returns:
        Nothing
    """

    colors = DataFrame(np.array([rgb() for _ in range(30)]).reshape(10, 3))
    predictions = train_model(DataFrame(choices)).predict(colors)

    print(predictions)
    for i in range(0, 10):
        w.create_rectangle(0, i*40, 400, i*40+40, fill=f"#{''.join(list(colors.iloc[i, :]))}")
        w.create_text((100, i*40+20), font=('Courier', 16), text='Preference',
                      fill=f'#{results.colors[int(predictions[i])]}'
                      )
        w.create_text((300, i*40+20), font=('Courier', 16), text='Alternative',
                      fill=f'#{results.colors[(int(predictions[i])+1)%2]}'
                      )


def action(selection):
    """Stores user's information and decides next iteration action.

    Args:
        selection (:str:): '0' representing left selection or '1' representing right selection

    Returns:
        Nothing
    """

    global choices

    choices[-1, -1] = selection
    if len(choices) == results.iterations:
        waiting_painter()
        results_display()
    else:
        choices = np.concatenate([choices, np.array([[rgb(), rgb(), rgb(), 'X']])])
        combo_painter()


if __name__ == '__main__':
    color_base = [rgb(), rgb(), rgb()]

    parser = argparse.ArgumentParser(description='Machine Learning Algorithm to Select Appropriate Font Colors')
    parser.add_argument('-c', nargs='*', dest='colors', action='store',
                        default=[''.join(color_base), ''.join(["{:02x}".format(255 - int(i, 16)) for i in color_base])],
                        help='2 len list of font colors to compare. EX: 05ab1b 55abc8. Default is random selection.')
    parser.add_argument('-i', dest='iterations', action='store', type=int,
                        default=100,
                        help='Number of training iterations. Minimum 50. Default is 100.')

    results = parser.parse_args()
    if len(results.colors) != 2:
        raise ValueError(f'Color list must be length 0 or 2 only, not {len(results.colors)}')
    if results.iterations < 50:
        raise ValueError(f'Iterations must be at least 50, not {results.iterations}')

    choices = np.array([[rgb(), rgb(), rgb(), 'X']])

    master = Tk()
    w = Canvas(master, width=400, height=400)
    w.pack()
    Button(master, text='Number 1', command=lambda: action('0')).pack(side='left')
    Button(master, text='Number 2', command=lambda: action('1')).pack(side='right')
    combo_painter()
    w.mainloop()