students = [ "hermaione","ron", "harry"]

#To print the complete list
print(students )


#To print the first element of the list
print(students[0])

#We gonna use a for loop to print all the elements of the list


#student is already a variable, so we don't need to declare it
#we can use it directly in the for loop

print()


for student in students:
    print(student)


print()

for i in range(len(students)):
    print(i + 1, students[i])
    