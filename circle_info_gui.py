from math import pi
import tkinter as tk 


def area_of_circle(radius: float) -> float:
    return pi * radius ** 2 

def circumference_of_circle(radius: float) -> float:
    return pi * radius * 2 


class Circle_info_gui:

    def __init__(self):
        self.win = tk.Tk()
        self.radius_stringvar = tk.StringVar()
        self.area_stringvar = tk.StringVar()
        self.area_stringvar.set("Area:")
        self.circumference_stringvar = tk.StringVar() 
        self.circumference_stringvar.set("Circumference:")
        self.initialise_widgets()

    def initialise_widgets(self):
        # main_frame = tk.Frame(self.win)
        # main_frame.pack()

        radius_label = tk.Label(self.win, text= "Radius in cm:", anchor='w')
        radius_label.pack(fill='x')

        #! Couldnt figure how to left align an entry
        radius_entry = tk.Entry(self.win, textvariable= self.radius_stringvar,)
        radius_entry.pack()

        area_label = tk.Label(self.win, textvariable= self.area_stringvar, anchor='w') 
        area_label.pack(fill='x')

        circumference_label = tk.Label(self.win, textvariable= self.circumference_stringvar, anchor='w')
        circumference_label.pack(fill='x')

        calculate_button = tk.Button(
            self.win,
            text= "Calculate",
            command= self.handle_calculate,
            width= 10
        )
        calculate_button.pack(side= "left", padx=5, pady=5)

        close_button = tk.Button(
            self.win,
            text= "Close",
            command= self.win.destroy,
            width= 7
        )
        close_button.pack(side= "right", padx=5, pady=5)

    def handle_calculate(self):
        radius = int(self.radius_stringvar.get())
        area = area_of_circle(radius)
        circumference = circumference_of_circle(radius)
        self.area_stringvar.set(f"Area: {area :.2f} cm^2")
        self.circumference_stringvar.set(f"Circumference: {circumference :.2f} cm")


    def mainloop(self):
        self.win.mainloop()


app = Circle_info_gui()
app.mainloop()