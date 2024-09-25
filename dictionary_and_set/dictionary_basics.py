# Basic concepts of Dictionary

student_info = {
    "name" : "vrushali",
    "age" : 27,
    "marks" : [87,95,68,62,76],
    "age" : 26  #Overrides key value
}

print(student_info)

print(type(student_info))

print(student_info["name"])

print(student_info["marks"])

student_info["name"] = "varad"

print(student_info)

null_dictionary = {}    # null dictionary

null_dictionary["name"] = "ApnaCollege" #Adding elements in null dict
print(null_dictionary)

###############################################################################################################################

# Nested dictionary

student_result = {
    "rollNo" : 27,
    "name" : "vrushali",
    "result" : {
        "physics" : 89,
        "chemistry" : 67,
        "math" : 83
    }
}

print(student_result)
print(student_result["name"])
print(student_result["result"]["math"])

