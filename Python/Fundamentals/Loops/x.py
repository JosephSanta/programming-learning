
students = {"Hermaione": 1,
            "Ron": 2,
            "Harry": 2,
            "Draco": 4}

x =0
for student in students:
    print(students[student])
    
    x = x + students[student]
    
print(x)