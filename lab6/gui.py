import re
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from equation import poisson_equation
from graph import Graph
from parameters import Parameters


class Form:
    def __init__(self):
        self.fig = plt.figure(facecolor='ghostwhite')

        # self.style = ttk.Style()
        self._init_root()
        self._create_text_boxes()
        self._create_labels()
        self._create_buttons()

        self.graph = Graph(self.fig, title='Решение уравнения Пуассона')

    def _init_root(self):
        self.root = tk.Tk()
        self.root.wm_title('Уравнение Пуассона')
        self.root.geometry('816x489')
        self.root.config(background='ghostwhite')
        self.root.protocol("WM_DELETE_WINDOW", lambda: (self.root.destroy(), plt.close()))

        self._frame1 = tk.Frame(self.root, bg='ghostwhite')
        self._frame1.place(x=0, y=0, relwidth=0.75, relheight=1)

        self._canvas = FigureCanvasTkAgg(self.fig, master=self._frame1)
        self._canvas.get_tk_widget().place(x=0, y=0, relwidth=1, relheight=0.9)

        self._toolbar = NavigationToolbar2Tk(self._canvas, self.root)
        # self._toolbar.config(background='ghostwhite', padx=8, highlightbackground='red', width=1)
        # self._toolbar._message_label.config(background='ghostwhite')
        self._toolbar.update()

        self._frame2 = tk.Frame(self.root, bg='ghostwhite')
        self._frame2.place(relx=0.75, y=0, relwidth=0.25, relheight=0.9)

    def _create_text_boxes(self):
        # self.style.configure("TEntry", foreground="black", background="red")
        check_int = (self.root.register(lambda x: re.match(r'^(-|\d*)\d*$', x) is not None), "%P")
        check_float = (self.root.register(lambda x: re.match(r'^(-|\d*)\d*(\.|\d*)\d*$', x) is not None), "%P")
        self.textbox_a_x = ttk.Entry(self._frame2, background='ghostwhite', width=20, validate='key',
                                   validatecommand=check_int)
        self.textbox_b_x = ttk.Entry(self._frame2, background='ghostwhite', width=20, validate='key',
                                   validatecommand=check_int)
        self.textbox_a_y = ttk.Entry(self._frame2, background='ghostwhite', width=20, validate='key',
                                     validatecommand=check_int)
        self.textbox_b_y = ttk.Entry(self._frame2, background='ghostwhite', width=20, validate='key',
                                     validatecommand=check_int)
        self.textbox_h = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)
        self.textbox_e = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)


        self.textbox_a_x.place(x=60, y=23)
        self.textbox_b_x.place(x=60, y=49)
        self.textbox_a_y.place(x=60, y=75)
        self.textbox_b_y.place(x=60, y=101)
        self.textbox_h.place(x=60, y=127)
        self.textbox_e.place(x=60, y=153)

        self.textbox_a_x.insert(0, '0')
        self.textbox_b_x.insert(0, '1')
        self.textbox_a_y.insert(0, '0')
        self.textbox_b_y.insert(0, '1')
        self.textbox_h.insert(0, '0.05')
        self.textbox_e.insert(0, '0.001')

        self.textbox_a_x.bind('<Return>', self.btn_click)
        self.textbox_b_x.bind('<Return>', self.btn_click)
        self.textbox_a_y.bind('<Return>', self.btn_click)
        self.textbox_b_y.bind('<Return>', self.btn_click)
        self.textbox_h.bind('<Return>', self.btn_click)
        self.textbox_e.bind('<Return>', self.btn_click)

    def _create_labels(self):
        self.label_a_x = tk.Label(self._frame2, text='Лево', background='ghostwhite')
        self.label_b_x = tk.Label(self._frame2, text='Право', background='ghostwhite')
        self.label_a_y = tk.Label(self._frame2, text='Низ', background='ghostwhite')
        self.label_b_y = tk.Label(self._frame2, text='Верх', background='ghostwhite')
        self.label_h = tk.Label(self._frame2, text='Шаг', background='ghostwhite')
        self.label_e = tk.Label(self._frame2, text='Точность', background='ghostwhite')

        self.label_a_x.place(x=0, y=23)
        self.label_b_x.place(x=0, y=49)
        self.label_a_y.place(x=0, y=75)
        self.label_b_y.place(x=0, y=101)
        self.label_h.place(x=0, y=127)
        self.label_e.place(x=0, y=153)

    def _create_buttons(self):
        self.btn = ttk.Button(self._frame2, text='Вычислить', width=20, command=self.btn_click)
        self.btn.place(x=51, y=286)

    def get_parameters(self) -> Parameters | None:
        try:
            a_x = int(self.textbox_a_x.get())
            b_x = int(self.textbox_b_x.get())
            a_y = int(self.textbox_a_y.get())
            b_y = int(self.textbox_b_y.get())
            h = float(self.textbox_h.get())
            e = float(self.textbox_e.get())
        except ValueError:
            return

        if b_x <= a_x or b_y <= a_y:
            return

        return Parameters(a_x, b_x, a_y, b_y, h, e)
        # return Parameters()

    def btn_click(self, e=None):
        if params := self.get_parameters():
            self.graph.clear()

            x = params.x[1:-1]
            y = params.y[1:-1]
            u = poisson_equation(params)
            u = [_u[1:-1] for _u in u[1:-1]]
            self.graph.draw(x, y, u, levels=60, cmap=plt.cm.magma)
            self._canvas.draw()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    form = Form()
    form.run()
