from coordinate_system import CoordinateSystem
from fsm import FSM
from vaccine import Vaccine
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from random import randint

def plan(fileoutName,virusPlotName,runNumber):

	fileT = fileoutName+str(runNumber)+".dat"
	fileT2 = virusPlotName+str(runNumber)

	l = []
	for i in range(0,constants.N_vacc):
		x = randint(constants.cs_minX,constants.cs_maxX)
		y = randint(constants.cs_minY,constants.cs_maxY)
		l.append((x,y))

	operator = Operate(CoordinateSystem(),[FSM(24,1)],Vaccine(l))
	reporter = Report(operator,fileT,fileT2,[0.33,0.42,0.5,0.58,0.67])

	for i in range(constants.N_turns):
		operator.run()
		reporter.update()
		#reporter.reveal_virus(i)

	reporter.output()

def main():
	n_cores = 48
	for i in range(100):
		print(i)
		p = Process(target=plan, args=('Feb9_run_','virus_spatial_',i))
		p.start()
		if(i % n_cores == 0 and i != 0):
			p.join()

if __name__ == "__main__":
	main()
