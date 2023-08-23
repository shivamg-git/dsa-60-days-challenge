import functools

fib = [1,1,2]

def climbing_stairs(n):
    if len(fib)-1<n:
        i= len(fib)-1
        while len(fib) != n+1:
            fib.append(fib[i-1]+fib[i-2])
            i+=1
    
    return fib[n]


for i in range(0,10):
    print(climbing_stairs(n=i))
