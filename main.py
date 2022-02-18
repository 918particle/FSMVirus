from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from random import randint
from time import sleep

def plan(fileoutName,virusPlotName,runNumber):

	fileT = fileoutName+str(runNumber)+".dat"
	fileT2 = virusPlotName+str(runNumber)
	fsm_list = [FSM(0,0,0),FSM(49,49,200)]
	operator = Operate(CoordinateSystem(),fsm_list)
	reporter = Report(operator,fileT,fileT2,[0.75,0.85,0.95])

	for i in range(constants.N_turns):
		operator.run()
		reporter.update()
		reporter.reveal_virus(i)

	reporter.output()

def main():
	n_cores = 48
	for i in range(48):
		p = Process(target=plan, args=('Feb17_run_','virus_spatial_',i))
		p.start()
		if(i % n_cores == 0 and i != 0):
			p.join()
		sleep(0.1)

if __name__ == "__main__":
	main()
