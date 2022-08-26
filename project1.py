from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import math
import pyodbc
m=Tk()
m.title("Dynamo Calculator")
m.geometry('1000x600')

def cal():
    torq=float(e4.get())
    rpm=float(e5.get())
    t=float(e7.get())
    p=float(e8.get())
    rot=float(e3.get())
    w=float(e6.get())

    hp = (torq * rpm) / 5252
    cf = (1.18*((990/(p*0.01))*math.sqrt((t+273)/298)))-0.176
    chp = hp * cf
    v = (rpm / 60) * 2 * math.pi * rot
    pwr = hp / w

    ol3.config(text=round(hp,2))
    ol5.config(text=round(cf,2))
    ol7.config(text=round(chp,2))
    ol9.config(text=round(v,2))
    ol11.config(text=round(pwr,2))

def display():
    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=D:\Database1.accdb;')
    cursor1 = con.cursor()
    cursor1.execute('select * from Table1 ORDER By ID')
    rows = cursor1.fetchall()
    if len(rows) != 0:
        for i in rows:
            table.insert('', END, values=i)
    con.close()

def insert():
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Database1.accdb;')
    cursor2 = con.cursor()
    cursor2.execute(f'''INSERT INTO Table1 (id, Names, Horsepower, Corrected_Horsepower, Speed, Correction_factor, Power_weight_ratio) 
                    VALUES({e2.get()}, '{e1.get()}', {ol3['text']}, {ol7['text']}, {ol9['text']},{ol5['text']},{ol11['text']})''')
    con.commit()
    messagebox.showinfo(title='Message box',message='Record added')
    con.close()

def delete():
    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Database1.accdb;')
    cursor3 = con.cursor()
    cursor3.execute(f'''DELETE FROM Table1 WHERE id in ({e2.get()})''')
    con.commit()
    messagebox.showinfo(title='Message box',message='Record deleted')
    con.close()

def clear():
    for i in table.get_children():
        table.delete(i)


h=Label(m,text='Dynamo calculator',bg='blue',fg='white',font=('calibre',20,'bold')).pack(side=TOP,fill=X)

f1=Frame(m,bg='royalblue1')
f1.place(x=0,y=40,width=450,height=700)
f2=Frame(f1,bg='light blue')
f2.place(x=5,y=80,width=440,height=250)
l=Label(f1,text='Correction factor uses the SAE standard and includes frictional loss by the formula:',fg='white',bg='royalblue1').grid(row=0,column=0)
img=PhotoImage(file=r'D:\images.PNG').subsample(1,1)
img_l=Label(f1,image=img).grid(row=1,column=0)


#INPUTS:
l1=Label(f2,text=' Inputs: ',bg='light blue',font=('calibre',10,'bold','underline'),width=5).grid(row=0,column=0,pady=2)
ll=Label(f2,text=' ID: ',bg='light blue',font=('calibre',10,'bold','underline'),width=5).grid(row=0,column=2,pady=2)


l2=Label(f2,text='Name:',bg='light blue').grid(row=1,column=0,pady=5,padx=3)
e1=Entry(f2,bd=0)
e1.grid(row=1,column=1,pady=5)

#ID
e2=Entry(f2,bd=0)
e2.grid(row=1,column=2,pady=5)

l3=Label(f2,text='Tire Radius(m):',bg='light blue').grid(row=2,column=0,pady=5,padx=3)
e3=Entry(f2,bd=0)
e3.grid(row=2,column=1,pady=5)
b2=Button(f2,text='Calculate',bd=0,bg='royalblue1',fg='white',width=20,font=('calibre',9,'bold'),command=cal).grid(row=2,column=2,pady=5,padx=50)

l4=Label(f2,text='torque(Nm):',bg='light blue').grid(row=3,column=0,pady=5,padx=3)
e4=Entry(f2,bd=0)
e4.grid(row=3,column=1,pady=5)
b3=Button(f2,text='Display',bd=0,bg='royalblue1',fg='white',width=20,font=('calibre',9,'bold'),command=display).grid(row=3,column=2,pady=5,padx=50)

