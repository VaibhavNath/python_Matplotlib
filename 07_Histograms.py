import pandas as pd
from matplotlib import lines, pyplot as plt

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

data = pd.read_csv('data2.csv')
ids = data['Responder_id']
ages = data['Age']

bins=[10,20,30,40,50,60,70,80,90,100]

plt.hist(ages , bins=bins , edgecolor = 'black' , log=True)    #log is used to show all data if the data is very small as between 80-90 and 90-100



median_age = 29
color = '#fc4f30'
plt.axvline(median_age , color=color , label='Age median' , linewidth = 2)
plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig('07_plot.png')

plt.show()