import random
import datetime
from time import*
now = datetime.datetime.now()


class Homework():
    def __init__(self):
        """
        Instantiates a homework object with attributes of the actual \
        answer to the question and the users input in response to question
        and the user guess which is the user input converted into a form\
        that can be compared with the actual answer. Until these are\
        set by a setter function they remain as NoneType
        """
        self.actual_ans = None
        self.ask_question = None
        self.user_guess = None
        
        
    def check(self, i):
        """
        checks answer given by user
        
        i: int index for checking where you are in a multipart\
        question
        
        return True of False
        
        """        
        try:
            type(self.user_guess) == type(self.actual_ans)
        except:
            print('User guess and actual answer are different types\
            and cannot be compared in the check function')
            
        return self.user_guess == self.actual_ans


    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        Returns a (string) question to be asked
        
        i: int, for keeping track of where you are in a multipart question
        """
        pass

    def setUser_guess(self):
        """
        requests user input
        converts user input into a form that can be compared\
        with the actual answer
        This method is not activated in the Homework parent class
        """
        pass

    def setActual_ans(self, things):
        """
        sets self.actual ans when called
        things: type not specified at this stage, but this argument is\
        extra info required for the question
        """         
        pass

    def getAsk_questions(self):
        return self.ask_question


    def getActual_ans(self):
        """ return actual answer of the homework question"""
        return self.actual_ans


    def getUser_guess(self):
        """
        return user guess after conversion to form for\
        comparison with the actual answer
        """
        return self.user_guess


    def __str__(self):
        print("this is a homework task") 


class Addition(Homework):
    task = 'Addition' ##class variable (name)
    def __init__(self):
        """
        Instantiates an Addition (Homework) object with two random ints\
        in a range
        """
        Homework.__init__(self)
        self.x = None
        self.y = None
        
        
    def setActual_ans(self, things):
        """
        resets self.actual ans when called

        things: a tuple containing a range for randint
        """         
        self.x = random.randint(things[0],things[1])
        self.y = random.randint(things[0],things[1]) 
        self.actual_ans = self.x + self.y


    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        This is a de facto getter
        
        i: int, for keeping track of where you are in a multipart question
        Not used in this case
        """
        self.ask_question = (str(self.x)+" + "+str(self.y)+" = ")
        return self.ask_question
        
    
    def setUser_guess(self):
        """
        requests user input
        converts user in put into a form that can be compared\
        with the actual answer  
        """
        while True:
            try:
                user_ans = input(self.ask_question)
                self.user_guess = int(user_ans)
                break
            except ValueError:
                print ("Number value please")
        
        
    def getXY(self):
        """
        returns x and y as tuple (x,y)  
        """
        return (self.x,self.y)



class EquivalentToFifth(Addition):
    def setActual_ans(self, things):
        """
        resets self.actual ans when called

        things: a tuple containing a range for randint
        """         
        self.x = random.randint(things[0],things[1])*5
        self.y = random.randint(things[0],things[1]) 
        self.actual_ans = (self.x) / 5
    
    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        This is a de facto getter
        
        i: int, for keeping track of where you are in a multipart question
        Not used in this case
        """
        self.ask_question = (" 1     ?\n=== = ===   \n 5    "+str(self.x)+"     ? = ")
        return self.ask_question


class EquivalentToThreeFifths(Addition):
    def setActual_ans(self, things):
        """
        resets self.actual ans when called

        things: a tuple containing a range for randint
        """         
        self.x = random.randint(things[0],things[1])*5
        self.y = random.randint(things[0],things[1])*3 
        self.actual_ans = (3*self.x)/5
    
    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        This is a de facto getter
        
        i: int, for keeping track of where you are in a multipart question
        Not used in this case
        """
        self.ask_question = (" 3     ?\n=== = ===   \n 5    "+str(self.x)+"     ? = ")
        return self.ask_question




class DevideByTen(Addition):
    task = 'DevideByTen'
    def __init__(self):
        Addition.__init__(self)

    def setActual_ans(self, things):
        """
        resets self.actual ans when called

        things: a tuple containing a range for randint
        """          
        self.x = random.randint(things[0],things[1])
        self.actual_ans = self.x

    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        Returns the question as a string
        
        i: int, for keeping track of where you are in a multipart question
        Not used in this case
        """
        try:
            multipleOfTen = self.x * 10
            self.ask_question = " 1\n--- of "+ (str(multipleOfTen))+" is \n10            :"
        except:
            print("Could not generate a multiple of 10")
        return self.ask_question


class CakesByTen(DevideByTen):
    task = 'CakesByTen'


    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        Returns the question as a string
        
        i: int, for keeping track of where you are in a multipart question
        Not used in this case
        """
        try:
            multipleOfTen = self.x * 10
            self.ask_question = "What is one tenth of the cakes \n"+5*((int((multipleOfTen/5))*"0 ")+"\n")
        except:
            print("Could not generate a multiple of 10")
        return self.ask_question

