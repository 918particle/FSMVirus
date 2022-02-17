from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from random import randint

def plan(fileoutName,virusPlotName,runNumber):

	fileT = fileoutName+str(runNumber)+".dat"
	fileT2 = virusPlotName+str(runNumber)

	operator = Operate(CoordinateSystem(),[FSM(50,50)])
	reporter = Report(operator,fileT,fileT2,[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])

	for i in range(constants.N_turns):
		operator.run()
		reporter.update()
		reporter.reveal_virus(i)

	reporter.output()

def main():
	n_cores = 48
	for i in range(100):
		p = Process(target=plan, args=('Feb9_run_vacc_','virus_spatial_',i))
		p.start()
		if(i % n_cores == 0 and i != 0):
			p.join()

if __name__ == "__main__":
	main()
