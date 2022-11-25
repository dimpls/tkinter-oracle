import datetime
import tkinter.ttk
import csv

import cx_Oracle
from tkinter import *
from tkinter import messagebox

update_date = 0
tmp_select = 0
table_selected = "Participants"
root = Tk()

# def selected(combobox):
#     global table_selected
#     table_selected = combobox.get()
#     print(table_selected)

def inition(tree):
    conStr = 'system/admin123@127.0.0.1/xe'

    conn = cx_Oracle.connect(conStr)
    cur = conn.cursor()
    data = 'select * from database.participants'

    cur.execute(data)
    res = cur.fetchall()



    columns = ("ID", "FNAME", "ACADEMICDEGREE", "PLACEOFWORK", "POSITION", "CITIZENSHIP", "BDATE")


    for i in range(len(columns)):
        tree.heading(str(columns[i]), text=str(columns[i]))
        tree.column(str(columns[i]), width=150)

    for row in res:
        tree.insert("", END, values=row)

def click_button1():
    btn_delete['state'] = DISABLED
    btn_update['state'] = DISABLED
    def click_button2(event):
        global table_selected
        selection = combobox.get()
        table_selected = selection
        print(selection)

        global tree
        tree.destroy()

        tables = ["Award", "Papers", "Participants", "Section"]

        if (selection == tables[0]):
            columns = ("ID", "PRICE")
            data = 'select * from database.award'
        elif (selection == tables[1]):
            columns = ("ID_R", "TITLE", "ID", "TYPE", "SECTIONNAME", "SDATE")
            data = 'select * from database.papers'
        elif (selection == tables[2]):
            columns = ("ID", "FNAME", "ACADEMICDEGREE", "PLACEOFWORK", "POSITION", "CITIZENSHIP", "BDATE")
            data = 'select * from database.participants'
        elif (selection == tables[3]):
            columns = ("SECTION_NUM", "SECTION_NAME", "DESCRIPTION")
            data = 'select * from database.section'

        tree = tkinter.ttk.Treeview(columns=columns, show="headings", height=8)
        tree.place(x=10, y=150)
        conStr = 'system/admin123@127.0.0.1/xe'

        conn = cx_Oracle.connect(conStr)
        cur = conn.cursor()
        cur.execute(data)
        res = cur.fetchall()


        for i in range(len(columns)):
            tree.heading(str(columns[i]), text=str(columns[i]))
            tree.column(str(columns[i]), width=150)

        for row in res:
            tree.insert("", END, values=row)

        tree.bind('<ButtonRelease-1>', unlock)


    tables = ["Award", "Papers", "Participants", "Section"]
    new_window_1 = Tk()
    new_window_1.title('Выбор таблицы')
    new_window_1.geometry('200x200')
    new_window_1.resizable(width=False, height=False)

    combobox = tkinter.ttk.Combobox(new_window_1, values=tables)
    combobox.pack(anchor=NW, padx=6, pady=6)

    btn3 = tkinter.ttk.Button(new_window_1, text="Ok", command=new_window_1.destroy)
    btn3.place(x=10, y=50)
    combobox.bind("<<ComboboxSelected>>", click_button2)

#
# #insert
# #sqlText = 'insert into database.award values(1551, 555)'
# #cur.execute(sqlText)
#
#
# #get data

# print(type(res))
# for row in res:
#     print(row)
#
# #conn.commit()
#
# cur.close()
# conn.close()

