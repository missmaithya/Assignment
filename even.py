def even_no(list1):
    sum=0
    for i in list1:
        if not i % 2:
            sum=sum+i
            print(sum)
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    integer=int(input("Enter the elements "))
    list1.append(integer)
print("List elements are ",list1)
even_no(list1)