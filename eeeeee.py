GOOD_COMMENTS= ["WAY TTO GO","KEEP IT UP","FANTASTIC"]
BAD_COMMENTS=["TRY AGAIN","DO NOT GIVEUP","MAY BE NEXT TIME"]
# Ask the user their name and save it
name =input("What is your name")
#Greet the user and introduce the quiz
print("Let us play a game.")
print("welcome to this quiz,", name)
print("This quiz  is  about  capital cities of the world")
print(" wellington is the  capital of New Zealand.")
#Ask the user a question
answer =input("what is the cpital of new zealand?")
#check the user's answer and give a feedback


#tell the user the answer
 
    
if answer=="wellington":
    print("it is correct answer")
elif answer != "auckland" and answer != "auckland":
    
    print("that is wrong.")
else:
    print("wrong")
    print("the answer is wellington.")
print("that was not an option.")
#End the quiz
print("well done{}YOu have finished the quiz. Your score is {}. (name, score)")
import random
QUESTION_FORMAT="{}/nA.{}.B{}. C{}. D{}"
question="what is the capital of New zealand?"
a= "wellington"
b= "auckland"
c= "christchurch"
d= "london"
answer=input(QUESTION_FORMAT.format(question,a,b,c,d)).lower()
#ccheck user's answer.
if answer=="a" or answer==a:
    print ("you are correct.")
elif answer!= "a" and answer!= a :
    print ("that was not an option")
else:
    print ("wrong!")
print("correct answer is wellington")
play ="yes"
while play=="yes":
    score=0
    question ='what is the capital of new zealand?'
    play==input("do you want to play again?").lower()
while True:
    try:
        tries= int (input("how many attemts do you want to each question?1-4"))  
        tries=int(tries) 
        break
    except:
        print("that is not anumber.")

    tries =1
while tries<=4:
    print("you can try again.")
tries=tries-1
question_attempts= tries 
while question_attempts>=0:
    #Ask the user a question
    question = "what is te capital of new zealand?"
    if answer == "auckland":
        print("corrcet")
        score+=5
        print(GOOD_COMMENTS[0])
        break
    else :
        print ("wrong")
        print(BAD_COMMENTS[0])
    question_attempts-=1
    print("the answer is wellington")

questions=["what is the capital of new zealand?",
           "what is the highest mountain in new zealnd?",
           "what is the most common pet in New zealnd?"]
options=[["auckland", "wellington","christchurch"],
         ["cat", "dog","rabbit"],
         ["mt taranaki","mt eiden"]]
short_options=["a","b","c","d"]
answers=[2,1,1]
for i in range(len (questions)):
    question_attempts= tries 
    while question_attempts>=0:
    #Ask the user a question
        answer=input(QUESTION_FORMAT= format(questions[i], 
                                     options[i][0],options[i][1], options[i][2], options[i][3])).lower
        if answer== options[0] [answers[0]] or  answers== short_options [answers[i]]:
            print("corrcet") 
            score+=5
            print (random.chice(GOOD_COMMENTS))
            break
        elif answer=="":
            print("not sure")
        elif answer in short_options or answers in [answers[i]]:
