# display fibonacci sequence using recursion

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
    
nterms = 15

for i in range(nterms):
    print(recur_fibo(i))