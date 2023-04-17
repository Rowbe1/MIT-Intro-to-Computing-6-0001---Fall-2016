# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:07:23 2020

@author: Rowan
"""

annual_salary = int(input('Enter your annual salary: '))
#portion_saved = float(input('Enter the percentage of your salary to save, as a decimal: '))
reset_annual_salary = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
monthly_r = r/12
low = 0
high = 10000
portion_saved = (high + low)//2
steps = 0
while True:
    for months in range(1,37):
        current_savings = current_savings + (current_savings * monthly_r) + (annual_salary/12*portion_saved/10000) 
        if months%6 == 0:
            annual_salary = annual_salary + annual_salary*semi_annual_raise 
    # print('steps: ',steps)
    # print('months: ',months)
    # print('savings: ',current_savings)
    # print('saving rate: ',portion_saved/10000)
    # print('annual salary: ',annual_salary) 
    # print('savings-deposit gap: ',abs(down_payment - current_savings))
    if abs(down_payment - current_savings) < 100 or portion_saved == 9999:
        break
    if current_savings > down_payment:
        high = portion_saved
    else:
        low = portion_saved
    portion_saved = (high + low)//2
    current_savings = 0
    annual_salary = reset_annual_salary
    steps += 1
  
if portion_saved == 9999 and abs(down_payment - current_savings) > 100:
    print('It is not possible to pay the down payment in 3 years')        
else:
    #print(months)
    #print(current_savings)
    print('Best savings rate: ', portion_saved/10000)
    print('Steps in bisection search: ', steps)