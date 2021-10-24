# Title:            p1_statespace.py
# Files:            p1_statespace.py
# Semester:         CS540 Fall 2020
# Author:           Kenta Shibasaki
# Email:            kshibasaki@wisc.edu
# CS Login:         kenta

# This program is to state space generation of the water juggle puzzle
# including four functions to fill the jug, empty the jug, and pour into another jug

# this is the function to return a copy of state
# state: a list of two ints
# max: a list of maximum capacity of two jugs
# which: int 0 or 1 for two jugs
def fill(state, max, which):
	ret_state = list(state)
	ret_state[which] = max[which]
	return ret_state

# this is the function to return a copy of emptying jug of which side
# state: a list of two ints
# max: a list of maximum capacity of two jugs
# which: int 0 or 1 for two jugs
def empty(state, max, which):
	ret_state = list(state)
	ret_state[which] = 0
	return ret_state

# this is the function to return a copy of jug state after transfering  until
# source is empty or dest is full
# state: a list of two ints
# max: a list of maximum capacity of two jugs
# source: int 0 or 1 for two jugs
# dest: int 0 or 1 for two jugs
def xfer(state, max, source, dest):
	ret_state = list(state)
	if(state[dest] + state[source] <= max[dest]):
		ret_state[source] = 0
		ret_state[dest] = state[dest] + state[source]
	else:
		ret_state[source] = state[source] - max[dest] + state[dest]
		ret_state[dest] = max[dest]

	return ret_state

# this is the function to print out the list of unique successor states
# state: a list of two ints
# max: a list of maximum capacity of two jugs
def succ(state, max):
	state_result_list =[]
	s1 = fill(state, max, 0)
	if s1 not in state_result_list:
		print(s1)
		state_result_list.append(s1)

	s2 = fill(state, max, 1)
	if s2 not in state_result_list:
		print(s2)
		state_result_list.append(s2)
	s3 = empty(state, max, 0)
	if s3 not in state_result_list:
		print(s3)
		state_result_list.append(s3)

	s4 = empty(state, max, 1)
	if s4 not in state_result_list:
		print(s4)
		state_result_list.append(s4)

	s5 = xfer(state, max, 0, 1)
	if s5 not in state_result_list:
		print(s5)
		state_result_list.append(s5)
	s6 = xfer(state, max, 1, 0)
	if s6 not in state_result_list:
		print(s6)
		state_result_list.append(s6)
