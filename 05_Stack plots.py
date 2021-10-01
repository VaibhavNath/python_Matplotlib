from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]


   
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]



# plt.pie([1,1,1] , labels = ['Player 1','Player 2' , 'Player 3'])

labels = ['player 1','player 2' , 'player 3']

colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes , player1 , player2 , player3 , labels=labels , colors= colors)     #create a stack plot

# plt.legend(loc = 'upper left')       #used to label the different plots , loc is used to set location for labels to display on plot

plt.legend(loc = (0.07,0.05))   #pass coordinate of graph in order to place lables correctly

'''Valid locations for loc are:-
	best
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center'''


plt.title('My awesome stack plot')
plt.tight_layout()
plt.savefig('plot(5.1).png')
plt.show()



# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f