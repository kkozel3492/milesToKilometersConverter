from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Calculate MPH to KPH
def calculate():
    miles = userEntry.get()
    conversion = float(miles) * 1.60934
    conversion = round(conversion, 2)

    convertLabel.config(text=str(conversion))

#Create the GUI

#Create Button
calculateButton = Button(text="Calculate", command=calculate)
calculateButton.grid(column=1, row=2)

#Create Labels
isEqualToLabel = Label(text="is equal to")
isEqualToLabel.grid(column=0, row=1)

milesLabel = Label(text='Miles')
milesLabel.grid(column=2, row=0)

km = Label(text='Km')
km.grid(column=2, row=1)

convertLabel = Label(text='0')
convertLabel.grid(column=1, row=1)

userEntry = Entry()
userEntry.config(width=10)
userEntry.grid(column=1, row=0)


window.mainloop()