from string import ascii_uppercase
asci=ascii_uppercase
print("1 : encription")
print("2 : decription")
x=input(">>> ")

ch=input("mesagge : ")
n=int(input("forword : "))

if x =='1':
    miss={}
    j=0
    for i in range(n,len(asci)+n):
        if i==26:
            #miss[asci[(i-1)-len(asci)]]=asci[(i-1)-len(asci)]
            miss[asci[j]]=asci[(i-1)-len(asci)]
        else:
            #miss[asci[(i-1)-(n-1)]]=asci[(i-1)-len(asci)]
            miss[asci[j]]=asci[(i-1)-len(asci)]
        j+=1
    miss[' ']=' '
    s=''
    ch=ch.upper()
    for c in ch:
        s=s+miss[c]
    print(s)
else:
    # decript your message
    n=3
    order={}
    j=0
    for i in range(n,len(asci)+n):
        if i==26:
            order[asci[(i-1)-len(asci)]]=asci[j]
        else:
            order[asci[(i-1)-len(asci)]]=asci[j]
        j+=1
    order[' ']=' '
    s=''
    ch=ch.upper()
    for c in ch:
        s=s+order[c]
    print(s)
    
