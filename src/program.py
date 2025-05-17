# ----------------------------------------------
# Program made by Sobhan Ashrafi
# ----------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox

class Program:
    def __init__(self, root):
        self.root = root
        self.root.title("Yasin")
        self.root.geometry("450x350")
        
        # Create a notebook widget for tabbed interface
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create three tabs as frames
        self.bio_tab = ttk.Frame(self.notebook)
        self.calc_tab = ttk.Frame(self.notebook)
        self.hello_tab = ttk.Frame(self.notebook)
        
        # Add tabs to the notebook
        self.notebook.add(self.bio_tab, text="Biography")
        self.notebook.add(self.calc_tab, text="Calculator")
        self.notebook.add(self.hello_tab, text="Say Hello")
        
        # Initialize the content of each tab
        self.setup_bio_tab()
        self.setup_calc_tab()
        self.setup_hello_tab()
        
        # Simple status bar at the bottom of the window
        self.status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_bio_tab(self):
        """Setup the Biography tab with entry fields and buttons."""
        # Name field
        tk.Label(self.bio_tab, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = tk.Entry(self.bio_tab)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Age field
        tk.Label(self.bio_tab, text="Age:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.age_entry = tk.Entry(self.bio_tab)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Email field
        tk.Label(self.bio_tab, text="Email:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.email_entry = tk.Entry(self.bio_tab)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Bio field (multi-line text)
        tk.Label(self.bio_tab, text="About:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.bio_text = tk.Text(self.bio_tab, height=4, width=20)
        self.bio_text.grid(row=3, column=1, padx=10, pady=5)
        
        # Save and Clear buttons for the biography form
        save_btn = tk.Button(self.bio_tab, text="Save", command=self.save_bio)
        save_btn.grid(row=4, column=0, padx=10, pady=10)
        
        clear_btn = tk.Button(self.bio_tab, text="Clear", command=self.clear_bio)
        clear_btn.grid(row=4, column=1, padx=10, pady=10)
    
    def setup_calc_tab(self):
        """Setup the Calculator tab with entry fields, result label, and operation buttons."""
        # First number input
        tk.Label(self.calc_tab, text="First number:").grid(row=0, column=0, padx=10, pady=5)
        self.num1 = tk.Entry(self.calc_tab)
        self.num1.grid(row=0, column=1, padx=10, pady=5)
        
        # Second number input
        tk.Label(self.calc_tab, text="Second number:").grid(row=1, column=0, padx=10, pady=5)
        self.num2 = tk.Entry(self.calc_tab)
        self.num2.grid(row=1, column=1, padx=10, pady=5)
        
        # Result display label
        tk.Label(self.calc_tab, text="Result:").grid(row=2, column=0, padx=10, pady=5)
        self.result = tk.Label(self.calc_tab, text="")
        self.result.grid(row=2, column=1, padx=10, pady=5)
        
        # Frame for operation buttons
        btn_frame = tk.Frame(self.calc_tab)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Operation buttons (+, -, *, /)
        tk.Button(btn_frame, text="+", command=lambda: self.calculate("+")).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="-", command=lambda: self.calculate("-")).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="*", command=lambda: self.calculate("*")).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="/", command=lambda: self.calculate("/")).grid(row=0, column=3, padx=5)
        # Clear button for calculator
        tk.Button(btn_frame, text="Clear", command=self.clear_calc).grid(row=1, column=1, columnspan=2, pady=5)
    
    def setup_hello_tab(self):
        """Setup the Say Hello tab with entry, buttons, and result label."""
        # Exit button to close the app
        exit_btn = tk.Button(self.hello_tab, text="Exit", command=self.root.destroy)
        exit_btn.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        
        # Name entry field for greeting
        tk.Label(self.hello_tab, text="Enter your name:").grid(row=1, column=0, padx=10, pady=5)
        self.hello_name = tk.Entry(self.hello_tab)
        self.hello_name.grid(row=1, column=1, padx=10, pady=5)
        
        # Clear and Say Hello buttons
        clear_btn = tk.Button(self.hello_tab, text="Clear", command=self.clear_hello)
        clear_btn.grid(row=2, column=0, padx=10, pady=5)
        
        hello_btn = tk.Button(self.hello_tab, text="Say Hello", command=self.say_hello)
        hello_btn.grid(row=2, column=1, padx=10, pady=5)
        
        # Result label for greeting
        self.hello_result = tk.Label(self.hello_tab, text="")
        self.hello_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
    
    def save_bio(self):
        """Save the biography information and update the status bar."""
        name = self.name_entry.get()
        if not name:
            messagebox.showinfo("Error", "Please enter at least your name")
            return
        
        # Show a success message and update status
        messagebox.showinfo("Success", "Biography saved!")
        self.status.config(text=f"Bio saved for {name}")
    
    def clear_bio(self):
        """Clear all biography fields and update the status bar."""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.bio_text.delete("1.0", tk.END)
        self.status.config(text="Bio form cleared")
    
    def calculate(self, op):
        """Perform calculation based on the selected operation and update result/status."""
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            
            # Perform the selected operation
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    messagebox.showinfo("Error", "Cannot divide by zero")
                    return
                result = num1 / num2
            
            # Display result and update status
            self.result.config(text=str(result))
            self.status.config(text=f"Calculated: {num1} {op} {num2} = {result}")
            
        except ValueError:
            messagebox.showinfo("Error", "Please enter valid numbers")
    
    def clear_calc(self):
        """Clear calculator fields and result label, update status bar."""
        self.num1.delete(0, tk.END)
        self.num2.delete(0, tk.END)
        self.result.config(text="")
        self.status.config(text="Calculator cleared")
    
    def say_hello(self):
        """Display a greeting using the entered name and update status."""
        name = self.hello_name.get()
        if name:
            self.hello_result.config(text=f"Result: Hello {name}")
            self.status.config(text=f"Greeted {name}")
        else:
            messagebox.showinfo("Info", "Please enter your name first")
    
    def clear_hello(self):
        """Clear the hello tab fields and result label, update status bar."""
        self.hello_name.delete(0, tk.END)
        self.hello_result.config(text="")
        self.status.config(text="Hello form cleared")


if __name__ == "__main__":
    # Start the application
    root = tk.Tk()
    app = Program(root)
    root.mainloop()