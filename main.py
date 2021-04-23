print(" Welcome to Treasure Island ")
print (" Your mission is to find the treasure ")

choice1 = input('You\' re at a crossroad, where do you want to go ? Type "left" or "right" : \n').lower()   # lower is to change if they type Right

if choice1 == "left" :  #continue the game
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim"to swim across : \n').lower()
  if choice2 == "wait" :   # Game will continue
    choice3= input(" You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and on blue. Which colour do you choose ? \n").lower()
    if choice3 == "red" :
      print (" it is a room full of fire. Game over.")
    elif choice3 == "yellow" :
      print (" You found the treasure ! you win ! ")
    elif choice3 == "blue"  :
      print (" You entered a room of beasts. Game over.")
    else :   
      print (" You chose a door that doesn't exit. Game over.")
  else : 
   print(" You got attacked by an angry trout, the Game is over ")
else :
   print(" You fell into a hole , the Game is over ")
