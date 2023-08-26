# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:59:43 2023

@author: Bekhzod
"""
import random 


#def user_name(name):
   # username=(name[::-1].lower()+str(random.randint(0, 9)))
    #return username

user_name=(lambda name:(name[::-1].lower()+str(random.randint(0, 9))))
name=input("Sizning ismingiz nima?>>>")
print(user_name(name))