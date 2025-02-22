# import statements
import random
import turtle
import time

USER_START_HEART = 3

# Main Function
def main():
    startpage()
    instructions()
    userNum = int(input('Pick a number between 1 and 4 to be assigned a character: '))

    while userNum < 1 or userNum > 4:
        userNum = int(input('Invalid number chosen. Pick a number between 1 and 4 to be assigned a character: '))

    # If loop used to assign character to user.
    if userNum == 1:
        print('You are a Paranormal Investigator.')
        paranormalInvestigator()
    elif userNum == 2:
        print('You are a Formal Student Spirit.')
        studentSpirit()
    elif userNum == 3:
        print('You are a Medium.')
        medium()
    elif userNum == 4:
        print('You are an Exorcist.')
        exorcist()

    specialInstructions()
    #schoolmap()
    #chooseRoom()

    hearts = USER_START_HEART
    continue_game = True

    while continue_game:
        schoolmap()
        chooseRoom()
        roomNum = int(input('Enter room number (1-5): '))

        while roomNum < 1 or roomNum > 5:
            roomNum = int(input("Invalid room number. Enter room number (1-5): "))

        if roomNum == 1:
            principalOfficeInstructions()
            hearts = principalOffice(hearts)
        elif roomNum == 2:
            msMimiClassInstructions()
            msMimiClass(hearts)
        elif roomNum == 3:
            gymInstructions()
            gym(hearts)
        elif roomNum == 4:
            playgroundInstructions()
            playground(hearts)
        elif roomNum == 5:
            cafeteriaInstructions()
            cafeteria(hearts)

        if hearts <= 0:
            print("Game Over! You lost all your hearts.")
            break

        continue_choice = input("Do you want to go to another room? (Y/N): ").lower()

        if continue_choice != 'y':
            continue_game = False

    print("Thank you for playing!")





def startpage():
    # Screen Details
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Game Name
    pen.penup()
    pen.goto(-20, 200)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.pendown()
    pen.write('Ghost Hunter', font=('Comic Sans MS', 30, 'bold'))

    pen.color("white")
    pen.pensize(3)

    # Draw Ghost Design

    # Ghost Head
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("white")
    pen.circle(100)
    pen.end_fill()

    # Right End Circle
    pen.penup()
    pen.goto(100,-100)
    pen.pendown()
    pen.begin_fill()
    pen.circle(36)
    pen.end_fill()

    # Right Middle Circle
    pen.penup()
    pen.goto(50, -125)
    pen.pendown()
    pen.begin_fill()
    pen.circle(36)
    pen.end_fill()

    # Middle Circle
    pen.penup()
    pen.goto(0,-150)
    pen.pendown()
    pen.begin_fill()
    pen.circle(36)
    pen.end_fill()

    # Right Middle Circle
    pen.penup()
    pen.goto(-50, -125)
    pen.pendown()
    pen.begin_fill()
    pen.circle(36)
    pen.end_fill()

    # Left End Circle
    pen.penup()
    pen.goto(-100,-100)
    pen.pendown()
    pen.begin_fill()
    pen.circle(36)
    pen.end_fill()

    # Ghost Eyes

    # Left Eye
    pen.penup()
    pen.goto(-25, 20)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("black")
    pen.circle(10)
    pen.end_fill()

    # Right Eye
    pen.penup()
    pen.goto(25, 20)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("black")
    pen.circle(10)
    pen.end_fill()

    # Ghost Mouth
    pen.color("black")
    pen.penup()
    pen.goto(-25, -20)
    pen.pendown()

    # Squiggly mouth
    pen.forward(10)
    pen.left(25)
    pen.forward(10)
    pen.right(25)
    pen.forward(10)
    pen.left(-25)
    pen.forward(10)
    pen.right(-25)
    pen.forward(10)

    pen.penup()
    pen.goto(-390, -250)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()


def instructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("midnightblue")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 270)
    pen.pencolor("black")
    pen.pensize(10)
    pen.pendown()
    pen.write('Welcome to Ghost Hunter', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 250)
    pen.pendown()
    pen.write('=================================================', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 230)
    pen.pendown()
    pen.write('Your goal is to find the last ghost.', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 200)
    pen.pendown()
    pen.write('Now for the backstory.', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 170)
    pen.pendown()
    pen.write('You are in an abandoned school where people are planning to', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 140)
    pen.pendown()
    pen.write("rebuild it but in order to do so we must first find the last ghost", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 110)
    pen.pendown()
    pen.write("that is hidden throughout the school. Your mission is to search", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 80)
    pen.pendown()
    pen.write("the school, explore the rooms, complete the challenges, and find", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 50)
    pen.pendown()
    pen.write("the ghost. The school has five rooms where the ghost could be:", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 20)
    pen.pendown()
    pen.write("1) The Principal's Office", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -10)
    pen.pendown()
    pen.write("2) Ms. Mimi's Class", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -40)
    pen.pendown()
    pen.write("3) The Gym", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -70)
    pen.pendown()
    pen.write("4) The Playground", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -100)
    pen.pendown()
    pen.write("5) The Cafeteria", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -130)
    pen.pendown()
    pen.write("But before you begin, you are assigned a character for this", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -150)
    pen.pendown()
    pen.write("adventure (use the console to type in your choice):" , font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -180)
    pen.pendown()
    pen.write("Pick a number between 1 and 4 to be assigned a character:", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -210)
    pen.pendown()
    pen.color("white")
    pen.write("You are given two minutes to read this and decide on your number...", font=('Comic Sans MS', 18, 'bold'))

    pen.penup()
    pen.goto(-390, -300)

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    time.sleep(5)
    pen.clear()

    #screen.bye()


def paranormalInvestigator():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("midnightblue")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 250)
    pen.pendown()
    pen.color("black")
    pen.pensize(10)
    pen.write("YOU ARE A PARANORMAL INVESTIGATOR!", font=('Comic Sans MS', 30, 'bold'))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    #pen.circle(50)

    pen.write("🕵️‍♀️🔍", align="center", font=('Comic Sans MS', 150, 'bold'))

    pen.penup()
    pen.goto(-390, -250)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()

def studentSpirit():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("midnightblue")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pendown()
    pen.color("black")
    pen.pensize(10)
    pen.write("YOU ARE A FORMAL STUDENT SPIRIT!", font=('Comic Sans MS', 30, 'bold'))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    # pen.circle(50)

    pen.write("👧📓", align="center", font=('Comic Sans MS', 150, 'bold'))

    pen.penup()
    pen.goto(-390, -250)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()

