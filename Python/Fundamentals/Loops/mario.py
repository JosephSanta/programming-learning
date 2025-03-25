

#column in the game Mario
#def main():
#    print_column(3)
    
#def print_column(n):
    #for _ in range(n):
    #    print("#")
    
#    print("#\n" * n, end="")
  
#main()




#Horizontal line in the game Mario

#def main():
#    print_row(4)
    
#def print_row(n):
#    print("?" * n)
    
#main()


def main():
    print_square(3)
   
#the out prints top to bottom
#the inner prints left to right
 
 

def print_square(n):
    
    #for each row in the square
    
    for i in range(n):
        #print("#" * n)
        
        #for each brick in the row
        for j in range(n):
            
            #print a brick
            print("#", end="")
            
    #print a new line after the row is printed
        print()  
        
main()