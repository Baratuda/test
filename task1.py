import random as ra

# Метод который позволяет производить input() для переменной и массива и принимает на как параметр значение 
# "message" и "arrayIndex" - нужен для определения что данный метод будет заполнять.
# Если  "arrayIndex" = True то будет произведен  
def data_entry_method(message="", arrayIndex=False):
    if arrayIndex:
        print(message)
        return [int(i) for i in input().split()]  
    else:
        return input(message)
#Метод создает массив заполненный случайными числами от 1 до 10 при помощи метода randrange()
#  и принимает на вход размер массива.
def array_create_method(array_size):
    return list([ra.randrange(1,10) for _ in range(array_size)])
#метод находит элементы которые есть в 1-м массиве но нет во 2-м массиве.
def find_intersections_method(first_array, second_array):
    return [i for i in first_array 
                 if not(i in second_array)]

def main():
    #Создаем наши массивы при помощи метода array_create_method() который в качестве параметра 
    # принмает метод который реализует input() размера массива.
    first_array = array_create_method(int(data_entry_method("Please input first array size: ")))
    second_array = array_create_method(int(data_entry_method("Please input second array size: ")))

    #Вызываем метод нахождения элементов которые есть в 1-м но нет во 2-м массиве.
    intersection_of_sets = find_intersections_method(first_array, second_array)

    print(f"Arrays#1 {first_array} and #2 {second_array} : {intersection_of_sets}")