def medium():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("midnightblue")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pendown()
    pen.color("black")
    pen.pensize(10)
    pen.write("YOU ARE A MEDIUM!", font=('Comic Sans MS', 30, 'bold'))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    # pen.circle(50)

    pen.write("🕴🔮", align="center", font=('Comic Sans MS', 150, 'bold'))

    pen.penup()
    pen.goto(-390, -250)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()

def exorcist():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("midnightblue")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pendown()
    pen.color("black")
    pen.pensize(10)
    pen.write("YOU ARE AN EXORCIST!", font=('Comic Sans MS', 30, 'bold'))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    # pen.circle(50)

    pen.write("👨🏻‍🦰✝️", align="center", font=('Comic Sans MS', 150, 'bold'))

    pen.penup()
    pen.goto(-390, -250)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()


def specialInstructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-20, 260)
    pen.pencolor("white")
    pen.pensize(10)
    pen.pendown()
    pen.write("Special Instructions", align="center", font=('Comic Sans MS', 24, 'bold'))
    pen.penup()
    pen.goto(-20, 240)
    pen.pendown()
    pen.write("++++++++++++++++++++++++++++++++++++++++++", align="center", font=('Comic Sans MS', 24, 'bold'))

    pen.up()
    pen.goto(-390, 220)
    pen.pendown()
    pen.write("Now you will be shown the school map", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 190)
    pen.pendown()
    pen.write("Wait! Oooops before you go I forgot to mention there's a twist", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 160)
    pen.pendown()
    pen.write("I added.", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 130)
    pen.pendown()
    pen.write("Additional Instructions:", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 100)
    pen.pendown()
    pen.write("Starting Hearts: You begin with 3 hearts.", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 70)
    pen.pendown()
    pen.write("Gaining Hearts: As you complete tasks quickly and efficiently,", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 40)
    pen.pendown()
    pen.write("you will earn extra hearts, which represent additional 'lives' you", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 10)
    pen.pendown()
    pen.write("can use.", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -20)
    pen.pendown()
    pen.write("Using Hearts to Skip Games: If you want to skip a mini-game,", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -50)
    pen.pendown()
    pen.write("you can use one heart. Be careful, though-this will cost you a", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -80)
    pen.pendown()
    pen.write("heart, so use it wisely!", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -110)
    pen.pendown()
    pen.write("Losing Hearts: If you take too long on a task or fail to complete",align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -140)
    pen.pendown()
    pen.write("it in time, you will lose a heart. Keep an eye on your hearts, as", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -170)
    pen.pendown()
    pen.write("running out means game over!", align="left", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -250)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()


# Drawing of School Map
def schoolmap():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-20, 260)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.pendown()
    pen.write('School Map', font=('Comic Sans MS', 24, 'bold'))

    # School Outline
    pen.penup()
    pen.pencolor("white")
    pen.goto(-250, 250)
    pen.pendown()
    pen.forward(500)
    pen.left(-90)
    pen.forward(500)
    pen.right(90)
    pen.forward(500)
    pen.left(-90)
    pen.forward(500)
    pen.hideturtle()

    # Lobby

    # Left Building
    pen.penup()
    pen.goto(-150, 250)
    pen.pendown()
    pen.left(180)
    pen.forward(450)
    pen.left(-90)
    pen.forward(100)

    #
    # Left Classrooms
    pen.penup()
    pen.goto(-150, 125)
    pen.pendown()
    pen.left(-180)
    pen.forward(-100)

    pen.penup()
    pen.goto(-240,180)
    pen.pendown()
    pen.write("Ms. Mimi's Classroom")


    pen.penup()
    pen.goto(-150, -72)
    pen.pendown()
    pen.left(-180)
    pen.forward(100)

    pen.penup()
    pen.goto(-240, 50)
    pen.pendown()
    pen.write("Classroom Lab Room")

    pen.penup()
    pen.goto(-240, -140)
    pen.pendown()
    pen.write("Classroom 1")

    # Right Building
    pen.penup()
    pen.goto(150, 250)
    pen.pendown()
    pen.left(90)
    pen.forward(500)

    # Right Classrooms
    pen.penup()
    pen.goto(150, 90 )
    pen.pendown()
    pen.left(90)
    pen.forward(100)

    pen.penup()
    pen.goto(180, 180)
    pen.pendown()
    pen.write("Gym")

    pen.penup()
    pen.goto(150, -20)
    pen.pendown()
    pen.forward(100)

    pen.penup()
    pen.goto(180, 40)
    pen.pendown()
    pen.write("Classroom 2")

    pen.penup()
    pen.goto(150, -150)
    pen.pendown()
    pen.forward(100)

    pen.penup()
    pen.goto(180, -100)
    pen.pendown()
    pen.write("Classroom 3")

    pen.penup()
    pen.goto(180, -200)
    pen.pendown()
    pen.write("Classroom 4")

    # Lobby
    pen.penup()
    pen.goto(-100, -250)
    pen.pendown()
    pen.setheading(90)
    pen.forward(150)

    pen.setheading(0)
    pen.forward(200)

    pen.setheading(270)
    pen.forward(150)

    pen.penup()
    pen.goto(-10, -200)
    pen.pendown()
    pen.write("Lobby")

    # Principal's Office
    pen.penup()
    pen.goto(50, -150)
    pen.pendown()
    pen.setheading(0)
    pen.forward(50)

    pen.setheading(270)
    pen.forward(50)

    pen.setheading(180)
    pen.forward(50)

    pen.setheading(90)
    pen.forward(50)

    pen.penup()
    pen.goto(60, -190)
    pen.pendown()
    pen.write("Principal's Office")

    # Cafeteria
    pen.penup()
    pen.goto(-100, 250)
    pen.pendown()
    pen.setheading(270)
    pen.forward(150)
    pen.setheading(0)
    pen.forward(200)
    pen.setheading(90)
    pen.forward(150)

    pen.penup()
    pen.goto(-10, 180)
    pen.pendown()
    pen.write("Cafeteria")

    # Playground
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.write("Playground")

    pen.penup()
    pen.goto(-390, -280)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()

