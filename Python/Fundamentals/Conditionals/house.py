
#match 
#Harry, Hermione, Ron = Gryffindor
#Draco = Slytherin
#Others = Who?




name = input("Whats your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        
    





#VERSION 1

#if name == "Harry" or name == "Hermione" or name == "Ron": 
#    print("Gryffindor")

#elif name == "Draco":
#    print("Slytherin")
    
#else:
#    print("Who?")