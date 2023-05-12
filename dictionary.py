def sort(dictionary, key):
    return sorted(dictionary, key=lambda x:x[key])
dictionary= {}
n=int(input("Enter number of users"))
for i in range(n):
    name = input("Enter employee's name: ")
    salary = int(input("Enter employee's salary: "))

    dictionary[name] = salary
print(dictionary)
print(sort(dictionary, 'salary'))
