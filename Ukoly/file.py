def ApproxOfSquare(a, n): # a = Cislo, jehoz odmocninu chceme dostat a n = pocet iteraci
    if a > 0:   
        x0 = a
        for i in range(1,n):
            xk = ((a/x0)+x0)/2
            x0 = xk
    else:
        return "Stay real"
    
    return xk

def regular(n):  
    v_n = ApproxOfSquare(1 - 1/4, 100) # |AB| = |BC| = 1
    b_n = 1   #  sqrt(1/4 + ((1-v_n) ** 2))
    for i in range(1,n+1):
        b_2n = ApproxOfSquare(((b_n/2)**2) + ((1-v_n)**2),100)
        v_2n = ApproxOfSquare(1 - ((b_2n/2) ** 2), 100)
        v_n = v_2n
        b_n = b_2n    
    S = 6 * (2**n) * b_2n * v_2n/2
    return S

def series(n):   
    a0 = 1/16
    it = n
    sum = 0
    num = ApproxOfSquare(3,1000)
    sum += a0/3
    for i in range(2,it):
        a1 = a0*(((2*i - 3)/(2 * i))* (1/4))
        a0 = a1
        sum += a1/(2*i + 1)
    return 12 * (-(num/8) + (1/2) - sum)
