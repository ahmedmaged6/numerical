from PreConfig import *

def get_x_minus1():
    return float(XMinusOneEntry.get())

def get_x_node():
    return float(XNodeEntry.get())

def get_epson():
    return float(EpsEntry.get())


def Evaluate_Function(var):
    exp=entry.get().replace('x', "*"+str(var)).replace("^","**")
    return float(eval(exp))


def secant():
    x_1=get_x_minus1()
    xi=get_x_node()
    ep=get_epson()
    x1=0
    i=0

    while True:
        FX_1=Evaluate_Function(x_1)
        Fxi=Evaluate_Function(xi)
        error=abs((xi-x_1)/xi)*100

        
        if i==0:
            iter.insert(parent='', index='end', iid=i, text='',values=(i,x_1,FX_1,xi,Fxi,"-"))
        else:
            iter.insert(parent='', index='end', iid=i, text='',values=(i,x_1,FX_1,xi,Fxi,error))

        i=i+1
        xMin1=xi
        xi=xi-((Fxi*(x_1-xi))/(FX_1-Fxi))  
        print(xi)
        x_1=xMin1

        if i>0:
            if error<=ep:
                break

    ResultRoot['text']=f"The Root is :{xi} "
    
    return xi



#########################################################################
Frame1=Frame(root,width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')

LabelTitle=Label(Frame1,text='Secant Method',width='300',font=('', 16, 'bold'))
LabelTitle.pack(padx='5',pady='5')

XMinusOneLabel=Label(root,text="xi-1",font=('', 11, 'bold')).pack(padx='10')
XMinusOneEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
XMinusOneEntry.pack(padx='5',pady='5')

XNodeLabel=Label(root,text=' xi',font=('', 11, 'bold')).pack(padx='10')
XNodeEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
XNodeEntry.pack(padx='5',pady='5')


EpsLabel=Label(root,text=' Epson',font=('', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
EpsEntry.pack(padx='5',pady='5')

fx_flabel=Label(root, text="f(x)",font=('', 11, 'bold')).pack()
entry = Entry(root,borderwidth=5,width='30',justify=CENTER)
entry.pack(padx='10',pady='10')



#########################################################################


iter=ttk.Treeview(root,columns=(1,2,3,4,5,6),show='headings',height=8)
iter.pack()
iter.column("1",anchor=CENTER, stretch=NO, width=100)
iter.heading(1,text='i',anchor=CENTER)
iter.column("2",anchor=CENTER, stretch=NO, width=100)
iter.heading(2,text="Xi-1",anchor=CENTER)
iter.column("3",anchor=CENTER, stretch=NO, width=100)
iter.heading(3,text='f(xi-1)',anchor=CENTER)
iter.column("4",anchor=CENTER, stretch=NO, width=100)
iter.heading(4,text='xᵢ',anchor=CENTER)
iter.column("5",anchor=CENTER, stretch=NO, width=100)
iter.heading(5,text='f(xᵢ)',anchor=CENTER)
iter.column("6",anchor=CENTER, stretch=NO, width=100)
iter.heading(6,text='ُError%',anchor=CENTER)


ButtonRes=Button(root,text='Determine Root',font=('', 11, 'bold'),command=secant).pack(padx='5',pady='5')
ResultRoot=Label(root,text=" ",font=('', 14, 'bold'))
ResultRoot.pack()

root.mainloop()