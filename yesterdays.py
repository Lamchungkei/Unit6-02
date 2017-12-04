# Created by: Kay Lin 
# Created on: 28th-Nov-2017
# Created for: ICS3U
# This program displays entering the day of the week then showing the order

from enum import Enum

# an enumerated type of the days of the week

week = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
      
# input
print('Sunday(1), Monday(2), Tuesday(3), Wednesday(4), Thursday(5), Friday(6), Saturday(7)')

input_day = raw_input('Enter your favorite day of the week: ')

# process
input_day = input_day.title()
if input_day in week:
    counter = 1
    for a_day in week:
        if input_day == str(a_day):
            print (str(counter) + ' is the number that corresponds to your favourite day of the week')
        else:
            counter = counter + 1
else:
    print('Please input valid day')
    
print('\n')



