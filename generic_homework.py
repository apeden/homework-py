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
        self.user_input = None
        self.user_guess = None
        
        
    def check(self):
        """
        checks answer given by user, return True or False
        """        
        return self.user_guess == self.actual_ans


    def setUser_input(self):
        """
        Asks for user input to in reponse to a question
        Returns user input
        This method is not activated in the Homework parent class
        """
        pass

    def setUser_guess(self):
        """
        converts user in put into a form that can be compared\
        with the actual answer
        This method is not activated in the Homework parent class
        """
        pass

    def getActual_ans(self):
        """
        return actual answer of the homework question
        """
        return self.actual_ans

    def getUser_input(self):
        """
        return user input
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

    def setUser_input(self):
        """
        Asks for user input to in reponse to a question
        Returns user input
        """
        self.user_input = input(self.x+" + "+self.y+"=")
        
    def setUser_guess(self):
        """
        converts user in put into a form that can be compared\
        with the actual answer, in this case an int  
        """
        self.user_guess = int(self.user_input)
        assert type(self.user_guess) == int
        
    def getXY(self):
        """
        returns x and y as tuple (x,y)  
        """
        return (self.x,self.y)

