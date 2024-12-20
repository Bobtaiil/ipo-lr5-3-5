#Ввод строк
string = input("Введите строку: ") 
#Определяем гласные буквы
vowel_letters = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
#Счётчик гласных букв
count = 0
#Цикл
for char in string:
    #Проверка
    if char in vowel_letters:
        #Если гласная count +1
        count += 1
#Вывод
print("Количество гласных букв в строке равно", count)