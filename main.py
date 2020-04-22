import coordinate_system
import fsm
import operate
import constants
from numpy import sum

def main():
	#simulation setup phase
	operator1 = operate.Operate(coordinate_system.CoordinateSystem(),[fsm.FSM(-2,0)])
	for i in range(constants.N_turns):
		operator1.run()
		print(i,len(operator1.main_fsm_list),sum(operator1.main_coordinate_system.space))

if __name__ == "__main__":
	main()