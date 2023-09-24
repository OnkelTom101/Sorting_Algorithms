#Imports
import time
import random

#Making the data list and variables

data_list =  []
comparing_list = []

biggest_number = 0
total_time = 0
counter = 1000

for number in range(0, 1000):
    data_list.append(random.randint(1, 1000))

#Sorting the data

def sorting_max(data):
    for element in data:
        comparing_list.append(element)

        if len(comparing_list) == 2:
            if comparing_list[0] < comparing_list[1]:
                del(comparing_list[0])
            
            elif comparing_list[0] > comparing_list[1]:
                del(comparing_list[1])    
    return comparing_list[0]
        
#Printing it out

for loop in range(counter):
    starting_time = time.process_time()

    biggest_number = sorting_max(data_list)

    elapse_time = time.process_time() - starting_time

    total_time += elapse_time

    print("List: " + str(data_list))
    print("Biggest number: " + str(biggest_number)) 
    print("Runtime: " + str(elapse_time))

average_time = total_time / counter
print(average_time)

file = open("Runtime.txt", "a")
file.write("\n Runtime of biggest_number_list: " + str(average_time))
file.write("\n Biggest number of biggest_number_list: " + str(biggest_number))
file.write("\n List of biggest_number_list: " + str(data_list) + "\n")
file.close()

input()