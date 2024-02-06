from tkinter import *


class Calculator:
    
    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("200x200")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

        self.num1 = IntVar()
        self.num2 = IntVar()
        self.result = StringVar()
        self.result.set("Result: 0")

        # Q4
        self.possible_operations = ["Add", "Sub", "Mul", "Div"]
        self.selected_operation = StringVar()
        self.selected_operation.set(self.possible_operations[0])

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblNum1 = Label(self.mainFrame, text="Number 1:")
        lblNum1.pack()

        entryNum1 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num1
        )
        entryNum1.pack()

        lblNum2 = Label(self.mainFrame, text="Number 2:")
        lblNum2.pack()

        entryNum2 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num2
        )
        entryNum2.pack()

        lblResult = Label(
            self.mainFrame,
            textvariable=self.result
        )
        lblResult.pack()

        # Q4
        operationListbox = OptionMenu(
            self.mainFrame,
            self.selected_operation,
            *self.possible_operations
        )
        operationListbox.pack()

        btnMultiply = Button(
            self.mainFrame,
            text="Calc",
            command=self.perform_operation
        )
        btnMultiply.pack(side="left")

        btnClose = Button(
            self.mainFrame,
            text="Close",
            command=self.win.destroy
        )
        btnClose.pack(side="right")

    # Q4
    def perform_operation(self):
        match self.selected_operation.get():
            case "Add":
                self.add()
            case "Sub":
                self.subtract()
            case "Mul":
                self.multiply()
            case "Div":
                self.divide()
        
    def get_inputs(self):
        return self.num1.get(), self.num2.get()
    
    def add(self):
        num1, num2 = self.get_inputs()
        result = num1 + num2
        self.result.set(f"Result: {result}")

    def subtract(self):
        num1, num2 = self.get_inputs()
        result = num1 - num2
        self.result.set(f"Result: {result}")

    def multiply(self):
        num1, num2 = self.get_inputs()
        result = num1 * num2
        self.result.set(f"Result: {result}")

    def divide(self):
        num1, num2 = self.get_inputs()
        result = num1 / num2
        self.result.set(f"Result: {result}")


def main():
    calc = Calculator()
    calc.run()

main()