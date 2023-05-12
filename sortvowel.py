def count_vowel(String):
    count=0
    vowel='aeiouAEIOU'
    for alphabet in String:
        if alphabet in vowel:
            count+=1
    return count
def sort_vowel(String):
    return sorted(String, key=count_vowel)
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    String=(input("Enter the elements "))
    list1.append(String)
print("List elements are ",list1)
print(sort_vowel(list1))