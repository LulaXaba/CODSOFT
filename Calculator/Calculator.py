import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == 'x':
            result = num1 * num2
        elif operation == '%':
            result = num1 % num2
        else:
            raise ValueError("Invalid operation")

        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main window
root = tk.Tk()
root.title("Minimalistic Calculator")

# Entry for the first number
entry_num1 = tk.Entry(root, width=15, font=('Arial', 14))
entry_num1.grid(row=0, column=0, padx=10, pady=10)

# Dropdown for the operation
operations = ['+', '-', 'x', '%']
combo_operation = tk.StringVar()
combo_operation.set(operations[0])
operation_dropdown = tk.OptionMenu(root, combo_operation, *operations)
operation_dropdown.config(font=('Arial', 14))
operation_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Entry for the second number
entry_num2 = tk.Entry(root, width=15, font=('Arial', 14))
entry_num2.grid(row=0, column=2, padx=10, pady=10)

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 14))
calculate_button.grid(row=1, column=1, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=('Arial', 16))
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
