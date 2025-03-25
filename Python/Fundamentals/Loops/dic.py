#dict 
# Data type that stores a key-value pair
# Keys are unique
# Keys are immutable
# Keys are case sensitive
# Values are mutable
# Values can be duplicated
# Values can be of any data type
# Values can be changed

# Creating a dictionary
# To create a dictionary, we use curly braces {}
# We separate the keys and values with a colon :
# We separate the key-value pairs with a comma ,

#We want to assign the students to their house

students = {"Hermaione": "Gryffindor", 
            "Ron": "Gryffindor",
            "Harry": "Gryffindor" , 
            "Draco": "Slytherin"}

#We dont use indexes in dictionaries
#We use keys to access values
#We use square brackets [] to access values             
print(students["Hermaione"])    
print(students["Ron"])
print(students["Harry"])
print(students["Draco"])


#For loop
#We can use a for loop to iterate over the keys of a dictionary

print()
for student in students:
    print(student , students[student]) 
    
