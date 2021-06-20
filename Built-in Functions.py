import math

def myabs(number):
    """ Implementation of built-in `abs` function """
    print("\nBUILT-IN FUNCTION: abs(" ,number , ")= " ,abs(number))
    sqr= number*number
    print("Absolute value= " ,int(math.sqrt(sqr)))
    


def myall(iterable):
    """ Implementation of built-in `all` function """
    print("\n\nBUILT-IN FUNCTION: all = " ,all(iterable))
    flag=0
    for i in iterable:
        if(i==False):
            flag=1
            break
    if(flag==1):
        print("All = False")
    else:
        print("All = True")
    


def myany(iterable):
    """ Implementation of built-in `any` function """
    print("\n\nBUILT-IN FUNCTION: any = " ,any(iterable))
    flag=0
    for i in iterable:
        if(i==True):
            flag=1
            break
    if(flag==1):
        print("All = True")
    else:
        print("All = False")


def mylen(s):
    """ Implementation of built-in `len` function """
    print("\n\nBUILT-IN FUNCTION: len('"+s+ "')= " ,len(s))
    c=0
    for i in s:
        if(i!='\0'):
            c+=1
        else:
            break
    print("Length of String = ",c)


def mysum(iterable):
    """ Implementation of built-in `sum` function """
    print("\n\nBUILT-IN FUNCTION: sum = " ,sum(iterable))
    add=0
    for i in iterable:
        add=add+i
    print("Total Sum = ",add)


def mymax(iterable):
    """ Implementation of built-in `max` function """
    print("\n\nBUILT-IN FUNCTION: max = " ,max(iterable))
    big=iterable[0]
    for i in iterable:
        if(i > big):
            big=i
    print("Maximum value = ",big)


def mymin(iterable):
    """ Implementation of built-in `min` function """
    print("\n\nBUILT-IN FUNCTION: min = " ,min(iterable))
    small=iterable[0]
    for i in iterable:
        if(i < small):
            small=i
    print("Minimum value = ",small)


def mydivmod(a, b):
    """ Implementation of built-in `divmod` function """
    print("\n\nBUILT-IN FUNCTION: divmod(" ,a ,"," ,b , ")= " ,divmod(a,b))
    q=a//b
    r=a%b
    print("DivMod value = ",q,",",r)
    


def mybool(x):
    """ Implementation of built-in `bool` function """
    print("\n\nBUILT-IN FUNCTION: bool(" ,x ,")= " ,bool(x))
    falsy= [0,0.0,0j,'',[],(),{}]
    if(x in falsy):
        print("Boolean value = False")
    else:
        print("Boolean value = True")


def mypow(base, exp):
    """ Implementation of built-in `pow` function """
    print("\n\nBUILT-IN FUNCTION: pow(" ,base , ",",exp , ")= " ,pow(base,exp))
    prd=1
    for i in range(exp):
        prd=prd*base
    print("Power value = ",prd)


def myreversed(seq):
    """ Implementation of built-in `reversed` function """
    seq.reverse()
    print("\n\nBUILT-IN FUNCTION: reverse= " ,seq)
    print("Reverse order = ", seq[-1: :-1])


def myenumerate(iterable, start=0):
    """ Implementation of built-in `enumerate` function """
    print("\n\nBUILT-IN FUNCTION: enumerate= " ,list(enumerate(iterable)))
    lst=[]
    for i in range(len(iterable)):
        lst.append((i,iterable[i]))
    print("Enumerate values = ",lst)
        


def mybin(x):
    """ Implementation of built-in `bin` function """
    print("\n\nBUILT-IN FUNCTION: bin(" ,x , ")= " ,bin(x))
    rem=['0b']
    while(x!=0):
        r=str(x%2)
        rem.insert(1,r)
        x=x//2
    re=''.join(rem)
    print("Binary value = ",re)


def myhex(x):
    """ Implementation of built-in `hex` function """
    print("\n\nBUILT-IN FUNCTION: hex(" ,x , ")= " ,hex(x))
    rem=['0x']
    while(x!=0):
        r=str(x%16)
        if(r==10):
            r='A'
        elif(r==11):
            r='B'
        elif(r==12):
            r='C'
        elif(r==13):
            r='D'
        elif(r==14):
            r='E'
        elif(r==15):
            r='F'
        rem.insert(1,r)
        x=x//16
    re=''.join(rem)
    print("Hexadecimal value = ",re)


def myoct(x):
    """ Implementation of built-in `oct` function """
    print("\n\nBUILT-IN FUNCTION: oct(" ,x , ")= " ,oct(x))
    rem=['0o']
    while(x!=0):
        r=str(x%8)
        rem.insert(1,r)
        x=x//8
    re=''.join(rem)
    print("Octal value = ",re)


def mysorted(iterable, reverse=False):
    """ Implementation of built-in `sorted` function """
    print("\n\nBUILT-IN FUNCTION: sort= " ,sorted(iterable))
    sort=[]
    while iterable:
        first=iterable[0]
        for i in iterable:
            if(i<first):
                first=i
        sort.append(first)
        iterable.remove(first)
    print("Sorted values = ",sort)
            

num = -28

num1 = 35

num2 = 4

lst = [8,9,7,3,1,0,4,7]

string = "This is my string "

myabs(num)

mylen(string)

mydivmod(num1,num2)

mybool(num1)

mypow(num1,num2)

mybin(num1)

myhex(num1)

myoct(num1)

print("\n**************************************")
print("\n LIST = ", lst)

myall(lst)

myany(lst)

mysum(lst)

mymax(lst)

mymin(lst)

myreversed(lst)

myenumerate(lst)

mysorted(lst)
