from PreConfig import *

##Get Entries #####################
def get_xi():
    return float(XiEntry.get())

def get_epson():
    return float(EpsEntry.get())
    
def Evaluate_Function(var):
    exp=entry.get().replace('x', "*"+str(var)).replace("^","**")
    return float(eval(exp))

    


def simple():
    xi=get_xi()
    ep=get_epson()

    xi_min1=0
    error=0.0
    i=0

    while True:

        FXI=Evaluate_Function(xi)
    
        error=abs((xi-xi_min1)/xi)*100

        if i==0:
            table.insert(parent='', index='end', iid=i, text='',values=(i,round(xi,3),"{:.3f}".format(FXI),'-'))
        else:
            table.insert(parent='', index='end', iid=i, text='',values=(i,round(xi,3),"{:.3f}".format(FXI),"{:.2f}".format(error)+"%"))
        


        if i>0 and error<=ep:
            break

        i=i+1
        xi_min1=xi
        xi=FXI 



    ResultRoot['text']=f"The Root is :{round(xi,3)} "

    
    return xi


# **********************************     GUI       **********************************************

Frame1=Frame(root,width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')

LabelTitle=Label(Frame1,text='Simple Fixed Point Method',width='300',font=('', 16, 'bold'))
LabelTitle.pack(padx='5',pady='5')

XiLAbel=Label(root,text=' Xi',font=('', 11, 'bold')).pack(padx='10')
XiEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
XiEntry.pack(padx='5',pady='5')

EpsLabel=Label(root,text='Epson',font=('', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
EpsEntry.pack(padx='5',pady='5')

f=Label(root, text="f(x)",font=('', 11, 'bold')).pack()
entry = Entry(root,borderwidth=5,width='40',justify=CENTER)
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

ButtonRes=Button(root,text='Determine Root',font=('', 11, 'bold'),command=simple).pack(padx='5',pady='5')
ResultRoot=Label(root,text=" ",font=('', 14, 'bold'))
ResultRoot.pack()

root.mainloop()