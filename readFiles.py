# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:59:35 2016

@author: hduser
"""

'''Reading files into python Example'''
# Change working directory 
import os
os.chdir('hduser/python_data_analysis')
my_file = open('car.names.txt', 'r')
my_str = my_file.read()
# Only one line
my_file.readline()
# list of all lines
lines = my_file.readlines()

my_file.close()


people = open('people.txt', 'r')
data_pointer = people.read()

temp = [line[:-1] for line in people]


with people as f:
    myList = f.read().splitlines()
    

def func(my_file):
    with open(my_file) as f:
        myList = f.read().splitlines()
    return myList
    
# OR
def file_to_list(myFile):    
    # Make a connection to the file
    file_pointer = open(myFile, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    out_list = []
    for line in data:
        stripped_line = line.strip('\n')
        out_list.append(stripped_line)
    return out_list
    

'''Write a function that accepts a filename(string) of a CSV file which contains 
the information about student's names and their grades for four courses and 
returns a dictionary of the information. The keys of the dictionary should be the 
name of the students and the values should be a list of floating point numbers 
of their grades.''' 
def file_to_dict(my_file):
    file_pointer = open(my_file, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dict = {}
    for item in data:
        name, course1, course2, course3, course4 = item.strip().split(',')
        my_dict[name] = [float(course1), float(course2), float(course3), float(course4)]
    return my_dict
    

'''Write a function that takes a file name (string) of a CSV file which contains 
the information about student's names and their grades for four courses and 
returns a dictionary that contains information about the students whose grades 
in both Math and Chemistry is above 70. Note that if the file has any comments 
(lines starting with #) then you should ignore such a line.'''

def file_to_dict_greater_70(my_file):
    file_pointer = open(my_file, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dict = {}    
    for item in data:
        if not item.startswith('#'):
            name, math, physics, chemistry, biology = item.strip().split(',')
            if float(math) > 70.0 and float(chemistry) > 70.0:
                my_dict[name] = [float(math), float(physics), float(chemistry), float(biology)]
    return my_dict

    
'''Write a function that accepts a filename as input argument, the file contains 
the information about a persons expenses on milk and bread and returns a 
dictionary that contains exactly the strings 'milk' and 'bread' as the keys 
and their floating point values in a list as values. Each line of the file may 
start with a 'm' or a 'b' denoting milk or bread respectively'''
def _construct_nested_list_from_file_sample_(filename):
    my_dictionary = {}
    my_dictionary["milk"] = []
    my_dictionary["bread"] = []
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        first_character = line[0]
        if first_character == "m":
            # remove the first character
            # strip and split by white space
            vertex = line[1::].strip().split()
            # change the string items into floats
            vertex = [float(x) for x in vertex]
            my_dictionary["milk"] += [vertex]

        if first_character == "b":
            face = line[1::].strip().split()
            face = [float(x) for x in face]
            my_dictionary["bread"] += [face]
    return my_dictionary
    
    
'''Write a function that accepts a file name as input argument and constructs 
and returns a nested dictionary from it. The keys of this dictionary should 
be last names, and the values should be dictionaries that contain first names 
as the keys and integer ages as the values. Note that the data may contain 
multiple people with the same last name, but it will have unique first names. 
Ignore any lines that start with "#"'''

def names_info(my_file):
    file_pointer = open(my_file, 'r')
    data = file_pointer.readlines()
    my_dict = {}
    
    for line in data:
        if not line.startswith('#'):
            # Strip the line (that's get rid of the \n) and split it at the ','
            first_name, last_name, age = line.strip().split(',')
            # If last name is not in my_dict, add it            
            if last_name not in my_dict:
                my_dict[last_name] = {first_name: int(age)}
            # Same for the first name as the last name
            else:
                if first_name not in my_dict[last_name]:
                    my_dict[last_name][first_name] = int(age)
    return my_dict
    


        


    
        
    

