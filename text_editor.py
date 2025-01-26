import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        # Ensure the file has a `.txt` extension
        if not file_path.endswith(".txt"):
            file_path += ".txt"
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("INFO", "File saved successfully")

root = tk.Tk()
root.title("SIMPLE TEXT EDITOR")
root.geometry("800x600")

# Menu setup
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Text widget setup
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()