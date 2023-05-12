def longestComnSuffix(strs):
    comn_suffix = strs[0]
    for next_word in strs[1:]:
        while not next_word.endswith(comn_suffix):
            comn_suffix = comn_suffix[1:]
    return comn_suffix
n=int(input("Enter integer "))
list1=[]
for i in range(n):
    String=(input("Enter the elements "))
    list1.append(String)
print("List elements are ",list1)  
print(longestComnSuffix(list1))