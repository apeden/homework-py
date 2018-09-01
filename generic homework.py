import random

class Homework():
    def __init__(self):
        """
        Instantiates a homework object with attribute of name and user input and task
        """
        self.name = None
        self.task = None
        self.ans = None
        self.user_input = None
        
        
    def check(self):
        """
        checks answer given by user, return True or False
        """        
        return self.user_input == self.ans


    def answer(self):
        """
        Asks for user input to question and gives printed response.\
        Returns user input
        """
        pass

    def openfile(self):


class Homework():
    def __init__(self):
        """
        Instantiates a Sum object with two random ints\
        in a range
        """
        self.x = random.randint(1,12)
        self.y = random.randint(1,12)
        self.ans = None
        self.user_input = None
        self.label = None
        
    def check(self):
        """
        checks answer given by user, return True or False
        """        
        return int(self.user_input) == self.ans

    def add(self):
        """
        return correct answer
        """ 
        self.label = "Addition practice"
        self.ans = self.x + self.y
        print('in add self ans is',self.ans)
        return self.ans

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








class Worktime():
    def __init__(self, question_class, num_questions):
        self.num_questions = num_questions
        self.question_class = question_class

    def session():
        for i in range(num_questions):
            
            print('Question', i,'of ', self.num_qestions)
        
                       


        

question = Sum()
question.add()
question.answer()
        

    
