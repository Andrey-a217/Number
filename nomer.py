while True:
    user_input = input("Введите номер:")
    if 3 <= len(user_input) <= 9 and user_input.isdigit():
        break
    print('Можно вводить только от 3 до 9 цифр!')
d_num = [digit for digit in user_input]
l = d_num[1]
o = d_num[2]
x = d_num[3]
bez = l,o,x
myString = ''.join(bez)
print(myString)
input()
