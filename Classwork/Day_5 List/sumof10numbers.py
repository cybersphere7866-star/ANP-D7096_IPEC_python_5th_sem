'''Write a program to find out sum of 10 numbers'''
numbers=[]
print ("Enter any 10 numbers: ")
for x in range(10):
    #input of element from user
    num=int(input())
    #inserting data in list at end 
    numbers.append(num)
    #---------------------------------------------------
print("Numbers are: ", numbers)
#finding sum 
sum = 0
for x in numbers:
    sum+=x
print("Sum", sum)