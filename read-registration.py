import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Read Registration")
window.geometry("820x300")
latestVar = tk.StringVar()

def refresh():
    pass

columns = ("Naam", "Email" ,"Geboorte", "Geslacht")

register = ttk.Treeview(window, columns=columns, show='headings')
register.heading("Naam", text="Naam")
register.heading("Email", text="Email")
register.heading("Geboorte", text="Geboortejaar")
register.heading('Geslacht', text="Geslacht")
register.grid(row=0, column=0, sticky='nsew')

scroll = ttk.Scrollbar(window, orient=tk.VERTICAL, command=register.yview)
register.configure(yscroll=scroll.set)
scroll.grid(row=0, column=1, sticky='ns')

btn = ttk.Button(window,text="Vernieuwen",command=refresh)
btn.grid(row=2,column=0, sticky='ns')

latest = ttk.Label(window, textvariable=latestVar)
latest.grid(row=3,column=0)

#refresh()

window.mainloop()