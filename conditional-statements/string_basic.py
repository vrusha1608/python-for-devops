# String syntax and basic operations

firstName = 'Vrushali'

middleName = "Arun"

lastName = '''Potdar'''

#  string concatenation
name = firstName + middleName + lastName 

print(name)

str1 = "This is a String. We are creating it in Python"

print(str1)

str2 = "This is a String.\nWe are creating it in Python"

print(str2)

str3 = "This is a String. \tWe are creating it in Python"

print(str3)

# Length of String
len1 = len(str1)

print("Length of <<",str1,">> is",len1)

#Indexing

str = "Apna_College"

print(str[3])
print(str[7])

# re-Assigning character to an index
#str[6] = 'y'

# Slicing
str = "ApnaCollege"
print(len(str))
print(str[1:6])
print(str[ :7]) # str[0:7]
print(str[1:])  #str[1:len(str)]
print(str[4:len(str)])

# Negative index in slicing

print(str[-8:-3])