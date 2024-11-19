def entrance():
    print("You enter the entrance!")
    print("You see two doors infront of you")
    print("The one in front leads to the livingroom")
    print("The one to the side leads to kitchen")
    print("Where do you want to go")
    ans= input("1, Enter the livingroom \n2, Check out the kitchen \n3, Look around the entrance \n")
    if(ans == "1"):
        livingroom()
    elif(ans == "2"):
        kitchen()
    elif(ans == "3"):
        print("You look around for anything of importance")
        print("Other than the main entrance and the other two doors")
        print("You dont spot anything")
        print("Where do you want to go?")
        ans= input("1, Enter the living room \n2, Look in the kitchen \n")
        if(ans == "1"):
            livingroom()
        elif(ans == "2"):
            kitchen()
        else:
            print("You decide to stay in the room")
            print("A dark presance takes over you")
            print("You die!")
    else:
        print("You decide to stay in the room")
        print("A dark presance takes over you")
        print("You die!")

def entrance2():
    print("You head back into the entrance")
    print("The door to the kitchen is still there")
    print("Where do you want to go")
    ans= input("1, Go back to the livingroom \n2, Check out the kitchen \n")
    if(ans == "1"):
        livingroom()
    elif(ans == "2"):
        kitchen()
    else:
        print("You decide to stay in the room")
        print("A dark presance takes over you")
        print("You die!")

def entrance3():
    print("You head back into the entrance")
    print("The door to the livingroom is still there")
    print("Where do you want to go")
    ans= input("1, Go to the livingroom \n2, Get back in the kitchen \n")
    if(ans == "1"):
        livingroom()
    elif(ans == "2"):
        kitchen()
    else:
        print("You decide to stay in the room")
        print("A dark presance takes over you")
        print("You die!")

def livingroom():
    print("You step into the livingroom")
    print("You see a sofa and a tv")
    print("Nothing else seems of importance")
    print("You see two doors aswell")
    print("One leads to the kitchen")
    print("The other door has no label, only a symbol on the door.")
    print("What do you want to do?")
    ans= input("1, Enter the kitchen \n2, Enter the other door \n3, Go back to the entrance \n4, Sit down of the sofa and watch some tv \n5, Inspect the symbol on the door \n")
    if(ans == "1"):
        kitchen()
    elif(ans == "2"):
        writersRoom()
    elif(ans == "3"):
        entrance2()
    elif(ans == "4"):
        tv()
    elif(ans == "5"):
        print("You inspect the symbol on the door")
        print("The symbol looks like a spiral")
        ans= input("1, Enter the room \n2, Step away from the door \n")
        if(ans == "1"):
            writersRoom()
        elif(ans == "2"):
            livingroom3()
        else:
            print("You stay in the livingroom")
            print("A dark presance takes over")
            print("You die!")
    else:
        print("You decide to stay in the room")
        print("A dark presance takes over you")
        print("You die!")

def livingroom2():
    print("You get up from the sofa")
    print("All the doors are still there")
    print("What do you do?")
    ans= input("1, Enter the kitchen \n2, Enter the other room \n3, Go back into the entrance \n4, Inspect the symbol on the other door \n")
    if(ans == "1"):
        kitchen()
    elif(ans == "2"):
        writersRoom()
    elif(ans == "3"):
        entrance()
    elif(ans == "4"):
        print("You inspect the symbol on the door")
        print("The symbol looks like a spiral")
        ans= input("1, Enter the room \n2, Step away from the door \n")
        if(ans == "1"):
            writersRoom()
        elif(ans == "2"):
            livingroom3()
        else:
            print("You stay in the livingroom")
            print("A dark presance takes over")
            print("You die!")

def livingroom3():
    print("You step away from the dooe with the symbol")
    print("The room looks the same")
    print("What do you do?")
    ans= input("1, Enter the kitchen \n2, Go back to the entrace \n3, Open the door with the symbol \n4, Sit down at the sofa \n")
    if(ans == "1"):
        kitchen()
    elif(ans == "2"):
        entrance()
    elif(ans == "3"):
        writersRoom()
    elif(ans == "4"):
        tv()
    else:
        print("You stay in the livingroom")
        print("A dark presance takes over")
        print("You die!")

def kitchen():
    print("You enter the kitchen")
    print("From a first glance, it appears it's a normal kitchen")
    print("There is some food on the tabel")
    print("The two doors in the room lead to the entrance and the livingroom")
    print("What do you do?")
    ans= input("1, Enter the entrance \n2, Enter the livingroom \n3, Take a seat at the table \n")
    if(ans == "1"):
        entrance()
    elif(ans == "2"):
        livingroom()
    elif(ans == "3"):
        table()
    else:
        print("You decide to stay in the room")
        print("A dark presance takes over you")
        print("You die!")

def kitchen2():
    print("You get up from the table")
    print("The two doors are still there")
    print("What do you do?")
    ans= input("1, Go to the entrance \n2, Enter the livingroom \n")
    if(ans == "1"):
        entrance3()
    elif(ans == "2"):
        livingroom()
    else:
        print("You decide to stay in the room")
        print("A dark presance takes over you")
        print("You die!")

def writersRoom():
    print("As the room the the writers room creak open")
    print("You see a man sitting at the other end")
    print("They don't seem to notice you at first")
    print("Too engulfed in typing away at his old computer")
    print("Suddenly, he looks up")
    print("Before you can react, you sit up awake in your bed")
    print("You seem to have escaped this nightmare")
    print("You win!")
    print("Congrats!")
    end()

def tv():
    print("You sit down at the sofa infront of you")
    print("Infront of you is the remote to the tv")
    print("What do you do?")
    ans= input("1, Pick up the remote and begin watching \n2, Stand back up \n")
    if(ans == "1"):
        print("As you begin flipping through the channels")
        print("Nothing seems to be on")
        print("Static channel after static channel")
        print("Nothing seems to be playing")
        print("But still, you watch on")
        print("After awhile, you start to feel abit sleepy")
        print("Maybe closing your eyes for a few seconds wont hurt")
        print("But as seconds turn to minutes")
        print("Minutes to hours")
        print("And hours to days")
        print("This is a sleep you wont wake up from")
        print("Game over!")
    if(ans == "2"):
        livingroom2()
    else:
        print("You decide to stay seated in the sofa")
        print("A dark presance takes over you")
        print("You die!")

def table():
    print("As you take a seat at the table")
    print("The smell of the foods takes you by supries")
    print("It smells really good")
    print("Almost too good")
    print("But maybe one bite wont hurt")
    print("What do you do?")
    ans= input("1, Take a bite of the strange food \n2, Get back up from the table \n")
    if(ans == "1"):
        print("As you take just one bite from the food")
        print("You instantly fall in love with it")
        print("Even though you don't know what it is")
        print("It tastes perfect")
        print("As you go in for a second bite")
        print("You suddenly feel full")
        print("Realizing what is going to happen you feel abit sad")
        print("Sad in knowing you wont be able to take a second bite")
        print("You get up from the chair")
        kitchen2()
    if(ans == "2"):
        kitchen()
    else:
        print("You decide to stay seated")
        print("A dark presance takes over you")
        print("You die!")

def end():
    quit

entrance()