# Title:            p1_weather.py
# Files:            p1_weather.py
# Semester:         CS540 Fall 2020
# Author:           Kenta Shibasaki
# Email:            kshibasaki@wisc.edu
# CS Login:         kenta

# This program is to predict data from historical data

# this is the function to return the manhattan distance
def manhattan_distance(data_point1, data_point2):
	dist_prcp = abs(data_point1['PRCP'] - data_point2['PRCP'])
	dist_tmax = abs(data_point1['TMAX'] - data_point2['TMAX'])
	dist_tmin = abs(data_point1['TMIN'] - data_point2['TMIN'])
	manhattan_dist = dist_prcp + dist_tmax + dist_tmin
	return manhattan_dist

# this is the function to return a list of data point dictionaries read
# from the file rain.txt
def read_dataset(filename):
	f_open = open(filename,'r').readlines()
	diction_list = []
	for line in f_open:
		lst = line.strip().split()
		diction ={}
		diction['DATE'] = lst[0]
		diction['PRCP'] = float(lst[1])
		diction['TMAX'] = float(lst[2])
		diction['TMIN'] = float(lst[3])
		diction['RAIN'] = lst[4]
		diction_list.append(diction)

	return diction_list

# this is the function to return a prediction if its raining or not based on data
def majority_vote(nearest_neighbors):
	total_true = 0
	total_false = 0
	for elem in nearest_neighbors:
		if(elem['RAIN'] == 'TRUE'):
			total_true+=1
		else:
			total_false+=1
	if(total_true>=total_false):
		return 'TRUE'
	else:
		return 'FALSE'

# this is the function to return the majojrity vote based on data given by
# three functions
def k_nearest_neighbors(filename, test_point, k, year_interval):
	diction_list = read_dataset(filename)
	test_year = int(test_point['DATE'].split('-')[0])
	nearest_diction_list = []
	distance_tuple_list = []
	for elem in diction_list:
		year = int(elem['DATE'].split('-')[0])
		if(year>= test_year+ year_interval or year <= test_year - year_interval):
			continue
		dist = manhattan_distance(test_point, elem)
		distance_tuple_list.append((dist, elem))

	distance_tuple_list.sort(key = lambda tup:tup[0])
	if(len(distance_tuple_list)==0):
		return 'TRUE'
	nearest_neighbors =[]
	count = 0
	for elem in distance_tuple_list:
		nearest_neighbors.append(elem[1])
		count+=1
		if(count==k):
			break
	res = majority_vote(nearest_neighbors)
	return res
