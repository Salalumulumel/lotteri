from tkinter import *
from tkinter import messagebox
import lotteri

# create a root window.
root = Tk()
root.title("Lotteri")

# create listbox object
listbox = Listbox(root, height = 4,
                  width = 30,
                  bg = "white",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "blue")

# Define the size of the window.
root.geometry("380x300")

lotteriet = lotteri.Lotteri()

# create a label
label_antal = Label(root, text="Antal Lotter, max 3st :")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

# create an input textbox
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def update_listBox(antal_lotter):
    #tömmer listbox
    listbox.delete(0, END)
    # insert elements by their
    listbox.insert(1,"Grattis du vann det här!")

    try: 
        int_antal_lotter = int(antal_lotter)
        i = 0
        if (int_antal_lotter < 4):
                        
            while i < int_antal_lotter:
                #print("while = " + str(i))
                vinst = lotteriet.get_vinst()
                listbox.insert((i+2), vinst)
                i += 1 
            
        elif (int_antal_lotter > 3):
            def show_alert():
                messagebox.showinfo("Du har valt för många lotter!")
    except ValueError:
        def show_alert():
            messagebox.showinfo("Endast siffror tillåtna!")

def clickSlumpaButton():
    antal_lott = textbox_antal.get()
    #Tömmer Entrys dvs textboxar
    textbox_antal.delete(0, END)
    #sätter focus på första entry
    textbox_antal.focus_set()
    
    update_listBox(antal_lott)

button_slumpa = Button(text="Tur Knapp", command = clickSlumpaButton)
button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

# pack the widgets
#label.pack()
#listbox.pack()
 
 
# Display until User
# exits themselves.
root.mainloop()