# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:43:27 2018

@author: user
"""

import random
from generic_homework import *

student_name = input('\n\nHello, what is your name?:')
date = input("What is today's date?:")
num_questions = 4
homework_task = Addition

work = Session(student_name, num_questions, homework_task, date)
work.run_task()