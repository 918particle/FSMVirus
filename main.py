from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from time import time

def plan(fileoutName,virusPlotName,runNumber):
	fileTitle = fileoutName+str(runNumber)+".dat"
	fileTitle2 = virusPlotName+str(runNumber)
	operator = Operate(CoordinateSystem(),[FSM(50,50)])
	reporter = Report(operator,fileTitle,fileTitle2,[0,0.1,0.2,0.3,0.4,0.5])
	for i in range(constants.N_turns):
		operator.run()
		if(i == 275):
			operator.insert_fsm(50,50)
			operator.insert_fsm(51,50)
			operator.insert_fsm(50,51)
			operator.insert_fsm(51,51)
		reporter.update()
		#reporter.reveal_virus(i)
	reporter.output()

def main():
	for i in range(0,8):
		p = Process(target=plan, args=('May25_output_run','virus_spatial',i))
		p.start()
		if(i % 8 ==0 and i != 0):
			p.join()


if __name__ == "__main__":
	main()