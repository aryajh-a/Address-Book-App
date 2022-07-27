from tkinter import *
import sqlite3


root=Tk()
root.title("Enter Address\n")             
root.geometry("330x320")

# CREATE A DATABASE OR CONNECT TO ONE
# creating
db1=sqlite3.connect("AddressBook.db")
# creating cursor 
cur= db1.cursor()
#creating table
cur.execute("CREATE TABLE ADDRESSES (first_name text, last_name text, address text, city text, state text, zipcode int)")


#creating text boxes for gui

# ENTRY WIDGET ~~~~~~
f_name = Entry(root, width=30, bg='lavender')
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30, bg='lavender')
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30, bg='lavender')
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30, bg='lavender')
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30, bg='lavender')
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30, bg='lavender')
zipcode.grid(row=5, column=1, padx=20)
oid= Entry(root,width=30, bg='lavender' )
oid.grid(row=9, column=1, padx=20)

#creating text labels
# TEXT LABELS
f_namelabel = Label(root, text="Enter first name : ")
f_namelabel.grid(row=0, column=0)
l_namelabel = Label(root, text="Enter last name : ")
l_namelabel.grid(row=1, column=0)
addresslabel = Label(root, text="Enter address : ")
addresslabel.grid(row=2, column=0)
citylabel = Label(root, text="Enter city name : ")
citylabel.grid(row=3, column=0)
statelabel = Label(root, text="Enter state : ")
statelabel.grid(row=4, column=0)
zipcodelabel = Label(root, text="Enter zipcode : ")
zipcodelabel.grid(row=5, column=0)
oidlabel = Label(root, text="Enter record id : ")
oidlabel.grid(row=9, column=0)

# you gotta connect your database and cursor inside the every function

# ALL FUNCIONS USED :

def add():
    db1=sqlite3.connect("AddressBook.db")
    cur= db1.cursor()

#adding data into table using python dictionary
    cur.execute("INSERT INTO ADDRESSES VALUES( :f_name, :l_name, :address, :city, :state, :zipcode)"  , # :f_name etc are dummy variables
            {
                'f_name' : f_name.get(),
                'l_name' : l_name.get(),
                'address' : address.get(),
                'city' : city.get(),
                'state' : state.get(),
                'zipcode' : zipcode.get(),
            })

    db1.commit()

    db1.close()

#clear the text boxes as submitting so new data can be entered
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query function
def show():
    db1=sqlite3.connect("AddressBook.db")
    cur= db1.cursor()

    #adding data into table using python dictionary
    cur.execute("SELECT *, oid FROM ADDRESSES")     # oid is a primary key created by sqllite automatically
    records= cur.fetchall()  # returns a python list which has tuples in its content


    # loop through records
    print_records=''
    for record in records:
        print_records += str(record) + "\n"

    querylabel=Label(root, text=print_records)
    querylabel.grid(row=8, column=0, columnspan=2)


    # the list conatins tuples
    # they can be accessed via indices


    db1.commit()

    db1.close()

# creating delete function
def delete():
    db1=sqlite3.connect("AddressBook.db")
    cur= db1.cursor()

    #adding data into table using python dictionary
    cur.execute("DELETE FROM ADDRESSES WHERE oid= " + oid.get())    # .get() function returns string type

    db1.commit()

    db1.close()

    oid.delete(0, END)
 
# creating update function
def update():
    db1=sqlite3.connect("AddressBook.db")
    cur= db1.cursor()

    #creating a new window for editting
    edit=Tk()
    edit.geometry("350x200")
    edit.title("Update records :")

    #creating text label
    f_namelabel = Label(edit, text="Enter first name : ")
    f_namelabel.grid(row=0, column=0)
    l_namelabel = Label(edit, text="Enter last name : ")
    l_namelabel.grid(row=1, column=0)
    addresslabel = Label(edit, text="Enter address : ")
    addresslabel.grid(row=2, column=0)
    citylabel = Label(edit, text="Enter city name : ")
    citylabel.grid(row=3, column=0)
    statelabel = Label(edit, text="Enter state : ")
    statelabel.grid(row=4, column=0)
    zipcodelabel = Label(edit, text="Enter zipcode : ")
    zipcodelabel.grid(row=5, column=0)

    # Entry widget ~~~~~~
    f_name = Entry(edit, width=30, bg='pink2')
    f_name.grid(row=0, column=1, padx=20)
    l_name = Entry(edit, width=30, bg='pink2')
    l_name.grid(row=1, column=1, padx=20)
    address = Entry(edit, width=30, bg='pink2')
    address.grid(row=2, column=1, padx=20)
    city = Entry(edit, width=30, bg='pink2')
    city.grid(row=3, column=1, padx=20)
    state = Entry(edit, width=30, bg='pink2')
    state.grid(row=4, column=1, padx=20)
    zipcode = Entry(edit, width=30, bg='pink2')
    zipcode.grid(row=5, column=1, padx=20)


    # prnting in edit box
    record_id=oid.get()
    cur.execute("SELECT * FROM ADDRESSES WHERE oid= "+ record_id)
    editRecords=cur.fetchall()
    # so now all the data of given id is in editRecords
    # now...
    for record in editRecords:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])



# SAVE FUNCTION FOR SAVING UPDATED INFORMATION
    def save():
        db1=sqlite3.connect("AddressBook.db")
        cur= db1.cursor()

        # we have to use names as used while creating the table
        cur.execute('''UPDATE ADDRESSES SET 
        fIRST_name = :first,
        lAST_name = :last,
        address = :address,
        city = :city,                                   
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid''',
        {
            'first' : f_name.get(),
            'last' : l_name.get(),
            'address' : address.get(),
            'city' : city.get(),
            'state' : state.get(),
            'zipcode' : zipcode.get(),

            'oid' : record_id
        })    # using python dictionary again

        savedLabel= Label(edit, text='SAVED!\nClose the window', fg='pink3')
        savedLabel.grid(row=9, column=0, columnspan=2)

        db1.commit()

        db1.close()




    btn1=Button(edit, text="SAVE", command=save, bg='plum3')
    btn1.grid(row=6, column=0, columnspan=2, pady=(10,0),ipadx=100)

    db1.commit()

    db1.close()



# BUTTONS

#creating submit button
btn=Button(root, text="ADD INFORMATION",fg='white', bg='pink2', command=add )
btn.grid(row=6, column=0, columnspan=2, pady=(10,0),ipadx=100)   # ipad stretches the button
#creating show records button
btn2=Button(root, text="SHOW INFORMATION",fg='white', bg='pink2', command= show)
btn2.grid(row=7, column=0, columnspan=2,pady=(10,0), ipadx=95)
#creating delete button
btn3=Button(root, text="DELETE INFORMATION",fg='white', bg='pink2', command= delete)
btn3.grid(row=10, column=0, columnspan=2,pady=(10,0), ipadx=95)
#creating update button
btn4=Button(root, text="EDIT INFORMATION",fg='white', bg='pink2', command= update)
btn4.grid(row=11, column=0, columnspan=2,pady=(10,0), ipadx=102)




root.mainloop()
