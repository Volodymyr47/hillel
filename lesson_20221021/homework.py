print('''
1. Задача: Створіть дві змінні first=10, second=30.
Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
''')

first=10
second=30
print(f'first = {first}, second = {second} \n')


print(f'Operation + : {first + second}')
print(f'Operation - : {first - second}')
print(f'Operation * : {first * second}')
print(f'Operation / : {first / second}')
print(f'Operation // : {first // second}')
print(f'Operation % : {first % second}')
print(f'Operation ** : {first ** second}')


print('''
2. Задача: Створіть змінну і почергово запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
Виведіть на екран результат кожного порівняння.
''')

print(f'Operation < : {first < second}')
print(f'Operation > : {first > second}')
print(f'Operation == : {first == second}')
print(f'Operation != : {first != second}')
# print(f'Operation >= : {first >= second}')
# print(f'Operation <= : {first <= second}')


print('''
3. Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". Виведіть на екран.
''')
str1 = 'Hello '
str2 = 'world'
print(f'str1 = {str1}, str2 = {str2} \n')


greeting = str1 + str2
print(f'Greeting is: {greeting}')