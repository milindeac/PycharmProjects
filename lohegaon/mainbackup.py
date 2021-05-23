import pymysql
import os
from tkinter import *
from intvalidate import int_validate
from tkinter import messagebox
# import tkinter.filedialog
from tkinter import filedialog
conn=pymysql.connect(host='localhost',database='lohegaon',user='root',password='Sanjay1*')
cur=conn.cursor()
if cur:
    print ("Success")

root=Tk()
root.geometry("756x522")
root.title("LOHEGAON APP")

global item1,item2,item3,item4

def retri():
    cur.execute("select * from tenant")
    for row in cur.fetchall():
        print(row)
retri()



photo1=PhotoImage(file="main.gif")
loh_label=Label(root,image=photo1)
loh_label.pack()

def clear():
    roomno.set('')
    name.set('')
    address.set('')
    aadharno.set('')
    brent.set('')
    occupation.set('')
    mobno.set('')
    e1.configure(state='normal')

def add():
    w1 = Tk()
    w1.title('Lohegaon Rent App')
    w1.geometry('700x500')
    ptitle = Label(w1, text='''Lohegaon Bunglow App Version 1''')
    ptitle.grid(row=0, column=0, columnspan=2)
    global roomno, name, address, aadharno, brent, occupation, mobno, status , uploadaadhar,regupload
    roomno = StringVar()
    name = StringVar()
    address = StringVar()
    aadharno = StringVar()
    brent = StringVar()
    occupation = StringVar()
    mobno = StringVar()
    uploadaadhar=StringVar()
    regupload=StringVar()
    global e1, e2, e3, e4, e5, e6, e7
    l1 = Label(w1, text=' Room No ')
    e1 = Entry(w1, textvariable=roomno)
    int_validate(e1,from_=1, to=9)
    # reg = w1.register(chkroomno)
    # e1.config(validate="key", validatecommand=(reg, '%P'))
    l2 = Label(w1, text=' Tenant Name ')
    e2 = Entry(w1, textvariable=name)
    l3 = Label(w1, text=' Address ')
    e3 = Entry(w1, textvariable=address)
    l4 = Label(w1, text=' Aadhar Card No ')
    e4 = Entry(w1, textvariable=aadharno)
    # reg1 = w1.register(chkaadharno)
    # e4.config(validate="key", validatecommand=(reg1, '%P'))
    int_validate(e4, from_=0, to=999999999999)
    b1 = Button(w1, text=' Upload Aadhar ', command=upload_aadhar)

    l5 = Label(w1, text=' Basic Rent ')
    e5 = Entry(w1, textvariable=brent)
    # reg2 = w1.register(chkbrent)
    # e5.config(validate="key", validatecommand=(reg2, '%P'))
    int_validate(e5, from_=0, to=99999)
    l6 = Label(w1, text=' Occupation ')
    e6 = Entry(w1, textvariable=occupation)
    l7 = Label(w1, text=' Mobile  No ')
    e7 = Entry(w1, textvariable=mobno)

    listbox=Listbox(w1,height=20,width=60)
    listbox.grid(row=1,column=3,rowspan=8,columnspan=2)

    b2 = Button(w1, text=' Upload Registration Doc ', command=uploadreg_doc)
    # reg3 = w1.register(chkmobno)
    # e7.config(validate="key", validatecommand=(reg3, '%P'))
    int_validate(e7, from_=7000000000, to=9999999999)

    b3 = Button(w1, text=' Add ', command=addtenant)
    b4 = Button(w1, text=' Delete ', command=deltenant)
    b5 = Button(w1, text=' Modify ', command=modtenant)
    b6 = Button(w1, text=' Search ', command=searchtenant)
    b7 = Button(w1, text=' Delete All ', command=deleteall)
    b8 = Button(w1, text=' Show Records ', command=showrecords)


    l1.grid(row=1, column=0)
    e1.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    e2.grid(row=2, column=1)
    l3.grid(row=3, column=0)
    e3.grid(row=3, column=1)
    l4.grid(row=4, column=0)
    e4.grid(row=4, column=1)

    l5.grid(row=6, column=0)
    e5.grid(row=6, column=1)
    l6.grid(row=7, column=0)
    e6.grid(row=7, column=1)
    l7.grid(row=8, column=0)
    e7.grid(row=8, column=1)

    b1.grid(row=11, column=0)
    b2.grid(row=11, column=1)

    b3.grid(row=13, column=0)
    b4.grid(row=13, column=1)
    b5.grid(row=14, column=0)
    b6.grid(row=14, column=1)
    b7.grid(row=15, column=0)
    b8.grid(row=15, column=1)

    w1.mainloop()


