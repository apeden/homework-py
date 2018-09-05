# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 08:16:42 2018

@author: user
"""

import random
from generic_homework import *
###TESTING OF THE HOMEWORK CLASS####
#h = Homework()
#print(h.check())
#print(h.setUser_input())
#print(h.setUser_guess())
#print(h.setActual_ans())
#print(h.getActual_ans())
#print(h.getUser_input())
#print(h.getUser_guess())
#

####TESTING OF THE ADDITION CLASS####
j = Addition()
r = 3
print(type(j))
print(type(r))
#print(j.ask_questions())
#print(j.setUser_guess())
#print(j.setActual_ans())
#print(j.getActual_ans())
#print(j.getUser_input())
#print(j.getUser_guess())
#print(j.getXY())
#print(j.check())
#print(j.task)

####TESTING OF SESSION CLASS####
work = Session("Euan",4,Addition)
#print(work.student_name)
#print(work.num_questions)
#print(work.homework_task)
#work.question_check()
work.run_task()