def insertData():

    def getDataFromEmpty():

        if (table_selected == "Award"):
            conStr = 'system/admin123@127.0.0.1/xe'

            conn = cx_Oracle.connect(conStr)
            cur = conn.cursor()

            text = []
            text.append(box4_1.get())
            text.append(box4_2.get())


            sqlText = 'insert into database.award(ID, PRICE) values(:ID, :PRICE)'

            try:
                cur.execute(sqlText, text)
                conn.commit()
                tree.insert("", END, values=text)
            except cx_Oracle.IntegrityError as e:
                messagebox.showwarning("Ошибка", "Проверьте введенные данные и попробуйте заново")
            else:
                print("DONE")

            text = tuple(text)

            print(text, type(text))
        elif(table_selected == 'Section'):
            conStr = 'system/admin123@127.0.0.1/xe'
            conn = cx_Oracle.connect(conStr)
            cur = conn.cursor()

            text = []
            text.append(box3_1.get())
            text.append(box3_2.get())
            text.append(box3_3.get())

            sqlText = 'insert into database.section(SECTION_NUM, SECTION_NAME, DESCRIPTION) values(:SECTION_NUM, :SECTION_NAME, :DESCRIPTION)'

            try:
                cur.execute(sqlText, text)
                conn.commit()
                tree.insert("", END, values=text)
            except cx_Oracle.IntegrityError as e:
                messagebox.showwarning("Ошибка", "Проверьте введенные данные и попробуйте заново")
            else:
                print("DONE")
            text = tuple(text)

            print(text, type(text))


        elif(table_selected == 'Papers'):
            conStr = 'system/admin123@127.0.0.1/xe'
            conn = cx_Oracle.connect(conStr)
            cur = conn.cursor()

            text = []
            text.append(box2_1.get())
            text.append(box2_2.get())
            text.append(box2_3.get())
            text.append(box2_4.get())
            text.append(box2_5.get())
            time = box2_6.get().split('/')
            d = datetime.datetime(int(time[2]), int(time[1]), int(time[0]), 0, 0)
            text.append(d)
            sqlText = 'insert into database.papers(ID_R, TITLE, ID, TYPE, SECTIONNAME, SDATE) values(:ID_R, :ITLE, :ID, :TYPE, :SECTIONNAME, :SDATE)'

            text = tuple(text)
            try:
                cur.execute(sqlText, text)
                conn.commit()
                tree.insert("", END, values=text)
            except cx_Oracle.IntegrityError as e:
                messagebox.showwarning("Ошибка", "Проверьте введенные данные и попробуйте заново")
            else:
                print("DONE")
            print(text)
        elif(table_selected == 'Participants'):

            conStr = 'system/admin123@127.0.0.1/xe'
            conn = cx_Oracle.connect(conStr)
            cur = conn.cursor()

            text = []
            text.append(box1_1.get())
            text.append(box1_2.get())
            text.append(box1_3.get())
            text.append(box1_4.get())
            text.append(box1_5.get())
            text.append(box1_6.get())
            time = box1_7.get().split('/')
            d = datetime.datetime(int(time[2]), int(time[1]), int(time[0]), 0, 0)
            text.append(d)

            sqlText = 'insert into database.participants(ID, FNAME, ACADEMICDEGREE, PLACEOFWORK, POSITION, CITIZENSHIP, BDATE) values(:ID, :FNAME, :ACADEMICDEGREE, :PLACEOFWORK, :POSITION, :CITIZENSHIP, :BDATE)'

            text = tuple(text)

            try:
                cur.execute(sqlText, text)
                conn.commit()
                tree.insert("", END, values=text)
            except cx_Oracle.IntegrityError as e:
                messagebox.showwarning("Ошибка", "Проверьте введенные данные и попробуйте заново")
            else:
                print("DONE")

            print(text)
    global table_selected
    new_window_2 = Tk()
    new_window_2.title('Выбор таблицы')

    new_window_2.resizable(width=False, height=False)
    if(table_selected == "Participants"):
        new_window_2.geometry('900x150')
        text1 = Label(new_window_2, text="ID")
        text1.place(x=40, y=30)
        box1_1 = Entry(new_window_2, width=6)
        box1_1.place(x=30, y=60)

        text2 = Label(new_window_2, text="FNAME")
        text2.place(x=112, y=30)
        box1_2 = Entry(new_window_2, width=15)
        box1_2.place(x=90, y=60)

        text3 = Label(new_window_2, text="ACADEMICDEGREE")
        text3.place(x=220, y=30)
        box1_3 = Entry(new_window_2, width=17)
        box1_3.place(x=220, y=60)

        text4 = Label(new_window_2, text="PLACEOFWORK")
        text4.place(x=363, y=30)
        box1_4 = Entry(new_window_2, width=15)
        box1_4.place(x=360, y=60)

        text5 = Label(new_window_2, text="POSITION")
        text5.place(x=505, y=30)
        box1_5 = Entry(new_window_2, width=15)
        box1_5.place(x=490, y=60)

        text6 = Label(new_window_2, text="CITIZENSHIP")
        text6.place(x=630, y=30)
        box1_6 = Entry(new_window_2, width=17)
        box1_6.place(x=615, y=60)

        text7 = Label(new_window_2, text="BDATE")
        text7.place(x=775, y=30)
        box1_7 = Entry(new_window_2, width=15)
        box1_7.place(x=750, y=60)

        btn4 = tkinter.ttk.Button(new_window_2, text="Insert", command=getDataFromEmpty)
        btn4.place(x=760, y=110)

    elif(table_selected == "Papers"):
        new_window_2.geometry('760x150')
        text1 = Label(new_window_2, text="ID_R")
        text1.place(x=40, y=30)
        box2_1 = Entry(new_window_2, width=6)
        box2_1.place(x=30, y=60)

        text2 = Label(new_window_2, text="TITLE")
        text2.place(x=117, y=30)
        box2_2 = Entry(new_window_2, width=15)
        box2_2.place(x=90, y=60)

        text3 = Label(new_window_2, text="ID")
        text3.place(x=267, y=30)
        box2_3 = Entry(new_window_2, width=17)
        box2_3.place(x=220, y=60)

        text4 = Label(new_window_2, text="TYPE")
        text4.place(x=395, y=30)
        box2_4 = Entry(new_window_2, width=15)
        box2_4.place(x=360, y=60)

        text5 = Label(new_window_2, text="SECTIONNAME")
        text5.place(x=494, y=30)
        box2_5 = Entry(new_window_2, width=15)
        box2_5.place(x=490, y=60)

        text6 = Label(new_window_2, text="SDATE")
        text6.place(x=645, y=30)
        box2_6 = Entry(new_window_2, width=17)
        box2_6.place(x=615, y=60)

        btn4 = tkinter.ttk.Button(new_window_2, text="Insert", command=getDataFromEmpty)
        btn4.place(x=630, y=110)

    elif(table_selected == "Section"):
        new_window_2.geometry('455x150')
        text1 = Label(new_window_2, text="SECTION_NUM")
        text1.place(x=35, y=30)
        box3_1 = Entry(new_window_2, width=17)
        box3_1.place(x=30, y=60)

        text2 = Label(new_window_2, text="SECTION_NAME")
        text2.place(x=177, y=30)
        box3_2 = Entry(new_window_2, width=17)
        box3_2.place(x=170, y=60)

        text3 = Label(new_window_2, text="DESCRIPTION")
        text3.place(x=320, y=30)
        box3_3 = Entry(new_window_2, width=17)
        box3_3.place(x=310, y=60)

        btn4 = tkinter.ttk.Button(new_window_2, text="Insert", command=getDataFromEmpty)
        btn4.place(x=325, y=110)

    elif(table_selected == "Award"):
        columns = ("ID", "PRICE")

        new_window_2.geometry('260x150')
        text1 = Label(new_window_2, text="ID")
        text1.place(x=55, y=30)
        box4_1 = Entry(new_window_2, width=10)
        box4_1.place(x=30, y=60)

        text2 = Label(new_window_2, text="PRICE")
        text2.place(x=163, y=30)
        box4_2 = Entry(new_window_2, width=13)
        box4_2.place(x=140, y=60)

        btn4 = tkinter.ttk.Button(new_window_2, text="Insert", command=getDataFromEmpty)
        btn4.place(x=142, y=110)

