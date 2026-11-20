def aa(a,v=0):
    if a==0:
        return v
    
    e=a%10
    def av(n):
        if n == 1 or n == 0:
            return 1
        return n*av(n-1)
    h=av(e)
    v=v+h
    return aa(a//10,v)
n=int(input("enter: "))
b=aa(n)
if n == b:
    print(f"{n} is string number")
else:
    print(f"not {n} a strong a number")
