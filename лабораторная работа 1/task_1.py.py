numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
summa = 0
for value in numbers:
    if value:
        summa += value
srarif = summa / len(numbers)

for i in range(len(numbers)-1):
    if numbers[i] == None:
        numbers[i] = srarif

print("Измененный список:", numbers)