l5=Label(f2,text='RPM:',bg='light blue').grid(row=4,column=0,pady=5,padx=3)
e5=Entry(f2,bd=0)
e5.grid(row=4,column=1,pady=5)

l6=Label(f2,text='Weight(Kg):',bg='light blue').grid(row=5,column=0,pady=5,padx=3)
e6=Entry(f2,bd=0)
e6.grid(row=5,column=1,pady=5)
b4=Button(f2,text='Insert',bd=0,bg='royalblue1',fg='white',width=20,font=('calibre',9,'bold'),command=insert).grid(row=4,column=2,pady=5,padx=50)

l7=Label(f2,text='Temperature(C):',bg='light blue').grid(row=6,column=0,pady=5,padx=3)
e7=Entry(f2,bd=0)
e7.grid(row=6,column=1,pady=5)
b5=Button(f2,text='Delete',bd=0,bg='royalblue1',fg='white',width=20,font=('calibre',9,'bold'),command=delete).grid(row=5,column=2,pady=5,padx=50)

l8=Label(f2,text='Air pressure(P):',bg='light blue').grid(row=7,column=0,pady=5,padx=3)
e8=Entry(f2,bd=0)
e8.grid(row=7,column=1,pady=5)
b6=Button(f2,text='Exit',bd=0,bg='red',fg='white',width=20,command=m.destroy,font=('calibre',9,'bold')).grid(row=7, column=2,pady=5,padx=50)


b7=Button(f2,text='Clear screen',bd=0,bg='royalblue1', fg='white',width=20,command=clear ,font=('calibre',9,'bold')).grid(row=6, column=2,pady=5,padx=50)



#OUTPUTS

f3=Frame(f1,bg='light blue')
f3.place(x=5,y=335,width=440,height=185)
ol1=Label(f3,text='Outputs: ', bg='light blue', font=('calibre', 10, 'bold', 'underline')).grid(row=0, column=0, padx=7, pady=2)

ol2=Label(f3,text='Horsepower:',bg='light blue').grid(row=1,column=0,pady=5,padx=3)
ol3=Label(f3,width=20,bg='white')
ol3.grid(row=1,column=1,pady=5)

ol4=Label(f3,text='Correction factor:',bg='light blue').grid(row=2,column=0,pady=5,padx=3)
ol5=Label(f3,width=20,bg='white')
ol5.grid(row=2,column=1,pady=5)

ol6=Label(f3,text='Corrected HP:',bg='light blue').grid(row=3,column=0,pady=5,padx=3)
ol7=Label(f3,width=20,bg='white')
ol7.grid(row=3,column=1,pady=5)

ol8=Label(f3,text='Speed:',bg='light blue').grid(row=4,column=0,pady=5,padx=3)
ol9=Label(f3,width=20,bg='white')
ol9.grid(row=4,column=1,pady=5)

ol10=Label(f3,text='Power/weight ratio:',bg='light blue').grid(row=5,column=0,pady=5,padx=3)
ol11=Label(f3,width=20,bg='white')
ol11.grid(row=5,column=1,pady=5)


#lists
f=Frame(m,bg='white')
f.place(x=450,y=40,width=900,height=700)

table=ttk.Treeview(f,height=650,columns=('id','Names','Horsepower','Correction_factor','Corrected_Horsepower','Speed','Power_weight_ratio'),show='headings')

table.column("#1", width=130)
table.column("#2", width=130)
table.column("#3", width=130)
table.column("#4", width=130)
table.column("#5", width=130)
table.column("#6", width=130)
table.column("#7", width=130)

table.heading("#1", text="ID")
table.heading("#2", text="Names")
table.heading("#3", text="Horsepower")
table.heading("#4", text="Corrected Horsepower")
table.heading("#5", text="Speed(Km/h)")
table.heading("#6", text="P/W ratio")
table.heading("#7", text="Correction factor")
table.pack()
m.mainloop()

