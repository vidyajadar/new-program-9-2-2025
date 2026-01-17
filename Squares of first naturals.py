#sum of squares of n numbers

#Keeps the program running again and again

while True:
    n=int(input("Enter a Number:"))
    Sum = 0

    for i in range(1,n+1):
        Sum = Sum + i*i
    

    print("Sum of squares of n numbers", Sum)

    choice = input("Do you want to calculate for another number? (Yes/No):").strip().lower()
    #.strip() removes the extra spaces " yes " to "yes"

    #lower() is used to accept user input in any letter case
    if choice == "yes":
        break
    elif choice == "No":
        print("Thank you")
        exit()
    else:
        print("Invalid input. Please type yes or no.")
