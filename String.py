def get_max_length(lst):
    return len(max(lst, key=len))
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    String=(input("Enter the elements "))
    list1.append(String)
print("List elements are ",list1)
print(get_max_length(['Letty','Wow','job']))