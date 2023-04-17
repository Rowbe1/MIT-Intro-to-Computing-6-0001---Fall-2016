# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:07:23 2020

@author: Rowan
"""

annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percentage of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
monthly_r = r/12
months = 1
while current_savings < down_payment:
    if months%6 == 0:
        annual_salary = annual_salary + annual_salary*semi_annual_raise
    current_savings = current_savings + (current_savings * monthly_r) + (annual_salary/12 * portion_saved) 
    months += 1
print('Number of months: ' + str(months))