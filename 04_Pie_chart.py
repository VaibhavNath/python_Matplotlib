from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

# slices=[120,80,30,20]             #create a list with any values 

# colors=['blue','red','yellow','green']    #change colors of pie chart

# labels=['Sixty','Forty','Extra1','Extra2']      #apply labels to pie chart

# plt.pie(slices , labels = labels , colors = colors ,wedgeprops = {'edgecolor':'black'})        #plot a pie chart with some labels

#  shadow makes chart look 3D
#  startangle makes pic chart rotate by given angle value.
#  autopct tells percentage of pie chart occupied by different labels.



slices = [59219, 55466, 47544, 36443, 35917]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode=[0,0.1,0,0.4,0]    #used to carve out pie for specific labels , 0.1 is radius distance and can be any value

plt.pie(slices , labels = labels , explode = explode , shadow = True ,
        startangle = 90 , autopct= '%1.1f%%' , wedgeprops = {'edgecolor':'black'}) 



plt.title('My awesome pie chart')
plt.tight_layout()
plt.savefig('plot(4.2).png')
plt.show()