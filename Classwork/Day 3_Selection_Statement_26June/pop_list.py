lst=[]
print("Enter 10 numbers :")
for i in range(10):
    num=int(input())
    lst.append(num)
print("The list is :",lst)
print("----------------------------")
print("Enter the element to be removed :")
ele = int(input())
if ele in lst:
    lst.pop(lst.index(ele))
    print("The list after removing the element is :",lst)
else:
    print("Element not found in the list.")