act = input('Выберите операцию ("+", "-", "*", "/"): ')

while (act != "+") and (act != "-") and (act != "*") and (act != "/"):
    print("\nОшибка ввода")
    act = input("Введите действие (+, -, *, /): ")

count_sequence = int(input("Сколько операндов? "))

for sequence in range(1, count_sequence + 1):
    text = "Введите операнд " + str(sequence) + ": "
    user_num = int(input(text))
    if sequence == 1:
        answer = user_num
    else:
        if act == "+":
            answer += user_num
        elif act == "-":
            answer -= user_num
        elif act == "*":
            answer *= user_num
        elif act == "/":
            answer /= user_num

print("CHANGES")
print("Ответ:", answer)
