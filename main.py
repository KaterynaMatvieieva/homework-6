# #Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
#
# import random
# def get_numbers_list(list_length:int = 3, start_value:int = -5, end_value:int = 10) -> list:
#     return [random.randint(start_value, end_value) for _ in range(list_length)]
#
# numbers = get_numbers_list()
#
# print(numbers)
#
# def product_of_list_values(values: list, values_product: int = 1) -> int:
#     for number in values:
#         values_product = values_product * number
#     return values_product
#
# print(product_of_list_values(numbers))

#Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
#
# import random
#
# def get_numbers_list(list_length:int = 10, start_value:int = -10, end_value:int = 100) -> list:
#     return[random.randint(start_value, end_value) for _ in range(list_length)]
#
# numbers = get_numbers_list()
#
# print(numbers)
#
# def minimum_in_list(values:list) -> int:
#     return (min(values))
#
# minimal_value = minimum_in_list(numbers)
#
# print(minimal_value)

# #Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
#
# import random
#
# def get_numbers_list(list_length:int = 10, start_value:int = 0, end_value:int = 10) -> list:
#     return[random.randint(start_value, end_value) for _ in range(list_length)]
#
# numbers = get_numbers_list()
#
# print(numbers)
#
# def simple_values_in_list(values:list, simple_count:int = 0) -> int:
#     for number in values:
#         if number == 1 or number == 0:
#             continue
#
#         counter = 0
#         for i in range(2,number//2+1):
#             if number % i == 0:
#                 counter += 1
#
#         if counter <= 0:
#             simple_count += 1
#
#     return simple_count
#
# print(f"Amount of simple values in list is: {simple_values_in_list(numbers)}")

#Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.

# import random
#
# def get_numbers_list(list_length:int = 10, start_value:int = -10, end_value:int = 10) -> list:
#     return[random.randint(start_value, end_value) for _ in range(list_length)]
#
# numbers = get_numbers_list()
# print(numbers)
#
# def deletion_from_list(values:list, value_to_delete:int, amount_of_deleted:int = 0) -> int:
#     amount_of_deleted = values.count(value_to_delete)
#     new_list = values.copy()
#     new_list.remove(value_to_delete)
#
#     print(f"New list: {new_list}")
#     print(f"Amount of deleted values is: {amount_of_deleted}")
#
# try:
#     deletion_from_list(numbers, int(input("Enter the value you want to deletefrom the list: ")))
# except Exception as error:
#     print(error)

#Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
# import random
#
# def get_numbers_list(list_length:int = 10, start_value:int = 0, end_value:int = 10) -> list:
#     return[random.randint(start_value, end_value) for _ in range(list_length)]
#
# numbers_one = get_numbers_list()
# numbers_two = get_numbers_list()
# print(numbers_one)
# print(numbers_two)
#
# def common_elements(values_one:list, values_two:list) -> list:
#     return list(set(values_one).intersection(values_two))
#
# try:
#     print(f"Common elements in two lists are:{common_elements(numbers_one, numbers_two)}")
# except Exception as error:
#     print(error)

# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.
# import random
#
# def get_numbers_list(list_length:int = 10, start_value:int = 0, end_value:int = 10) -> list:
#     return[random.randint(start_value, end_value) for _ in range(list_length)]
#
# numbers = get_numbers_list()
# print(numbers)
#
# def get_num_pow(values:list, degree:float, new_list:list = []) -> list:
#     for value in values:
#         num_pow = value**degree
#         new_list.append(num_pow)
#     return new_list
#
# try:
#     print(get_num_pow(numbers,float(input("Enter degree value to create new list:"))))
# except Exception as error:
#     print(error)
