import random

class Homework():
    def __init__(self):
        """
        Instantiates a homework object with attributes of the actual answer to the question\
        and the users guess. Until these are set by a setter function they remain as
        NoneType
        """
        self.actual_ans = None
        self.user_guess = None
        
        
    def check(self):
        """
        checks answer given by user, return True or False
        """        
        return self.user_guess == self.actual_ans


    def user_guess(self):
        """
        Asks for user input to in reponse to a question
        Returns user input
        """
        pass
    


class Addition(Homework):
    task = 'Addition' ##class variable
    def __init__(self):
        """
        Instantiates an Addition (Homework) object with two random ints\
        in a range
        """
        Homework.__init__(self)
        self.x = random.randint(1,12)
        self.y = random.randint(1,12)


    def getAddAns(self):
        """
        return correct answer
        """ 
        self.ans = self.x + self.y
        return self.ans


    def getUserInput(self):
        """
        Asks for user input to in reponse to a question
        Returns user input as int
        """
        string_input = input('What is'+self.x+'+'+self.y+'?:')
        self.user_input = int(string_input)        
        return self.user_input










class Session():
    def __init__(self, task, num_questions):
        """
        instantiates a homework session
        task: int used as an index to select a task from a dict inside this class
        num_questions = int indicating number of questions to be asked
        """
        self.task = task_dict[task]
        self.num_questions = num_questions
        self.name = None
        self.date = None        

    def ():
        for i in range(num_questions):
            
            print('Question', i,'of ', self.num_qestions)
        
    def setDate(self):
        """
        Asks user to input date 
        Returns user input (string)
        """
        self.date = input("What is today's date?:")

    def setName(self):
        """
        Asks user to input name 
        Returns user input (string)
        """
        self.date = input("What is your name?:")







    def answer(self):
        """Asks for user input to question and gives printed response. Return nothing """
        self.user_input = input('Next question:'+str(self.x)+'+'+str(self.y)+'=')
        print('First user input was',self.user_input)
        print(self.check())
        while not self.check():            
            self.user_input = input('Try again:'+str(self.x)+'+'+str(self.y)+'=')
            print('First user input was',self.user_input)
            self.check()
        else:
            print('Correct, well done!')
                       


        

question = Sum()
question.add()
question.answer()
        

    
