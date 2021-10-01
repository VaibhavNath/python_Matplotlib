import pandas as pd
from matplotlib import lines, pyplot as plt

data=pd.read_csv('data1.csv')
ages=data['Age']
dev_salaries=data ['All_Devs']
py_salaries=data ['Python']
js_salaries=data ['JavaScript']

plt.plot(ages , dev_salaries , color = 'red' , lineStyle = '--' , label = 'All Devs')

plt.plot(ages , py_salaries , label = 'Python')

overall_median = 57287

plt.fill_between(ages , py_salaries ,dev_salaries ,
                    where = (py_salaries >dev_salaries) , interpolate=True  ,alpha=0.25 , label ='Above avg')   
 #Regulate the transparency of a graph plot using the alpha attribute. By default, alpha=1.

plt.fill_between(ages , py_salaries ,dev_salaries ,
                    where = (py_salaries <= dev_salaries) , interpolate=True  ,color= 'red' , alpha=0.25 , label= 'Below avg')


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig('06_plot.png')

plt.show()