# Title:            nqueens.py
# Files:            nqueens.py
# Semester:         CS540 Fall 2020
# Author:           Kenta Shibasaki
# Email:            kshibasaki@wisc.edu
# CS Login:         kenta

import random

# This is the function to return the all valid successor lists of current state
def succ(state, static_x, static_y):
    if(state[static_x]!=static_y):
        return []
    succ_list = []
    for i in range(len(state)):
        if(i==static_x):
            continue
        temp_state_1 = list(state)
        if(state[i]+1<len(state)):
            temp_state_1[i] = temp_state_1[i]+1
            succ_list.append(temp_state_1)
        temp_state_2 = list(state)
        if(state[i]-1 >= 0):
            temp_state_2[i] = temp_state_2[i]-1
            succ_list.append(temp_state_2)
    succ_list = sorted(succ_list)
    return succ_list

# This is the helper function to check if attacked or not
def is_attacked(state,curr):
    for j in range(len(state)):
        if(curr!=j and state[j]==state[curr]):
            return True
    j = curr-1
    while(j>=0):
        step = curr - j
        if(state[j]==state[curr]+step or state[j]==state[curr]-step):
            return True
        j = j -1
    j = curr+1
    while(j<len(state)):
        step = j - curr
        if(state[j]==state[curr]+step or state[j]==state[curr]-step):
            return True
        j = j +1
    return False

# This is the function to retun the score of a given state
def f(state):
    num_attacks = 0
    for i in range(len(state)):
        if(is_attacked(state,i)):
            num_attacks+=1
    return num_attacks

# This is the function to select the next state by using the succ()
def choose_next(curr, static_x, static_y):

    if(curr[static_x]!=static_y):
        return None
    succ_states = succ(curr, static_x, static_y)
    succ_states.append(curr)
    succ_states = sorted(succ_states)
    succ_tuple_list = []
    for elem in succ_states:
        succ_tuple_list.append((f(elem), elem))
    succ_tuple_list.sort(key=lambda x:x[0])

    if(len(succ_tuple_list)==1):
        return succ_tuple_list[0][1]
    if(succ_tuple_list[0][0] == succ_tuple_list[len(succ_tuple_list)-1][0]):
      return succ_states[0]
    filtered_succ_tuple_list = []
    min_f = succ_tuple_list[0][0]
    for tupl in succ_tuple_list:
      if(tupl[0]==min_f):
        filtered_succ_tuple_list.append(tupl[1])
    filtered_succ_tuple_list = sorted(filtered_succ_tuple_list)
    return filtered_succ_tuple_list[0]

# This is the function to return the convergence state after running hill climbing algorithm
def n_queens(initial_state, static_x, static_y, print_steps=True):
    is_done = False
    curr_state = initial_state
    final_state = None
    if(print_steps):
        print("{} - f={}".format(curr_state,f(curr_state)))
    if(f(curr_state)==0):
        is_done= True
        final_state = curr_state
    while(not is_done):
        next_state = choose_next(curr_state, static_x, static_y)
        f_curr = f(curr_state)
        f_next = f(next_state)
        if(print_steps):
            print("{} - f={}".format(next_state,f_next))
        if(f_next==0 or f_curr == f_next):
            is_done= True
            final_state = next_state
            continue
        curr_state = next_state

    return final_state

# This is the function to random-restart the algorim
def n_queens_restart(n, k, static_x, static_y):
    random.seed(1)
    state = n*[0]
    state[static_x] = static_y
    is_converge  = False
    solution_states_tuple = []
    for turn in range(k):
        for i in range(n):
            if(i==static_x):
                continue
            rand_int = random.randint(0,n-1)
            state[i]=rand_int
        converged_state = n_queens(state, static_x, static_y, print_steps=False)
        if(f(converged_state)==0):
            is_converge= True
            break
        solution_states_tuple.append((f(converged_state), converged_state))
    solution_states_tuple.sort(key=lambda x:x[0])
    min_f = solution_states_tuple[0][0]
    filtered_succ_tuple_list = []
    for tupl in solution_states_tuple:
        if(tupl[0]==min_f):
            filtered_succ_tuple_list.append(tupl[1])

    filtered_succ_tuple_list = list(set(tuple(i) for i in filtered_succ_tuple_list))
    filtered_succ_tuple_list = sorted(filtered_succ_tuple_list)
    if(is_converge):
        print("{} - f={}".format(converged_state,0))
    else:
        for elem in filtered_succ_tuple_list:
            print("{} - f={}".format(elem,f(elem)))
