import re
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from equation import impurities_transfer
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

        self.graph = Graph(self.fig, title='Перенос примесей')

    def _init_root(self):
        self.root = tk.Tk()
        self.root.wm_title('Перенос примесей')
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
        self.textbox_c = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_int)
        self.textbox_d = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_int)
        self.textbox_c_ang = ttk.Entry(self._frame2, width=20)
        self.textbox_t_max = ttk.Entry(self._frame2, width=20, validate='key', validatecommand=check_float)

        self.textbox_c.place(x=53, y=23)
        self.textbox_c_ang.place(x=53, y=49)
        self.textbox_d.place(x=53, y=75)
        self.textbox_t_max.place(x=53, y=101)

        self.textbox_c.insert(0, '10')
        self.textbox_d.insert(0, '10')
        self.textbox_c_ang.insert(0, 'pi/4')
        self.textbox_t_max.insert(0, '10')

        self.textbox_c.bind('<Return>', self.btn_click)
        self.textbox_d.bind('<Return>', self.btn_click)
        self.textbox_c_ang.bind('<Return>', self.btn_click)
        self.textbox_t_max.bind('<Return>', self.btn_click)

    def _create_labels(self):
        self.label_c = tk.Label(self._frame2, text='C', background='ghostwhite')
        self.label_d = tk.Label(self._frame2, text='Angle', background='ghostwhite')
        self.label_c_ang = tk.Label(self._frame2, text='D', background='ghostwhite')
        self.label_t_max = tk.Label(self._frame2, text='t max', background='ghostwhite')

        self.label_c.place(x=15, y=23)
        self.label_d.place(x=15, y=49)
        self.label_c_ang.place(x=15, y=75)
        self.label_t_max.place(x=15, y=101)

    def _create_buttons(self):
        self.btn = ttk.Button(self._frame2, text='Вычислить', width=20, command=self.btn_click)
        self.btn.place(x=51, y=290)

    def get_parameters(self) -> Parameters | None:
        try:
            c = int(self.textbox_c.get())
            d = int(self.textbox_d.get())
            c_angle = self.textbox_c_ang.get()
            t_max = float(self.textbox_t_max.get())
        except ValueError:
            return

        return Parameters(C=c, C_angle=c_angle, D=d, t_max=t_max)
        # return Parameters()

    def btn_click(self, e=None):
        if params := self.get_parameters():
            self.graph.clear()

            p = impurities_transfer(params)

            for i in range(len(params.x)):
                for j in range(len(params.y)):
                    print(f'{params.x[i]=}, {params.y[j]=}, {p[i][j]=}')

            self.graph.contour(params.x, params.y, p)
            self._canvas.draw()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    form = Form()
    form.run()
