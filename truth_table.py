from tkinter import *

class Truth_table_1d:

    def __init__(self) -> None:
        self.win = Tk()
        self.mainframe = Frame(self.win)
        self.mainframe.pack()
        self.result = StringVar()
        
        self.condition1_ans = BooleanVar()
        self.condition2_ans = BooleanVar()
        self.condition3_ans = BooleanVar()
        self.condition4_ans = BooleanVar()

        self.initialise_widgets()

    def initialise_widgets(self):
        '''
        condition 1: 0 OR 0
        condition 2: 0 OR 1
        condition 3: 1 OR 0
        condition 4: 1 OR 1
        '''
        lbl_condition_1 = Label(self.mainframe, text="0 OR 0")
        lbl_condition_1.grid(row=0, column=0)
        lbl_condition_2 = Label(self.mainframe, text="0 OR 1")
        lbl_condition_2.grid(row=0, column=1)
        lbl_condition_3 = Label(self.mainframe, text="1 OR 0")
        lbl_condition_3.grid(row=0, column=2)
        lbl_condition_4 = Label(self.mainframe, text="1 OR 1")
        lbl_condition_4.grid(row=0, column=3)

        entry_condition_1 = Entry(self.mainframe, textvariable=self.condition1_ans)
        entry_condition_1.grid(row=1, column=0)
        entry_condition_2 = Entry(self.mainframe, textvariable=self.condition2_ans)
        entry_condition_2.grid(row=1, column=1)
        entry_condition_3 = Entry(self.mainframe, textvariable=self.condition3_ans)
        entry_condition_3.grid(row=1, column=2)
        entry_condition_4 = Entry(self.mainframe, textvariable=self.condition4_ans)
        entry_condition_4.grid(row=1, column=3)

        btn_enter = Button(self.win, text="Enter", command=self.enter_answers)
        btn_enter.pack()

        lbl_result = Label(self.win, textvariable=self.result)
        lbl_result.pack()

    def enter_answers(self):
        if all([
            self.condition1_ans.get() is False,
            self.condition2_ans.get() is False,
            self.condition3_ans.get() is False,
            self.condition4_ans.get() is True
        ]):
            self.result.set("Congratulations! You got it right!")
        else:
            self.result.set("This is incorrect.")
            

    def mainloop(self):
        self.win.mainloop()

# app = Truth_table_1d()
# app.mainloop()



class Truth_table_2d:

    def __init__(self) -> None:
        self.win = Tk()
        self.mainframe = Frame(self.win)
        self.mainframe.pack()
        self.result = StringVar()
    
        '''
        condition 1: 0 OR 0
        condition 2: 0 OR 1
        condition 3: 1 OR 0
        condition 4: 1 OR 1
        '''
        self.condition1_ans = BooleanVar()
        self.condition2_ans = BooleanVar()
        self.condition3_ans = BooleanVar()
        self.condition4_ans = BooleanVar()


        self.entries = self.initialise_widgets()

    def initialise_widgets(self):
        lbl_OR = Label(self.mainframe, text="OR")
        lbl_OR.grid(row=0, column=0)

        lbl_horizontal_0 = Label(self.mainframe, text="0")
        lbl_horizontal_0.grid(row=0, column=1)
        lbl_horizontal_1 = Label(self.mainframe, text="1")
        lbl_horizontal_1.grid(row=0, column=2)
        lbl_vertical_0 = Label(self.mainframe, text="0")
        lbl_vertical_0.grid(row=1, column=0)
        lbl_vertical_1 = Label(self.mainframe, text="1")
        lbl_vertical_1.grid(row=2, column=0)

        entry_condition_1 = Entry(self.mainframe, textvariable=self.condition1_ans)
        entry_condition_1.grid(row=1, column=1)
        entry_condition_2 = Entry(self.mainframe, textvariable=self.condition2_ans)
        entry_condition_2.grid(row=1, column=2)
        entry_condition_3 = Entry(self.mainframe, textvariable=self.condition3_ans)
        entry_condition_3.grid(row=2, column=1)
        entry_condition_4 = Entry(self.mainframe, textvariable=self.condition4_ans)
        entry_condition_4.grid(row=2, column=2)

        btn_enter = Button(self.win, text="Enter", command=self.enter_answers)
        btn_enter.pack()

        lbl_result = Label(self.win, textvariable=self.result)
        lbl_result.pack()

        return [entry_condition_1, entry_condition_2, entry_condition_3, entry_condition_4]

    def enter_answers(self):
        conditions = [
            self.condition1_ans.get() is False,
            self.condition2_ans.get() is False,
            self.condition3_ans.get() is False,
            self.condition4_ans.get() is True
        ]
        for i, condition in enumerate(conditions):
            curr_entry = self.entries[i]
            if condition:
                curr_entry.config(fg="green")
            else:
                curr_entry.config(fg="red")

        if all(conditions):
            self.result.set("Congratulations! You got it right!")
        else:
            self.result.set("This is incorrect.")
            

    def mainloop(self):
        self.win.mainloop()


app = Truth_table_2d()
app.mainloop()