def updateData():

    def update_func():
        conStr = 'system/admin123@127.0.0.1/xe'
        conn = cx_Oracle.connect(conStr)
        cur = conn.cursor()

        global table_selected
        selected = tree.focus()
        if(table_selected == 'Participants'):

            temp = []
            for child in tree.get_children():
                if (box1_1.get() in str(tree.item(child)['values'])):
                    print(tree.item(child), "!!")
                    temp.append(child)
            for i in range(len(temp)):
                tree.item(temp[i], text="", values=(box1_1.get(), box1_2.get(), box1_3.get(), box1_4.get(), box1_5.get(), box1_6.get(), box1_7.get()))

            text = []
            text.append(box1_1.get())
            text.append(box1_2.get())
            text.append(box1_3.get())
            text.append(box1_4.get())
            text.append(box1_5.get())
            text.append(box1_6.get())
            time = box1_7.get().split('-')

            print(time)
            d = datetime.datetime(int(time[0]), int(time[1]), int(time[2][0:2]), 0, 0)

            text.append(d)

            cur.execute("""update database.participants set
                        ID = :ID,
                        FNAME = :FNAME,
                        ACADEMICDEGREE = :ACADEMICDEGREE,
                        PLACEOFWORK = :PLACEOFWORK,
                        POSITION = :POSITION,
                        CITIZENSHIP = :CITIZENSHIP,
                        BDATE = :BDATE
                        where ID = :ID""",
                        {
                            'ID': text[0],
                            'FNAME': text[1],
                            'ACADEMICDEGREE': text[2],
                            'PLACEOFWORK': text[3],
                            'POSITION': text[4],
                            'CITIZENSHIP': text[5],
                            'BDATE': text[6]
                        })
            conn.commit()
            print(text)
        elif(table_selected == 'Papers'):

            temp = []
            for child in tree.get_children():
                if (box2_1.get() in str(tree.item(child)['values'])):
                    print(tree.item(child), "!!")
                    temp.append(child)
            for i in range(len(temp)):
                tree.item(temp[i], text="", values=(box2_1.get(), box2_2.get(), box2_3.get(), box2_4.get(), box2_5.get(), box2_6.get()))

            text = []
            text.append(box2_1.get())
            text.append(box2_2.get())
            text.append(box2_3.get())
            text.append(box2_4.get())
            text.append(box2_5.get())
            time = box2_6.get().split('-')

            print(time)
            d = datetime.datetime(int(time[0]), int(time[1]), int(time[2][0:2]), 0, 0)

            text.append(d)

            cur.execute("""update database.papers set
                                    ID_R = :ID_R,
                                    TITLE = :TITLE,
                                    ID = :ID,
                                    TYPE = :TYPE,
                                    SECTIONNAME = :SECTIONNAME,
                                    SDATE = :SDATE
                                    where ID_R = :ID_R""",
                                    {
                                    'ID_R': text[0],
                                    'TITLE': text[1],
                                    'ID': text[2],
                                    'TYPE': text[3],
                                    'SECTIONNAME': text[4],
                                    'SDATE': text[5]
                        })
            conn.commit()

            print(text)

        elif(table_selected == 'Section'):
            temp = []
            for child in tree.get_children():
                if(box3_1.get() in str(tree.item(child)['values'])):
                    print(tree.item(child), "!!")
                    temp.append(child)
            for i in range(len(temp)):
                tree.item(temp[i], text="", values=(box3_1.get(), box3_2.get(), box3_3.get()))
            text = []
            text.append(box3_1.get())
            text.append(box3_2.get())
            text.append(box3_3.get())

            cur.execute("""update database.section set
                                                SECTION_NUM = :SECTION_NUM,
                                                SECTION_NAME = :SECTION_NAME,
                                                DESCRIPTION = :DESCRIPTION
                                                where SECTION_NUM = :SECTION_NUM""",
                        {
                            'SECTION_NUM': text[0],
                            'SECTION_NAME': text[1],
                            'DESCRIPTION': text[2],
                        })
            conn.commit()

            print(text)
        elif(table_selected == "Award"):
            print(type(box4_1.get()))
            temp = []
            for child in tree.get_children():
                if(box4_1.get() in str(tree.item(child)['values'])):
                    print(tree.item(child), "!!")
                    temp.append(child)
            for i in range(len(temp)):
                tree.item(temp[i], text="", values=(box4_1.get(), box4_2.get()))

            text = []
            text.append(box4_1.get())
            text.append(box4_2.get())
            cur.execute("""update database.award set
                                                ID = :ID,
                                                PRICE = :PRICE
                                                where ID = :ID""",
                        {
                            'ID': text[0],
                            'PRICE': text[1],
                        })
            conn.commit()
            box4_1.delete(0, END)
            box4_2.delete(0, END)
            new_window_3.destroy()
            #print(text)

        #print(selected)
    global update_date
    global table_selected
    print(update_date)
    new_window_3 = Tk()
    new_window_3.title('Выбор таблицы')

    new_window_3.resizable(width=False, height=False)
    if (table_selected == "Participants"):
        new_window_3.geometry('900x150')
        text1 = Label(new_window_3, text="ID")
        text1.place(x=40, y=30)
        box1_1 = Entry(new_window_3, width=6)
        box1_1.insert(0, update_date[0])
        box1_1['state'] = DISABLED
        box1_1.place(x=30, y=60)

        text2 = Label(new_window_3, text="FNAME")
        text2.place(x=112, y=30)
        box1_2 = Entry(new_window_3, width=15)
        box1_2.insert(0, update_date[1])
        box1_2.place(x=90, y=60)

        text3 = Label(new_window_3, text="ACADEMICDEGREE")
        text3.place(x=220, y=30)
        box1_3 = Entry(new_window_3, width=17)
        box1_3.insert(0, update_date[2])
        box1_3.place(x=220, y=60)

        text4 = Label(new_window_3, text="PLACEOFWORK")
        text4.place(x=363, y=30)
        box1_4 = Entry(new_window_3, width=15)
        box1_4.insert(0, update_date[3])
        box1_4.place(x=360, y=60)

        text5 = Label(new_window_3, text="POSITION")
        text5.place(x=505, y=30)
        box1_5 = Entry(new_window_3, width=15)
        box1_5.insert(0, update_date[4])
        box1_5.place(x=490, y=60)

        text6 = Label(new_window_3, text="CITIZENSHIP")
        text6.place(x=630, y=30)
        box1_6 = Entry(new_window_3, width=17)
        box1_6.insert(0, update_date[5])
        box1_6.place(x=615, y=60)

        text7 = Label(new_window_3, text="BDATE")
        text7.place(x=775, y=30)
        box1_7 = Entry(new_window_3, width=15)
        box1_7.insert(0, update_date[6])
        box1_7.place(x=750, y=60)

        btn4 = tkinter.ttk.Button(new_window_3, text="Update", command=update_func)
        btn4.place(x=760, y=110)

    elif (table_selected == "Papers"):
        new_window_3.geometry('760x150')
        text1 = Label(new_window_3, text="ID_R")
        text1.place(x=40, y=30)
        box2_1 = Entry(new_window_3, width=6)
        box2_1.insert(0, update_date[0])
        box2_1['state'] = DISABLED
        box2_1.place(x=30, y=60)

        text2 = Label(new_window_3, text="TITLE")
        text2.place(x=117, y=30)
        box2_2 = Entry(new_window_3, width=15)
        box2_2.insert(0, update_date[1])
        box2_2.place(x=90, y=60)

        text3 = Label(new_window_3, text="ID")
        text3.place(x=267, y=30)
        box2_3 = Entry(new_window_3, width=17)
        box2_3.insert(0, update_date[2])
        box2_3.place(x=220, y=60)

        text4 = Label(new_window_3, text="TYPE")
        text4.place(x=395, y=30)
        box2_4 = Entry(new_window_3, width=15)
        box2_4.insert(0, update_date[3])
        box2_4.place(x=360, y=60)

        text5 = Label(new_window_3, text="SECTIONNAME")
        text5.place(x=494, y=30)
        box2_5 = Entry(new_window_3, width=15)
        box2_5.insert(0, update_date[4])
        box2_5.place(x=490, y=60)

        text6 = Label(new_window_3, text="SDATE")
        text6.place(x=645, y=30)
        box2_6 = Entry(new_window_3, width=17)
        box2_6.insert(0, update_date[5])
        box2_6.place(x=615, y=60)

        btn4 = tkinter.ttk.Button(new_window_3, text="Update", command=update_func)
        btn4.place(x=630, y=110)

    elif (table_selected == "Section"):
        new_window_3.geometry('455x150')
        text1 = Label(new_window_3, text="SECTION_NUM")
        text1.place(x=35, y=30)
        box3_1 = Entry(new_window_3, width=17)
        box3_1.insert(0, update_date[0])
        box3_1['state'] = DISABLED
        box3_1.place(x=30, y=60)

        text2 = Label(new_window_3, text="SECTION_NAME")
        text2.place(x=177, y=30)
        box3_2 = Entry(new_window_3, width=17)
        box3_2.insert(0, update_date[1])
        box3_2.place(x=170, y=60)

        text3 = Label(new_window_3, text="DESCRIPTION")
        text3.place(x=320, y=30)
        box3_3 = Entry(new_window_3, width=17)
        box3_3.insert(0, update_date[2])
        box3_3.place(x=310, y=60)

        btn4 = tkinter.ttk.Button(new_window_3, text="Update", command=update_func)
        btn4.place(x=325, y=110)

    elif (table_selected == "Award"):
        columns = ("ID", "PRICE")

        new_window_3.geometry('260x150')
        text1 = Label(new_window_3, text="ID")
        text1.place(x=55, y=30)
        box4_1 = Entry(new_window_3, width=10)
        box4_1.insert(0, update_date[0])
        box4_1['state'] = DISABLED
        box4_1.place(x=30, y=60)

        text2 = Label(new_window_3, text="PRICE")
        text2.place(x=163, y=30)
        box4_2 = Entry(new_window_3, width=13)
        box4_2.insert(0, update_date[1])
        box4_2.place(x=140, y=60)

        btn4 = tkinter.ttk.Button(new_window_3, text="Update", command=update_func)
        btn4.place(x=142, y=110)

