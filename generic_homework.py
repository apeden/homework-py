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
        self.ask_question = (str(self.x)+" + "+str(self.y)+" = ")
        return self.ask_question
        
    def setUser_guess(self):
        """
        requests user input
        converts user in put into a form that can be compared\
        with the actual answer
        This method is not activated in the Homework parent class  
        """
        user_ans = input(self.ask_question)
        self.user_guess = int(user_ans)
        assert type(self.user_guess) == int
        
    def getXY(self):
        """
        returns x and y as tuple (x,y)  
        """
        return (self.x,self.y)

class Session():
    def __init__(self, student_name, num_questions, homework_task):
        """
        instantiates a homework session object using number of questions
        and a home_work task as inputs
        
        num_questions: int indicating number of questions to be asked
        homework_task: the class of homework to be used to generate 
        objects. 
        """
        self.student_name = student_name
        assert type(self.student_name) == str
        self.num_questions = num_questions
        assert type(self.num_questions) == int
        self.homework_task = homework_task
        self.record_file = open("homework.txt", "w")
    
    def question_check(self):        
        q = self.homework_task()
        q.setActual_ans()
        attempt = 1
        while True:            
            q.ask_questions()
            q.setUser_guess()
            if q.check():
                print("Well done",self.student_name,",that's right!")
                ##record to file
                self.record_file.write(self.student_name + " gave the\
                right answer after "+ str(attempt) + "attempt(s)")
                del q
                break
            print("Try again",self.student_name)
            attempt += 1
    
    def run_task(self):
        question = 1
        while question < self.num_questions + 1:
            self.record_file.write("Question "+str(question)+"\n")
            self.question_check()
            question += 1
        self.record_file.close()
