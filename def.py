def name():
    name=input("Enter your name: ")
    d={}
    for x in name: 
        val=d.get(x,0)+1 
        d[x]=val
    return d.items()
    
#key-value pair    
print(name())
    
#values>1
for keys,values in name():
    if values>1:
        print(keys,':',values)
        
#values=1
for keys,values in name():
    if values==1:
        print(keys,':',values)
        
#Max values
l=[]
for keys,values in name():
    l.append(values)
print(l)
for keys,values in name():    
    if (values==max(l)):
        print(keys,'this letter occurs max times of',values)
    
    
