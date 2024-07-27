# recursion

def show(n):
    if (n == 0):
        return
    print(n)
    show (n-1)
    print("end")
show(10) # 5, 4= n - 1 ,3 = n - 2, 2 = n-3, 1=n - 4

