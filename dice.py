import random

dice = ['1', '2', '3', '4', '5', '6']

result = random.choice(dice)
 
print("Вам выпало:", result)

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
