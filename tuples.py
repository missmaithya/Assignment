def sort_tuples(tuples):
    return sorted(tuples, key=lambda x:x[1])
n=int(input("Enter the number of tuples "))
tuples=[]
for i in range(n):
    print(f"Enter tuple {i+1}:")
    String=(input("Enter the elements "))
    tuples.append(String)
print("Tuples elements are ",tuples)
print(sort_tuples(tuples))