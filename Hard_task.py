n = int(input('Введите число от 3 до 20: '))
result = ''
list_numbers = []
for i in range(1, n):
    list_numbers.append(i)
for j in range(len(list_numbers)):
    for k in range(1, len(list_numbers)):
        if n % (list_numbers[j]+list_numbers[k]) == 0 and list_numbers[j] != list_numbers[k] and list_numbers[j] < list_numbers[k]:
            result += str(list_numbers[j])
            result += str(list_numbers[k])
print(result)


# Для упрощения сверки с правильными ответами и практики применения функций:
def check():
    if int(result) in answers:
        win = True
    else:
        win = False
    return win
answers = \
[12,
13,
1423,
121524,
162534,
13172635,
1218273645,
141923283746,
11029384756,
12131511124210394857,
112211310495867,
1611325212343114105968,
1214114232133124115106978,
1317115262143531341251161079,
11621531441351261171089,
12151811724272163631545414513612711810,
118217316415514613712811910,
13141911923282183731746416515614713812911]
print(check())