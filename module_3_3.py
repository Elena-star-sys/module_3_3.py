def print_params(a=1, b="строка", c= True):
    print(a, b, c)


print("1. Функция с параметром по умолчанию:")
print_params()
print_params(b=25)
print_params(c=[1,2,3])  #почему горит жёлтым?

print()
print("2. Распаковка параметров:")
values_list = [35, 'Elena', True]
print_params(*values_list)
values_dict = {'a': 77, 'b': 'text', 'c': False}
print_params(**values_dict)

print()
print("3. Распаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)   #работает


