


#Def is a keyword that tells python that we are defining a function
#hello is the name of the function
#() is used to pass arguments to the function
#Arguments are the values that are sent to the function



#def have to be up top before the function is called
#thats why i create a function called main
#main is the first function that is called



#scope is the area of the code where a variable can be used
#variables that are defined inside a function are only available inside that function
#variables that are defined outside a function are available everywhere in the code
#variables that are defined inside a function are called local variables
#variables that are defined outside a function are called global variables


#return
#return is a keyword that is used to return a value from a function
#return is used to exit a function
#return can be used to return a value from a function
#return can be used to return a variable from a function
#return can be used to return the result of an expression

#def main():  
#    myname = input("What is your name? ")
#    hello(myname)



#def hello(name="world"):
#    print(f"hi {name}")
    
    
#main()
    
###############################

def square(x):
    return pow(x, 2)


def main():
    x = int (input("Give me a number: "))
    print("x squeared is" , square(x))


main()