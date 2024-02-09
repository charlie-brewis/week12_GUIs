from tkinter import *


class Temperature_converter_gui:

    def __init__(self):
        self.win = Tk()
        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=5, pady=5)
        self.doublevar_celsius = DoubleVar()
        self.doublevar_fahrenheit = DoubleVar()
        self.to_fahrenheit()
        self.initialise_widgets()

    def initialise_widgets(self):
        lbl_celsius = Label(self.main_frame, text="Celsius")
        lbl_celsius.grid(row=0, column=0)

        lbl_fahrenheit = Label(self.main_frame, text="Fahrenheit")
        lbl_fahrenheit.grid(row=0, column=1)

        entry_celsius = Entry(self.main_frame, textvariable=self.doublevar_celsius)
        entry_celsius.grid(row=1, column=0, padx=5)

        entry_fahrenheit = Entry(self.main_frame, textvariable=self.doublevar_fahrenheit)
        entry_fahrenheit.grid(row=1, column=1, padx=5)

        btn_to_fahrenheit = Button(self.main_frame, text="Convert to fahrenheit", command=self.to_fahrenheit)
        btn_to_fahrenheit.grid(row=2, column=0)

        btn_to_celsius = Button(self.main_frame, text="Convert to Celsius", command=self.to_celsius)
        btn_to_celsius.grid(row=2, column=1)

    def to_fahrenheit(self):
        self.doublevar_fahrenheit.set(self.doublevar_celsius.get() * (9 / 5) + 32)

    def to_celsius(self):
        self.doublevar_celsius.set((self.doublevar_fahrenheit.get() - 32) * 5/9)
        
    def mainloop(self):
        self.win.mainloop()

app = Temperature_converter_gui()
app.mainloop()