BIGGEST_COUNTRIES_ANSWERS=["russia","USA", "india", "brazil","canada", "australia" ]
#-------functions-------
#welcome users and introducers to the quiz
def intro():
    #ask the user their name
    name =input("what is your name")
    # great the users and introduce the quiz
    print("welcome to the quiz", name)
    print("this qui is a about largest countries in the world Can you name  them?")

def getlives():
        while True:
              lives=input("how many times do you need?")
              try : 
                    lives=int(lives)
                    if lives>= 0:
                          return lives
                    else :
                        print(" choose a positive number.")
              except:
                    print("that was not a number")

def isCorrect (answer,list):
      if answer in list:
            return True
      else :
        return False

#------main_code----
intro()
lives=getlives()

score=0
while lives>0:
      answer=input("name one of the top 10 biggest countries in the world:/n").lower()
      if isCorrect(answer, BIGGEST_COUNTRIES_ANSWERS)==True:
            print ("correct")
            score+=5
      else:
             print("wrong") 

      lives-=1     

