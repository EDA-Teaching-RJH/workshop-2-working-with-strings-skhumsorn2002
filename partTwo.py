import math  

def main():
    #TO DO 
    adjacent = int(input("Enter adjacent: "))
    opposite = int(input("Enter opposite: "))
    pythag(adjacent,opposite)

def pythag(A,B):
    #TO DO  
    C = A**2 + B**2
    print(f"The value for the hypotenuse are: {C}")

main()
