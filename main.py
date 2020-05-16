from coordinate_system import CoordinateSystem
from fsm import FSM
from operate import Operate
import constants
from numpy import sum

def main():
	#simulation setup phase
	operator1 = Operate(CoordinateSystem(),[FSM(0,0)])
	#Event loop
	for i in range(constants.N_turns):
		operator1.run()
		print(i,len(operator1.main_fsm_list),sum(operator1.main_coordinate_system.space))

if __name__ == "__main__":
	main()