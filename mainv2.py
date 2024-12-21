from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

mainWin = Tk()
mainWin.title("Adress Book")
# -----------------------------------------------------------------
myAdressBook = {}

def clear_all():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def update():
    key=name.get()
    if key == "":
        messagebox.showinfo("Error", "Name cannot be empty")
    else:
        if key not in myAdressBook.keys():
            book_list.insert(END,key)
        # update dictionary
        myAdressBook[key]=(address.get(),mobile.get(),email.get(),birthday.get)
        clear_all()

# ------------------------------------------------------------------

def edit():
    clear_all()
    index = book_list.curselection()
    if index:
        name.insert(0,book_list.get(index))
        details=myAdressBook[name.get()]

        address.insert(0,details[0])
        mobile.insert(0,details[1])
        email.insert(0,details[2])
        birthday.insert(0,details[3])
    else:
        messagebox.showinfo("Error","Select a name")
    
def delete():
    index = book_list.curselection()
    if index:
        del myAdressBook[book_list.get(index)]
        book_list.delete(index)
        clear_all()
    else:
        messagebox.showinfo("Erorr","Select a name")

# -----------------------------------------------------------

def display(event):
    # Toplevel creates a new window
    newWindow = Toplevel(mainWin)

    # Get selected line index
    index = book_list.curselection()

    # Variable to store details
    contact = ""

    if index:
        key = book_list.get(index)
        contact = "NAME : " + key + "\n\n"

        details = myAdressBook[key]
        # Add details to text boxes
        contact += "ADDRESS : " + details[0] + "\n"
        contact += "MOBILE : " + details[1] + "\n"
        contact += "E-MAIL : " + details[2] + "\n"
        contact += "BIRTHDAY : " + details[3] + "\n"
    
    # label widgets to show in toplevel
    lbl=Label(newWindow)
    lbl.grid(row=0,column=0)
    lbl.configure(text=contact)

# ------------------------------------------------------------------



def reset():
    clear_all()
    book_list.delete(0,END)
    myAdressBook.clear()
    bookName.configure(text="My Address Book")

# -------------------------------------------------------------------

def save():
    # get file using dialog
    # default extension is optional, here will add .txt if no extension is availabe
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        print(myAdressBook,file=fout)
        reset()
    else:
        messagebox.showinfo("Warning","Address book not saved")

# -----------------------------------------------------------------------

def openFile():
    global myAdressBook
    reset()
    fin = askopenfile(title='Open File')
    if fin:
        myAdressBook=eval(fin.read())
        for key in myAdressBook.keys():
            book_list.insert(END,key)
        bookName.configure(text=os.path.basename(fin.name))
    else:
        messagebox.showinfo("Warning", "No address book opened")


# ---------------------------------------------------------------------
# Design main windown

# Label address book name
bookName = Label(mainWin, text='My Address Book', width=35)
bookName.grid(row=0, column=1, pady=10, columnspan=3)

# Open address book
open_button = Button(mainWin, text='Open', command=openFile)
open_button.grid(row=0, column=3, pady=10)

# Contact list
book_list = Listbox(mainWin, height=15, width=30)
book_list.grid(row=2, column=0, columnspan=3, rowspan=5)
book_list.bind('<<ListboxSelect>>', display)

# ===================================================================

### Text fields to display contact information ###
# Name
name_label = Label(mainWin, text='Name:')
name_label.grid(row=2, column=3)

name = Entry(mainWin)
name.grid(row=2, column=4, padx=5)

# Address
address_label = Label(mainWin, text='Address:')
address_label.grid(row=3, column=3)

address = Entry(mainWin)
address.grid(row=3, column=4)

# Mobile phone
mobile_label  =Label(mainWin, text = "Mobile: ")
mobile_label.grid(row = 4, column = 3)
mobile = Entry(mainWin)
mobile.grid(row = 4, column= 4, padx = 5)

# Email
email_label = Label(mainWin,text = "Email: ")
email_label.grid(row = 5, column= 3)
email = Entry(mainWin)
email.grid(row = 5, column=4, padx=5)

# Birthday
# Birthday
birthday_label = Label(mainWin, text = 'Birthday:')
birthday_label.grid(row = 6, column = 3)
birthday = Entry(mainWin)
birthday.grid(row = 6, column = 4, padx=5)

# buttons

# Edit contact button
Edit_button = Button(mainWin, text = 'Edit', width=10, command=edit)
Edit_button.grid(row = 7, column = 0, padx = 12, pady=12)

# Delete contact button
delete_button = Button(mainWin, text = 'Delete', width=10, command=delete)
delete_button.grid(row = 7, column = 1, pady=12)

# Update/Add contact button
add_button = Button(mainWin, text = 'Update/Add', command=update)
add_button.grid(row = 7, column = 4, pady=12)

# save address book button
save_button = Button(mainWin, text='Save', width=35, command=save)
save_button.grid(row = 8, column = 1, pady = 10, columnspan=3)

mainWin.mainloop()


