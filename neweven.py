def even_no(list):
    new_list=[]
    for i in list:
        if i % 2==0:
            new_list.append(i)
    return new_list
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    integer=int(input("Enter the elements "))
    list1.append(integer)
print("List elements are ",list1)
print(even_no(list1))