def unlock(event):
    global update_date
    btn_update['state'] = NORMAL
    btn_delete['state'] = NORMAL
    test = tree.item(tree.selection())
    print(test)
    update_date = tuple(test.get('values'))

def deleteRow():
    conStr = 'system/admin123@127.0.0.1/xe'
    conn = cx_Oracle.connect(conStr)
    cur = conn.cursor()

    global table_selected

    x = tree.selection()[0]
    temp = tuple(tree.item(x)['values'])

    if(table_selected == 'Participants'):
        try:
            cur.execute("""delete from database.participants
                                        where ID = :ID""",
                        {
                            'ID': temp[0],
                        })
            conn.commit()
            tree.delete(x)
        except cx_Oracle.IntegrityError as e:
            messagebox.showwarning("Ошибка", "Ошибка удаления")
    elif(table_selected == 'Papers'):
        try:
            cur.execute("""delete from database.papers
                                        where ID_R = :ID_R""",
                        {
                            'ID_R': temp[0],
                        })
            conn.commit()
            tree.delete(x)
        except cx_Oracle.IntegrityError as e:
            messagebox.showwarning("Ошибка", "Ошибка удаления")
    elif(table_selected == 'Section'):
        try:
            cur.execute("""delete from database.section
                                        where SECTION_NUM = :SECTION_NUM""",
                        {
                            'SECTION_NUM': temp[0],
                        })
            conn.commit()
            tree.delete(x)
        except cx_Oracle.IntegrityError as e:
            messagebox.showwarning("Ошибка", "Ошибка удаления")
    elif(table_selected == 'Award'):
        try:
            tmp = []
            tmp2 = tree.item(tree.selection())
            tmp3 = tuple(tmp2.get('values'))
            for child in tree.get_children():
                if (tmp3[0] in tree.item(child)['values']):
                    print(tree.item(child), "!!")
                    tmp.append(child)

            for i in range(len(tmp)):
                tree.delete(tmp[i])

            cur.execute("""delete from database.award
                                        where ID = :ID""",
                        {
                            'ID': temp[0],
                        })
            conn.commit()

        except cx_Oracle.IntegrityError as e:
            messagebox.showwarning("Ошибка", "Ошибка удаления")

