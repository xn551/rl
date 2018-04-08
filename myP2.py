import numpy as np

ROWs = 3
COLs = 3

class Board:
	def __init__(self):
		self.data = np.zeros((ROWs, COLs))
		self.winner = None
		self.end = None
	
	def HaveSpace(self):
		p = 0
		for i in range(0,3):
			for j in range(0,3):
				if self.data[i,j] == 0:
					p += 1
		if p == 0:
			print('no space,Game over')
			self.end = 	1

	def judge(self):
		for i in range(0,3):
			if self.data[i,0] == self.data[i,1] == self.data[i,2]:
				self.winner = self.data[i,1]
		for j in range(0,3):
			if self.data[0,j] == self.data[1,j] == self.data[2,j]:
				self.winner = self.data[1,j]
		if self.data[0,0] == self.data[1,1] == self.data[2,2]:
			self.winner = self.data[1,1]
		if self.data[2,0] == self.data[1,1] == self.data[0,2]:
			self.winner = self.data[1,1]
		if self.winner != 0:
			print('player %d  win!'% self.winner)
			self.end = 1
	
	def IsEnd(self):
		self.HaveSpace()
		self.judge()
		return self.end


	def plot(self):
		print('   1   2   3   ')
		for i in range(0,ROWs):
			print(' -------------')
			out = str(i+1) + '|'
			for j in range(0,COLs):
				if self.data[i,j] == 1:
					token =  ' o '
				if self.data[i,j] == 2:
					token = ' x '
				if self.data[i,j] == 0:
					token = '   '
				out += token + '|'
			print(out)
		print(' -------------')

	def nextState(self,i,j,symbol):
		BoardNewState = Board()
		BoardNewState.data = np.copy(self.data)
		BoardNewState[i,j] = symbol
		return BoardNewState

	def getHash(self):
		if self.hashValue = None:
			hashValue = 0
			if i in self.data.reshape(ROWs, COLs):
				hashValue = HashValue*3 + i
		return self.hashValue

class HumanPlayer:
	def __init__(self,myBo,symbol):
		self.symbol = symbol
		self.state = None
	def Action(self):
		if myBo.end!=1:
			while True:
				pos1,pos2 = map(int,raw_input("Player"+str(self.symbol)+",Input your position:").split())
				if myBo.data[pos1-1,pos2-1] == 0:
					break
				else:
					print("The space has chess!")

			myBo.data[pos1-1,pos2-1] = self.symbol
			myBo.plot()
			myBo.judge()
			myBo.HaveSpace()

class AIPlayer:
	def __init__(self,myBO,symbol):
		self.symbol = symbol
		self.state = []
	def Action(self):
		if myBo.end!=1:
			while True:		
				pos1 =np.random.randint(3)
				pos2 =np.random.randint(3)
				if myBo.data[pos1,pos2] == 0:
					break
			else:
				print("The space has chess!")

			myBo.data[pos1,pos2] = self.symbol
			myBo.plot()
			myBo.judge()
		myBo.HaveSpace()
	def state_log(self):
		self.state.append = myBO.current_state


'''
class AIPlayer:
	def __init__(self,myBO,symbol):
		self.symbol = symbol
		self.state = None
	def Action(self):
		if myBo.end!=1:
			while True:		
				pos1 =np.random.randint(3)
				pos2 =np.random.randint(3)
				if myBo.data[pos1,pos2] == 0:
					break
			else:
				print("The space has chess!")

			myBo.data[pos1,pos2] = self.symbol
			myBo.plot()
			myBo.judge()
		myBo.HaveSpace()
'''
if __name__ == '__main__':
	myBo = Board()
	myBo.plot()
	print "inialize"
	time.sleep(1)
	Hp1 = AIPlayer(Board,1)
	Hp2 = AIPlayer(Board,2)
	while myBo.end !=1:
		Hp1.Action()
		Hp1.state_log()
		Hp2.Action()
		Hp2.state_log()

	print "good";
	time.sleep(1000000)
	print Hp2.state;
