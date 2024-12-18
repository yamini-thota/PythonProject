command = ""
started = False
while True :
    command = input("> ")
    if command == 'start':
        if started:
            print('car is already started...!')
        else:
            started = True
            print('car is started...!')
    elif command == 'stop':
        if not started:
            print("Car is already stopped...!")
        else:
            started = False
            print("car is stopped...!")
    elif command == 'help':
        print("""
              start - to starts the car
              stop -  to stops the car
              quit -  to quit
              """)
    elif command == 'quit':
        break
    else:
        print("sorry, I don't understand...!")



