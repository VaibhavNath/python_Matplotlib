# Matplotib

'''Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

It is a cross-platform library for making 2D plots from data in arrays.

Matplotlib is open source and we can use it freely.'''



'''A format string consists of a part for color , marker and line. '''
# fmt='[marker][line][color]'


#linewidth makes the line of plot darker i.e. increases its width


from matplotlib import pyplot as plt

# plt.xkcd()   #to change style of plot

# print(plt.style.available)

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]              # create a list

dev_y = [38496, 42000, 46752, 49320, 53200,                        # create a list
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x,dev_y ,'k--',linewidth=2, label='All devs')   #plot the graph with label in order to recognise which plot is for what values.'k-- is format string for dashed line'

#or
# plt.plot(ages_x,dev_y ,color='k',LineStyle='--', marker='.', label='All devs') 


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x,py_dev_y ,'b',linewidth=3, label='Python')     #plot the graph with label in order to recognise which plot is for what values.'b' is format string for blue line.

#or
# plt.plot(ages_x,py_dev_y ,color='b',marker='o', label='Python')


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_dev_y ,'y', linewidth=3,label='JavaScript')     #plot the graph with label in order to recognise which plot is for what values.'y' is format string for yellow line.       



plt.xlabel('Ages')                            #label x axis
plt.ylabel('Median Salary (USD)')              #label y axis
plt.title('Median Salary (USD) by Age')         #give graph a title

plt.legend()       #used to label the different plots   

plt.tight_layout()   #tight_layout automatically adjusts subplot parameter so that the subplot(s) fits in to the figure area.

plt.grid(True)      #to add grid lines to plot

plt.savefig('plot(1).png')           #to save the plot in current working directory

plt.show()        # show the graph 