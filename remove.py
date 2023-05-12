def replace_vowel(String, K):
    vowel='aeiouAEIOU'
    for ele in vowel:
        String=String.replace(ele, K)
    return String
b=(input("Enter the elements "))
print("Given string",b)
K = "*"
print(replace_vowel(b, K))