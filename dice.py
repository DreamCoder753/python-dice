import random, os
from time import sleep
dice = ['1', '2', '3', '4', '5', '6']

result = random.choice(dice)

input('Нажмите ENTER чтобы бросить кубик')

msg = "Бросаем кубик.."
for x in range(3):
  msg = msg + "."
  print(msg)
  sleep(1)
  os.system("cls")

print("%sГотово!" % msg)
print()


print("Вам выпало:", result)
print()

if result == '1':
	print()
	print('  ·')
	
if result == '2':
	print("     ·")
	print()
	print(" ·")
	
if result == '3':
	print("     ·")
	print("   ·")
	print(" ·")
	
if result == '4':
	print(" ·   ·")
	print()
	print(" ·   ·")
	
if result == '5':
	print(" ·   ·")
	print("   ·  ")
	print(" ·   ·")
	
if result == '6':
	print(" ·   ·")
	print(" ·   ·")
	print(" ·   ·")

print()
input('Нажмите ENTER чтобы выйти')
