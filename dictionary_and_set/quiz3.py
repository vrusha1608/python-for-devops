# WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary and add one by one. 
# Use subject name as key and marks as value

marks = {}

print(marks)

m = int(input("Enter marks of 'Physics':"))

marks.update({"Physics" : m})

m = int(input("Enter marks of 'Chemistry':"))

marks.update({"Chemistry" : m})

m = int(input("Enter marks of 'Math':"))

marks.update({"Math" : m})

print(marks)