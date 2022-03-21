import os,json
import tkinter as tk
from tkinter import ttk
from datetime import datetime

window = tk.Tk()
window.title("Read Registration")
window.geometry("820x300")
latestVar = tk.StringVar()

def refresh():
    global latestVar
    
    mainFile = os.listdir(r"C:\Projecten\Software Dev\Mapje 9\file-communicate\databron/")
    fileList = []
    latest = 0
    for filename in mainFile:
        file = open(r"C:\Projecten\Software Dev\Mapje 9\file-communicate\databron/"+filename, "r")
        fileRead = file.read()
        jsonString = json.loads(fileRead)
        fileList.append((jsonString["Naam"],jsonString["Email"], jsonString["Geboorte"], jsonString["Geslacht"]))
        latest = max(latest, os.path.getmtime(r"C:\Projecten\Software Dev\Mapje 9\file-communicate\databron/"+filename))

    register.delete(*register.get_children())    
    for files in fileList:
        register.insert('', tk.END, values=files)
    
    latestVar.set("Laatste Aanpassing: "+str(datetime.fromtimestamp(latest).strftime("%A, %B %d, %Y %I:%M:%S")))

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

refresh()

window.mainloop()