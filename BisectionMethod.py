from PreConfig import *


# **********************************     Function Logic       **********************************************

def get_x_lower():
    return float(XLowerEntry.get())

def get_x_upper():
    return float(XUpperEntry.get())

def get_epson():
    return float(EpsEntry.get())
    


def Evaluate_Function(var):
    exp=entry.get().replace('x', "*"+str(var)).replace("^","**")
    return float(eval(exp))

    


def bisect():
    xl=get_x_lower()
    xu=get_x_upper()
    ep=get_epson()

    xr=0.0
    xr_old=0.0
    error=0.0
    i=0

    while True:

        FXL=Evaluate_Function(xl)
        FXU=Evaluate_Function(xu)
        if FXL*FXU>=0:
            messagebox.showwarning("Warning!!","Has No Solution")
            exit()


        xr_old=xr
        xr=(xl+xu)/2
        
        FXR=Evaluate_Function(xr)

        
        error=abs((xr-xr_old)/xr)*100

        
        if i==0:
            table.insert(parent='', index='end', iid=i, text='',values=(i,xl,"{:.3f}".format(FXL),xu,"{:.3f}".format(FXU),xr,"{:.3f}".format(FXR),'-'))
        else:
            table.insert(parent='', index='end', iid=i, text='',values=(i,xl,"{:.3f}".format(FXL),xu,"{:.3f}".format(FXU),xr,"{:.3f}".format(FXR), "{:.2f}".format(error)+"%"))

        i=i+1

        if FXL*FXR>0:
            xl=xr
        elif FXL*FXR<0:
            xu=xr

        if error<=ep:
            break


    ResultRoot['text']=f"The Root is :{xr} "

    
    return xr 


# **********************************     GUI       **********************************************

Frame1=Frame(root,width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')

LabelTitle=Label(Frame1,text='Bisection Method',width='300',font=('', 16, 'bold'))
LabelTitle.pack(padx='5',pady='5')

XlowerLAbel=Label(root,text=' X lower',font=('', 11, 'bold')).pack(padx='10')
XLowerEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
XLowerEntry.pack(padx='5',pady='5')

XUpperLAbel=Label(root,text=' X Upper',font=('', 11, 'bold')).pack(padx='10')
XUpperEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
XUpperEntry.pack(padx='5',pady='5')

EpsLabel=Label(root,text='Epson',font=('', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
EpsEntry.pack(padx='5',pady='5')

f=Label(root, text="f(x)",font=('', 11, 'bold')).pack()
entry = Entry(root,borderwidth=5,width='30',justify=CENTER)
entry.pack(padx='10',pady='10')


# **********************************     TABLE       **********************************************
table=ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8),show='headings',height=15)
table.pack()
table.column("1",anchor=CENTER, stretch=NO, width=100)
table.heading(1,text='i')
table.column("2",anchor=CENTER, stretch=NO, width=100)
table.heading(2,text='Xl')
table.column("3",anchor=CENTER, stretch=NO, width=100)
table.heading(3,text='F(Xl)')
table.column("4",anchor=CENTER, stretch=NO, width=100)
table.heading(4,text='Xu')
table.column("5",anchor=CENTER, stretch=NO, width=100)
table.heading(5,text='F(Xu)')
table.column("6",anchor=CENTER, stretch=NO, width=100)
table.heading(6,text='Xr')
table.column("7",anchor=CENTER, stretch=NO, width=100)
table.heading(7,text='F(Xr)')
table.column("8",anchor=CENTER, stretch=NO, width=100)
table.heading(8,text='Error%')

ButtonRes=Button(root,text='Determine Root',font=('', 11, 'bold'),command=bisect).pack(padx='5',pady='5')
ResultRoot=Label(root,text=" ",font=('', 14, 'bold'))
ResultRoot.pack()

root.mainloop()