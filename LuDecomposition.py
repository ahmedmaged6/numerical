from PreConfig import *

def lu_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j][j] = 1
        for i in range(j+1):
            U[i][j] = matrix[i][j] - sum(U[k][j] * L[i][k] for k in range(i))
        for i in range(j, n):
            L[i][j] = (matrix[i][j] - sum(U[k][j] * L[i][k] for k in range(j))) / U[j][j]

    return L, U

def solve_lu(L, U, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return x

def lu():
    
    matrix_str = [r1c1.get(), r1c2.get(), r1c3.get(), r1c4.get(),
            r2c1.get(), r2c2.get(), r2c3.get(), r2c4.get(),
            r3c1.get(), r3c2.get(), r3c3.get(), r3c4.get()]

    matrix_float = [float(value) for value in matrix_str]

    matrix = [matrix_float[i:i+4] for i in range(0, len(matrix_float), 4)]
    b = [row[-1] for row in matrix]
    
    A = [row[:-1] for row in matrix]

    L, U = lu_decomposition(A)


    solution = solve_lu(L, U, b)
    for i, sol in enumerate(solution):
        x1['text']=f"x1={solution[0]} "
        x2['text']=f"x2={solution[1]} "
        x3['text']=f"x2={solution[2]} "


# **********************************     GUI       **********************************************

Frame1 = Frame(root, width='300', height='200')
Frame1.pack(side=TOP, padx='20', pady='20')

frame2 = Frame(root, width='500', height='200')
frame2.pack(side=TOP, padx='20', pady='20')


LabelTitle = Label(Frame1, text='LU Decomposition Method', width='300', font=('', 16, 'bold'))
LabelTitle.pack(padx='5', pady='5')


r1c1=Entry(frame2, width=10, bd=5, justify=CENTER)
r1c1.grid(row=1, column=1, padx='10', pady='10')        
r1c2=Entry(frame2, width=10, bd=5, justify=CENTER)
r1c2.grid(row=1, column=2, padx='10', pady='10')        
r1c3=Entry(frame2, width=10, bd=5, justify=CENTER)
r1c3.grid(row=1, column=3, padx='10', pady='10')        
r1c4=Entry(frame2, width=10, bd=5, justify=CENTER)
r1c4.grid(row=1, column=4, padx='10', pady='10')        

r2c1=Entry(frame2, width=10, bd=5, justify=CENTER)
r2c1.grid(row=2, column=1, padx='10', pady='10')        
r2c2=Entry(frame2, width=10, bd=5, justify=CENTER)
r2c2.grid(row=2, column=2, padx='10', pady='10')        
r2c3=Entry(frame2, width=10, bd=5, justify=CENTER)
r2c3.grid(row=2, column=3, padx='10', pady='10')  
r2c4=Entry(frame2, width=10, bd=5, justify=CENTER)
r2c4.grid(row=2, column=4, padx='10', pady='10')            

r3c1=Entry(frame2, width=10, bd=5, justify=CENTER)
r3c1.grid(row=3, column=1, padx='10', pady='10')        
r3c2=Entry(frame2, width=10, bd=5, justify=CENTER)
r3c2.grid(row=3, column=2, padx='10', pady='10')        
r3c3=Entry(frame2, width=10, bd=5, justify=CENTER)
r3c3.grid(row=3, column=3, padx='10', pady='10')        
r3c4=Entry(frame2, width=10, bd=5, justify=CENTER)
r3c4.grid(row=3, column=4, padx='10', pady='10')      




ButtonGetX = Button(root, text="Calculate",  command=lu)
ButtonGetX.pack(side=TOP, padx='20', pady='20')

x1 = Label(root, text="x1=")
x1.pack(padx='20', pady='20')

x2 = Label(root, text="x2=")
x2.pack(padx='20', pady='20')

x3 = Label(root, text="x3=")
x3.pack(padx='20', pady='20')



root.mainloop()
