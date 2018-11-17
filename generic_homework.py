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
        user_ans = input(self.ask_question)
        self.user_guess = int(user_ans)
        assert type(self.user_guess) == int
        
        
    def getXY(self):
        """
        returns x and y as tuple (x,y)  
        """
        return (self.x,self.y)


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


class Spelling(Homework):
    task = 'Spelling' ##class variable (name)        
    def setActual_ans(self, things):
        """
        resets self.actual ans when called
        """         
        self.actual_ans = things


    def ask_questions(self, i):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        This is a de facto getter
        
        i: into index for keeping track of position in multipart question
        """
        self.ask_question = ('The word is: '+ self.actual_ans[i])
        return self.ask_question
 
       
    def setUser_guess(self):
        """
        requests user input
        assigns it to self_user_guess  
        """
        user_ans = input('\n\n\n\nHow do you spell it?')
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
        return self.user_guess == self.actual_ans[i]
        

class Sentence(Spelling):
    task = 'Sentence' ##class variable (name) 
    def setUser_guess(self):
        """
        requests user input
        assigns it to self_user_guess  
        """
        user_ans = input('\n\nWrite a sentence containing this word:  ')
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
        return self.actual_ans[i] in self.user_guess
 

        
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
        self.record_file.write('Homework task: '+ self.homework_task.task
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
        q = self.homework_task()##sets up homework questions
        q.setActual_ans(self.things)
        attempt = 1        
        ##ask question
        question = q.ask_questions(count)
        print(question)
        self.record_file.write(question+"\n")
        while True:            
            q.setUser_guess()
            ans = q.getUser_guess()
            self.record_file.write(self.student_name + 
" wrote:  "+str(ans)+"\n")
            ##check answer
            if q.check(count):
                print("Well done",self.student_name,",that's right!\n")
                ##record to file
                self.record_file.write(self.student_name + " gave the \
right answer after "+ str(attempt) + " attempt(s)\n")
                del q
                break
            print("Try again",self.student_name+"\n")
            attempt += 1
   
    
    def run_task(self):        
        """
        runs a session of homework by asking the user a set number of questions
        """

        question_num = 1
        print("\n"+self.student_name+", please answer these questions.\n")
        while question_num < self.num_questions + 1:
            print("\n\nQuestion "+str(question_num)+" of "+str(self.num_questions))
            self.record_file.write("Question "+str(question_num)+"\n")
            self.question_check(question_num-1)
            question_num += 1
        print('FINISH')
        self.record_file.close()       

