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
        self.textbox_in_cond = ttk.Entry(self._frame2, width=20)
        self.textbox_bound_cond_a = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)
        self.textbox_bound_cond_b = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)

        self.textbox_a.place(x=53, y=23)
        self.textbox_b.place(x=53, y=49)
        self.textbox_h.place(x=53, y=75)
        self.textbox_t_max.place(x=53, y=101)
        self.textbox_in_cond.place(x=53, y=154)
        self.textbox_bound_cond_a.place(x=53, y=204)
        self.textbox_bound_cond_b.place(x=53, y=230)

        self.textbox_a.insert(0, '0')
        self.textbox_b.insert(0, '1')
        self.textbox_h.insert(0, '0.02')
        self.textbox_t_max.insert(0, '0.3')
        self.textbox_in_cond.insert(0, '1-x')
        self.textbox_bound_cond_a.insert(0, '0')
        self.textbox_bound_cond_b.insert(0, '0')

        self.textbox_a.bind('<Return>', self.btn_click)
        self.textbox_b.bind('<Return>', self.btn_click)
        self.textbox_h.bind('<Return>', self.btn_click)
        self.textbox_t_max.bind('<Return>', self.btn_click)
        self.textbox_in_cond.bind('<Return>', self.btn_click)
        self.textbox_bound_cond_a.bind('<Return>', self.btn_click)
        self.textbox_bound_cond_b.bind('<Return>', self.btn_click)

    def _create_labels(self):
        self.label_a = tk.Label(self._frame2, text='a', background='ghostwhite')
        self.label_b = tk.Label(self._frame2, text='b', background='ghostwhite')
        self.label_h = tk.Label(self._frame2, text='h', background='ghostwhite')
        self.label_t_max = tk.Label(self._frame2, text='t max', background='ghostwhite')
        self.label_in_cond = tk.Label(self._frame2, text='НУ', background='ghostwhite')
        self.label_bound_cond_a = tk.Label(self._frame2, text='T a', background='ghostwhite')
        self.label_bound_cond_b = tk.Label(self._frame2, text='T b', background='ghostwhite')

        self.label_a.place(x=15, y=23)
        self.label_b.place(x=15, y=49)
        self.label_h.place(x=15, y=75)
        self.label_t_max.place(x=15, y=101)
        self.label_in_cond.place(x=15, y=154)
        self.label_bound_cond_a.place(x=15, y=204)
        self.label_bound_cond_b.place(x=15, y=230)

    def _create_buttons(self):
        self.btn = ttk.Button(self._frame2, text='Вычислить', width=20, command=self.btn_click)
        self.btn.place(x=51, y=260)

    def get_parameters(self) -> Parameters | None:
        try:
            a = int(self.textbox_a.get())
            b = int(self.textbox_b.get())
            h = float(self.textbox_h.get())
            t_max = float(self.textbox_t_max.get())
            T_a = float(self.textbox_bound_cond_a.get())
            T_b = float(self.textbox_bound_cond_b.get())
        except ValueError:
            return

        T0_expr = self.textbox_in_cond.get()

        if b <= a:
            return

        # return Parameters(a, b, h, t_max, T0_expr, T_a, T_b)
        return Parameters()

    def btn_click(self, e=None):
        if params := self.get_parameters():
            self.graph.clear()

            x = params.x
            t = list(np.arange(0, params.t_max + params.tau, params.tau))
            u = wave_equation(params)
            # self.graph.draw3d(x, t, u, color='#b7ddfe')
            # self.graph.draw2d(x, u[100])
            # print(len(t))

            # self.graph.draw(x, t, u)
            # try:
            #     self.graph.draw(x, t, T, cmap=plt.cm.coolwarm)
            # except ValueError:
            #     messagebox.showerror(':`(', 'Incorrect t max or h')
            # self._canvas.draw()
            plt.ion()
            line = self.graph.draw2d(x, u[0], color='black')
            for layer in u:
                # self.graph.clear()
                line.set_ydata(layer)
                plt.gcf().canvas.flush_events()
            plt.ioff()
            self._canvas.draw()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    form = Form()
    form.run()
