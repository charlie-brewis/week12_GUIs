from tkinter import *

class What_to_do_gui:

    def __init__(self):
        self.win = Tk()
        self.mainframe = Frame(self.win)
        self.mainframe.pack()
        self.temperature = DoubleVar()
        self.temperature_msg = StringVar()
        self.initialise_widgets()

    def initialise_widgets(self):
        lbl_enter = Label(self.mainframe, text="Enter todays temperature: ")
        lbl_enter.pack()

        entry_temp = Entry(self.mainframe, textvariable=self.temperature)
        entry_temp.pack()

        btn_enter_temp = Button(self.mainframe, text="Enter Temperature", command=self.update_suggestion)
        btn_enter_temp.pack()

        lbl_suggestion = Label(self.mainframe, textvariable=self.temperature_msg)
        lbl_suggestion.pack()

    def update_suggestion(self):
        if self.temperature.get() > 25:
            self.temperature_msg.set("Swim in the sea")
        elif self.temperature.get() < 10:
            self.temperature_msg.set("Watch a film at home")
        else:
            self.temperature_msg.set("Go to Gunwharf Quays")

    def mainloop(self):
        self.win.mainloop()


app = What_to_do_gui()
app.mainloop()