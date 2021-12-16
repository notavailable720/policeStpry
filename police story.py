import time
import tkinter
from tkinter import messagebox
from tkinter import *
root = tkinter.Tk()
root.withdraw()

top = Toplevel()
top.title("You lost")

solution1 = ["Nikita", "nikita", "bob"]
solution2 = 14
solution3 = "Houston"
solution4 = ["ass", "Ass", "Dog", "dog", "Pig", "pig", "cow", "Cow", "ewe", "Ewe"]
alligator = ["alligator", "Alligator"]

print("Hello?")
print("We found out that you have been copied. Everything about you has been completely copied excpept your memories")
time.sleep(3)
print("Now, we're not sure if you're the real one or the fake copied person.")
time.sleep(2)
print("So, we're going to ask you a few questions that you should know.")
time.sleep(3)
answer1 = input("Okay, first question. What is your name? ")
if answer1 not in solution1:
        print("IT'S THE FAKE!")
        time.sleep(0.4)
        print("GET HIM!")
        messagebox.showerror("Wrong answer", "Ur dumb", parent = top)
        quit()
    
    
print("Okay", time.sleep(2), "I see. Maybe another question?")
answer2 = input("Second question, how old are you? ")
answer2 = int(answer2)
if answer2 != solution2:
    print("I guess you didn't do enough research.")
    time.sleep(0.5)
    print("GET HIM!")
    messagebox.showwarning("oof", "Incorrect answer")
    quit()

print("Okay, good.")
time.sleep(0.5)
print("Next question.")

answer3 = input("A simple math question. What is 3+2? ")
answer3 = int(answer3)
if answer3 == 32:
        print("oof")
elif answer3 != 3+2:    
     print("wut. I so you know the facts of he person but not basic math? Weird")
     messagebox.showwarning("oof", "Incorrect answer")
     quit()
time.sleep(2)
print("Okay, last math question")
answer4 = input("What is 9*2? ")
answer4 = int(answer4)
if answer4 != 9*2:
    time.sleep(3)
    print("How did you manage to get this far?")
    time.sleep(1)
    print("Get it out of my sight")
    messagebox.showwarning("oof", "Incorrect answer")
    quit()

time.sleep(3)
print("Okay, last question. This one is a gimme." )
time.sleep(2)
answer4 = input("Name a farm animal with 3 letters in its name: ")
if answer4 not in solution4:
        print("Dang, that was a gimme.")
elif answer4 in alligator:
        print("Cue family fued laughter and stunned looks")


time.sleep(1)
print("Okay you're the real one.")
time.sleep(1)
print("Now we can work together to find the copy of you")
quit()
    
