bal=input("what do you want to enter either it is string or number:")
if (("str" or "string") in bal):
    x =(input("enter the string only: to check:"))
    y = x[ : : -1]
    if x ==y :
        print(y)
        #print(y+10)
        print("it is palindrome")
    else:
        print(y)
        print("it is not a palondrome")



elif (("num" or "number") in bal):
    x = int (input("enter the number only:to check:"))
    hari = x
    jyo = 0
    while hari > 0:
        num = hari%10

        jyo = jyo*10+num
        print("this is jyo",jyo)
        hari = hari//10
        print(hari)
    if jyo ==x:
        print("given number is palindrome")
    else:
        print("no,it is not a palindrome")
    
