# printing a game 
a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0], "|", a[1], "|", a[2])
	print("...........")
	print(a[3], "|", a[4], "|", a[5])
	print("...........")
	print(a[6], "|", a[7], "|", a[8])


playeroneturn = True
while True:
	printboard()
	p=input("choose an available space : ")
	if(p in a):
		if(a[int(p)-1]=='x' or a[int(p)-1]=='o'):
			print("place taken , choose another space.. ")
			continue

		else:
			if playeroneturn :
				print("player 1>>")
				a[int(p)-1] = 'x'
				playeroneturn = not playeroneturn
			else:
				print("player 2 >>")
				a[int(p)-1] = 'o'
				playeroneturn = not playeroneturn 
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i+2]):
					print("game over")
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i+6]):
					print(" game over")
					if(a[i]=='x'):
						print("congratulations to player one ")
					else:
						print("congratulation to player two ")
					printboard()
					exit()	
						
#checking for diagonal (from right to left)
				if(a[2]==a[4] and a[2]==a[6]):
					print("game over")
					if(a[4]=='x'):
						print("congratulations player one ")
					else:
						print("congratulations player two ")
					printboard()
					exit()
#checking for diagonal ( from left to right )				
				if(a[0]==a[4] and a[0]==a[8]):
					print("sorry game over")
					if(a[4]=='x'):
						print("congratulations player one ")
					else:
						print("congratulations player two ")
					printboard()
					exit()





			







