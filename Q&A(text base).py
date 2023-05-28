#making the slow motion of the word by control how fast or skow it is 
import time
#making the slow motion of the word
import sys
#making the slow motion of the word by making a function
def printSlow(text):
  for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)
  print("")

#making a function. called english_Q() 
def english_Q():
#variables needed
  coins = 0
  english_Q_counter = 0
#making conditional while loop to ask the question, but only giving two chances if the player got it worng at the fist 
  while english_Q_counter < 2:
#when the player choose 0, the game will print the question
    printSlow("\033[0;32;48mWhich author wrote “ Hunger Games”?\na. William Shakespere\nb. Suzanne Collins\nc. J.K.Rowling\nd. C.S.Lewis")
#after print the question, printing four choices to answer    
    english_A = input("Choose a,b,c,d:")
#if and elif statements to control the player's answer right or wrong 
    if english_A == "a" or english_A == "c" or english_A == "d":
      print("\033[0;34;48mWhat a pity, the answer is not correct. You earn 0 coins! However, I will give you 1 more chance to participate!") 
      english_Q_counter = english_Q_counter + 1
    
    elif english_A == "b":
      print("\033[0;34;48mThe answer is correct. You earn 20 coins.")
      coins = coins + 20
#when the answer is correct, stop the loop          
      break
#print the coins earned
  return coins

#making the function called maths_Q()
def maths_Q():
#variables needed
  coins = 0
  maths_Q_question_counter = 0
#Conditional while loop to ask the question, but only giving two chances if the player got it worng at the fist
  while maths_Q_question_counter < 2:
#When the player choose 1, the game will print the question    
    printSlow("\033[0;32;48mIt is a second grade question. There are 50 dogs signed up to compete in the dog show. There are 36 more small dogs than the large dogs signed to the dog show. Do you know how many large dogs there are in the dog show?")
#After print the question, give a exact number
    maths_A = input("Choose a number:")
#If and else statements to control the player's answer right or wrong
    if maths_A == "7":
      print("\033[0;34;48mCongradulation! You beat down the second graders. You earn 50 coins")
      coins = coins + 50
#When the answer is correct, stop the loop
      break
    
    else:
      print("\033[0;34;48mYou lose you but can try one more times!")

      maths_Q_question_counter = maths_Q_question_counter + 1
#Print the coins earned
  return coins

#Making the function called history_Q()
def history_Q():
#Variables needed  
  coins = 0
  history_Q_counter = 0
#Conditional while loop to ask the question, but only giving two chances if the player got it worng at the fist
  while history_Q_counter < 2:
#when the player choose 2, the game will print the question    
    printSlow("\033[0;32;48mWhich countries started World War 2?\na. Poland\nb. Russian\nc. Austria-Hungary\nd. Germany")
#After print the question, pirinting four choices to answer 
    history_A = input("Choose a,b,c,d:")
#If and elif statements to control the player's answer right or wrong 
    if history_A == "a" or history_A == "b" or history_A =="c":
      print("\033[0;34;48mWrong answer, try one more time.")
      history_Q_counter = history_Q_counter + 1
    
    if history_A == "d":
      print("\033[0;34;48mEvil Nazi started it. You earn 30.")
      coins = coins + 30
#When the answer is correct, stop the loop
      break
#Print the coins earned
  return coins

#Inro
printSlow("\033[1;31;48mWelcome to the game world!!! Q & A")
#Rules
printSlow("\033[1;36;48mRules:If you want to choose question, \nEnglish = 0 \nMaths   = 1 \nHistory = 2")

#Total variables ofcoins and turns
coins = 0
turns = 0
#Conditional while loop to ask the question, but only giving two chances if the player got it worng at the first 
while turns < 3:
  start = int(input("\033[1;37;48mEnter 0 or 1 or 2 to begin your journey:"))
#Making a list to control the 0,1,2 as English,Maths,History 
  subjects = ["English", "Maths","Hizstory"]
  #If statement control the 0,1,2 and the coins that earned by the player at corresponding questions   
  if start == 0:
    print("You chose to do", subjects[0])
    coinsEarned = english_Q()
    
  if start == 1:
    coinsEarned = maths_Q()
    print("You chose to do", subjects[1])
  
  if start == 2:
    coinsEarned = history_Q()
    print("You chose to do", subjects[2])
     
#To make it a conditional loop  
  turns = turns + 1
#To accumulate the coins the player earned, and 
  coins = coins + coinsEarned
#Because it is in the loop, after the player got the question right, it will automactically stop and print out the coins you earned, and finally, it will print out the total you got in this game. 
  print("\033[1;31;48mSo far you have earned", coins, "\033[1;31;48mcoins.")
