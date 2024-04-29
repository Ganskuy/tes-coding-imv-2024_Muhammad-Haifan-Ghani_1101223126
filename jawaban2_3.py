panjang_diagonal = int(input('Input lebar belah ketupat: '))
for i in range(panjang_diagonal):
  for j in range(panjang_diagonal-i):
    print(' ',end='')
      
  for k in range(i+1):
    print('* ',end='')
  print()
 
for i in range(1,panjang_diagonal):
  for j in range(i+1):
    print(' ',end='')
      
  for k in range(panjang_diagonal-i):
    print('* ',end='')
  print()