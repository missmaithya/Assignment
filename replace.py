def replaceVowelsWithK(test_str, K):
    vowels = 'AEIOUaeiou'
    for ele in vowels:
        test_str = test_str.replace(ele, K)
 
    return test_str
input_str =input("Enter a string")
K = "*"
print("Given String:", input_str)
print("Given Specified Character:", K)
print("After replacing vowels with the specified character:",
replaceVowelsWithK(input_str, K))