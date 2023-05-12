def longestCommonPrefix(strs):
    l = len(strs[0])
    for i in range(1, len(strs)):
        length = min(l, len(strs[i]))
        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            length = length - 1
            if length == 0:
                return 0
    return strs[0][0:length]

n=int(input("Enter integer "))
list1=[]
for i in range(n):
    String=(input("Enter the elements "))
    list1.append(String)
print("List elements are ",list1)    
print(longestCommonPrefix(list1))