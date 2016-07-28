# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 02:13:18 2016

@author: hduser
"""
def students_names(grades):
    names = []            
    for k, v in grades.items():
        if v[0] >= 78 and v[1] >= 78 and v[2] >= 78:
                names.append(k)
    return names


        
def fun(sample, n):
    value = []
    
    for k, v in sample.items():
        if n in v:
            value.append(k)
    return sorted(value)
    
    
    
#input_dict = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': 
 #   ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}

# Final Exam: Problem about revesed dictionary
def reverse_dictionary(input_dict):
    
    # Convert keys and values to lowercase
    d_lower = {k.lower(): [val.lower() for val in v] for k, v in 
                        input_dict.items()}    
    
    # Reversed dictionary: values become keys and keys become values
    reverse_d = {}    
    for k in d_lower:
        for v in d_lower[k]:
            reverse_d.setdefault(v, []).append(k)    
    
    # Sorted values
    reverse_d_sorted_vals = {k: sorted(v) for k, v in reverse_d.items()}
    
    return reverse_d_sorted_vals
    