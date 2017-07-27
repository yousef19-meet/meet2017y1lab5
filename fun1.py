def add_numbers():
    a=int(input("what is the start number ?"))
    b=int(input("what is the end number ?"))
    n=int(input("what is skipping number ?"))
    c=0
    for number in range(a,b,n):
        
        print (number)
        c=c+number
    return c

