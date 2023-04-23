from task1 import data_entry_method
#data_entry_method("Please input number: ") импортированный метод созданный в классе task1.
inputNumber = int(data_entry_method("Please input number: "))

#Метод вычисляет сумму делителей числа 
def checkNumber(number):
    delimeters_array = []
    for i in range(1, (number+number%2)//2+1): #хитрый метод прибавляющий +1 если число нечетное, чтобы не терять 1 элемент который будет потерян.
      #range() - от первого элемента и до середины так как делителем не может быть число больше половины числителя.
      if number % i == 0:
         delimeters_array.append(i)
    return sum(delimeters_array)       


#Cоздает масив типа [(2,1),(3,1),(4,3)] - первый элемент это само число, а второе это сумма делителей
array = [(i,str(checkNumber(i))) for i in range(2,inputNumber+1)]   
map={}

#метод объеденяет числа с одинаковыми суммаvи делителей в Dictionary {y:[a,b,c]}
# где Y - это сумма числа, а [a,b,c] - числа с одинаковыми суммами делителей
for x,y in array:
   if map.get(y)==None:
     map.update({y:[i for i,z in array if z==y]})

#Отбрасывает пары в которых длина массива значения ключа меньше 1 и выводит пары с одинаковыми 
for x,y in map.items():
   if len(y)>1:
     if int(x)==1:
         print(f"The squence of prime number: {y}")
     else:
         for z in range(len(y)-1):
            print(f"The sum(divisors) of the numbers ({y[0]},{y[z+1]}) = {int(x)}") 
    
