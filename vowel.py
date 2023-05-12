def count_vowel(String):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in String:
        if alphabet in vowel:
            count=count+1
    print("No of vowels;",count)
String=(input("Enter the elements "))
count_vowel(String)