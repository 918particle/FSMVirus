import coordinate_system
import fsm

def main():
	cs1 = coordinate_system.CoordinateSystem()
	cell1 = fsm.FSM()
	cell1.print_state()
	cell1.act('1')
	cell1.print_state()
	cell1.act('1')
	cell1.print_state()
	cell1.act('1')
	cell1.print_state()

if __name__ == "__main__":
	main()