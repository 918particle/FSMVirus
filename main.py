from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from report import Report
from multiprocessing import Process
from random import randint

def plan(fileoutName,virusPlotName,runNumber):
	fileTitle = fileoutName+str(runNumber)+".dat"
	fileTitle2 = virusPlotName+str(runNumber)
	operator = Operate(CoordinateSystem(),[FSM(50,50)])
	operator.main_coordinate_system.vaccinate_area(24,74,30,49) #Vaccine quadrant
	reporter = Report(operator,fileTitle,fileTitle2,[0,0.2,0.4,0.6,0.8,1])
	for i in range(constants.N_turns):
		operator.run()
		reporter.update()
		reporter.reveal_virus(i)
	reporter.output()

def main():
	for i in range(0,1):
		p = Process(target=plan, args=('Jun8_output_run','virus_spatial',i))
		p.start()
		if(i % 8 ==0 and i != 0):
			p.join()

if __name__ == "__main__":
	main()