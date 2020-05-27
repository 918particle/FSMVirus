from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from time import time
from random import randint

def plan(fileoutName,virusPlotName,runNumber):
	fileTitle = fileoutName+str(runNumber)+".dat"
	fileTitle2 = virusPlotName+str(runNumber)
	operator = Operate(CoordinateSystem(),[FSM(50,50)])
	reporter = Report(operator,fileTitle,fileTitle2,[0,0.1,0.2,0.3,0.4,0.5])
	reinfect_points = [275]
	for i in range(constants.N_turns):
		operator.run()
		#Reinfection
		if(i in reinfect_points):
			xc1 = randint(constants.cs_minX,constants.cs_maxX-1)
			yc1 = randint(constants.cs_minY,constants.cs_maxY-1)
			operator.insert_fsm(xc1,yc1)
			xc1 = randint(constants.cs_minX,constants.cs_maxX-1)
			yc1 = randint(constants.cs_minY,constants.cs_maxY-1)
			operator.insert_fsm(xc1,yc1)
		reporter.update()
		reporter.reveal_virus(i)
	reporter.output()

def main():
	for i in range(0,100):
		p = Process(target=plan, args=('May26_output_run','virus_spatial',i))
		p.start()
		if(i % 8 ==0 and i != 0):
			p.join()


if __name__ == "__main__":
	main()