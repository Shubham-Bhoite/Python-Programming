f readyToGo():
    userReady=input(f"Hello {userName} !!! Do You want to Start??(Y/N): ")
    if(userReady=="Y"or userReady=="y"):
         print("Here is your Questions")
    elif(userReady=="N"or userReady=="n"):
         print("Then Why You are Here?? Go Home(Nikal)")
    else:
        print("Wrong Choice!! Please Enter Y or N")
        readyToGo()

readyToGo()