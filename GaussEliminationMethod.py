from PreConfig import *

def gauss_elimination(matrix):
    n = len(matrix)    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][n] -= matrix[k][i] * x[i]
    return x

def gaus():

    matrix_str = [r1c1.get(), r1c2.get(), r1c3.get(), r1c4.get(),
            r2c1.get(), r2c2.get(), r2c3.get(), r2c4.get(),
            r3c1.get(), r3c2.get(), r3c3.get(), r3c4.get()]

    matrix_float = [float(value) for value in matrix_str]

    matrix = [matrix_float[i:i+4] for i in range(0, len(matrix_float), 4)]


    solutions = gauss_elimination(matrix)

    x1['text']=f"x1={round(solutions[0],2)} "
    x2['text']=f"x2={round(solutions[1],2)} "
    x3['text']=f"x2={round(solutions[2],2)} "    


# **********************************     GUI       **********************************************

Frame1 = Frame(root, width='300', height='200')
Frame1.pack(side=TOP, padx='20', pady='20')

frame2 = Frame(root, width='500', height='200')
frame2.pack(side=TOP, padx='20', pady='20')


LabelTitle = Label(Frame1, text='Gauss Elimination Method', width='300', font=('', 16, 'bold'))
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




ButtonGetX = Button(root, text="Calculate",  command=gaus)
ButtonGetX.pack(side=TOP, padx='20', pady='20')

x1 = Label(root, text="x1=")
x1.pack(padx='20', pady='20')

x2 = Label(root, text="x2=")
x2.pack(padx='20', pady='20')

x3 = Label(root, text="x3=")
x3.pack(padx='20', pady='20')



root.mainloop()
