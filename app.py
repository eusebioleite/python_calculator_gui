import tkinter as tk

''' First column '''
def add_1():
    text_block.insert(tk.END, "1")

def add_2():
    text_block.insert(tk.END, "2")

def add_3():
    text_block.insert(tk.END, "3")

def add_div():
    text_block.insert(tk.END, "/")

''' Second column '''
def add_4():
    text_block.insert(tk.END, "4")

def add_5():
    text_block.insert(tk.END, "5")

def add_6():
    text_block.insert(tk.END, "6")

def add_mul():
    text_block.insert(tk.END, "*")

''' Third column '''
def add_7():
    text_block.insert(tk.END, "7")

def add_8():
    text_block.insert(tk.END, "8")

def add_9():
    text_block.insert(tk.END, "9")

def add_sub():
    text_block.insert(tk.END, "-")

''' Fourth column '''
def submit():
    current_text = text_block.get("1.0", tk.END).strip()  # Get the current text in the text block
    if current_text:  # Check if there's any text
        try:
            result = eval(current_text)  # Evaluate the expression
            text_block.delete("1.0", tk.END)  # Clear the text block
            text_block.insert("1.0", result)  # Insert the result into the text block
        except Exception as e:       
            text_block.delete("1.0", tk.END)  # Clear the text block
            text_block.insert("1.0", f"Error: {e}")

def add_0():
    text_block.insert(tk.END, "0")

def clear():
    text_block.delete("1.0", tk.END)

def add_add():
    text_block.insert(tk.END, "+")

# Create the main window
root = tk.Tk()
root.title("pycalc")
root.geometry("185x255")

# Create a text block
text_block = tk.Text(root, height=2, width=21)
text_block.pack(side=tk.TOP)

''' Create frame for buttons '''
buttons_frame = tk.Frame(root)
buttons_frame.pack(side=tk.TOP)

''' Create frame for top buttons '''
top_frame = tk.Frame(buttons_frame)
top_frame.pack(side=tk.TOP)

# Create the "1" button
button_1 = tk.Button(top_frame, text="1", command=add_1, width=2, height=2)
button_1.pack(side=tk.LEFT)

# Create the "2" button
button_2 = tk.Button(top_frame, text="2", command=add_2, width=2, height=2)
button_2.pack(side=tk.LEFT)

# Create the "3" button
button_3 = tk.Button(top_frame, text="3", command=add_3, width=2, height=2)
button_3.pack(side=tk.LEFT)

# Create the Division button
button_div = tk.Button(top_frame, text="/", command=add_div, width=2, height=2)
button_div.pack(side=tk.LEFT)

''' Create frame for middle buttons '''
middle_frame = tk.Frame(buttons_frame)
middle_frame.pack(side=tk.TOP)

# Create the "4" button
button_4 = tk.Button(middle_frame, text="4", command=add_4, width=2, height=2)
button_4.pack(side=tk.LEFT)

# Create the "5" button
button_5 = tk.Button(middle_frame, text="5", command=add_5, width=2, height=2)
button_5.pack(side=tk.LEFT)

# Create the "6" button
button_6 = tk.Button(middle_frame, text="6", command=add_6, width=2, height=2)
button_6.pack(side=tk.LEFT)

# Create the Multiplication button
button_mul = tk.Button(middle_frame, text="*", command=add_mul, width=2, height=2)
button_mul.pack(side=tk.LEFT)

''' Create frame for bottom buttons '''
bottom_frame = tk.Frame(buttons_frame)
bottom_frame.pack(side=tk.TOP)

# Create the "7" button
button_7 = tk.Button(bottom_frame, text="7", command=add_7, width=2, height=2)
button_7.pack(side=tk.LEFT)

# Create the "8" button
button_8 = tk.Button(bottom_frame, text="8", command=add_8, width=2, height=2)
button_8.pack(side=tk.LEFT)

# Create the "9" button
button_9 = tk.Button(bottom_frame, text="9", command=add_9, width=2, height=2)
button_9.pack(side=tk.LEFT)

# Create the Subtraction button
button_sub = tk.Button(bottom_frame, text="-", command=add_sub, width=2, height=2)
button_sub.pack(side=tk.LEFT)

''' Create frame for far bottom buttons '''
farbottom_frame = tk.Frame(buttons_frame)
farbottom_frame.pack(side=tk.TOP)

# Create the Submit button
button_submit = tk.Button(farbottom_frame, text="E", command=submit, width=2, height=2)
button_submit.pack(side=tk.LEFT)

# Create the "0" button
button_0 = tk.Button(farbottom_frame, text="0", command=add_0, width=2, height=2)
button_0.pack(side=tk.LEFT)

# Create the Clear button
button_clear = tk.Button(farbottom_frame, text="C", command=clear, width=2, height=2)
button_clear.pack(side=tk.LEFT)

# Create the Addition button
button_add = tk.Button(farbottom_frame, text="+", command=add_add, width=2, height=2)
button_add.pack(side=tk.LEFT)

# Run the Tkinter event loop
root.mainloop()
