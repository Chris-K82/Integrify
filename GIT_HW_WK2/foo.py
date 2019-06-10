import random
import numpy as np 
import names

def gender_picker():
    return random.randint(0,1)

def random_name():
    gender = ['male', 'female']
    gender = gender[gender_picker()]
    return names.get_full_name(gender = gender)

def gen_name_list():
    name_list = np.arange(100)
    return map(lambda name: random_name(), name_list)

def display_name_list(name_list):
    for i in name_list:
        print(i)

display_name_list(gen_name_list())  
