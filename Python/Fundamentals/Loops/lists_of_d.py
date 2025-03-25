#We can combine lists and dictionaries
#Lists of dictionaries


students= [
    {"name": "Hermaione", "house": "Gryffindor" , "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor" , "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor" , "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin" , "patronus": None}
]

#none
#None is a special value in python
#None is used to represent the absence of a value


#we have to standardize the key names

for student in students:
    print( student["name"] , student["house"], student["patronus"] , sep=", ")
    