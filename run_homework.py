"""
Created on Thu Sep  6 00:43:27 2018

@author: Alex Peden
"""

import random
from generic_homework import *
6
homeworkTasks = {"1":Addition,
                "2":EquivalentToFifth,
                "3":EquivalentToThreeFifths,
                "4":DevideByTen,
                "5":CakesByTen,
                "6":Spelling,
                "7":Sentence,
                "8":Percentages}
student_name = ""
date =""

things = (
"Je m'appelle", 
"Anniversaire",
"Aujourd'hui",
"Repetez",
"Ecosse",
"Merci",
"Beaucoup",
"S'il vous plait",
"J'aime",
"Croissant",
"Pomme",
"Pain au chocolate",
)


things2 =(
(1,4,60),
(1,5,60),
(1,3,36),
(1,3,48),
(1,10,80),
(1,10,150),
(1,3,54),
(1,2,32),
(1,10,220),
(1,2,18),
(13,20,40),
(9,15,30),
(1,10,130),
(1,100,2300),
(11,20,40),
(26,30,30),
(1,9,81))

num_questions = len(things)

def inputRequest(request):
    userInput =""
    while userInput == "":
        try:
            userInput = input('\n\nWhat\'s' + request+ "? ")
            assert(userInput != "")
        except:
            userInput == ""
            print("Please write something for" + request)     
    return userInput
        
student_name = inputRequest(" your name")
date = inputRequest(" today\'s date.")

def homeworkSelection():   
    selection = None
    while selection == None:
        try:
            for key, value in homeworkTasks.items():
                print(key+": " + str(value.__name__))
            i = input("Select the homework task you would like \
to perform from this list: ")         
            selection = homeworkTasks[i] 
            return selection
        except KeyError:
            print("Enter a number between 1 and 7")
    
homework_task  = homeworkSelection()
print(homework_task)

if ((homework_task != Sentence) and  (homework_task != Spelling)):
    num_questions = 10
    things = (1,100)

##homework_task = FractionsToLetter
##things = things2

work = Session(student_name, num_questions, homework_task, date, things)
work.run_task()
work.get_record_file().close() 

