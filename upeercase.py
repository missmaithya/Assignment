def all_upper(list1):
    return [x.upper() for x in list1]
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    String=(input("Enter the elements "))
    list1.append(String)
print("List elements are ",list1)
print(all_upper(list1))