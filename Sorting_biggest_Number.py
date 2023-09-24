#Imports

import time
import random

#Making the data list and variables

data_list =  []

total_time = 0
counter = 1000

for number in range(0, 1000):
    data_list.append(random.randint(1, 1000))

#Sorting the data

def sorting_max(data):
    biggest_number = 0

    for element in data:
        if biggest_number == 0 or element > biggest_number:
            biggest_number = element
        
        else:
            continue
        

    return biggest_number
        
#Printing it out

for loop in range(counter):
    starting_time = time.process_time()

    result = sorting_max(data_list)

    elapse_time = time.process_time() - starting_time

    total_time += elapse_time

    #print("List: " + str(data_list))
    #print("Biggest number: " + str(biggest_number)) 
    #print("Runtime: " + str(elapse_time))

average_time = total_time / counter
print(average_time)

file = open("Runtime.txt", "a")
file.write("\n Runtime of biggest_number: " + str(average_time))
file.write("\n Biggest number of biggest_number: " + str(result))
#file.write("\n List of biggest_number: " + str(data_list) + "\n")
file.close()

input()
