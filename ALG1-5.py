# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('vvedite dve bukvy :')
letter1 = input('bukva 1 = ')
letter2 = input('bukva 2 = ')

if 96 < ord(letter1) < 123 and 96 < ord(letter2) < 123:

      print(f'bukva "{letter1}" №-{ord(letter1) - 96} v alfavite\n'
            f'bukva "{letter2}" №-{ord(letter2) - 96} v alfavite\n'
            f'rasstoyanie mezhdu bukvami {abs(ord(letter1) - ord(letter2)) - 1}')

elif 1071 < ord(letter1) < 1105 and 1071 < ord(letter2) < 1105:
      print(f'bukva "{letter1}" №-{ord(letter1) - 1071} v alfavite\n'
            f'bukva "{letter2}" №-{ord(letter2) - 1071} v alfavite\n'
            f'rasstoyanie mezhdu bukvami {abs(ord(letter1) - ord(letter2)) - 1}')
else:
      print("odno iz vvedennih znacheniy ne bukva")