from PreConfig import *
from sympy import symbols, diff

def get_x_node():
    return float(XNodeEntry.get())

def get_epson():
    return float(EpsEntry.get())

def get_func():
        return entry.get().replace('x', "*x").replace("^","**")


def Evaluate_Function(var):
    exp=get_func().replace('x',str(var))
    return float(eval(exp))

def Evaluate_Derivative(var):
    f=get_func()
    x = symbols('x')
    f_derivative = str(diff(f, x))
    exp=f_derivative.replace('x',str(var))
    return float(eval(exp))



def newton():
    i=0
    xo=get_x_node()
    ep=get_epson()
    xi=xo
    xi_minus1=0.0
    while True:
        f_xi=Evaluate_Function(xi)
        fdash_xi=Evaluate_Derivative(xi)
        error=abs((xi-xi_minus1)/xi)*100

        if i==0:
            iter.insert(parent='', index='end', iid=i, text='',values=(i,xi,f_xi,fdash_xi,"-"))
        else:
            iter.insert(parent='', index='end', iid=i, text='',values=(i,xi,f_xi,fdash_xi,error))
        
        i=i+1
        xi_minus1=xi
        xi=xi-(f_xi/fdash_xi)

        if i>0:
            if error<=ep:
                break

    ResultRoot['text']=f"The Root is :{xi} "
    
    return xi

#########################################################################

Frame1=Frame(root,width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')

LabelTitle=Label(Frame1,text='Newton Method',width='300',font=('', 16, 'bold'))
LabelTitle.pack(padx='5',pady='5')

XNodeLabel=Label(root,text=' Xo',font=('', 11, 'bold')).pack(padx='10')
XNodeEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
XNodeEntry.pack(padx='5',pady='5')


EpsLabel=Label(root,text=' Epson',font=('', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(root,borderwidth=5,width='30',justify=CENTER)
EpsEntry.pack(padx='5',pady='5')

fx_flabel=Label(root, text="f(x)",font=('', 11, 'bold')).pack()
entry = Entry(root,borderwidth=5,width='30',justify=CENTER)
entry.pack(padx='10',pady='10')



#########################################################################


iter=ttk.Treeview(root,columns=(1,2,3,4,5),show='headings',height=8)
iter.pack()
iter.column("1",anchor=CENTER, stretch=NO, width=100)
iter.heading(1,text='i',anchor=CENTER)
iter.column("2",anchor=CENTER, stretch=NO, width=100)
iter.heading(2,text='Xi',anchor=CENTER)
iter.column("3",anchor=CENTER, stretch=NO, width=100)
iter.heading(3,text='f(Xi)',anchor=CENTER)
iter.column("4",anchor=CENTER, stretch=NO, width=100)
iter.heading(4,text='f\'(Xi)',anchor=CENTER)
iter.column("5",anchor=CENTER, stretch=NO, width=100)
iter.heading(5,text='Error%',anchor=CENTER)

ButtonRes=Button(root,text='Determine Root',font=('', 11, 'bold'),command=newton).pack(padx='5',pady='5')
ResultRoot=Label(root,text=" ",font=('', 14, 'bold'))
ResultRoot.pack()
root.mainloop()