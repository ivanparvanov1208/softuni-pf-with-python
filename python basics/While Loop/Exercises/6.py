width = int(input())
length = int(input())

pieces = width * length

while True:
    command = input()

    if command.isdigit():
        takenPieces = int(command)
        pieces -= takenPieces
        if pieces <= 0:
            print(f"No more cake left! You need {abs(pieces)} pieces more.")
            break

    elif command == "STOP":
        print(f"{pieces} pieces are left.")
        break