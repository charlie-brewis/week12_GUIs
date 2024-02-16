import tkinter as tk
import csv


class Sign_up_form:

    def __init__(self,  password_requirements: dict) -> None:
        self.win = tk.Tk()

        self.error_msg = tk.StringVar()
        self.showing_passwords = tk.BooleanVar()
        self.showing_passwords.set(False)

        self.password_requirements = password_requirements

        self.fields = self.initialise_widgets()

    def initialise_widgets(self) -> None:
        lbl_error = tk.Label(self.win, textvariable=self.error_msg)
        lbl_error.pack(padx=5, pady=5)

        username_field = Field(self.win, "Username")
        password_field = Field(self.win, "Password", False)
        confirm_password_field = Field(self.win, "Confirm Password", False)

        # Checkbox works but doesnt display graphically, i think its a bug with my system's theme
        checkbox_show_password = tk.Checkbutton(
            self.win,
            text = "Show Password", 
            command = self.toggle_password, 
            variable = self.showing_passwords,
            onvalue = True,
            offvalue = False,
            indicatoron = True
        )
        checkbox_show_password.pack(padx=5, pady=5)

        btn_sign_up = tk.Button(self.win, text="Sign Up", command=self.handle_sign_up)
        btn_sign_up.pack(padx=5, pady=5, side="left")

        btn_cancel = tk.Button(self.win, text="Cancel", command=self.win.quit)
        btn_cancel.pack(padx=5, pady=5, side="right")

        return [username_field, password_field, confirm_password_field]


    def toggle_password(self) -> None:
        self.showing_passwords.set(not self.showing_passwords.get())
        password_field, confirm_password_field = self.fields[1:]
        password_field.toggle_showing()
        confirm_password_field.toggle_showing()

    def handle_sign_up(self) -> None:
        username, password, confirm_password = [field.get_value() for field in self.fields]
        if self.validate_details(username, password, confirm_password):
            self.sign_up_or_login(username, password)

    def sign_up_or_login(self, username: str, password: str) -> None:
        login_details = LoginDetails(username, password)
        if login_details.check_already_exists():
            self.error_msg.set("Login Successful!")
        else:
            login_details.write_to_file()
            self.error_msg.set("Sign up successful")
    
    def validate_details(self, username: str, password: str, confirm_password: str) -> bool:
        errors_queue = PriorityQueue()
        if not username:
            errors_queue.insert("Username cannot be empty", 1)
        if password != confirm_password:
            errors_queue.insert("Passwords do not match", 1)
        for requirement, data in self.password_requirements.items():
            requirement_function, error_message, priority = data
            if not requirement_function(password):
                errors_queue.insert(error_message, priority)
        return not errors_queue.queue
    

    def mainloop(self) -> None:
        self.win.mainloop()


class Field:

    def __init__(self, win: tk.Tk, field_name: str, showing: bool = True) -> None:
        self.name = field_name
        self.showing = tk.BooleanVar()
        self.showing.set(showing)

        self.win = win 
        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)


        lbl_name = tk.Label(self.main_frame, text=self.name)
        lbl_name.grid(row=0, column=0, sticky=tk.W)

        self.value = tk.StringVar()  
        self.entry = tk.Entry(self.main_frame, textvariable=self.value)
        self.refresh_entry_text()
        self.entry.grid(row=0, column=1, sticky=tk.E)
        # Allows column 1 to expand and take up the space
        self.main_frame.grid_columnconfigure(1, weight=1)

    def refresh_entry_text(self) -> None:
        if not self.showing.get():
            self.entry.config(show="*")
        else:
            self.entry.config(show="")

    def get_value(self) -> str:
        return self.value.get()
    
    def toggle_showing(self) -> None:
        self.showing.set(not self.showing.get())
        self.refresh_entry_text()


class LoginDetails:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def write_to_file(self) -> None:
        with open("login_details.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.username, self.password])
    
    def check_already_exists(self) -> bool:
        if not self.check_file_exists():
            return False
        with open("login_details.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.username and row[1] == self.password:
                    return True
        return False
    
    def check_file_exists(self) -> bool:
        try:
            with open("login_details.csv", "r") as file:
                return True
        except FileNotFoundError:
            return False


class PriorityQueue:
    
        def __init__(self) -> None:
            self.queue = []
    
        def insert(self, item: str, priority: int) -> None:
            self.queue.append((item, priority))
            self.queue.sort(key=lambda x: x[1])
    
        def pop(self) -> str:
            return self.queue.pop(0)[0]
        
    
        def __str__(self) -> str:
            return str(self.queue)

password_requirements = {
    'min_length': [lambda x: len(x) >= 8, "Password must be at least 8 characters long", 2],
    'upper_case': [lambda x: any(char.isupper() for char in x), "Password must contain an upper case letter", 4],
    'lower_case': [lambda x: any(char.islower() for char in x), "Password must contain a lower case letter", 4],
    'digit': [lambda x: any(char.isdigit() for char in x), "Password must contain a digit", 3],
    'special_char': [lambda x: any(not char.isalnum() for char in x), "Password must contain a special character", 3],
    'no_spaces': [lambda x: ' ' not in x, "Password must not contain any spaces", 5]
}
app = Sign_up_form(password_requirements)
app.mainloop()
