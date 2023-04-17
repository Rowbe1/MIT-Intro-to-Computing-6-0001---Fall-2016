# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:36:49 2022

@author: Rowan
"""

from ps5 import *
from datetime import timedelta



dt = '12 Oct 2016 23:59:59'
dt2 = '13 Oct 2016 23:59:59' 
dt3 = '12 Dec 2016 23:59:59'
dt4 = '12 Oct 2019 23:59:59' 

print(datetime.now())
dta = datetime.strptime(dt, "%d %b %Y %X")
dta = dta.replace(tzinfo=pytz.timezone('EST'))
print(dta)

print(dt>dt2)

dto = timedelta(seconds=5)
now = datetime(2016, 10, 12, 23, 59, 59)
now = now.replace(tzinfo=pytz.timezone("EST"))

ancient_time = datetime(1987, 10, 15)
ancient_time = ancient_time.replace(tzinfo=pytz.timezone("EST"))


future_time = datetime(2087, 10, 15)
future_time = future_time.replace(tzinfo=pytz.timezone("EST"))

print('dta:', dta)
print('now:', now)
print('ancient time:', ancient_time)
print('future time:', future_time)

print(dta>future_time)