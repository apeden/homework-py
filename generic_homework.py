import random

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
        
        
    def check(self):
        """
        checks answer given by user, return True or False
        """        
        return self.user_guess == self.actual_ans


    def ask_questions(self):
        """
        Asks for user input to in reponse to a question
        Returns a (string) question to be asked
        """
        pass

    def setUser_guess(self):
        """
        requests user input
        converts user in put into a form that can be compared\
        with the actual answer
        This method is not activated in the Homework parent class
        """
        pass

    def setActual_ans(self):
        """
        resets self.actual ans when called
        """         
        pass

    def getActual_ans(self):
        """
        return actual answer of the homework question
        """
        return self.actual_ans

    def getUser_input(self):
        """
        return user input, as string
        """
        return self.user_input

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
        self.x = random.randint(1,12)
        self.y = random.randint(1,12)
        
    def setActual_ans(self):
        """
        resets self.actual ans when called
        """         
        self.actual_ans = self.x + self.y

    def ask_questions(self):
        """
        Asks for user input to in reponse to a question
        sets a (string) question to be asked
        """
        self.ask_question = (str(self.x)+" + "+str(self.y)+"=")
        return self.ask_question
        
    def setUser_guess(self):
        """
        requests user input
        converts user in put into a form that can be compared\
        with the actual answer
        This method is not activated in the Homework parent class  
        """
        self.user_guess = int(input())
        assert type(self.user_guess) == int
        
    def getXY(self):
        """
        returns x and y as tuple (x,y)  
        """
        return (self.x,self.y)

class Session():
    def __init__(self, num_questions, homework_task):
        """
        instantiates a homework session object using number of questions
        and a home_work task as inputs
        
        num_questions: int indicating number of questions to be asked
        homework_task: the class of homework to be used to generate 
        objects. 
        """
        self.num_questions = num_questions
        self.homework_task = homework_task
        self.record_file = open("homework.txt", "w")
    
    def question_check(self):        
        self.homework_task.ask_question()
        self.homework_task.setUser_guess()
        self.homework_task.setActual_ans()
            if self.check():
                print("We done
    
    
    
    def run_task:
        question = 1
        while question < self.num_questions+1:
            self.homework_task.setUser_input()
            self.homework_task.setUser_guess()
            self.homework_task.setActual_ans()
            if self.get
