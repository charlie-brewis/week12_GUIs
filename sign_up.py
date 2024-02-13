import tkinter as tk


class Sign_up_form:

    def __init__(self) -> None:
        self.win = tk.Tk()

        self.error_msg = tk.StringVar()

        self.fields = self.initialise_widgets()



    def initialise_widgets(self) -> None:
        lbl_error = tk.Label(self.win, textvariable=self.error_msg)
        lbl_error.pack(padx=5, pady=5)

        username_field = Field(self.win, "Username")
        password_field = Field(self.win, "Password")
        confirm_password_field = Field(self.win, "Confirm Password")

        checkbox_show_password = tk.Checkbutton(self.win, text="Show Password", command=toggle_password)

        return [username_field, password_field, confirm_password_field]


    def toggle_password(self) -> None:
        password_field, confirm_password_field = self.fields[1:]
        #! Need config logic
        password_field.entry.config(show='*')
        confirm_password_field.entry.config(show='*')

    def mainloop(self) -> None:
        self.win.mainloop()


class Field:

    def __init__(self, win: tk.Tk, field_name: str, field_requirements: list) -> None:
        self.name = field_name
        self.requirements = field_requirements

        self.win = win 
        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)


        lbl_name = tk.Label(self.main_frame, text=self.name)
        lbl_name.grid(row=0, column=0, sticky=tk.W)

        self.value = tk.StringVar()  
        self.entry = tk.Entry(self.main_frame, textvariable=self.value)
        self.entry.grid(row=0, column=1, sticky=tk.E)
        # Allows column 1 to expand and take up the space
        self.main_frame.grid_columnconfigure(1, weight=1)

    def get_value(self):
        return self.value.get()
    


app = Sign_up_form()
app.mainloop()