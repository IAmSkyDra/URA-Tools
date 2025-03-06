import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import main
import threading
import sys

class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.insert(tk.END, str)
        self.widget.see(tk.END)

    def flush(self):
        pass

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_selected)

def run_main():
    folder_path = folder_entry.get()
    file_type = file_type_var.get()
    threading.Thread(target=main_thread, args=(folder_path, file_type)).start()

def main_thread(folder_path, file_type):
    main.main(folder_path, file_type)

root = tk.Tk()
root.title("Denoise Tool")

# Folder selection
tk.Label(root, text="Select Folder:").grid(row=0, column=0, padx=10, pady=10)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0, column=2, padx=10, pady=10)

# File type selection
tk.Label(root, text="Select File Type:").grid(row=1, column=0, padx=10, pady=10)
file_type_var = tk.StringVar(value="mp4")
file_type_options = ["mp4", "mov"]
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)
file_type_menu.grid(row=1, column=1, padx=10, pady=10)

# Run button
tk.Button(root, text="Run", command=run_main).grid(row=2, column=0, columnspan=3, pady=20)

# Output text box
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Redirect stdout to the text box
sys.stdout = TextRedirector(output_text, "stdout")

root.mainloop()