def savePapers():
    conn = cx_Oracle.connect(conStr)
    cur = conn.cursor()
    data = 'select * from database.papers'
    cur.execute(data)
    res = cur.fetchall()
    print(type(res))

    with open('Papers.cvs', 'w') as out:
        cvs_out = csv.writer(out)
        cvs_out.writerow(['ID_R', 'TITLE', 'ID', 'TYPE', 'SECTIONNAME', 'SDATE'])
        for row in res:
            print(row)
            cvs_out.writerow(row)



root.title('Лабораторная работа №9')
root.geometry('1080x480')
root.resizable(width=False, height=False)
tables = ["Award", "Papers", "Participants", "Section"]

btn1 = tkinter.ttk.Button(text="Выбрать новую таблицу", command=click_button1)
btn1.place(x=10, y=50)

btn2 = tkinter.ttk.Button(text="insert", command=insertData)
btn2.place(x=180, y=50)

btn_update = tkinter.ttk.Button(text="update", command=updateData, state=tkinter.DISABLED)
btn_update.place(x=280, y=50)

btn_delete = tkinter.ttk.Button(text="delete", command=deleteRow, state=tkinter.DISABLED)
btn_delete.place(x=380, y=50)

btn_save = tkinter.ttk.Button(text="save", command=savePapers)
btn_save.place(x=480, y=50)

columns = ("ID", "FNAME", "ACADEMICDEGREE", "PLACEOFWORK", "POSITION", "CITIZENSHIP", "BDATE")
tree = tkinter.ttk.Treeview(columns=columns, show="headings", height=8)
tree.place(x=10, y=150)
tree.bind('<ButtonRelease-1>', unlock)
inition(tree)



conStr = 'system/admin123@127.0.0.1/xe'

conn = cx_Oracle.connect(conStr)
cur = conn.cursor()
data = 'select * from database.participants'

cur.execute(data)
res = cur.fetchall()
#tableViewParticipants(res)

print(res)
print(type(res[0]))

root.mainloop()
