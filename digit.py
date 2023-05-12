def sort_digit(numbers):
    return sorted(numbers, key=lambda x: len(str(x)))
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    integer=int(input("Enter the elements "))
    list1.append(integer)
print("List elements are ",list1)
print(sort_digit(list1))