#Imports

import time
import random

#Creating variables

data_list = []
counter = 1000
total_time = 0

#Creating data_list

for element in range(0, 1000):
    element = random.randint(0, 1000)
    data_list.append(element)

#Defining the sorting-function

def sorting(data) -> list:
    sorted_list = []

    for data_element in data:
        index_found = False

        while index_found == False:
            if len(sorted_list) == 0:
                sorted_list.append(data_element)

                index_found = True
        
            else:
                for sorted_element in sorted_list:
                    
                    if index_found == False:
                    
                        if sorted_element < data_element:
                            if sorted_list.index(sorted_element) + 1 == len(sorted_list):
                                index = sorted_list.index(sorted_element) + 1
                                sorted_list.insert(index, data_element)

                                index_found = True

                            else:
                                continue

                        else:
                            index = sorted_list.index(sorted_element)
                            sorted_list.insert(index, data_element)

                            index_found = True

                            

    return sorted_list

#Printing it out

for loop in range(counter):
    starting_time = time.process_time()

    result = sorting(data_list)

    elapse_time = time.process_time() - starting_time

    total_time += elapse_time

average_time = total_time / counter
print(average_time)

file = open("Runtime.txt", "a")
file.write("\n Runtime of Sorting Basic: " + str(average_time))
file.close()