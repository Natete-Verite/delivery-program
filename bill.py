def delivery_project():

    print('Welcome to your Python Pizza Deliveries!')
    size= str(input("Which size of pizza do you want? S, M, or L: "))
    add_pepperoni= str(input("Do you want to add pepperoni? Y or N: "))
    cheese= str(input('Do you want extra cheese? Y or N: '))
    location= str(input('Enter your Location: '))
    bill=0
    delivery_fee= 5
    if size == 'S' and location == "":
        bill+=10
    elif size == 'M' and location == "":
        bill+=15
    else:
        bill+=20

    if add_pepperoni == 'Y' and location == "":
        if size == 'S' and location == "":
            bill+=1
        else:
            bill+=3

    if cheese == 'Y' and location == "":
        bill+=2
    print(f'Your final bill is ${(bill)+(delivery_fee)}')

delivery_project()