class FractionsToLetter(Addition):
    task = "FractionsToLetter"


    def setActual_ans(self, things):
        """
        resets self.actual ans when called

        things: a tuple containing operands
        """          
        self.actual_ans = things

    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        Returns the question as a string
        
        i: int, for keeping track of where you are in a multipart question
        Not used in this case
        """

        self.ask_question = " "+str(self.actual_ans[i][0])+"\n--- TIMES "+str(self.actual_ans[i][2])+" is \n"+ str(self.actual_ans[i][1])+"            :"
        return self.ask_question


    def check(self, i):
        """
        checks answer given by user
        
        i: int index for checking where you are in a multipart\
        question
        
        return True of False
        
        """        
        try:
            type(self.user_guess) == type(self.actual_ans)
        except:
            print('User guess and actual answer are different types\
            and cannot be compared in the check function')
        return self.user_guess == (self.actual_ans[i][0]/self.actual_ans[i][1])*self.actual_ans[i][2]

class Spelling(Homework):
    task = 'Spelling' ##class variable (name)        
    def __init__(self):
        Homework.__init__(self)

    def setActual_ans(self, things):
        """
        resets self.actual ans when called
        """         
        self.actual_ans = things


    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        
        i: into index for keeping track of position in multipart question
        """
        self.ask_question = 'The word is: '+ self.actual_ans[i]
 
       
    def setUser_guess(self):
        """
        requests user input
        assigns it to self_user_guess  
        """
        print(self.ask_question)
        user_ans = input('\n\n\n\n\n\n\n\How do you spell it?')
        self.user_guess = user_ans.lower()
 
       
    def check(self, i):
        """
        checks answer given by user, return True or False
        
        i: int index for keeping track of where one is\
        in a multipart question
        """        
        try:
            type(self.user_guess) == type(self.actual_ans[i])
        except:
            print('User guess and actual answer are different types\
and cannot be compared in the check function')
        return self.actual_ans[i].lower() in self.user_guess.lower()
        

class Sentence(Spelling):
    task = 'Sentence' 
    def setUser_guess(self):
        """
        requests user input
        assigns it to self.user_guess  
        """
        print(self.ask_question)
        user_ans = input('\n\n\n\n\nWrite a sentence containing this word:  ')
        self.user_guess = user_ans.lower()

    def check(self, i):
        """
        checks answer given by user, return True or False
        
        i: int index for keeping track of where one is\
        in a multipart question
        """        
        try:
            type(self.user_guess) == type(self.actual_ans[i])
        except:
            print('User guess and actual answer are different types\
and cannot be compared in the check function')

        
        target_word = self.actual_ans[i].lower()
        guess = self.user_guess.lower()
        target_word_start = guess.index(target_word)
        try:
            after_char = guess[target_word_start + len(target_word)]
        except:
            after_char = None
        try:
            before_char = guess[target_word_start - 1]
        except:
            before_char = None

        if not (before_char == None) and not (after_char == None):
            print("Before Char is " + before_char)
            print("After Char is " + after_char)
        
        if len(guess) > len(target_word):
            if target_word in guess:
                if (target_word_start == 0) and ((after_char == " ") or (after_char == ",") or (after_char == ".")):
                    return True
                elif (before_char == " ") and ((after_char == " ") or (after_char == ",") or (after_char == ".") or (after_char == None)): 
                    return True
            else:
                return False
        else:
            return False


        
class Session():
    def __init__(self, student_name, num_questions, homework_task, date, things):
        """
        instantiates a homework session object using number of questions
        and a home_work task as inputs
        
        num_questions: int, indicating number of questions to be asked
        homework_task: the class of homework to be used
        date: string, date when homework is done written by user
        things: (usually tuple extra info required to set questions
        e.g. spelling words, range of numbers etc
        """
        self.date = date
        self.student_name = student_name
        self.num_questions = num_questions
        self.homework_task = homework_task
        self.things = things
        ##open and start to right to a file to record student work
        self.record_file = open("homework"+str(random.randint(1,1000))+".txt", "w")
        self.record_file.write('Homework task: '+ str(self.homework_task.__name__)
+ '\nby '+self.student_name+ '\n' + self.date + "\n\n"
+ now.strftime("%Y-%m-%d %H:%M")+"\n\n")
        
        
    def question_check(self, count):        
        """
        instantiates a homework task question object.
        Calls on object to generate question, generate answer,
        ask user the question, check answer, ask same question again if the user was wrong,
        congratulate user when they get it right and record all the results to a file
        
        count: int, used to keep a track within a multipart question

        returns nothing
        """
        q = self.homework_task()
        q.setActual_ans(self.things)
        attempt = 1        
        q.ask_questions(count)
        self.record_file.write(q.getAsk_questions()+"\n")
        while True:            
            q.setUser_guess()
            ans = q.getUser_guess()
            self.record_file.write(self.student_name + 
" wrote:  "+str(ans)+"\n")
            if q.check(count):
                print("Well done",self.student_name,",that's right!\n")
                self.record_file.write(self.student_name + " gave the \
right answer after "+ str(attempt) + " attempt(s)\n")
                del q
                break
            print("SORRY",self.student_name.upper()+"\nYOU NEED TO TRY AGAIN!")
            attempt += 1
   
    
    def run_task(self):        
        """
        runs a session of homework by asking the user a set number of questions
        """

        question_num = 1
        print("\n"+self.student_name+", please answer these questions.\n")
        while question_num < self.num_questions + 1:
            print("\n\nQuestion "+str(question_num)+" of "+str(self.num_questions))
            self.record_file.write("\nQuestion "+str(question_num)+"\n")
            self.question_check(question_num-1)
            question_num += 1
        print('FINISH')
        self.record_file.close()       

