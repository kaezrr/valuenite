import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app import main


root = tk.Tk()
root.title('Valuenite')
w = 420
h = 200

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def open_file_dialog():
    button.destroy()
    l = tk.Label(root, text='Wait...', font=('System', 15))
    l.pack(padx=20, pady= 20)
    
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        msg = main(file_path)
        label = msg
    else:
        label = 'Invalid file! Try Again'

    l.destroy()
    l = tk.Label(root, text=label, font=('System', 15))
    l.pack(padx=20, pady= 20)

button = tk.Button(root, text="Select CSV File", command=open_file_dialog, font=('System', 15))
button.pack(pady=50)

root.mainloop()