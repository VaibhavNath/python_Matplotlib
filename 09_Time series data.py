import pandas as pd
from datetime import datetime , timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
# dates=[
#     datetime(2021,5,24),
#     datetime(2021,5,25) ,   
#     datetime(2021,5,26),
#     datetime(2021,5,27),
#     datetime(2021,5,28),
#     datetime(2021,5,29),
#     datetime(2021,5,30),
# ]

# y=[0,1,3,4,5,6,7]

# plt.plot_date(dates , y , lineStyle = 'solid')

# plt.gcf().autofmt_xdate()    #gcf=get current figure

# date_format=mpl_dates.DateFormatter('%b , %d  %Y')

# plt.gca().xaxis.set_major_formatter(date_format)


data=pd.read_csv('data4.csv')
data['Date']=pd.to_datetime(data['Date'])
data.sort_values('Date' , inplace=True)



price_date=data['Date']
price_close=data['Close']

plt.plot_date(price_date , price_close , lineStyle = 'solid')

plt.gcf().autofmt_xdate()    #gcf=get current figure



# plt.title('Trending Youtube videos')
# plt.xlabel('View Count')
# plt.ylabel('Total likes')

plt.tight_layout()
plt.savefig('09.2_plot.png')

plt.show()