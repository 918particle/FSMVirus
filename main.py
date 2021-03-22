from coordinate_system import CoordinateSystem
from fsm import FSM
from vaccine import Vaccine
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from random import randint

def plan(fileoutName,virusPlotName,runNumber):

	fileTitle = fileoutName+str(runNumber)+".dat"
	fileTitle2 = virusPlotName+str(runNumber)

	l = []
	for i in range(0,constants.N_vacc):
		x = randint(constants.cs_minX,constants.cs_maxX)
		y = randint(constants.cs_minY,constants.cs_maxY)
		l.append((x,y))

	operator = Operate(CoordinateSystem(),[FSM(49,49)],Vaccine(l))
	reporter = Report(operator,fileTitle,fileTitle2,[0,0.1,0.2,0.3,0.4,0.5])

	for i in range(constants.N_turns):
		operator.run()
		reporter.update()
		#reporter.reveal_virus(i)

	reporter.output()

def main():
	for i in range(0,10):
		p = Process(target=plan, args=('Repr2_run_','virus_spatial_',i))
		p.start()
		if(i % 8 == 0 and i != 0):
			p.join()

if __name__ == "__main__":
	main()
