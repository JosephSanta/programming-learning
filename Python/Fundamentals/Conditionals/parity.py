
def main():
    x = int(input("whats x? "))
    
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")
        

def is_even(x):
    #this function will return true if x is even, and false if x is odd
    return ( x % 2 ==0)

main()