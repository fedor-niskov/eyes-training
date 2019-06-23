from tkinter import *
from tkinter import messagebox



class App(Tk):


    def __init__(self):

        super(App, self).__init__()
        self.title('Program')

        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=0)

        self.canvas = Canvas(self, bg='black')
        self.canvas.grid(row=0, column=0, sticky=W+E+N+S)

        contr = Frame(self)
        self.controls = contr
        contr.grid(row=1, column=0, sticky=N+S)

        PARAMS = { 'font' : 'courier 20' }
        NUM_WIDTH = 6
        PADX = (0, 15)
        PADY = (5, 5)

        contr.label_x1 = Label(contr, text='X1:', **PARAMS)
        contr.label_x1.grid(row=0, column=0)
        contr.entry_x1 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_x1.grid(row=0, column=1, padx=PADX, pady=PADY)

        contr.label_y1 = Label(contr, text='Y1:', **PARAMS)
        contr.label_y1.grid(row=1, column=0)
        contr.entry_y1 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_y1.grid(row=1, column=1, padx=PADX, pady=PADY)

        contr.label_x2 = Label(contr, text='X2:', **PARAMS)
        contr.label_x2.grid(row=0, column=2)
        contr.entry_x2 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_x2.grid(row=0, column=3, padx=PADX, pady=PADY)

        contr.label_y2 = Label(contr, text='Y2:', **PARAMS)
        contr.label_y2.grid(row=1, column=2)
        contr.entry_y2 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_y2.grid(row=1, column=3, padx=PADX, pady=PADY)
        
        contr.label_x3 = Label(contr, text='X3:', **PARAMS)
        contr.label_x3.grid(row=0, column=4)
        contr.entry_x3 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_x3.grid(row=0, column=5, padx=PADX, pady=PADY)

        contr.label_y3 = Label(contr, text='Y3:', **PARAMS)
        contr.label_y3.grid(row=1, column=4)
        contr.entry_y3 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_y3.grid(row=1, column=5, padx=PADX, pady=PADY)
        
        contr.label_x4 = Label(contr, text='X4:', **PARAMS)
        contr.label_x4.grid(row=0, column=6)
        contr.entry_x4 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_x4.grid(row=0, column=7, padx=PADX, pady=PADY)

        contr.label_y4 = Label(contr, text='Y4:', **PARAMS)
        contr.label_y4.grid(row=1, column=6)
        contr.entry_y4 = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_y4.grid(row=1, column=7, padx=PADX, pady=PADY)

        contr.label_r = Label(contr, text='R:', **PARAMS)
        contr.label_r.grid(row=0, rowspan=2, column=8)
        contr.entry_r = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_r.grid(row=0, rowspan=2, column=9, padx=PADX, pady=PADY)

        contr.label_ppi = Label(contr, text='PPI:', **PARAMS)
        contr.label_ppi.grid(row=0, rowspan=2, column=10)
        contr.entry_ppi = Entry(contr, width=NUM_WIDTH, **PARAMS)
        contr.entry_ppi.grid(row=0, rowspan=2, column=11, padx=PADX, pady=PADY)

        contr.button_paint = Button(contr, text='OK', command=self.paint, **PARAMS)
        contr.button_paint.grid(row=0, rowspan=2, column=12)

        for c in range(contr.size()[0]):
            contr.columnconfigure(index=c, weight=1)
        for r in range(contr.size()[1]):
            contr.rowconfigure(index=r, weight=1)

        contr.entry_x1.insert(0, '-10.00')
        contr.entry_y1.insert(0, '+10.00')
        contr.entry_x2.insert(0, '+10.00')
        contr.entry_y2.insert(0, '+10.00')
        contr.entry_x3.insert(0, '-10.00')
        contr.entry_y3.insert(0, '-10.00')
        contr.entry_x4.insert(0, '+10.00')
        contr.entry_y4.insert(0, '-10.00')
        contr.entry_r.insert(0, '9')
        contr.entry_ppi.insert(0, '130')

        self.update()
        self.update_idletasks()

        self.bind('<Key>', self.key_handler)
        self.bind('<Button-1>', self.unfocus)
        self.bind('<Configure>', lambda event: self.paint())

        self.paint()


    def unfocus(self, event):
        if event.widget.__class__ != Entry:
            self.focus_set()


    def coord_modify(self, entry, d):
        try:
            v = float(entry.get())
            v += d
            entry.delete(0, 'end')
            entry.insert(0, '{:+06.2f}'.format(v))
        except BaseException:
            messagebox.showerror('Error', 'Error!')


    def key_handler(self, event):

        if self.focus_get().__class__ == Entry:
            return

        k = event.keysym.upper()
        contr = self.controls
        
        STEP = 0.10

        if   k == 'W':
            self.coord_modify(self.controls.entry_y1, +STEP)
        elif k == 'A':
            self.coord_modify(self.controls.entry_x1, -STEP)
        elif k == 'S':
            self.coord_modify(self.controls.entry_y1, -STEP)
        elif k == 'D':
            self.coord_modify(self.controls.entry_x1, +STEP)

        elif k == 'K':
            self.coord_modify(self.controls.entry_y3, +STEP)
        elif k == 'H':
            self.coord_modify(self.controls.entry_x3, -STEP)
        elif k == 'J':
            self.coord_modify(self.controls.entry_y3, -STEP)
        elif k == 'L':
            self.coord_modify(self.controls.entry_x3, +STEP)

        elif k == 'UP':
            self.coord_modify(self.controls.entry_y4, +STEP)
        elif k == 'LEFT':
            self.coord_modify(self.controls.entry_x4, -STEP)
        elif k == 'DOWN':
            self.coord_modify(self.controls.entry_y4, -STEP)
        elif k == 'RIGHT':
            self.coord_modify(self.controls.entry_x4, +STEP)

        elif k == 'KP_UP':
            self.coord_modify(self.controls.entry_y2, +STEP)
        elif k == 'KP_LEFT':
            self.coord_modify(self.controls.entry_x2, -STEP)
        elif k == 'KP_DOWN':
            self.coord_modify(self.controls.entry_y2, -STEP)
        elif k == 'KP_RIGHT':
            self.coord_modify(self.controls.entry_x2, +STEP)
    
        elif k == '8':
            self.coord_modify(self.controls.entry_y2, +STEP)
        elif k == '4':
            self.coord_modify(self.controls.entry_x2, -STEP)
        elif k == '2':
            self.coord_modify(self.controls.entry_y2, -STEP)
        elif k == '6':
            self.coord_modify(self.controls.entry_x2, +STEP)

        elif k == '5':
            self.coord_modify(self.controls.entry_y2, -STEP)
        elif k == 'KP_BEGIN':
            self.coord_modify(self.controls.entry_y2, -STEP)
        elif k == 'CLEAR':
            self.coord_modify(self.controls.entry_y2, -STEP)

        self.paint()


    def convert_coord(self, x0m, y0m, width, height, ppm):
        x0 = x0m * ppm
        y0 = y0m * ppm
        x = x0 + width / 2
        y = -y0 + height / 2
        return x, y


    def paint(self):
        try:
            self.canvas.delete('all')
            x1 = float(self.controls.entry_x1.get())
            y1 = float(self.controls.entry_y1.get())
            x2 = float(self.controls.entry_x2.get())
            y2 = float(self.controls.entry_y2.get())
            x3 = float(self.controls.entry_x3.get())
            y3 = float(self.controls.entry_y3.get())
            x4 = float(self.controls.entry_x4.get())
            y4 = float(self.controls.entry_y4.get())
            r = float(self.controls.entry_r.get())
            ppi = float(self.controls.entry_ppi.get())
            ppm = ppi / 25.4
            w = self.canvas.winfo_width()
            h = self.canvas.winfo_height()
            x1p, y1p = self.convert_coord(x1, y1, w, h, ppm)
            x2p, y2p = self.convert_coord(x2, y2, w, h, ppm)
            x3p, y3p = self.convert_coord(x3, y3, w, h, ppm)
            x4p, y4p = self.convert_coord(x4, y4, w, h, ppm)
            rp = r * ppm
            self.canvas.create_oval(x1p-rp, y1p-rp, x1p+rp, y1p+rp,
                                    fill='yellow', width=0)
            self.canvas.create_oval(x2p-rp, y2p-rp, x2p+rp, y2p+rp,
                                    fill='yellow', width=0)
            self.canvas.create_oval(x3p-rp, y3p-rp, x3p+rp, y3p+rp,
                                    fill='yellow', width=0)
            self.canvas.create_oval(x4p-rp, y4p-rp, x4p+rp, y4p+rp,
                                    fill='yellow', width=0)
        except BaseException:
            messagebox.showerror('Error', 'Error!')



if __name__ == '__main__':
    app = App()
    app.mainloop()

