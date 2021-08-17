# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print('Vvedite nomer bukvy ot 1 do 26:')
num = int(input()) + 64
if 64 < num < 91:
    print(f'Bukva : "{chr(num)}"')
else:
    print('vvedeno nekorrektnoe chislo')