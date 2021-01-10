row =1
while row<=5:
	col = 1
	while col<=row:
		print(row,end=' ')
		col+=1
	print()
	row+=1 
    
# output
# 1 
# 2 2    
# 3 3 3
# 4 4 4 4 
# 5 5 5 5 5


row =1
while row<=5:
	col = 1
	while col<=row:
		print((col+row),end=' ')
		col+=1
	print()
	row+=1 
    
# output
# 2 
# 3 4    
# 4 5 6
# 5 6 7 8 
# 6 7 8 9 10    
    
	
row =1
while row<=5:
	col = 1
	while col<=row:
		print((col*row),end=' ')
		col+=1
	print()
	row+=1 
    
# output
# 1 
# 2 4    
# 3 6 9
# 4 8 12 16 
# 5 10 15 20 25      

row =1
while row<=5:
	col = 1
	while col<=row:
		print((col-row),end=' ')
		col+=1
	print()
	row+=1 #2
    
# output
# 0 
# -1 0    
# -2 -1 0
# -3 -2 -1 0 
# -4 -3 -2 -1 0      
   
    
    
# sentence=input("Enter sentence: ") 
# wordcount=1
# i=0
# while i<len(sentence)-1:
    # if sentence[i]==' ':
        # wordcount+=1
    # i+=1    
# print(wordcount)
  
    


paragraph=input("Enter paragraph: ") 
sentencecount=1
i=0
while i<len(paragraph)-1:
    if paragraph[i]=='.':
        sentencecount+=1
    i+=1    
print("The number of sentences in the paragraph are:",sentencecount)
  

row =1
while row<=5:
	col = 1
	while col<=row:
		print(row,end=' ')
		col+=1
	print()
	row+=2 #2
# output
# 1    
# 3 3 3 
# 5 5 5 5 5
	

row =1
while row<=5:
	col = 1
	while col<=row:
		print(row,end=' ')
		col+=2
	print()
	row+=1 
#output
# 1
# 2 
# 3 3
# 4 4  
# 5 5 5
