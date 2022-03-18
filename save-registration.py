import os
import datetime as dt
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Formulier")
window.geometry("300x400")

genders = ('Man', 'M'),('Vrouw', 'V')
verenigingVal = ["Ja", "Nee"]
code = ""
naamVar = tk.StringVar()
emailVar = tk.StringVar()
geboorteVar = tk.StringVar()
geslachtVar = tk.StringVar()
verenigingVar = tk.StringVar()
sportVar = tk.StringVar()
thisYear = dt.date.today().year
choicesYear = list(range(thisYear-100, thisYear+1))

titelLabel = tk.Label(text="Informatie Formulier", font=("Calibri Light", 14))
titelLabel.pack(fill="x")

# Checkt of de map databron bestaat, zo niet maakt het programma deze aan.
# Iedere registratie in een apart bestand in JSON format in de data word opgeslagen.
# Sla de velden/keys die je gebruikt om de json op te bouwen in een YAML file op.


def destroyWidgets():
    for widget in window.winfo_children():
        widget.destroy()
    FormulierControle()

def FormulierControle():
    window.geometry("300x200")
    naamResult = tk.Label(text="Naam: " + naamVar.get(), font=("Calibri Light", 12))
    naamResult.pack()
    emailResult = tk.Label(text="Email: " + emailVar.get(),font=("Calibri Light", 12))
    emailResult.pack()
    geboorteResult = tk.Label(text="Geboortejaar: " + geboorteVar.get(),font=("Calibri Light", 12))
    geboorteResult.pack()
    geslachtResult = tk.Label(text="Geslacht: " + geslachtVar.get(),font=("Calibri Light", 12))
    geslachtResult.pack()
    sportResult = tk.Label(text="Sport: " + sportVar.get(),font=("Calibri Light", 12))
    sportResult.pack()
    createCode()
    regestratieCode = tk.Label(text="Regestratie Code: " + code,font=("Calibri Light", 10))
    regestratieCode.pack(side="bottom")

def createCode():
    geboorte = geboorteVar.get()
    geslacht = geslachtVar.get()
    sport = sportVar.get()
    sportList = list(sportVar.get())
    naam = list(naamVar.get())

    code += geboorte
    code += naam[0]
    if geslacht == "Man":
        code += "M"
    else:
        code += "V"
    if sport != "":
        code += sportList[0]

# Widgets ----------------------------------------------------------------------------------------------------------------------------------
naamLabel = tk.Label(text="Wat is uw volledige naam?")
naamLabel.pack()
naamEntry = tk.Entry(width=30,textvariable=naamVar)
naamEntry.pack()

emailLabel = tk.Label(text="Wat is uw email?")
emailLabel.pack()
emailEntry = tk.Entry(width=30,textvariable=emailVar)
emailEntry.pack()

geboorteLabel = tk.Label(text="Wat is uw geboortejaar?")
geboorteLabel.pack()
geboorteCombo = ttk.Combobox(width=15,values=choicesYear, textvariable=geboorteVar)
geboorteCombo.pack()

geslachtLabel = tk.Label(text="Wat is uw geslacht?")
geslachtLabel.pack()
geslachtRadio = tk.Radiobutton(text="Man", value="Man",variable=geslachtVar)
geslachtRadio.pack()
geslachtRadio = tk.Radiobutton(text="Vrouw", value="Vrouw",variable=geslachtVar)
geslachtRadio.pack()

verenigingLabel = tk.Label(text="Bent u lid van een sportvereniging?")
verenigingLabel.pack()
verenigingCombo = ttk.Combobox(width=15, values=verenigingVal)
verenigingCombo.pack()

sportLabel = tk.Label(text="Zoja, welke sport beoefent u? (optioneel)")
sportLabel.pack()
sportEntry = tk.Entry(width=30,textvariable=sportVar)
sportEntry.pack()

btn = tk.Button(text="Formulier Controleren", command=destroyWidgets)
btn.pack(side="bottom")



window.mainloop()