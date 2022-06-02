command = ""
while command != "quit":  #while true:
    command = input().lower()
    if command == 'help':
        print("start = to start the car")
        print("stop = to stop the car")
        print("quit = to quit")
    elif command == 'start':
        print("car started...ready to go")
    elif command == 'stop':
        print("car stopped")
    elif command == 'quit':
        print("end")       #break
    else:
        print("i don't understand")
