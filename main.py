while True:

    print("\nChoose Option: \n \n[1] Fixed Path \n[2] User Path")
    choice = int(input("You Choose: "))

    if choice == 1:
        import Fixed_Path

        break

    elif choice == 2:
        import User_Path

        break

    else:
        print("Invalid Input...")
