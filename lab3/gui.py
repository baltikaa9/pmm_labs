import re
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from equation import wave_equation
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

        self.graph = Graph(self.fig, title='Волновое уравнение')

    def _init_root(self):
        self.root = tk.Tk()
        self.root.wm_title('Волновое уравнение')
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
        self.textbox_a = ttk.Entry(self._frame2, background='ghostwhite', width=20, validate='key',
                                   validatecommand=check_int)
        self.textbox_b = ttk.Entry(self._frame2, background='ghostwhite', width=20, validate='key',
                                   validatecommand=check_int)
        self.textbox_h = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)
        self.textbox_t_max = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)
        self.textbox_in_cond_1 = ttk.Entry(self._frame2, width=20)
        self.textbox_in_cond_2 = ttk.Entry(self._frame2, width=20)
        self.textbox_bound_cond_a = ttk.Entry(self._frame2, width=20)
        self.textbox_bound_cond_b = ttk.Entry(self._frame2, width=20)

        self.textbox_a.place(x=53, y=23)
        self.textbox_b.place(x=53, y=49)
        self.textbox_h.place(x=53, y=75)
        self.textbox_t_max.place(x=53, y=101)
        self.textbox_in_cond_1.place(x=53, y=154)
        self.textbox_in_cond_2.place(x=53, y=180)
        self.textbox_bound_cond_a.place(x=53, y=230)
        self.textbox_bound_cond_b.place(x=53, y=256)

        self.textbox_a.insert(0, '0')
        self.textbox_b.insert(0, '1')
        self.textbox_h.insert(0, '0.02')
        self.textbox_t_max.insert(0, '30')
        self.textbox_in_cond_1.insert(0, '0')
        self.textbox_in_cond_2.insert(0, '0')
        self.textbox_bound_cond_a.insert(0, '0')
        self.textbox_bound_cond_b.insert(0, 't * exp(-t)')

        self.textbox_a.bind('<Return>', self.btn_click)
        self.textbox_b.bind('<Return>', self.btn_click)
        self.textbox_h.bind('<Return>', self.btn_click)
        self.textbox_t_max.bind('<Return>', self.btn_click)
        self.textbox_in_cond_1.bind('<Return>', self.btn_click)
        self.textbox_in_cond_2.bind('<Return>', self.btn_click)
        self.textbox_bound_cond_a.bind('<Return>', self.btn_click)
        self.textbox_bound_cond_b.bind('<Return>', self.btn_click)

    def _create_labels(self):
        self.label_a = tk.Label(self._frame2, text='a', background='ghostwhite')
        self.label_b = tk.Label(self._frame2, text='b', background='ghostwhite')
        self.label_h = tk.Label(self._frame2, text='h', background='ghostwhite')
        self.label_t_max = tk.Label(self._frame2, text='t max', background='ghostwhite')
        self.label_in_cond_1 = tk.Label(self._frame2, text='НУ 1', background='ghostwhite')
        self.label_in_cond_2 = tk.Label(self._frame2, text='НУ 2', background='ghostwhite')
        self.label_bound_cond_a = tk.Label(self._frame2, text='ГУ 1', background='ghostwhite')
        self.label_bound_cond_b = tk.Label(self._frame2, text='ГУ 2', background='ghostwhite')

        self.label_a.place(x=15, y=23)
        self.label_b.place(x=15, y=49)
        self.label_h.place(x=15, y=75)
        self.label_t_max.place(x=15, y=101)
        self.label_in_cond_1.place(x=15, y=154)
        self.label_in_cond_2.place(x=15, y=180)
        self.label_bound_cond_a.place(x=15, y=230)
        self.label_bound_cond_b.place(x=15, y=256)

    def _create_buttons(self):
        self.btn = ttk.Button(self._frame2, text='Вычислить', width=20, command=self.btn_click)
        self.btn.place(x=51, y=290)

    def get_parameters(self) -> Parameters | None:
        try:
            a = int(self.textbox_a.get())
            b = int(self.textbox_b.get())
            h = float(self.textbox_h.get())
            t_max = float(self.textbox_t_max.get())
        except ValueError:
            return

        init_cond_1 = self.textbox_in_cond_1.get()
        init_cond_2 = self.textbox_in_cond_2.get()
        left_bound = self.textbox_bound_cond_a.get()
        right_bound = self.textbox_bound_cond_b.get()

        if b <= a:
            return

        return Parameters(a, b, h, t_max, init_cond_1, init_cond_2, left_bound, right_bound)
        # return Parameters()

    def btn_click(self, e=None):
        if params := self.get_parameters():
            self.graph.clear()

            x = params.x
            u = wave_equation(params)

            with plt.ion():
                line = self.graph.draw2d(x, u[0], color='black')
                for layer in u:
                    # self.graph.clear()
                    line.set_ydata(layer)
                    plt.gcf().canvas.flush_events()
            self._canvas.draw()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    form = Form()
    form.run()
