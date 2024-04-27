from PreConfig import *

def nextPage_BisectionMethod():
    root.destroy()
    run_file('BisectionMethod.py')
def nextPage_FalsePositionMethod():
    root.destroy()
    run_file('FalsePositionMethod.py')

def nextPage_SimpleFixedPointMethod():
    root.destroy()
    run_file('SimpleFixedPoint.py')

def nextPage_SecantMethod():
    root.destroy()
    run_file('SecantMethod.py')
def nextPage_NewtonMethod():
    root.destroy()
    run_file('NewtonMethod.py')
def nextPage_GaussEliminationMethod():
    root.destroy()
    run_file('GaussEliminationMethod.py')


def nextPage_LuDecomposition():
    root.destroy()
    run_file('LuDecomposition.py')

def nextPage_Cramer():
    root.destroy()
    run_file('Cramer.py') 

LabelForTitle=Label(root,text='Numerical Analysis Calculator',fg='black',font=('', 16, 'bold')).pack(padx='10',pady='10')

LabelForList=Label(root,text='Choose a Numerical Method: ',fg='black',font=('', 14, 'bold')).pack(padx='10',pady='10')

BisectionButton=Button(root,width='50',text='Bisection Method',command=nextPage_BisectionMethod).pack(padx='3',pady='3')
FalsePositionButton=Button(root,width='50',text='False Position Method',command=nextPage_FalsePositionMethod).pack(padx='3',pady='3')
SimpleFixedButton=Button(root,width='50',text='Simple Fixed Point',command=nextPage_SimpleFixedPointMethod).pack(padx='3',pady='3')
NewtonButton=Button(root,width='50',text='Newton Method',command=nextPage_NewtonMethod).pack(padx='3',pady='3')
SecantButton=Button(root,width='50',text='Secant Method',command=nextPage_SecantMethod).pack(padx='3',pady='3')
GaussButton=Button(root,width='50',text='Gauss Elimination',command=nextPage_GaussEliminationMethod).pack(padx='3',pady='3')
LUButton=Button(root,width='50',text='LU Decomposition',command=nextPage_LuDecomposition).pack(padx='3',pady='3')
CramerButton=Button(root,width='50',text='Cramer Rule',command=nextPage_Cramer).pack(padx='3',pady='3')
root.mainloop()