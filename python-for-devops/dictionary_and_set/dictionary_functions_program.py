# Implementation of in-built functions of Dictionary

student_result = {
    "rollNo" : 27,
    "name" : "vrushali",
    "age" : 27,
    "result" : {
        "physics" : 89,
        "chemistry" : 67,
        "math" : 83
    }
}

print("Dictionary => ",student_result)

print("Keys =>", student_result.keys())

print("List of Keys =>", list(student_result.keys()))

print("Values =>",student_result.values())

print("List of Values =>", list(student_result.values()))

print("Items of Dictionary=>", student_result.items())

print("List of Items of Dictionary=>", list(student_result.items()))

pairs = list(student_result.items())
print("first key-value pair=>", pairs[1])

print("Value of 'name' key=>", student_result.get("name"))

print(student_result["name"])   # it is not ideal way to print value of particular key istead we should use get() function

student_result.update({"city" : "sangli", "gender" : "female"})
print("New Dictionary =>", student_result)

