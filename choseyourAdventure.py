"""
Chose Your Adventure
Sky Tang, Luke Ullrich
@date: 9/13/19
"""
print("You wake up in a location foreign to you with the warm, dry rays of the sun hitting your skin among the humid air.")

def firstDecision():
  x = input("Your confused on what to do first. Type 'sit' to sit around for a little longer or 'search' to search the room: \n")
  if(x == "sit"):
    sit()
  elif(x == "search"):
    search()
  else:
    print("type the right commands")
    firstDecision()
  

def sit():
    print("You sit for a little bit, with little to no effect on your current state of being. You eventually start searching the room and come across a box requiring three numbers to open it.")
  
def search():
  print("You search the room and come across a box that requires a three-digit code.")
  
firstDecision()

print("________________________________ \n")

print("You end up going outside and finding out that you're alone on an island, you're a castaway.")

def secondDecision():
  y = input("Type 'left' or 'right' to direct yourself: \n" )
  if(y == "left"):
    left()
  elif(y == "right"):
    right()
  else:
    print("type the right commands")
    secondDecision()

def right():
 w = input("You've come across a boat, but the key is missing and the gas is depleted. Would you like to 'search the boat' or go 'back'? \n")
 if(w == "search the boat"):
   searchtheBoat()
 elif(w == "back"):
    back()
 else:
    print("type the right commands")
    right()


def searchtheBoat():
  print("You find a glovebox and open it, finding a three-digit code.")

def left():
    print("You've come across a locked shed with a red key hole. You head back to the house.")

def back():
  secondDecision()

secondDecision()
back()

print("________________________________ \n")


def thirdPart():
  print("You've returned to the house with the knowledge of the code found in the boat. The box is unlocked and a key with a key dipped in red paint on one end. \n")
  z = input("After opening the shed, you find a jerry can full of fuel for the boat and the boat keys. You fuel the boat and are left with two choices: type 'swim' or 'ride' for your end. \n")
  if(z == "swim"):
    swim()
  elif(z == "ride"):
    ride()
  else:
    print("type the right commands")
    thirdPart()

def swim():
  print("Even through all this effort, you decide to swim anyways, you inevitably drown in the end.")

def ride():
  print("You get into the boat, start it up, and ride off into the horizon, with hope to find the civilization you were once part of before you were CASTED AWAY. \n")

thirdPart()

print("________________________________ \n")

def replay():
  u = input("Would you like to play again? 'y' or 'n' \n ")
  if (u == "y"):
    firstDecision()
  elif(u == "n"):
    print("Goodbye!")

replay()
