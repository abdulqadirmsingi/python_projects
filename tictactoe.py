global x
global o
global xn
global on
x=[]
o=[]
l=["1","2","3","4","5","6","7","8","9"]
wp=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
xn=input("Enter name of Player 1(X)")
on=input("Enter name of Player 2(O)")
print(f" {(l[0])} | {(l[1])} | {(l[2])} ")
print("---|---|---")
print(f" {(l[3])} | {(l[4])} | {(l[5])} ")
print("---|---|---")
print(f" {(l[6])} | {(l[7])} | {(l[8])} ")
def space(a):
    if a.isdigit():
        a=" "
    return a
def draw(l):
    c=0
    for i in l:
        if i.isalpha():
            c+=1
    if c==len(l):
        print("MATCH DRAW..")
        return 1
def board():
    print(f" {space(l[0])} | {space(l[1])} | {space(l[2])} ")
    print("---|---|---")
    print(f" {space(l[3])} | {space(l[4])} | {space(l[5])} ")
    print("---|---|---")
    print(f" {space(l[6])} | {space(l[7])} | {space(l[8])} ")



def check_win(l,s):
    if len(l)>=3:
        for i in range(0,len(l)-2):
            for j in wp:
                if j==l[i:i+3]:
                    if s=="X":
                        q=xn
                    else:
                        q=on
                    print(f"{q} WINNER...")
                    return 1
                

def check_int(a):
    s=input(a)
    while 1>0:
        if s.isdigit() and len(s)==1:
            
            break
        else:
            s=input("Please enter the correct position")
    s=check_duplicate(int(s))
    return int(s)

def check_duplicate(n):
    while True:
        if n in x or n in o:
            n=int(input("Postion accqiured..enter correct position"))
        else:
            break
    return n
# board()
while True:
    
    xt=int(check_int("X's turn"))
    x.append(xt)
    x.sort()
    l[xt-1]="X"
    board()
    if draw(l)==1:
        break
    if check_win(x,"X")==1:
        break
    ot=int(check_int("enter O turn"))
    # check_duplicate(ot)
    o.append(ot)
    o.sort()
    l[ot-1]="O"
    board()
    if draw(l)==1:
        break
    if check_win(o,"O")==1:
        break