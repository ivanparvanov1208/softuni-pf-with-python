while True:
    command = input()

    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    elif command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    else:
        if len(command) < 5:
            print(f"{command} goes to Gryffindor.")
        elif len(command) == 5:
            print(f"{command} goes to Slytherin.")
        elif len(command) == 6:
            print(f"{command} goes to Ravenclaw.")
        else:
            print(f"{command} goes to Hufflepuff.")