def addtenant():
    global e1,e2,e3,e4,e5,e6,e7
    # print(e7.get())

    sql="insert into tenant(roomno,name,address,aadharno,brent,occupation,mobno) " \
        "values ('%s','%s','%s','%s','%s','%s','%s')"\
    %(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get())

    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('success','Record saved....')
    exit()
    # except:
    #     messagebox.showinfo('Error','Error in data entry')
    # finally:
    #     clear()


def upload_aadhar():
    global image_selected
    global image_file_name
    global file_new_home
    global file_to_copy
    path_to_image = filedialog.askopenfilename(initialdir="/",title="Open File",
                       filetypes=(("PNGs", "*.png"), ("GIFs", "*.gif"), ("All Files", "*.*")))
    try:
        if path_to_image:
            image_file_name = os.path.basename(path_to_image)
            file_new_home = db_config.PHOTO_DIRECTORY + image_file_name
            file_to_copy = path_to_image
            image_selected = True
            load_photo_tab_two(file_to_copy)
    except IOError as err:
        image_selected = False
        messagebox.showinfo("File Error", err)


def load_photo_tab_two(file_path):
    image = image_path(file_path)
    imgLabelTabTwo.configure(image=image)
    imgLabelTabTwo.image = image

def uploadreg_doc():
    global image_selected1
    global image_file_name1
    global file_new_home1
    global file_to_copy1
    path_to_image1 = filedialog.askopenfilename(initialdir="/",title="Open File",
                       filetypes=(("PNGs", "*.png"), ("GIFs", "*.gif"), ("All Files", "*.*")))
    try:
        if path_to_image1:
            image_file_name1 = os.path.basename(path_to_image1)
            file_new_home1 = db_config.PHOTO_DIRECTORY + image_file_name1
            file_to_copy1 = path_to_image
            image_selected1 = True
            load_photo_tab_two1(file_to_copy1)
    except IOError as err:
        image_selected1 = False
        messagebox.showinfo("File Error", err)

def load_photo_tab_two1(file_path1):
    image1 = image_path(file_path1)
    imgLabelTabTwo.configure(image=image1)
    imgLabelTabTwo.image = image1


def deltenant(roomno):
    cur.execute("Delete from tenant where roomno=?",(roomno))
    conn.commit()

def modtenant(roomno,name,address,aadharno,brent,occupation,mobno):
    cur.execute("update tenant set name=? , address=? , aadharno=? , brent=? , occupation=? , mobno=? where roomno=?",(name,address,aadharno,brent,occupation,mobno))
    conn.commit()

def searchtenant(roomno="", name="", address="", aadharno="", brent="", occupation="", mobno=""):
    cur.execute("select * from tenant where roomno=? or name=? or address=? or aadharno=? or brent=? or occupation=? or mobno=?",(roomno,name,address,aadharno,brent,occupation,mobno))
    row=cur.fetchall()
    return row

def deleteall():
    cur.execute("Delete from tenant")
    conn.commit()


def showrecords():
    cur.execute("select * from tenant")
    # row=cur.fetchall()
    for row in cur.fetchall():
        print(row)
    # return row

def msebsub():
    print("hi")

def msebmain():
    pass


def maintenance():
    print("Hi i m under construction ")

def addtanker():
    print("Hi i m under construction ")

def final():
    print("Hi i m under construction ")


mainmenu=Menu(root)
m2=Menu(mainmenu,tearoff=0)
m3=Menu(m2,tearoff=0)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Tenant",command=add)
# m1.add_command(label="Delete Tenant",command=deltenant)

mainmenu.add_cascade(label="Master",menu=m1)

m2.add_cascade(label="MSEB", menu=m3)
m2.add_command(label="Tanker",command=addtanker)
m2.add_command(label="Maintenance",command=maintenance)
m2.add_command(label="Final",command=final)

mainmenu.add_cascade(label="Monthly Bill",menu=m2)

m3.add_command(label="Main Meter Entry",command=msebmain)
m3.add_command(label="Sub Meter Entry",command=msebsub)
root.config(menu=m2)

root.config(menu=mainmenu)

root.mainloop()