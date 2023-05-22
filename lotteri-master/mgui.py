from tkinter import *
from tkinter import messagebox
import lotteri

#creates root window
root = Tk()
root.title("Lotteri")

#creates listbox
listbox = Listbox(root, 
                  height=4,
                  width= 30,
                  bg="white",
                  font="arial",
                  fg="blue")

#references size of window
root.geometry("300x300")

lotteriet = lotteri.Lotteri()

#creates label
label_antal= Label(root, text="Antal lotter, max 3st: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

#creates textbox
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def clickSlumpButton():
    antal_lott = textbox_antal.get()
    print(f"tryck {antal_lott}")

    #lotter textbox
    textbox_antal.delete(0, END)

    #set focus on first entry
    textbox_antal.focus_set()
    update_listBox(antal_lott)


def update_listBox(antal_lotter):
    #empty listbox
    listbox.delete(0, END)
    #insert elements
    listbox.insert(1, "Congratulations! You won these items!")

    try:
        int_antal_lotter = int(antal_lotter)
        i = 0
        if (int_antal_lotter < 4):

            while i < int_antal_lotter:
                print ("while =" + str(i))
                vinst = lotteriet.get_vinst()
                listbox.insert((i+2), vinst)
                i +=1

        elif (int_antal_lotter > 3):
            messagebox.showinfo("You've chosen too many lots!")

    except ValueError:
        messagebox.showinfo("Only numbers allowed!")


#creates button
button_slumpa = Button(text="LUCKY BUTTON :D", command=clickSlumpButton)
button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

root.mainloop()