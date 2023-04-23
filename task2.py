from task1 import data_entry_method, array_create_method

def find_neighbors_of_number(number, array):
    count_of_neighbors = 0
    for i in range(1,len(array)-1):
        if (array[i-1]<number) and (array[i+1]<number):
            count_of_neighbors = count_of_neighbors+1
    return count_of_neighbors 

number = int(data_entry_method("Please input number that you want to find: "))
array = data_entry_method(True)

print(find_neighbors_of_number(number, array))
