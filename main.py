from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from numpy import sum
from report import Report

def main():

	#simulation setup phase
	operator1 = Operate(CoordinateSystem(),[FSM(0,0)])
	reporter1 = Report(operator1,'May19_output1.dat')

	#Event loop
	for i in range(constants.N_turns):
		operator1.run()
		reporter1.update()

	reporter1.output();

if __name__ == "__main__":
	main()