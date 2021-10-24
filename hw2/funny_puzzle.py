# Title:            funny_puzzle.py
# Files:            funny_puzzle.py
# Semester:         CS540 Fall 2020
# Author:           Kenta Shibasaki
# Email:            kshibasaki@wisc.edu
# CS Login:         kenta

import numpy as np
import heapq

# This is the program to solve the 8-tile puzzle

# This is helper function to calculate the Manhattan distance of each tile to its goal position
def manhattan_distance(lst1, lst2):
    mat1 = np.reshape(lst1,(3,3))
    mat2 = np.reshape(lst2,(3,3))
    dist = 0
    for i in range(1,9):
        a1, b1 = np.where(mat1==i)
        a2, b2 = np.where(mat2==i)
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        dist+=abs(a1 -a2) + abs(b1-b2)
    return dist

# This is the helper function for print_succ(state) by getting sorted possible succesor states
def give_succ_state(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goal_mat = np.reshape(goal_state,(3,3))
    state_mat = np.reshape(state,(3,3))
    a, b = np.where(state_mat==0)
    a = int(a)
    b = int(b)
    move_x = [0,0,-1,1]
    move_y = [-1,1,0, 0]
    successor_states =[]
    for i in range(4):
        if a+ move_x[i]>= 0 and a + move_x[i]<3 and b + move_y[i] >=0 and b + move_y[i] < 3 :
            successor_mat = np.copy(state_mat)
            successor_mat[a+move_x[i]][b+move_y[i]]= 0
            successor_mat[a][b]= state_mat[a+move_x[i]][b+move_y[i]]
            successor_states.append(successor_mat.ravel().tolist())
    sorted_successor = sorted(successor_states)
    return sorted_successor

# This is the function to print all of the possible successor states
def print_succ(state):
    sorted_successor = give_succ_state(state)
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for elem in sorted_successor:
        h = manhattan_distance(elem, goal_state)
        print("{} h={}".format(elem, h))

# This is the helper function for solve(state) to choose the path
def find_in_any(state, pq_open, pq_closed):
    for elem in pq_open:
        if elem[1] == state :
            return True
    for elem in pq_closed:
        if elem[1] == state :
            return True
    return False

# This is the helper function for solve(state) to print paths in given format
def print_goal_path(pq_closed, popped_state):
    if(popped_state[2][2]==-1):
        print("{} h={} moves: {}".format(popped_state[1], popped_state[2][1], popped_state[2][0]))
        return
    print_goal_path(pq_closed,pq_closed[popped_state[2][2]])
    print("{} h={} moves: {}".format(popped_state[1], popped_state[2][1], popped_state[2][0]))

# This is the function to print the path from the current state to the goal state
def solve(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    pq_open = []
    pq_closed = []
    h = manhattan_distance(state, goal_state)
    g = 0
    heapq.heappush(pq_open,((g+h), state, (g, h, -1)))
    count = 1
    popped_state = None
    while(len(pq_open)!=0):
        popped_state = heapq.heappop(pq_open)
        pq_closed.append(popped_state)
        if(popped_state[1]==goal_state):
            break
        count+=1
        successor_states = give_succ_state(popped_state[1])
        g =  popped_state[2][0] + 1
        for small_state in successor_states:
            h = manhattan_distance(small_state, goal_state)
            if find_in_any(small_state, pq_open, pq_closed) == False:
                heapq.heappush(pq_open, ((g+h), small_state, (g, h, pq_closed.index(popped_state))))
            else:
                for i, elem in enumerate(pq_closed):
                    if elem[1] == small_state and elem[2][0] > g:
                        g_new = g
                        h_new = elem[2][1]
                        pq_closed[i] = (g_new+h_new, small_state, (g_new, h_new,pq_closed.index(popped_state)))


                for i, elem in enumerate(pq_open):
                    if elem[1] == small_state and elem[2][0] > g:
                        g_new = g
                        h_new = elem[2][1]
                        pq_open[i] = (g_new+h_new, small_state, (g_new, h_new,pq_closed.index(popped_state)))

    print_goal_path(pq_closed, popped_state)
