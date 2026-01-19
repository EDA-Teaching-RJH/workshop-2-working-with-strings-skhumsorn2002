def main():
    age = int(input("Enter age: "))
    AgeCheck(age)

def AgeCheck(a):
    if a >= 18:
        print("You are an adult.")
    else:
        print("You are a child.")

main()