import random
number=random.randint(1000,9999)
number1=str(number)
l=[]
for i in number1:
    l.append(i)
print(l)
ans=[]
def userinput():
    global ans
    if (ans==['c','c','c','c']):
        return ans
    else:    
        l1=[]
        number2=int(input("Enter 4 digit number"))
        num=str(number2)
        for i in num:
            l1.append(i)
        print(l1)    
        ans=[]
        for i in range(0,len(num)):
            for j in range(0,(len(num))):
                if l[i]==l1[i]:
                    ans.append('c')
                    break
                elif l1[i]==l[j]:
                    ans.append('p')
                    break
            else:
                ans.append('x')
        print(ans)
        userinput()    
userinput()



    