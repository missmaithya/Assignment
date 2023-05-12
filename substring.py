from collections import Counter

def extract_substrings(string):
    substring = []
    for i in range(len(string) - 2):
        substring.append(string[i:i+3])
    return substring

def find_most_common_substring(strings):
    substring = []
    for string in strings:
        substring.extend(extract_substrings(string))
    counter = Counter(substring)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None

strings = ['the', 'girl', 'beautiful', 'book', 'boom']
result = find_most_common_substring(strings)
print("Most common substring of length 3:", result)