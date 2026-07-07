#WAP to create a list of 20 numbers given by user. ask the user to input any other number . if the number is present in the list  then, remove its all duplicate occurences from the list.

lst=[]
print("Enter 10 numbers :")
#to repeat he same input 
for i in range(10):
    num=int(input())
    lst.append(num)
print("The list is :",lst)
print("----------------------------")
print("Enter the element to be removed :")
ele = int(input())
if ele in lst:
    count = lst.count(ele)
    for i in range(count):
        lst.remove(ele)
    print("The list after removing all occurrences of the element is :",lst)
else:
    print("Element not found in the list.")