def chooseRoom():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 270)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.pendown()
    pen.write('Now after viewing the map choose which room you would like to', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 240)
    pen.pendown()
    pen.write("go to first.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 210)
    pen.pendown()
    pen.write("1) The Principal's Office", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 180)
    pen.pendown()
    pen.write("2) Ms. Mimi's Class", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 150)
    pen.pendown()
    pen.write("3) The Gym", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 120)
    pen.pendown()
    pen.write("4) The Playground", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 90)
    pen.pendown()
    pen.write("5) The Cafeteria", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 60)
    pen.pendown()
    pen.write("Choose the room you want to go into by entering a number 1-5", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 30)
    pen.pendown()
    pen.write("that will indicate the choices above:", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -280)
    pen.pendown()
    pen.color("white")
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    pen.hideturtle()
    screen.update()
    # Time to close
    input("Press Enter to continue...")
    pen.clear()

def principalOfficeInstructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write('Special Instructions for: The Playground', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 230)
    pen.pendown()
    pen.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 200)
    pen.pendown()
    pen.write("Game Instructions: You must guess a randomly chosen number", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 170)
    pen.pendown()
    pen.write("between 1 and 10. You have a maximum of 5 attempts to guess", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 140)
    pen.pendown()
    pen.write("the correct number. ", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 110)
    pen.color("purple")
    pen.pendown()
    pen.write("Gaining Hearts: If you guess the correct number on the first",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 80)
    pen.pendown()
    pen.write("attempt, you gain one heart ❤️.",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 50)
    pen.color("red")
    pen.pendown()
    pen.write("Losing Hearts: If you fail to guess correctly within 5 attempts,",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 20)
    pen.pendown()
    pen.write("you lose one heart.", font=('Comic Sans MS', 24, 'bold'))


    pen.penup()
    pen.goto(-390, -280)
    pen.pencolor("midnightblue")
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))

    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()


def principalOffice(hearts):
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    # Title Pen
    title_pen = turtle.Turtle()
    title_pen.hideturtle()
    title_pen.penup()
    title_pen.speed(0)
    title_pen.pencolor("white")

    # Feedback Pen
    feedback_pen = turtle.Turtle()
    feedback_pen.hideturtle()
    feedback_pen.penup()
    feedback_pen.speed(0)
    feedback_pen.pencolor("white")

    # Guess Pen
    guess_pen = turtle.Turtle()
    guess_pen.hideturtle()
    guess_pen.penup()
    guess_pen.speed(0)
    guess_pen.pencolor("white")

    # Write Title
    title_pen.goto(-390, 260)
    title_pen.write("You have entered: Principal's Office", font=('Comic Sans MS', 30, 'bold'))

    title_pen.goto(-390, 230)
    title_pen.write("Task: Guess a number between 1-10 (use the console): ", font=('Comic Sans MS', 24, 'bold'))

    randNum = random.randint(1, 10)

    userGuess = 0

    numOfGuesses = 0

    while userGuess != randNum and numOfGuesses < 5:
        try:

            userGuess = int(input("Task: Guess a number between 1 -10 (use the console): "))

            guess_pen.clear()
            feedback_pen.clear()

            if userGuess < 1 or userGuess > 10:
                print("Invalid input. ")

                feedback_pen.goto(-390, 200)
                feedback_pen.write("Invalid input.", font=('Comic Sans MS', 24, 'bold'))
            else:
                numOfGuesses += 1

                guess_pen.goto(-390, 200)
                guess_pen.color("midnightblue")
                guess_pen.write(f"You guessed number: {userGuess}." , font=('Comic Sans MS', 24, 'bold'))

                if userGuess < randNum:
                    #print("Your guess was less than the number.")

                    feedback_pen.goto(-390, 120)
                    feedback_pen.write("That is incorrect. Guess Higher.", font=('Comic Sans MS', 24, 'bold'))
                elif userGuess > randNum:
                    #print("Your guess was greater than the number.")


                    feedback_pen.goto(-390, 120)
                    feedback_pen.write("That is incorrect. Guess Lower.", font=('Comic Sans MS', 24, 'bold'))
                else:
                    #print("You guessed correctly!")

                    feedback_pen.goto(-390, 120)
                    feedback_pen.write("You guessed correctly!", font=('Comic Sans MS', 24, 'bold'))
                    feedback_pen.goto(-390, 90)
                    feedback_pen.write("But sadly the ghost is not in here. You can now go to another", font=('Comic Sans MS', 24, 'bold'))
                    feedback_pen.goto(-390, 60)
                    feedback_pen.write("room.", font=('Comic Sans MS', 24, 'bold'))

                    if numOfGuesses == 1:
                        new_hearts = min(hearts + 1, USER_START_HEART)
                        if new_hearts > hearts:
                            print("You won a heart!")
                            feedback_pen.goto(-390, 30)
                            feedback_pen.write("You won a heart!", font=('Comic Sans MS', 24, 'bold'))
                            hearts = new_hearts
                        break
        except ValueError:
            print("Invalid input. Guess a number between 1-10: ")
            feedback_pen.clear()
            feedback_pen.goto(-390, 200)
            feedback_pen.write("Invalid input. Guess a number between 1-10.", font=('Comic Sans MS', 24, 'bold'))

    if numOfGuesses == 5 and userGuess != randNum:
        hearts -= 1
        print("You've used up your five guesses.")
        print("You lost a heart")
        feedback_pen.clear()
        feedback_pen.goto(-390, 120)
        feedback_pen.write("You've used up your five guesses. You lost a heart", font=('Comic Sans MS', 24, 'bold'))
    hearts_display = "❤️" * hearts
    print(f"Current Hearts: {hearts_display}")
    feedback_pen.goto(-390, 0)
    feedback_pen.write(f"Current Hearts: {hearts_display}",font=('Comic Sans MS', 24, 'bold'))

    title_pen.goto(-390, -280)
    title_pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))

    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()
    return hearts

    schoolmap()
    chooseRoom()

def msMimiClassInstructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write("Special Instructions for: Ms. Mimi's Class", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 230)
    pen.pendown()
    pen.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 200)
    pen.pendown()
    pen.write("Game Instructions: You must play 3 rounds of Rock, Paper,", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 170)
    pen.pendown()
    pen.write("Scissors against the computer.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 140)
    pen.color("purple")
    pen.pendown()
    pen.write("Gaining Hearts: If you beat the computer in a round, you", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 110)
    pen.pendown()
    pen.write("gain one heart ❤️.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 80)
    pen.color("red")
    pen.pendown()
    pen.write("Losing Hearts: If the computer wins a round, you lose", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 50)
    pen.pendown()
    pen.write("one heart.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 20)
    pen.color("midnightblue")
    pen.pendown()
    pen.write("Draw: If both you and the computer choose the same move, no ", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -10)
    pen.pendown()
    pen.write("hearts are won or lost.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -280)
    pen.pencolor("midnightblue")
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))

    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()




def msMimiClass(hearts):
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    title_pen = turtle.Turtle()
    title_pen.hideturtle()
    title_pen.penup()
    title_pen.speed(0)
    title_pen.pencolor("white")

    round_pen = turtle.Turtle()
    round_pen.hideturtle()
    round_pen.penup()
    round_pen.speed(0)
    round_pen.pencolor("white")

    player_choice_pen = turtle.Turtle()
    player_choice_pen.hideturtle()
    player_choice_pen.penup()
    player_choice_pen.speed(0)
    player_choice_pen.pencolor("white")

    computer_choice_pen = turtle.Turtle()
    computer_choice_pen.hideturtle()
    computer_choice_pen.penup()
    computer_choice_pen.speed(0)
    computer_choice_pen.pencolor("white")

    result_pen = turtle.Turtle()
    result_pen.hideturtle()
    result_pen.penup()
    result_pen.speed(0)
    result_pen.pencolor("white")


    title_pen.goto(-390, 260)
    title_pen.write("You have entered: Ms. Mimi's Class", font=('Comic Sans MS', 30, 'bold'))

    title_pen.goto(-390, 230)
    title_pen.write("Task: Playing Rock, Paper, Scissors with the computer (use the console): ", font=('Comic Sans MS', 24, 'bold'))

    rounds = 3

    for round_num in range(1, rounds + 1):
        round_pen.clear()
        player_choice_pen.clear()
        computer_choice_pen.clear()
        result_pen.clear()

        round_pen.goto(-390, 200)
        round_pen.write(f"Round {round_num} of {rounds}", font=('Comic Sans MS', 24, 'bold'))
        computerHand = random.randint(1, 3)

        if computerHand == 1:
            computerChoice = "Rock"
        elif computerHand == 2:
            computerChoice = "Paper"
        else:
            computerChoice = "Scissors"

        playerHand = input("Choose either rock, paper, or scissors by entering 'R', 'P' or 'S': ")

        while playerHand != "R" and playerHand != "P" and playerHand != "S":
            print('Invalid choice.')
            playerHand = input("Choose either rock, paper, or scissors by entering 'R', 'P' or 'S':")

        if playerHand == 'R':
            playerChoice = "Rock"
        elif playerHand == 'P':
            playerChoice = "Paper"
        else:
            playerChoice = "Scissors"

        player_choice_pen.goto(-390, 150)
        player_choice_pen.write(f" You chose {playerChoice}.", font=('Comic Sans MS', 24, 'bold'))
        computer_choice_pen.goto(-390, 120)
        computer_choice_pen.write(f"Computer chose {computerChoice}.", font=('Comic Sans MS', 24, 'bold'))

        #result_pen.goto(-390, 80)
        if playerHand == 'R' and computerHand == 3 or \
            playerHand == 'P' and computerHand == 1 or \
            playerHand == 'S' and computerHand == 2:
            result = "Congratulations, you win! You get one heart."
            new_hearts = min(hearts + 1, USER_START_HEART)
            if new_hearts > hearts:
                print("You won a heart!")
                #result_pen.goto(-390, 0)
                #result_pen.write(f"Congratulations, you win! You get one heart.", font=('Comic Sans MS', 24, 'bold'))
                #result_pen.goto(-390, -30)
                hearts = new_hearts

        elif playerHand == 'R' and computerHand == 2 or \
            playerHand == 'P' and computerHand == 3 or \
            playerHand == 'S' and computerHand == 1:
            result = "You lost the Rock, paper, scissors game. You lost a heart."
            hearts -= 1
            #result_pen.goto(-390, -20)
        else:
            result = "Its a draw. You get no hearts."

        result_pen.goto(-390, 80)
        result_pen.write(result, font=('Comic Sans MS', 24, 'bold'))

        if hearts == 0:
            print("You lost all your hearts! Game over.")
            result_pen.goto(-390, -20)
            result_pen.write("You lost all your hearts! Game over.", font=('Comic Sans MS', 24, 'bold'))
            break

        #result_pen.write(result, font=('Comic Sans MS', 24, 'bold'))

        hearts_display = "❤️" * hearts
        print(f"Current Hearts: {hearts}")
        result_pen.goto(-390, -50)
        result_pen.write(f"Current Hearts: {hearts_display}", font=('Comic Sans MS', 24, 'bold'))

        #result_pen.goto(-390, -280)
        if round_num < rounds:
            result_pen.goto(-390, -150)
            result_pen.write("Press Enter to continue to the next round ( on the console):", font=('Comic Sans MS', 24, 'bold'))
        else:
            result_pen.goto(-390, -150)
            result_pen.write("Press Enter to continue to next room (on the console)...", font=('Comic Sans MS', 18, 'bold'))

        input("Press Enter to continue...")

    result_pen.goto(-390, -250)
    hearts_display = "❤️" * hearts if hearts > 0 else "No hearts left."
    result_pen.write(f"Final Hearts: {hearts_display}", font=('Comic Sans MS', 24, 'bold'))
    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()
    return hearts

def gymInstructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write("Special Instructions for: The Gym", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 230)
    pen.pendown()
    pen.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 200)
    pen.pendown()
    pen.write("Game Instructions: You must complete a Word Search Challenge.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 170)
    pen.pendown()
    pen.write("The challenge involves finding 16 fitness-related words hidden", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 140)
    pen.pendown()
    pen.write("in a grid.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 110)
    pen.color("purple")
    pen.pendown()
    pen.write("Gaining Hearts: If all the words are found in under 5 minutes you", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 80)
    pen.pendown()
    pen.write("earn one heart ❤️.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 50)
    pen.color("red")
    pen.pendown()
    pen.write("Losing Hearts: If it takes longer than 10 minutes for you to find", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 20)
    pen.pendown()
    pen.write("all the words you lose one heart.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -10)
    pen.color("midnightblue")
    pen.pendown()
    pen.write("No Gain or Lost Hearts: If you find all the words between 5 and", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -40)
    pen.pendown()
    pen.write("10 minutes no hearts are won or lost.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -280)
    pen.pencolor("midnightblue")
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))

    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()


def gym(hearts):
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 270)
    pen.pencolor("white")
    pen.pensize(10)
    pen.pendown()
    pen.write('You have entered: The Gym', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 240)
    pen.pendown()
    pen.write("Task: Playing Word Search", font=('Comic Sans MS', 24, 'bold'))

    hearts_pen = turtle.Turtle()
    hearts_pen.hideturtle()
    hearts_pen.speed(0)
    hearts_pen.penup()
    hearts_pen.pencolor("white")
    hearts_pen.goto(50, 250)
    hearts_pen.write(f"Current Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))


    pen.penup()
    pen.goto(-390, 190)
    pen.pendown()
    pen.write("W   O   R   K   O   U   T   J   D   H   E   F   U   R   R",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 160)
    pen.pendown()
    pen.write("O   A    R   E   S   T   R   E   N   G   T   H   G   Q  R",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 130)
    pen.pendown()
    pen.write("H   C    J   F   H   H   I   K    I   N   G   P   Q   R  Y",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 100)
    pen.pendown()
    pen.write("P    R   U   N   N   I   N   G   N   E   Q  S   Q   Y   K",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 70)
    pen.pendown()
    pen.write("F    I   C   F   O   A   A   R   U   X   N   I   I   M   V",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 40)
    pen.pendown()
    pen.write("R    K   H   I   F   G   Q   U   T   E   I   A   U   A   W",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 10)
    pen.pendown()
    pen.write("P    K   R   T   O   Y   C    F   R   R   Z   E   N   N   A",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -20)
    pen.pendown()
    pen.write("V    Z   C   N   Z   B   G   D   I   C   D   R   C    B   L",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -50)
    pen.pendown()
    pen.write("A    F   H   E   G   Y   M   Y   T   I   A   O   B   Q   K",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -80)
    pen.pendown()
    pen.write("Y    F   B    S   F   S   A   O   I   S   N   B   B   Y   I",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -110)
    pen.pendown()
    pen.write("I    U   X   S   T   T    E   G   O   E   C   I   L   L   N",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -140)
    pen.pendown()
    pen.write("E    M   U   S   C   L    E   A   N   O  E   C   J   Z   G",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -170)
    pen.pendown()
    pen.write("I    R    Z   R   W  A   R   M   U   P   X   S  W   U   F",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -200)
    pen.pendown()
    pen.write("A   N    O   H   E   A   R   T   U   A   V   A   I   J   A",font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -230)
    pen.pendown()
    pen.write("T   W    E   I   G   H   T   S   K    F   O   V   J  H   H",font=('Comic Sans MS', 24, 'bold'))

    start_time = time.time()

    words_to_find = {"dance", "workout", "fitness", "walking", "strength", "nutrition", "aerobics", "heart", "weights",
                     "gym", "muscle", "yoga", "warmup", "exercise", "running", "hiking"}


    while words_to_find:
        pen.penup()
        pen.goto(-390, -260)
        pen.pendown()
        pen.write("Enter word (on the console): ",font=('Comic Sans MS', 24, 'bold'))
        userWord = input("Enter word: ").strip().lower()

        if userWord in words_to_find:
            words_to_find.remove(userWord)

            if userWord == "walking":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(295, 70)
                pen.setheading(270)
                pen.pendown()
                pen.forward(214)
            elif userWord == "workout":
                 pen.pencolor("midnightblue")
                 pen.pensize(5)
                 pen.penup()
                 pen.goto(-390, 210)
                 pen.setheading(0)
                 pen.pendown()
                 pen.forward(320)
            elif userWord == "fitness":
                 pen.pencolor("midnightblue")
                 pen.pensize(5)
                 pen.penup()
                 pen.goto(-235, 100)
                 pen.setheading(270)
                 pen.pendown()
                 pen.forward(200)
            elif userWord == "gym":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-190, -33)
                pen.setheading(0)
                pen.pendown()
                pen.forward(120)
            elif userWord == "strength":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-190, 175)
                pen.pendown()
                pen.forward(360)
            elif userWord == "nutrition":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(10, 120)
                pen.setheading(270)
                pen.pendown()
                pen.forward(250)
            elif userWord == "aerobics":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(150, 70)
                pen.setheading(270)
                pen.pendown()
                pen.forward(243)
            elif userWord == "heart":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-240, -180)
                pen.setheading(0)
                pen.pendown()
                pen.forward(220)
            elif userWord == "weights":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-350, -210)
                pen.setheading(0)
                pen.pendown()
                pen.forward(330)
            elif userWord == "dance":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(105, 5)
                pen.setheading(270)
                pen.pendown()
                pen.forward(145)
            elif userWord == "muscle":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-350, -122)
                pen.setheading(0)
                pen.pendown()
                pen.forward(290)
            elif userWord == "yoga":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-33, -17)
                pen.setheading(270)
                pen.pendown()
                pen.forward(120)
            elif userWord == "warmup":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-200, -150)
                pen.setheading(0)
                pen.pendown()
                pen.forward(280)
            elif userWord == "exercise":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(60, 127)
                pen.setheading(270)
                pen.pendown()
                pen.forward(230)
            elif userWord == "running":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-350, 115)
                pen.setheading(0)
                pen.pendown()
                pen.forward(323)
            elif userWord == "hiking":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-155, 145)
                pen.setheading(0)
                pen.pendown()
                pen.forward(287)


            print(f"'{userWord}' found! {len(words_to_find)} words left.")
        else:
            print("Word not found or already entered. Try again.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time <= 309:
        pen.clear()
        pen.penup()
        pen.goto(-390, 270)
        pen.pencolor("white")
        pen.pensize(10)
        pen.pendown()
        pen.write("Great job! You completed it quickly and earned a heart ❤️.", font=("Comic Sans MS", 24, "bold"))
        hearts = min(hearts + 1, USER_START_HEART)
    elif elapsed_time <= 609:
        pen.clear()
        pen.penup()
        pen.goto(-390, 270)
        pen.pencolor("white")
        pen.pensize(10)
        pen.pendown()
        pen.write("You completed it, but no extra heart earned.", font=("Comic Sans MS", 24, "bold"))
    else:
        pen.clear()
        pen.penup()
        pen.goto(-390, 270)
        pen.pencolor("white")
        pen.pensize(10)
        pen.pendown()
        pen.write("Too slow! You lost a heart 💔.", font=("Comic Sans MS", 24, "bold"))
        hearts -= 1

    hearts_pen.clear()
    hearts_pen.penup()
    hearts_pen.goto(-390, 240)
    hearts_pen.write(f"Hearts: {'❤️' * max(hearts, 0)}", font=("Comic Sans MS", 24, "bold"))

    if hearts == 0:
        pen.penup()
        pen.goto(-390, 60)
        pen.pendown()
        pen.write("You lost all your hearts! Game Over.", font=("Comic Sans MS", 24, "bold"))

    pen.penup()
    pen.goto(-390, -280)
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 18, 'bold'))


    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()

    return hearts

def playgroundInstructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write("Special Instructions for: The Playground", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 230)
    pen.pendown()
    pen.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 200)
    pen.pendown()
    pen.write("Game Instructions: You must complete a Hangman Challenge. It", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 170)
    pen.pendown()
    pen.write("involves guessing the correct letters to complete the hidden", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 140)
    pen.pendown()
    pen.write("word while avoiding too many incorrect guesses.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 110)
    pen.color("purple")
    pen.pendown()
    pen.write("Gaining Hearts: If you complete the hidden word with 9 tries", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 80)
    pen.pendown()
    pen.write("and no incorrect guesses you gain one heart ❤️.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 50)
    pen.color("red")
    pen.pendown()
    pen.write("Losing Hearts: If you make 6 or more incorrect guesses you lose", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 20)
    pen.pendown()
    pen.write("the game.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -10)
    pen.color("midnightblue")
    pen.pendown()
    pen.write("No Gain or Lost Hearts: If you complete the hidden word with", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -40)
    pen.pendown()
    pen.write("more than 9 tries and less than 6 incorrect guesses you don't", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -70)
    pen.pendown()
    pen.write("lose or gain a heart.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -280)
    pen.pencolor("midnightblue")
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))

    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()


def playground(hearts):
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 270)
    pen.pencolor("white")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write('You have entered: The Playground', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 240)
    pen.pendown()
    pen.write("Task: Playing Hangman with the computer (use emojis as a hint)", font=('Comic Sans MS', 24, 'bold'))

    hearts_pen = turtle.Turtle()
    hearts_pen.hideturtle()
    hearts_pen.speed(0)
    hearts_pen.penup()
    hearts_pen.pencolor("white")
    hearts_pen.goto(60, 270)
    hearts_pen.write(f"Current Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(250, 0)
    pen.pensize(5)
    pen.setheading(90)
    pen.pendown()
    pen.forward(200)

    pen.left(90)
    pen.forward(150)

    pen.setheading(270)
    pen.forward(50)

    pen.penup()
    pen.goto(-390, 0)
    pen.setheading(90)
    pen.pendown()
    pen.forward(200)
    pen.setheading(0)
    pen.forward(400)
    pen.setheading(270)
    pen.forward(200)
    pen.setheading(180)
    pen.forward(400)

    pen.penup()
    pen.goto(-330, 130)
    pen.pendown()

    pen.write("🧗‍♀️🪜", align="center", font=('Comic Sans MS', 50, 'bold'))

    pen.penup()
    pen.goto(-250, -100)
    pen.setheading(0)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)

    pen.penup()
    pen.goto(-300, -200)
    pen.setheading(0)
    pen.pendown()
    pen.forward(50)

    pen.penup()
    pen.forward(75)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.forward(50)

    letters = {"c", "l", "i", "m", "b", "a", "d", "e", "r"}

    notLetters = {"f", "g", "h", "j", "k", "n", "o", "p", "q", "s", "t", "u", "v", "w", "x", "y", "z"}

    incorrect_guesses = 0

    tries = 0

    while letters and incorrect_guesses < 6:
        #print(f"Loop running, remaining letters: {letters}")
        pen.color("white")
        pen.penup()
        pen.goto(-390, -230)
        pen.pendown()
        pen.write("Guess a letter (on the console): ", font=('Comic Sans MS', 24, 'bold'))
        userLetter = input("Guess a letter: ").strip().lower()
        #print(f"Initial tries: {tries}")
        tries += 1
        #print(f"tries increased: {tries}")

        if userLetter in letters:
            letters.remove(userLetter)
            #print("Letters after correct guess: ", letters)

            if userLetter == "c":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-235, -100)
                pen.setheading(0)
                pen.pendown()
                pen.write("C", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "l":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-135, -100)
                pen.setheading(0)
                pen.pendown()
                pen.write("L", font=('Comic Sans MS', 40, 'bold'))

                pen.penup()
                pen.goto(-164, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("L", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "i":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-35, -100)
                pen.setheading(0)
                pen.pendown()
                pen.write("I", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "m":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(65, -100)
                pen.setheading(0)
                pen.pendown()
                pen.write("M", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "b":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(165, -100)
                pen.setheading(0)
                pen.pendown()
                pen.write("B", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "a":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(-285, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("A", font=('Comic Sans MS', 40, 'bold'))

                pen.penup()
                pen.goto(-64, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("A", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "d":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(36, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("D", font=('Comic Sans MS', 40, 'bold'))

                pen.penup()
                pen.goto(136, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("D", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "e":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(236, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("E", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "r":
                pen.pencolor("midnightblue")
                pen.pensize(5)
                pen.penup()
                pen.goto(336, -200)
                pen.setheading(0)
                pen.pendown()
                pen.write("R", font=('Comic Sans MS', 40, 'bold'))
        elif userLetter in notLetters:
            notLetters.remove(userLetter)
            incorrect_guesses += 1
            print("Incorrect guess! The ghost is forming...")

            if userLetter == "f":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-270, 130)
                pen.setheading(0)
                pen.pendown()
                pen.write("F", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "g":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-230, 130)
                pen.setheading(0)
                pen.pendown()
                pen.write("G", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "h":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-190, 130)
                pen.setheading(0)
                pen.pendown()
                pen.write("H", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "j":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-150, 130)
                pen.setheading(0)
                pen.pendown()
                pen.write("J", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "k":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-110, 130)
                pen.setheading(0)
                pen.pendown()
                pen.write("K", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "n":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-70, 130)
                pen.setheading(0)
                pen.pendown()
                pen.write("N", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "o":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-380, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("O", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "p":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-340, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("P", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "q":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-300, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("Q", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "s":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-250, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("S", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "t":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-210, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("T", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "u":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-170, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("U", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "v":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-130, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("V", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "w":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-85, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("W", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "x":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-30, 75)
                pen.setheading(0)
                pen.pendown()
                pen.write("X", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "y":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-380, 0)
                pen.setheading(0)
                pen.pendown()
                pen.write("Y", font=('Comic Sans MS', 40, 'bold'))
            elif userLetter == "z":
                pen.pencolor("red")
                pen.pensize(3)
                pen.penup()
                pen.goto(-330, 0)
                pen.setheading(0)
                pen.pendown()
                pen.write("Z", font=('Comic Sans MS', 40, 'bold'))

            if incorrect_guesses == 1:
                pen.color("white")
                pen.pensize(3)

                # Draw Ghost Design

                # Ghost Head
                pen.penup()
                pen.goto(100, 50)
                pen.pendown()
                pen.begin_fill()
                pen.fillcolor("white")
                pen.circle(50)
                pen.end_fill()
            elif incorrect_guesses == 2:
                # Right End Circle
                pen.color("white")
                pen.pensize(3)
                pen.penup()
                pen.goto(150, 50)
                pen.pendown()
                pen.begin_fill()
                pen.circle(20)
                pen.end_fill()

                # Right Middle Circle
                pen.penup()
                pen.goto(130, 25)
                pen.pendown()
                pen.begin_fill()
                pen.circle(20)
                pen.end_fill()
            elif incorrect_guesses == 3:
                # Middle Circle
                pen.color("white")
                pen.pensize(3)
                pen.penup()
                pen.goto(100, 20)
                pen.pendown()
                pen.begin_fill()
                pen.circle(20)
                pen.end_fill()
            elif incorrect_guesses == 4:
                # Left Middle Circle
                pen.color("white")
                pen.pensize(3)
                pen.penup()
                pen.goto(70, 25)
                pen.pendown()
                pen.begin_fill()
                pen.circle(20)
                pen.end_fill()

                # Left End Circle
                pen.penup()
                pen.goto(50, 50)
                pen.pendown()
                pen.begin_fill()
                pen.circle(20)
                pen.end_fill()
            elif incorrect_guesses == 5:
                # Ghost Eyes

                # Left Eye
                pen.color("black")
                pen.penup()
                pen.goto(115, 110)
                pen.pendown()
                pen.begin_fill()
                pen.fillcolor("black")
                pen.circle(4)
                pen.end_fill()

                # Right Eye
                pen.penup()
                pen.goto(90, 110)
                pen.pendown()
                pen.begin_fill()
                pen.fillcolor("black")
                pen.circle(4)
                pen.end_fill()
            elif incorrect_guesses == 6:
                # Ghost Mouth
                pen.color("black")
                pen.penup()
                pen.goto(91, 90)
                pen.pendown()

                # Squiggly mouth
                pen.forward(5)
                pen.left(25)
                pen.forward(5)
                pen.right(25)
                pen.forward(5)
                pen.left(-25)
                pen.forward(5)
                pen.right(-25)
                pen.forward(5)
                # tries += 1
        else:
            print("Invalid input or already guessed! Try again.")


            # print(f"Tries: {tries}, Incorrect Guesses: {incorrect_guesses}, Hearts: {hearts}")
            #print("Before checking letters: ", letters)

            #print(f"Remaining letters before checking win condition: {letters}")

    if tries == 9 and incorrect_guesses == 0:
        # print("All letters guessed")
        if hearts < 3:
            hearts += 1
        # print(f"Checking if hearts should be cleared: tries = {tries}")
        hearts_pen.clear()
        hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

        pen.penup()
        pen.goto(-390, -260)
        pen.color("midnightblue")
        pen.pendown()
        pen.write("You won a heart! You have found the ghost as well!", font=('Comic Sans MS', 24, 'bold'))
        # time.sleep(2)
        # print(f"Breaking loop, tries = {tries}")
        #break


    #print(f"Checking tries condition: {tries}")
    if tries > 9 and incorrect_guesses < 6:
        # print("Tries exceeded")
        hearts_pen.clear()
        hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))
        pen.penup()
        pen.goto(-390, -260)
        pen.color("midnightblue")
        pen.pendown()
        pen.write("You won! You have found the ghost!", font=('Comic Sans MS', 24, 'bold'))
        # print("All letters guessed! You won!")
        #break

    if incorrect_guesses == 6:
        #print("Max incorrect guesses reached!")
        hearts -= 1
        hearts_pen.clear()
        hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

        pen.penup()
        pen.goto(-390, -260)
        pen.color("midnightblue")
        pen.pendown()
        pen.write("Game Over! You lost! The ghost got you!", font=('Comic Sans MS', 24, 'bold'))
        #break  # Exit the loop since the game is over


    pen.penup()
    pen.goto(-390, -285)
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))
    pen.hideturtle()

    screen.update()

    # Close Graphics
    # Time to close

    input("Press Enter to continue...")

    screen.clear()

    return hearts

def cafeteriaInstructions():
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    # Write Title
    pen.penup()
    pen.goto(-390, 260)
    pen.pencolor("midnightblue")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write("Special Instructions for: The Cafeteria", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 230)
    pen.pendown()
    pen.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 200)
    pen.pendown()
    pen.write("Game Instructions: You must complete a Tic Tac Toe Challenge", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 170)
    pen.pendown()
    pen.write("against the computer.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 140)
    pen.color("purple")
    pen.pendown()
    pen.write("Gaining Hearts: If you win, you earn one heart ❤️.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 110)
    pen.color("red")
    pen.pendown()
    pen.write("Losing Hearts: If you end up in a tie, you lose a heart. If", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 80)
    pen.pendown()
    pen.write("the computer wins, you lose a heart and lose the game.", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, -280)
    pen.pencolor("midnightblue")
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))

    # Close Graphics
    # Time to close
    input("Press Enter to continue...")
    screen.clear()


def cafeteria(hearts):
    screen = turtle.Screen()
    screen.title("Ghost Hunter")
    screen.setup(800, 600)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)

    hearts_pen = turtle.Turtle()
    hearts_pen.hideturtle()
    hearts_pen.speed(0)
    hearts_pen.penup()
    hearts_pen.pencolor("white")
    hearts_pen.goto(60, 270)
    hearts_pen.write(f"Current Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

    # Write Title
    pen.penup()
    pen.goto(-390, 270)
    pen.pencolor("white")
    pen.pensize(10)
    pen.hideturtle()
    pen.pendown()
    pen.write('You have entered: The Cafeteria', font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 240)
    pen.pendown()
    pen.write("Task: Playing Tic Tac Toe with the Computer", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-100, 200)
    pen.setheading(270)
    pen.pendown()
    pen.forward(300)

    pen.penup()
    pen.goto(100, 200)
    pen.setheading(270)
    pen.pendown()
    pen.forward(300)

    pen.penup()
    pen.goto(-250, 0)
    pen.setheading(0)
    pen.pendown()
    pen.forward(500)

    pen.penup()
    pen.goto(-250,100)
    pen.setheading(0)
    pen.pendown()
    pen.forward(500)

    pen.penup()
    pen.goto(-190, 180)
    pen.pendown()
    pen.color("yellow")
    pen.write("1", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-10, 180)
    pen.pendown()
    pen.color("yellow")
    pen.write("2", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(170, 180)
    pen.pendown()
    pen.color("yellow")
    pen.write("3", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-190, 60)
    pen.pendown()
    pen.color("yellow")
    pen.write("4", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-10, 60)
    pen.pendown()
    pen.color("yellow")
    pen.write("5", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(170, 60)
    pen.pendown()
    pen.color("yellow")
    pen.write("6", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-190, -40)
    pen.pendown()
    pen.color("yellow")
    pen.write("7", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-10, -40)
    pen.pendown()
    pen.color("yellow")
    pen.write("8", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(170, -40)
    pen.pendown()
    pen.color("yellow")
    pen.write("9", font=('Comic Sans MS', 24, 'bold'))



    computerMove = random.randint(1, 9)
    userMove = 0

    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]


    pen.penup()
    pen.goto(-390, -140)
    pen.pendown()
    pen.pencolor("yellow")
    pen.write("Reminder: Yellow numbers on board indicate position on board ", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 70)
    pen.pendown()
    pen.pencolor("red")
    pen.write("Computer's", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(-390, 40)
    pen.pendown()
    pen.pencolor("red")
    pen.write("Symbol: O ", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(270, 70)
    pen.pendown()
    pen.pencolor("purple")
    pen.write("Your", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(270, 40)
    pen.pendown()
    pen.pencolor("purple")
    pen.write("Symbol:", font=('Comic Sans MS', 24, 'bold'))

    pen.penup()
    pen.goto(270, 10)
    pen.pendown()
    pen.pencolor("purple")
    pen.write("X", font=('Comic Sans MS', 24, 'bold'))

    while True:

        pen.penup()
        pen.goto(-390, -170)
        pen.pendown()
        pen.pencolor("midnightblue")
        pen.write("Enter your move (1-9)? (on the console): ", font=('Comic Sans MS', 24, 'bold'))
        #user_move = int(input("Enter your move (1-9)? : "))

        while True:
            try:
                user_move = int(input("Enter your move (1-9)? : "))
                if 1 <= user_move <= 9 and is_valid_move(board, user_move):
                    break
                print("Invalid move. Try again.", end="")
            except ValueError:
                print("Please enter a number between 1 and 9.", end="")

        place_move(board, user_move, 'X', pen)

        if has_winner(board, 'X'):
            if hearts < 3:
                hearts += 1
            hearts_pen.clear()
            hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))
            pen.penup()
            pen.pencolor("red")
            pen.goto(-390, -200)
            pen.pendown()
            pen.write("You won! You get a heart! The ghost isn't here, you may go to", font=('Comic Sans MS', 24, 'bold'))
            pen.penup()
            pen.goto(-390, -230)
            pen.pendown()
            pen.write("another room.", font=('Comic Sans MS', 24, 'bold'))
            print("You won!")
            break

        if is_board_full(board):
            hearts -= 1
            hearts_pen.clear()
            hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

            pen.penup()
            pen.pencolor("red")
            pen.goto(-390, -200)
            pen.pendown()
            pen.write("It's a tie! You lost a heart! The ghost isn't here, you may go to",font=('Comic Sans MS', 24, 'bold'))
            pen.penup()
            pen.goto(-390, -230)
            pen.pendown()
            pen.write("another room.", font=('Comic Sans MS', 24, 'bold'))
            print("It's a tie! You lost a heart! The ghost isn't here, you may go to another room.")
            break

        # Computer's Turn
        computer_move = computer_turn(board)
        print(f"Computer chose {computer_move}")
        place_move(board, computer_move, 'O', pen)

        if has_winner(board, 'O'):
            hearts -= 1
            hearts_pen.clear()
            hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

            pen.penup()
            pen.pencolor("red")
            pen.penup()
            pen.pencolor("red")
            pen.goto(-390, -200)
            pen.pendown()
            pen.write("Computer wins! Game Over!", font=('Comic Sans MS', 24, 'bold'))
            print("Computer wins! Game Over!", end="")
            break

        if is_board_full(board):
            hearts -= 1
            hearts_pen.clear()
            hearts_pen.write(f"Final Hearts: {'❤️' * hearts}", font=('Comic Sans MS', 24, 'bold'))

            pen.penup()
            pen.pencolor("red")
            pen.penup()
            pen.pencolor("red")
            pen.goto(-390, -200)
            pen.pendown()
            pen.write("It's a tie! You lost a heart! The ghost isn't here, you may go to another room.", font=('Comic Sans MS', 24, 'bold'))
            pen.penup()
            pen.goto(-390, -230)
            pen.pendown()
            pen.write("another room.", font=('Comic Sans MS', 24, 'bold'))
            print("It's a tie! The ghost isn't here, you may go to another room.")
            break


    pen.penup()
    pen.goto(-390, -285)
    pen.pencolor("midnightblue")
    pen.pendown()
    pen.write("Press Enter to continue (on the console)...", font=('Comic Sans MS', 24, 'bold'))
    pen.hideturtle()

    screen.update()

    # Close Graphics
    # Time to close

    input("Press Enter to continue...")

    screen.clear()

def is_valid_move(board, position):
    row, col = (position - 1) // 3, (position - 1) % 3
    return board[row][col] == ' '

def place_move(board, position, symbol, pen):
    positions = {
        1: (-190, 120), 2: (-10, 120), 3: (170, 120),
        4: (-190, 10),  5: (-10, 10),  6: (170, 10),
        7: (-190, -90), 8: (-10, -90), 9: (170, -90)
    }

    row, col = (position - 1) // 3, (position - 1) % 3
    board[row][col] = symbol

    pen.penup()
    pen.goto(positions[position])
    pen.pendown()

    pen.color("purple" if symbol == 'X' else "red")
    pen.write(symbol, font=('Comic Sans MS', 52, 'bold'))


def has_winner(board, symbol):
    for row in board:
        if row[0] == row[1] == row[2] == symbol:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    if (board[0][0] == board[1][1] == board[2][2] == symbol) or (board[0][2] == board[1][1] == board[2][0] == symbol):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def computer_turn(board):
    while True:
        computer_move = random.randint(1, 9)
        if is_valid_move(board, computer_move):
            return computer_move




main()