'''
while True:
    user=input("enter the string:")


    if "e" in user and "l" in user and "f" in user:
           if user.index("e") < user.index("l") < user.index("f"):
                print("string is elfish")

           else:
                print("string is not elfish")
            
    else:
        print("string is not elfish")
'''
'''
3) count duplicates character:

user=input("Enter the string:")

repeated=[]
for char  in user:
    if user.count(char)>1:
        if char not in repeated:
            repeated.append(char)
            break
print(repeated)            


def func(x,li=[]):
    li.append(x)
    return li
l1=func(10)
print(l1)
l2=func(20)
print(l2)
l3=func(30)
print(l3)
'''

'''
4)Remove the Duplicate Element from list:

li=[10,20,30,10,20,10,40,50,60,10,10,10,10,20,20,20,10,20,20,10,30,40,30]

for i in li:
    if li.count(i)>1:
        for i in li:
            if li.count(i)>1:
                li.remove(i)
                      
print(li)            
'''


l1=['a','b','d','e','h','n']
l2=[1,2,0,0,1,3]

zipped_pairs=zip(l2,l1)
for i in zipped_pairs:
    z=sorted(zipped_pairs)
    print(list(z))
    
#z=[l1 for _,l1 in sorted(zipped_pairs)]

#print(z)
            

     
        
            
            



  


    

        
        
