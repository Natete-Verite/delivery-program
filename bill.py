def delivery_project():

    print('Welcome to your Python Pizza Deliveries!')
    size= str(input("Which size of pizza do you want? S, M, or L: "))
    add_pepperoni= str(input("Do you want to add pepperoni? Y or N: "))
    cheese= str(input('Do you want extra cheese? Y or N: '))
    bill=0
    if size == 'S':
        bill+=10
    elif size == 'M':
        bill+=15
    else:
        bill+=20

    if add_pepperoni == 'Y':
        if size == 'S':
            bill+=1
        else:
            bill+=3

    if cheese == 'Y':
        bill+=2
    print(f'Your final bill is ${bill}')

delivery_project()