from matplotlib import pyplot as plt

import numpy as np

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]              # create a list

width=0.25

x_index=np.arange(len(ages_x))           #creates index values for ages_x as 0 1 2 3 4 5 6 7 8 9 10

dev_y = [38496, 42000, 46752, 49320, 53200,                        # create a list
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar (x_index - width , dev_y , width = width , label='All devs')      #plot the bar graph with label in order to recognise which plot is for what values.


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar (x_index , py_dev_y , width = width , label='Python')


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar (x_index + width , js_dev_y , width = width , label='JavaScript')


plt.xticks(ticks=x_index , labels=ages_x)   #since above we created index for ages_x so in bar plot we get index , so in order to fix this we need to use xticks.

plt.xlabel('Ages')                              #label x axis
plt.ylabel('Median Salary (USD)')               #label y axis
plt.title('Median Salary (USD) by Age')         #give graph a title

plt.legend()       #used to label the different plots   

plt.tight_layout()

plt.show() 


'''To make vertical bar plot use command
plt.bar
followed by all other commands , xlabel , ylabel , legend , show etc.'''


'''To make highest value appear on top use command
variable name.reverse()
'''